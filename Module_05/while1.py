# Write a program to print all number 1 to N

# num = int (input ("Enter a Number :"))
# i = 1 
# while i <= num :
#     print (i)
#     i= i+1

# Write a program to print all numbers from N to 1

# num = int (input("Enter a Number :"))
# while num >=1 :
#     print (num)
#     num = num-1

# Write a program to count the total digit in a number

# num = int(input("Enter a Number :"))
# count = 0   
# while num > 0 :
#     count = count+1
#     num = num//10
# print  (count)

# Write a python program to calculate the sum of digit of a Number


# num = int(input("Enter a Number :"))
# sum = 0 
# while num > 0 :
#     digit = num %10
#     sum = sum+digit
#     num = num // 10
# print ("SUM :",sum)

# Write a program to calculate the product of digits of a number


# num = int(input("Enter a Number :"))
# product = 1
# while num>1 :
#     digit = num %10
#     product = product * digit 
#     num = num//10
# print ("PRODUCT :", product)

# Writw a program to Reverse a Number : 


# num = int(input("Enter a Number :"))
# rev = 0 
# while num > 0:
#     digit = num  % 10 
#     rev = rev * 10 + digit
#     num = num // 10 
# print ("Reverse :",rev)


# Writw a program to Reverse a Number (Leading zero) 

# num = (input("Enter a Number :"))
# rev = ""
# i = len(num)-1
# while i >=0:
#     rev = rev+num[i]
#     i = i-1
# print (rev)

# Write a program all alpphabet from A to Z

# ch=ord('A')
# while ch <= ord('Z'):
#     print (chr(ch))
#     ch=ch+1


# write a program to print all ASCII valu of A to E

# ch=ord('A')
# while ch <= ord('E'):
#     print (chr(ch),"=",ch)
#     ch=ch+1

# write a program to calulate the sum of all numbers from 1 to 20

i = 20 
sum=0
while i<=20:
    sum=sum+i
    i=i+2
print ("SUM",sum)
