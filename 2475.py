def solution(a, b, c, d, e):
    answer = ((a**2)+(b**2)+(c**2)+(d**2)+(e**2))%10
    return answer

a, b, c, d, e = map(int, input().split())
print(solution(a, b, c, d, e))