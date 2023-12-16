case = int(input())
for _ in range(case):
    str = input()
    if len(str) > 1:
        print(str[0]+str[-1])
    if len(str) == 1:
        print(str*2)