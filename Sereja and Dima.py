n = int(input())
a = list(map(int, input().split()))
l = 0
r = n - 1
sereja = 0
dima = 0

for i in range(n):
    if a[l] > a[r]:
      value = a[l]
      l += 1
    else:
      value = a[r]
      r -= 1

    if i % 2 == 0:     
      sereja += value
    else:              
      dima += value

print(sereja, dima)
