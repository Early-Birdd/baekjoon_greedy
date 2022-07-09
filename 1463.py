n = int(input())
d = [0] * (n + 1)

for i in range(2, n + 1):
    #d[i]는 횟수, i는 1로 만들 숫자
    #i - 1을 수행했으므로 횟수 d[i]에 +1 을 해준다.
    d[i] = d[i - 1] + 1
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)

print(d[n])