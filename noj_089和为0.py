class ZeroSum:
    def __init__(self, string):
        self.nums = list(map(int, string.split()))

    def get_zero_sum(self):
        result = []
        for i in range(len(self.nums)):
            for j in range(i, len(self.nums)):
                for k in range(j, len(self.nums)):
                    if self.nums[i] + self.nums[k] + self.nums[j] == 0:
                        combination = [self.nums[i], self.nums[j], self.nums[k]]
                        result.append(combination)
        return result

string = input()
zs = ZeroSum(string)
print(zs.get_zero_sum())
