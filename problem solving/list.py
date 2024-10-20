A = ["Ross","Rachel","Monica","Joe"]
#Write a program to swap first and forth element
A[0],A[3] = A[3],A[0]
print(A)
#Write a program to add a new value at second position
A.insert(1,"spider")
#Write a program to delete a value from 3rd position.
A.pop(2)
print(A)

B = [13,7,12,10]
#Write a program to multiply all the numbers in the list
mul = 1
for i in B:
    mul*=i
print(mul)
#Write a program to get the largest number form the list
#type - 1
num = 0
for i in B:
    if num<i:
        num = i
        print(i)
#type - 2
B.sort()
print(B[len(B)-1])
#type - 3
B.sort()
print(B[-1])
#Write a program to get the smallest number from the list
B.sort()
print(B[0])