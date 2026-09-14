num = [10,20,30]
num.append(40)
print(num)

num = [10,20,30]
num.insert(3,40)
print(num)

List1 = [10,20,30]
list2=[40,50,60]
List1.extend(list2)
print(List1)

num = [10,20,30,40]
num.remove(40)
print(num)


num = [10,20,30,40]
x = num.pop(3)
print(x)

num = [10,20,30]
num.clear()
print(num)

name = ["Ajay","Nippu","Arya","Khushi"]
print(name.index("Arya"))

num = [10,20,30,10,50,60]
print(num.count(10))
print(num.count(60))

num = [40,10,30,20]
num.sort()
print(num)

num = [10,20,30,40,50,60]
num.reverse()
print(num)

num = [10,20,30,40]
new_num=num.copy()
print(new_num)

