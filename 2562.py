lst = []
for i in range(9):
    lst.append(int(input()))
m = max(lst)
n = lst.index(m) + 1
print(m,n)