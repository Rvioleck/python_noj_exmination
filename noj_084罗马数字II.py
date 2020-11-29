class Roman_numeral:
    dict = {
        # 罗马符号对应阿拉伯数字
        'I': 1,
        'X': 10,
        'C': 100,
        'M': 1000,
        'V': 5,
        'L': 50,
        'D': 500
    }
    def __init__(self, r):
        # 罗马数字字符串抽象为列表
        self.roman_nums = [str(i) for i in r]

    def to_num(self):
        result = 0
        for i in range(len(self.roman_nums) - 1, 0, -1):
            # 对列表进行反向循环
            if self.dict[self.roman_nums[i]] > self.dict[self.roman_nums[i - 1]]:
                # 后者大于前者做差
                # result += self.dict[self.roman_nums[i]] - self.dict[self.roman_nums[i - 1]]
                result -= self.dict[self.roman_nums[i - 1]]
            else:
                # 后者小于前者直接加
                result += self.dict[self.roman_nums[i - 1]]
        # if self.dict[self.roman_nums[len(self.roman_nums) - 1]] <= self.dict[self.roman_nums[len(self.roman_nums) - 2]]:
            # 若末尾元素小于倒二元素，会忽略末尾元素，重新添加
        result += self.dict[self.roman_nums[len(self.roman_nums) - 1]]
        return result

if __name__ == '__main__':
    roman = input()
    roman_obj = Roman_numeral(roman)
    print(roman_obj.to_num())



