k, r = map(int, input().split())

for i in range(1, 11):
    t = k * i
    if t % 10 == 0 or t % 10 == r:
        break
print(i)
