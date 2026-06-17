t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    cur = 0

    for x in a:
        if x == 0:
            cur += 1
            ans = max(ans, cur)
        else:
            cur = 0

    print(ans)
