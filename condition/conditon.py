#only if
a = 10
if a==10:
    print(True)

#if else
a = 10
if a!=10:
    print(True)
else:
    print(False)

#if elif else
a = 10
if 10<a and a>0:
    print(True)
elif 20<a and a>10:
    print(True)
else:
    print(False)

#nested statement
a = 10
if a>0:
    if 10 < a and a > 0:
        print(True)
    elif 20 < a and a > 10:
        print(True)
    else:
        print(False)
else:
    print(False)

#short hand if
if a>10:print(True)

#short hand if else
print(True) if a>10 else print(False)

#match
match a:
    case a if a>0:
        print(True)
    case 10:
        print(True)
    case _: #default
        print(False)