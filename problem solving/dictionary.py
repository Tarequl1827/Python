a = {
    "a":1,
    "b":2,
    "c":3,
    "d":4
}
#Write a program to sort a dictionary by value.
a = sorted(a.values())
print(a)
#Write a python script to print a dictionary where the keys are numbers between 1 and 15 and the value are square of keys.
b = {}
for i in range(1,16):
    b[i] = i**2
print(b)
#Write a program to multiply all the items in a dictionary.
mul = 1
for i in a.values():
    mul*=i
print(mul)
#Write a program to sort a dictionary by key
a = sorted(a.keys())
print(a)