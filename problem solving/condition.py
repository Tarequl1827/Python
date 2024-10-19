#Write a program to check if a number is positive.
num = int(input())
if num==0:
    print("number is zero")
elif num>0:
    print("number is positive")
else:
    print("number is negative")
#Write a program to check whether a number is odd or even.
#type - 1
num = int(input())
if num%2==0:
    print("number is even")
else:
    print("number is odd")
#Write a program to create area calculator.
print("""press 1 to get area of square
press 2 to get area of rectangle
press 3 to get area of circle
press 4 to get area of triangle""")
choice = int(input())
base = int(input())
radius = int(input())
height = int(input())
match choice:
    case 1:
        print(height**2)
    case 2:
        print(height*base)
    case 3:
        print(3.1415*radius*radius)
    case 4:
        print(0.5*height*base)
    case _:
        print("choice right number")

#type - 2
print("""press 1 to get area of square
press 2 to get area of rectangle
press 3 to get area of circle
press 4 to get area of triangle""")
choice = int(input())
if choice == 1:
    height = int(input())
    print(height**2)
elif choice ==2:
    base = int(input())
    height = int(input())
    print(height*base)
elif choice == 3:
    radius = int(input())
    print(3.1415*radius*radius)
elif choice ==4:
    base = int(input())
    height = int(input())
    print(0.5*height * base)
else:
    print("choice right number")
#Write a program check whether the passed letter is a vowel or not.
letter = input()
if (letter in "aeiou") or (letter in "AEIOU"):
    print("It is a vowel")
else:
    print("It is not a vowel")
#Write a program to check if a number is a single digit number, 2- digit number and so on,,. up to 5 digit.
#type - 1
num = int(input())
if num<=9 and num>=0:
    print("It's a single digit number")
elif num>9 and num<=99:
    print("It's a 2 digit number")
elif num>99 and num<=999:
    print("It's a 3 digit number")
elif num>999 and num<=9999:
    print("It's a 4 digit number")
elif num>9999 and num<=99999:
    print("It's a 5 digit number")
else:
    print("more than 5 digit number")
#type - 2
num = int(input())
match num:
    case num if num<=9:
        print("It's a single digit number")
    case num if num<=99:
        print("It's a 2 digit number")
    case num if num <= 999:
        print("It's a 3 digit number")
    case num if num <= 9999:
        print("It's a 4 digit number")
    case num if num <= 99999:
        print("It's a 5 digit number")
    case _:
        print("more than 5 digit number")