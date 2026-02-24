from math import gcd
y, w = map(int, input().split())
m = max(y, w)
a = 7 - m 
b = 6        
g = gcd(a, b)
print(a//g, "/", b//g, sep="")
