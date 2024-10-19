a = "hello"
b = "123Hello"
c = "123456"
d = "HELLO"
e = " "
f = "Hello 123"
g = "1.234"
h = "Why fit in, When you are Born to Stand Out!"
i = "     hello\tworld       "
j = "     hello\nworld       "

#capitalize - first character capital
print(a.capitalize())

#casefold - every word first character small
print(h.casefold())

#title - every word first character capital
print(h.title())

#lower - every character small
print(d.lower())

#upper - every character upper
print(a.upper())

#islower - if every character small return True
print(a.islower())
print(h.islower()) #False for space

#istitle
print(d.istitle())
print(f.istitle())

#isupper - if every character capital return True
print(d.isupper())
print(h.isupper())

#isalpha - only alphabate return Turn
print(b.isalpha())
print(a.isalpha())

#isalnum - if alphabate+number return Turn
print(b.isalnum())
print(f.isalnum())

#swapcase - small convert capital and capital convert small
print(a.swapcase())
print(d.swapcase())

#isdigit/isdecimal/isnumeric - number
print(b.isdigit())
print(g.isdigit()) #False for point
print(c.isdigit())

#center
print(a.center(20,"*"))

#ljust
print(a.ljust(20,"*"),"world")

#rjust
print("world", a.rjust(10,"*"))

#expandtabs - \t => tab size
print(i.expandtabs(20))

#format
print("{} world".format(a))

#count
print(h.count("o"))
print(h.count("o",6,10))

#startswith
print(h.startswith("Why"))
print(h.startswith("Why",10,30))

#endswith
print(h.endswith("to"))
print(h.endswith("to",20,40))

#find/index
print(h.find("o"))
print(h.rfind("o"))
print(h.index("o"))
print(h.rindex("o"))
print(h.find("hello"))
try:
    print(h.index("hello"))
except:
    print("error")

#replace
print(a.replace("l","o"))

#split/partition
print(h.split()) #list
print(h.partition(" ")) #tuple but one time
print(h.rsplit())
print(h.rpartition(" "))
print(j.splitlines())

#strip
print(i.strip())
print(a.strip("o"))

#isspace
print(h.isspace())
print(e.isspace())

#isprintable
print(i.isprintable()) #escape is not printable
print(h.isprintable())

#isidentifier
print(a.isidentifier())
print(b.isidentifier())

#encode
print(a.encode('ascii','ignor'))

#zfill
print(a.zfill(20))

#join
print(a.join(d))

#maketrans and translate - equal value and swip
A = "abc"
B = "def"
table = A.maketrans(A,B)
print("ba".translate(table))