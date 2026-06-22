n=int(input())
for _ in range(n):
    q=int(input())
    s,t=map(str,input().split())
    s=sorted(s)
    t=sorted(t)
    if s==t:
        print("Yes")
    else:
        print("No")
    
