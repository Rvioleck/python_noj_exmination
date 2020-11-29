a = input().split()
print([ d:={a[-1]:{}} if x==-1 else  (d:={a[x]:d}) for x in range(-1,-(len(a)+1),-1)][-1])