a, b = map(int, input().split())
c = int(input())
n = b + c

h = a + (n // 60)
m = n % 60

if h >= 24 :
    h -= 24

print(h, m)
