a = [1,2,3,4,5]
b = "".join(map(str, a))
b = str(int(b)+1)
c = list(map(int, list(b)))
print(c)