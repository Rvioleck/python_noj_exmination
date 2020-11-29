roman_dict = {
    'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9,
    'X': 10, 'XX': 20, 'XXX': 30, 'XL': 40, 'L': 50, 'LX': 60, 'LXX': 70, 'LXXX': 80, 'XC': 90,
    'C': 100, 'CC': 200, 'CCC': 300, 'CD': 400, 'D': 500, 'DC': 600, 'DCC': 700, 'DCCC': 800, 'CM': 900,
    'M': 1000, 'MM': 2000, 'MMM': 3000
}

def get_min_gap_num(num):
    min_gap_num = 10000
    result = 0
    for value in roman_dict.values():
        if value <= num and num - value < min_gap_num:
            min_gap_num = num - value
            result = value
    return result

class Roman_numeral:
    def __init__(self, num):
        self.num = num

    def get_sum(self):
        num = self.num
        sum = []
        while num != 0:
            sum_elem = get_min_gap_num(num)
            num -= sum_elem
            sum.append(sum_elem)
        return sum

    def get_roman(self):
        sum = self.get_sum()
        roman = ""
        for one in sum:
            for k, v in roman_dict.items():
                if v == one:
                    roman += k
        return roman

    def __str__(self):
        return self.get_roman()

a = int(input())
roman = Roman_numeral(a)
print(roman)