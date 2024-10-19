# Write a program to get Fibonacci series up to 10 numbers
# type - 1
sum = 0
i = 1
print(sum, end=" ")
for n in range(11):
    sum1 = sum + i
    print(sum1, end=" ")
    i = sum
    sum = sum1
print()


# type - 2
def fact(sum, i):
    print(sum, end=" ")
    for n in range(11):
        sum1 = sum + i
        print(sum1, end=" ")
        i = sum
        sum = sum1


fact(0, 1)
# Write a program to check if a number is prime or not
n = int(input())
for i in range(2, n):
    if n % i == 0:
        print("not prime number")
        break
else:
    print("prime number")
# Write a program to find a palindrome of integers
n = int(input())
m = list(str(n))
m.reverse()
o = "".join(m)
p = int(o)
if n == p:
    print("palindrome")
else:
    print("not palindrome")

# type - 2
num = int(input())
temp = num
rev = 0
while num > 0:
    dig = num % 10
    rev = rev * 10 + dig
    num = num // 10
if rev == temp:
    print("palindrome")
else:
    print("not palindrome")
# Write a program to create an area calculator
print("""press 1 to get area of square
press 2 to get area of rectangle
press 3 to get area of circle
press 4 to get area of triangle""")
choice = int(input())
if choice == 1:
    height = int(input())
    print(height ** 2)
elif choice == 2:
    base = int(input())
    height = int(input())
    print(height * base)
elif choice == 3:
    radius = int(input())
    print(3.1415 * radius * radius)
elif choice == 4:
    base = int(input())
    height = int(input())
    print(0.5 * height * base)
else:
    print("choice right number")

# Write a program to separate the following string into comma separated values.
A = "OOTD.YOLO.ASAP.BRB.GTG.OTW"
print(A.split("."))

# Write a program to sort strings alphabetically in python.
print(sorted(A))

# Write a program to remove dot from the following string.
print(A.replace(".", " "))

# Write a program to check the number of occurrence of a substring in a string.
print(A.count("O"))

# Take an input from a user as a string then, reverse it.
str = input()
print(str[::-1])

# Write a program to check if a string is palindrom.
str = input()
rev = str[::-1]
if str == rev:
    print("it's palindrom")
else:
    print("it's not palindrom")

# Write a program to find number of vowels in a string.
str = input()
vowel = 0
for i in str:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
        vowel = +1