class Stack:
    # 栈类
    def __init__(self):
        self.item = []

    def push(self, c):
        # 添加新元素到栈顶
        for i in c:
            self.item.append(i)

    def pop(self):
        # 返回栈顶元素
        if self.is_empty():
            # 若为空返回False用作后续判断
            return False
        else:
            return self.item.pop()

    def is_empty(self):
        return self.item == []

    def print_stack(self):
        # 打印栈元素用于调试
        for i in self.item:
            print(i, end='')

match = {
    # 括号匹配
    '{': '}',
    '(': ')',
    '[': ']'
}

def is_matched(stack1):
    while stack1.is_empty() != True:
        # 持续匹配并消除顺利匹配的括号直到为空
        pending_match = Stack() # 生成待匹配的栈用于存储反括号
        inverted_bracket = stack1.pop()
        if inverted_bracket not in match.values():
            # 若读入的第一个字符不为反括号直接返回
            return False
        while inverted_bracket in match.values():
            # 反括号读出来放入待匹配的栈中
            pending_match.push(inverted_bracket)
            inverted_bracket = stack1.pop()
            if inverted_bracket == False:
                # 读出的最后一个反括号为空的话，直接返回
                return False
        stack1.push(inverted_bracket)  # 退出while循环时多读出的元素退回

        while pending_match.is_empty() != True:
            # 待匹配栈pending_match匹配完退出
            try:
                if match[stack1.pop()] != pending_match.pop():
                    # 匹配失败时退出，返回False
                    return False
            except KeyError:
                # 匹配时数量不够时，stack剩余栈为空返回值为False
                # 为KeyError，此时匹配失败，函数总体返回False
                return False
    if stack1.is_empty():
        # stack1匹配完毕则为空，返回True
        return True
    else:
        return False

if __name__ == '__main__':
    stack1 = Stack()
    brackets = input()
    stack1.push(brackets)
    while stack1.is_empty() != True:
        print(is_matched(stack1))
        stack1 = Stack()
        brackets = input()
        stack1.push(brackets)
