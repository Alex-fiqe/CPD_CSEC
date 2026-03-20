n = input().strip()
count = 0
for digit in n:
    if digit == '4' or digit == '7':
        count += 1

m = True
for digit in str(count):
    if digit != '4' and digit != '7':
        m = False
        break

if m and count > 0:
    print("YES")
else:
    print("NO")
