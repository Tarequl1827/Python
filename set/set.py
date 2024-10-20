a = {"Ironman","Hulk","Thor","Captain America"}

#add
a.add("spiderman")
print(a)

#pop
a.pop()
print(a)

#remove
a.remove("spiderman")
print(a)

#discard
a.discard("Hulk")
print(a)

#copy
b = a.copy()
print(b)

#clear
b.clear()
print(b)

a = {"Ironman","Hulk","Thor","Captain America"}
b = {"Superman","Batman","Wonder-Woman"}
c = {"Hulk","Thor","Spiderman"}

#isdisjoint
print(a.isdisjoint(b)) #uncommon

#issubset
print(a.issubset(b))

#issuperset
print(a.issuperset(b))

#updata
a.update(c)
print(a)

a = {"Ironman","Hulk","Thor","Captain America"}
b = {"Superman","Batman","Wonder-Woman"}
c = {"Hulk","Thor","Spiderman"}

#union
print(a.union(b))

#intersection
print(a.intersection(c))
b.intersection_update(c)
print(b)

#difference - (U-A)
print(a.difference(c))
a.difference_update(c)
print(a)

#symmetric_diference
print(a.symmetric_difference(b))
a.symmetric_difference_update(c)
print(a)