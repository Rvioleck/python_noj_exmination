import re
def url(string: str) -> list :
    # 含括号匹配时不作处理仅返回括号内容
    # 在括号前假设?:后返回所有元素
    result = re.findall(r'(?:https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]', string)
    return result

string = input() # "The latest news web is https://news.nwpu.edu.cn/info/1002/70871.htm, not https://www.nwpu.edu.cn/"
print(url(string))