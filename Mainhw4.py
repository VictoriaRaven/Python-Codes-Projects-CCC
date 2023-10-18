from Datehw4 import Date
from Eventhw4 import Event

events_l = []


def update_date(date):
    date.advance()


def main():
    u_input = None
    while u_input != "q":
        print()
        print("a - Add event")
        print("c - Cancel event")
        print("v - View all events")
        print("q - Quit")
        u_input = input("Your Option: ")
        u_input = u_input.lower()

        if u_input == "a":
            d = int(input("Enter day: "))
            m = int(input("Enter month: "))
            y = int(input("Enter year: "))
            s = int(input("Enter start time: "))
            e = int(input("Enter end time: "))
            n = input("Enter name: ")

            # object
            date_obj = Date(d, m, y)
            update_date(date_obj)
            event = Event(date_obj, n, s, e)
            if len(events_l) > 0:
                for i in range(len(events_l)):
                    if event.has_overlap(events_l[i]):
                        print(f"Event already exist or it overlaps: {events_l[i]}")
                        break
                    else:
                        events_l.append(event)
            else:
                events_l.append(event)
        elif u_input == "c":
            n2 = input("Event name: ")
            for i in range(len(events_l)):
                if events_l[i].event_name == n2:
                    del events_l[i]
        elif u_input == "v":
            for j in events_l:
                print(j)
        elif u_input == "q":
            break
        elif u_input != "q":
            print("You must pick an option!")


main()
