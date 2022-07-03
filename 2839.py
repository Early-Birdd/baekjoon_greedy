n = int(input())

count = 0
while n >= 0:
    if n % 5 == 0:
        #5로 나누어 떨어지지 않을 때 while을 다시 돌기 때문에 count += 사용
        count += n // 5
        print(count)
        break

    n -= 3
    count += 1

    if n < 0:
        print(-1)