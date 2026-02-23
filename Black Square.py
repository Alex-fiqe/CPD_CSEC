a = list(map(int, input().split()))
s = input()
t = 0
for i in s:
    t += a[int(i) - 1]
print(t)
