N,M = map(int, input().split())
square = []
for i in range(N):
    row = list(map(int, input().split(' ')))
    square.append(row)
dsquare = [[0] * M for _ in range(N)]
x = 0
for i in range(N):
    for j in range(M):
        if square[i][j] == 1:
            if dsquare[i][j-1] == 0 or dsquare[i-1][j] == 0:
                dsquare[i][j] = 1
            else:
                dsquare[i][j] = min(dsquare[i-1][j], dsquare[i][j-1], dsquare[i-1][j-1]) + 1
            x = max(dsquare[i][j],x)
print(x)

            


