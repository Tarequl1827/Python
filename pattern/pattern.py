#pattern

#type - 1
for i in range(5):
    for j in range(1,6):
        print(j, end=" ")
    print()

#type - 2
for i in range(5):
    for j in range(1,i+2):
        print(j, end=" ")
    print()

#type - 3
for i in range(5):
    for j in range(1,i+2):
        print("*", end=" ")
    print()

#type - 4
for i in range(1,6):
    for j in range(1,i+1):
        print(i, end=" ")
    print()

#type - 5
for i in range(5,0,-1):
    for j in range(1,i+1):
        print("*", end=" ")
    print()

#type - 6
for i in range(1,6):
    for j in range(6,i,-1):
        print("*", end=" ")
    print()

#type - 7
for i in range(5,0,-1):
    for j in range(1,i+1,):
        print(i, end=" ")
    print()

#type - 8
for i in range(5,0,-1):
    for j in range(1,i+1,):
        print(j, end=" ")
    print()

#type - 9
for i in range(1,5):
    for j in range(5,i,-1):
        print(" ", end=" ")
    for j in range(1,i+1):
        print("*", end=" ")
    print()

#type - 10
for i in range(0,5):
    for j in range(i+1,0,-1):
        print(j, end=" ")
    print()

#type - 11
for i in range(1,6):
    for j in range(1,i+1):
        print("*", end=" ")
    for k in range(5,i,-1):
        print(" ", end=" ")
    print()
for i in range(1,5):
    for l in range(5,i,-1):
        print("*", end=" ")
    for m in range(1,i+1):
        print(" ", end=" ")
    print()

#type - 12
for i in range(1,9):
    for j in range(1,i+1):
        print(i*j, end=" ")
    print()