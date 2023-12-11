case = int(input())
for _ in range(case):
    h, w, n = map(int, input().split())
    x = (n//h)+1
    y = n % h
    if n % h == 0:
        x = n // h
        y = h
    print(y * 100 + x)