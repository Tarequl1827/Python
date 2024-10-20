a = {"Ironman","Hulk","Thor","Captain America"}
b = {"Superman","Batman","Wonder-Woman"}
c = {"Hulk","Thor","Spiderman"}
d = {1,2,3,4,5,6}

#Write a program to find max and min in a set.
#type - 1
li = sorted(list(d),reverse=True)
print(li[0])
print(li[len(li)-1])
#type - 2
print(max(d))
print(min(d))

#Write a program to find common elements in three lists using sets.
c1 = a.intersection(c)
c2 = c1.intersection(b)
print(c2)

#Write a program to find difference between two sets.
print(a.difference(c))

#Write a Python program to remove an item from a set if it is present in the set.
a.remove("Thor")
print(a)
c.discard("Thor")
print(c)

#Write a Python program to check if a set is a subset of another set.
print(a.issuperset(c))