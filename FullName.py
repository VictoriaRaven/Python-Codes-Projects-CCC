
class FullName:

    # constructor
    def __init__(self, first_n, last_n):
        self.first_n = first_n
        self.last_n = last_n

    # return str of obj
    def __str__(self):
        return f" {str(self.first_n)} {str(self.last_n)}"

    # 2 obj are compared
    def __gt__(self, fullname):
        # last
        if self.last_n > fullname.last_n:
            return True
        elif self.last_n < fullname.last_n:
            return False
        # last "=", firstnames ?
        if self.first_n > fullname.first_n:
            return True
        elif self.first_n < fullname.first_n:
            return False
        if self.last_n == fullname.last_n:
            if self.first_n > fullname.first_n:
                return True
            else:
                return False
