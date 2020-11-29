class ReverseString:
    def __init__(self, string):
        self.string = string
        self.list = self.string.split()

    def reverse(self):
        anti_list = self.list[::-1]
        return " ".join(anti_list)

string = input()
rs = ReverseString(string)
print(rs.reverse())