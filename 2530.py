a, b, c = map(int, input().split())

d = int(input())

x = c + d
s = x % 60
y = b + (x // 60)

m = y % 60
h = (a + y // 60) % 24

print(h, m, s)
