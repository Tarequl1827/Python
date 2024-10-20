a = "Hello",1,2
print(type(a))

b = ("Hello",1,4)
print(type(b))

c = ("Hello , ")
print(type(c))

d = (1,2,3,4,5,6)

#slicing
print(a[1])
print(a[0][2])
print(a[::-1])
#list inside tuple
d = (1,[2,3])
d[1][1]=8 #list is mutable
print(d)

#iterate
#type - 1
A = (11,12,13,14,15,16)
for i in A:
    print(i)
#type - 2
for i in range(len(A)):
    print(A[i])
#type - 3
i = 0
while i<len(A):
    print(A[i])
    i+=1

#index
print(a.index("Hello"))

#count
print(a[0].count("l"))

#value add by list
h = list(A)
h.append("Spider")
i = tuple(h)
print(i)

#sort
B = (1,2,3,4,5)
print(B)
C = sorted(B,reverse=True)
print(C)