t = (1, 2, 3, 4, 5)
print(t)

print("Accessing element from tuple:", t[2])

t2 = (6, 7, 8)
t3 = t + t2
print("Tuple after concatenation:", t3)

print("Length of tuple:", len(t3))

print("Count of element 2 in tuple:", t3.count(2))

print("Index of element 4 in tuple:", t3.index(4))

print("Tuple after slicing:", t3[1:5])

print("Reversed tuple:", t3[::-1])