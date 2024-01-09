n, m = map(int, input().split())
a = []
b = []
c = []
for i in range(n*2):
    if i < n:
        for j in list(map(int, input().split())):
            a.append(j)
    else:
        for k in list(map(int, input().split())):
            b.append(k)
for l in range(0, n*m):
    c.append(a[l]+b[l])

for z in range(0, len(c), n):
    print(*c[z:z+n])







