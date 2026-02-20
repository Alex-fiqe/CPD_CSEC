s=input ()
a=0
b=0
for I in s:
  c=I
  if I==c.lower():
    a+=1
  else:
    b+=1
if a>=b:
  print(s.lower())
else:
  print(s.upper())
  
