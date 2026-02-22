n=int(input())
d=input()
b=0
for i in range(len(d)-1):
  if d[i]==d[i-1]:
    b+=1
print(b)
