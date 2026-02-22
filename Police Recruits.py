n = int(input())
s= map(int, input().split())

hired = 0
missed = 0

for i in s:
    if i > 0:
       hired += i       
    else:  
        if hired:
            hired -= 1    
        else:
            missed += 1  
print(missed)
