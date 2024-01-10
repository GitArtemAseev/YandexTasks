N, M = map(int, input().split())
cubes = list(map(int, input().split()))

p = 10 ** 9 + 7
x_ = 257
h = [0] * (N + 1)
h_rev = [0] * (N + 1)
x = [0] * (N + 1)
x[0] = 1
answer = []

for i in range(1, len(cubes) + 1):
    h[i] = (h[i - 1] * x_ + cubes[i - 1]) % p
    h_rev[i] = (h_rev[i - 1] * x_ + cubes[-i]) % p
    x[i] = (x[i - 1] * x_) % p

for i in range(len(cubes) // 2 + 1):
    l = min(i, len(cubes) - i)
    f = i
    s = len(cubes) - i
    if (h[f + l] + h_rev[s] * x[l]) % p == (h_rev[s + l] + h[f] * x[l]) % p:
        answer.append(s)
print(*answer[::-1])
