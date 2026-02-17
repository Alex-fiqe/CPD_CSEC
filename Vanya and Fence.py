a,b=map(int,input().split())
l=list(map(int,input().split()))
for i in range(len(l)):
  if(l[i]>b):
    l[i]=2
  else:
    l[i]=1
print(sum(l))
