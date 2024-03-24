case = int(input())
lst = []
for _ in range(case):
    a = input()
    lst = list(a)
    p = lst[0]
    s = lst[2:]
    plst = []
    for i in range(len(s)):
        t = s[i]*int(p)
        plst.append(t)
    print(''.join(plst))
