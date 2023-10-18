from Datehw4 import Date


class Event:
    _event_name = None
    _event_date = None
    _start_hour = None
    _end_hour = None

    def __init__(self, date, name, start, end):
        self.event_date = date
        self.event_name = name
        self.start_hour = start
        self.end_hour = end

    def __str__(self):
        return f"Event: {self.event_name}, Time: {self.start_hour} to {self.end_hour}, Date: {self.event_date}"

    @property
    def event_name(self):
        return self._event_name

    @event_name.setter
    def event_name(self, name):
        self._event_name = name

    @property
    def event_date(self):
        return self._event_date

    @event_date.setter
    def event_date(self, date):
        if isinstance(date, Date):
            self._event_date = date

    # pass an Event Obj to check overlaps
    def has_overlap(self, other):
        if self.event_date == other.event_date and self.start_hour < other.end_hour:
            return True
        else:
            return False

    @property
    def start_hour(self):
        return self._start_hour

    @start_hour.setter
    def start_hour(self, start):
        if 0 < start < 23:
            if self.end_hour is None or self.end_hour > self.start_hour:
                self._start_hour = start
        else:
            raise ValueError("Invalid hour: " + str(start) + " must be 0-23")

    @property
    def end_hour(self):
        return self._end_hour

    @end_hour.setter
    def end_hour(self, end):
        if 0 < end <= 23 and self.start_hour < end:
            self._end_hour = end
        else:
            raise ValueError("Invalid hour: " + str(end) + " must be 0-23")
