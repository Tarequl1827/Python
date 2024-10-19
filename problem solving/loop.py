#Write a program to multiplication table.
#type - 1
num = int(input())
for i in range(1,11,1):
    print(num,"x",i,"=",num*i)
#type - 2
num = int(input())
i=0
while(i<11):
    print(num, "x", i, "=", num * i)
    i+=1
#Write a program to a number pattern.
for i in range(1,6):
    for j in range(1,i+1):
        print(j, end=" ")
    print()

#Write a program to find a sum of all the even numbers up to 50.
#type - 1
add = 0
for i in range(0,51,2):
    add+=i
print(add)
#type - 2
add = 0
i = 0
while i<51:
    add+=i
    i+=2
print(add)
#type - 3
add = 0
i = 0
while True:
    add+=i
    i+=2
    if i>50:
        break
print(add)
#type - 4
add = 0
for i in range(1,51):
    if i%2 ==0:
        add+=i
print(add)
#Write a program to write first 20 numbers and their squared numbers.
for i in range(21):
    print(i**2)
#Write a program to find sum of first 10 odd numbers using while loop.
#type - 1
add = 0
for i in range(1,21,2):
    add+=i
print(add)
#type - 2
add = 0
i = 1
while i<21:
    add += i
    i+=2
print(add)
#Write a program to check if a number is divisible by 8 and 12, up to 100 numbers
for i in range(100):
    if i%8==0 and i%12==0:
        print(i)
#Write a program to crete a billing system at supermarket.

while True:
    name = input("Write customer name: ")
    total = 0
    while True:
        quantity = int(input("Write quantity number: "))
        price = float(input("Write price for every quantity: "))
        total += (price*quantity)
        repeat = input("Other product is available: say(Yes/No)")
        if (repeat == "no") or (repeat =="No"):
            break
    print("-"*40)
    print("Name",name)
    print("Amount to be paid", total)
    print("-"*40)
    print("**************Happy Shopping*****************")
    print("Come Again".center(40,"*"))
    break