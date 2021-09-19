x=[12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 30, 32, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5]
v=sum(x)
print(v/24)
print(max(x), min(x))
print("La ora", x.index(max(x))+1, "este inregistrat temperatura maxima")
print("La ora",x.index(min(x))+1,"este inregistrat temperatura minima")
