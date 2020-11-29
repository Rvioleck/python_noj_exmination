import math

# hav公式
def hav(theta):
    return (1-math.cos(theta))/2

# 输入经纬度转为弧度
latitude1 = float(input())*math.pi/180
longitude1 = float(input())*math.pi/180
latitude2 = float(input())*math.pi/180
longitude2 = float(input())*math.pi/180
r = 6371 # 地球半径

# hav(d/r)的定义式
hav_d_r = hav(latitude2-latitude1) + math.cos(latitude1)*math.cos(latitude2)*hav(longitude2-longitude1)
# 通过反三角函数反向求出d的值
d = r*math.acos(1-2*hav_d_r)

print("%.4fkm"%d)
# print("{:.4f}km".format(d))