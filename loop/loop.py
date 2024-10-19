#loop

#for
for i in range(1,10,2): #range(starting point, ending point, step)
    print(i)

#while
i=1
while(i<11):
    print(i)
    i+=2

#while true
while True:
    num1 = int(input())
    num2 = int(input())
    print(num2+num1)
    repeat = input()
    if repeat == "yes":
        break

#nested loop
for i in range(5):
    for j in range(3):
        print(j)

#break
for i in range(5):
    if i==3:
        break

#continue
for i in range(5):
    if i==3:
        continue