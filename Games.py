n=int(input())
home=[]
guest=[]
for _ in range(n):
  h,g=map(int, input().split())
  home.append(h)
  guest.append(g)
  t=0
for i in range(n):
  for j in range(n):
    if (i!=j and home[i]==guest[j]):
      t+=1
print(t)
