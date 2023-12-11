line = int(input())
for i in range(line):
    ox = input()
    jb = 1
    js = 0
    for j in ox:
        if j == "O":
            js += jb
            jb += 1
        elif j == "X":
            jb = 1
        else:
            break
    else:
        print(js)