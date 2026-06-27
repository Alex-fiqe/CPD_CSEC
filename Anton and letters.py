n = input().strip()
n = n.replace("{", "").replace("}", "").replace(",", "").replace(" ", "")
if n == "":
    print(0)
else:
    print(len(set(n)))
