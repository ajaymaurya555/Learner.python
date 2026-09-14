student ={
    "Name":"Ajay kr. Maurya",
   "Age": 20,
    "City":"Blp",
    "Skills": ["HTML", "CSS", "Python"]
}

print(type(student))
print(student)

# DECTNORY METHOD

# 1. Safely get value by key. Agar key nahi miltahai to default value (None) return karega

print(student.get("Name"))
print(student.get("City"))
print(student.get("Education"))


# 2. Returns All keys

print(student.keys())

# 3. Return All values


print(student.values())

# 4. Return key- values pairs

print(student.items())

# 5. Agr dect mein hai vo key value pairs to update karega
#  Agaar nahi hai to New key Values Pairs Add kardega. 

student.update({"Name": "Nippu Paswan","Grade": "A"})
print (student)


# 6. Remove key and returns its value


student.pop("Grade")
print(student)

# 7. Remove last insarted value pairs.

student.popitem()
print(student)

# 8. Remove All items in Dect .

student.clear()
print(student)

# 9. Make a Shallow copy 

New_student = student.copy()
print(student)

# 10. If key exits, return . if not,insert with default
student.setdefault("Grade","A")

student.setdefault("Name","XYZ")
print (student)



