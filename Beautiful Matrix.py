def mod (n):
    if n == 1 :
        return (2)
    elif n==2 :
        return(1)
    else:
        return (n%3)
for i in range(1,6):
    lis=list(map(int,input().split()))
    if 1 in lis:
        moves= mod(i)+mod((lis.index(1)+1))
        break
print(moves)
