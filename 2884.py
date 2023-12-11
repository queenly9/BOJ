n = input()
a, b = map(int, n.split())

if b >= 45:
    b -= 45
elif a == 0:
    a = 23
    b = (60-(45-b))
elif b < 45:
    a -= 1
    b = (60-(45-b))


print(abs(a), b)