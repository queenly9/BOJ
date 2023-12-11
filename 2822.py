score = []
for i in range(8):
    score.append(int(input()))

result = sorted(score, reverse=True)

score_index = []
for i in result[:5]:
    score_index.append(score.index(i)+1)

print(sum(result[:5]))
score_index.sort()
print(*score_index)


