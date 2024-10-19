#Write a program to display a person's name, age and address in three different lines.
#type - 1
print("person name is",input())
print("Person age is", int(input()))
print("Person address is", input())
#type - 2
name = input()
age = int(input())
address = input()
print("Person name is:", name)
print("Person age is:", age)
print("Person address is:", address)
#type - 3
name, address = input().split()
age = int(input())
print("Person name is:", name)
print("Person age is:", age)
print("Person address is:", address)
#Write a program to swap two variables.
#type - 1
var1 = int(input())
var2 = int(input())
var1, var2 = var2, var1
print(var1,var2)
#type - 2
var1 = int(input())
var2 = int(input())
print(var1, var2)
var = None
var = var1
var1 = var2
var2 = var
print(var1,var2)
#Write a program to convert a float into integer.
#type - 1
num = float(input())
print(int(num))
#type - 2
num = float(input())
con = int(num)
print(con)
#Write a program to take details from a student for ID-card and then print it in different lines.
#type - 1
name, grade, email, address = input().split()
print(name)
print(grade)
print(email)
print(address)
#Write a program to take an user input as integer then convert to float.
num = int(input())
print(float(num))