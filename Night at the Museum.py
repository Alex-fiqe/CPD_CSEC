s = input()
p = 0   
t = 0
for ch in s:
    new = ord(ch) - ord('a')  
    diff = abs(new - p)
    t += min(diff, 26 - diff)
    p = new
print(t)
