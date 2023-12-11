def solution(A, B):
    answer = (A + B) * (A - B)
    return answer


A, B = map(int, input().split())
print(solution(A, B))