# TUPPLE

num = (10,20,10,40,10,60)
print(num.count(10))

name = ("ajay","Nippu","Arya","Khushi")
print(name.index("Khushi"))

# SET

num = {10,20,30,20,40}
print(num)

# Method

a = {1,2,3,4}
a.add(5)
print(a)

a = {1,2,3,4}
a.update([5,6,7])
print(a)

a = {1,2,3,4,5}
a.remove(5)
print(a)

a = {1,2,3,4,5}
a.discard(5)
print(a)

a = {1,2,3,4,5,8}
x = a.pop()
print(x)
print(a)

a = {1,2,3,4,5}
a.clear()
print(a)

a = {1,2,3,4,5}
b = {4,5,6,7,8}
print(a.union(b))

a = {1,2,3,4,5}
b = {4,5,6,7,8}
print(a.difference(b))




