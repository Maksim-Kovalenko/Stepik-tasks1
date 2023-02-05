d = "12 -5 10.5 83"
d = list(filter(lambda x: not '.' in x,d.split()))
c = list(map(int,d))

print(c)