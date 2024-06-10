s = input()
lst = list(s)
mlst = []
for i in range(len(s)):
    m = lst.count(lst[i])
    mlst.append(m)
    a = max(mlst)


print(a)
aaaaaba