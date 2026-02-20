n=int(input())
arr=[]
a=1
for i in range(n):
    m=int (input())
    arr.append(m)
for i in range(n-1):
    if arr[i]!=arr[i+1]:
        a+=1
print(a) 
