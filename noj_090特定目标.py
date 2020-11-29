class SpecialGoal:
    def __init__(self, string, goal):
        self.nums = list(map(int, string.split()))
        self.goal = goal

    def get_special_goal(self):
        for i in range(len(self.nums)):
            for j in range(i, len(self.nums)):
                if self.nums[i] + self.nums[j] == self.goal:
                    result = "{} + {} = {}".format(self.nums[i], self.nums[j], self.goal)
                    return result

string = input()
goal = int(input())
sg = SpecialGoal(string, goal)
print(sg.get_special_goal())
