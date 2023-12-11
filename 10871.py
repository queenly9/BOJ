n, x = map(int, input().split())
_list = list(map(int, input().split()[:n]))
_list = [i for i in _list if i < x]
print(*_list)