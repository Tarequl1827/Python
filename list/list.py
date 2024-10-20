a = ["Ironman","Thor","Captain America","Hulk"]
b = ["Spider Man"]
l = [1,2,3,4,5,6]
print(a[2])
print(a[2][:7])
print(a[::2])
print(a[-3])
print(a[::-1]) #reverse
print(a[-1:-4:-1])
l[2:] = [14]
l[len(l):] = [10] #value add
l.sort(reverse=True)
print(l)
#create list
print(list(range(1,5)))
#Iteration using for loop
for i in a:
    print(i)
#Iteration using for loop with range and length function
for i in range(len(a)):
    print(a[i])
#Iteration using while loop
i = 0
while i<(len(a)):
    print(a[i])
    i+=1
#Iteration using short hand for loop
[print(i) for i in a]

#len
print(len(a))

#count
print(a[1].count("o"))

#append/extend/insert
a.append("spider man")
print(a)
a.insert(1,"vision")
print(a)
a.extend("venom")
print(a)

#index
print(a.index("Thor"))

#remove/pop
a.remove("Thor")
print(a)
a.pop(4)
print(a)

#copy
b = a.copy()
print(b)

#sort
a.sort()
print(a)

#reverse
a.reverse()
print(a)

#clear
a.clear()
print(a)

#del
del a
try:
    print(a)
except:
    print("a is not defined")

#list comprehension
#type - 1
l1 = [1,2,3]
l2=[]
for i in l1:
    if i>1:
        l2.append(i)
print(l2)
#type - 2
l3 = [i for i in l1]
print(l3)
#type -3
l4 = [i for i in l1 if i>1]
print(l4)

#multiple list
l = [ [1,2,3,],[4,5,6,],[7,8,9]]
sum = 0
for i in range(3):
    for j in range(3):
        print(l[i][j])
        sum += l[i][j]
print(sum)
print()

#enumerate - value with index no
l2 = [1,2,3,4,5,6]
l1 = list(enumerate(l2))
print(l1)
for i,j in enumerate(l1):
    print("index no is:",i,"value is:",j[1])

#zip
l = ["A","B","C","D"]
l1 = [2,3,4,8]
mapped = zip(l,l1)
print(list(mapped))

#zip with enumerate
for i,(l,l1) in enumerate(zip(l,l1)):
    print(i,l,l1)