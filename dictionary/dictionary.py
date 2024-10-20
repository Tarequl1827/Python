a = {
    "name": "Toriqul Islam",
    "age": 24,
    "department": "computer"
}
print(a)

#list/tuple to dict
d = ["name","age","department"]
b = ["Md. Toriqul Islam",25, "Computer"]
c = dict(zip(d,b))
print(c)

#iteration
print(a["age"])

#for loop for key
for i in a:
    print(i)

#for loop for value
for i in a:
    print(a[i])

#value
for i in a.values():
    print(i)

#key
for i in a.keys():
    print(i)

#item - key + value
for i,j in a.items():
    print(i,"-",j)

#get
print(a.get("age")) #value

#setdefault
print(a.get("age"))

#item
print(a.items())

#key
print(a.keys())

#value
print(a.values())

#copy
b = a.copy()
print(b)

#update
a.update({"address":"bagbari"})
print(a)

#pop
a.pop("age")
print(a)

#popitem
a.popitem()
print(a)

#clear
a.clear()
print(a)

#del
try:
    del a
    print(a)
except:
    print("a dictionary is delete")

#fromkey
x = ("a","b")
y = 2
key = dict.fromkeys(x,y)
print(key)