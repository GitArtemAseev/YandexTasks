n = int(input())
rating = [int(a) for a in input().split()]
result = []

tmp = rating.copy()
firstStudent = rating[0]
for i in range(n):
    tmp[i] = abs(firstStudent - tmp[i])

currentSum = sum(tmp)
result.append(currentSum)

for i in range(1, n):
    ratingDifference = rating[i] - rating[i - 1]
    result.append(currentSum + ratingDifference * (2 * i - n))
    currentSum = currentSum + ratingDifference * (2 * i - n)

print(*result)


