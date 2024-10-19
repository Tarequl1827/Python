# Arithmetic Operator

# addition
print(3 + 2)  # 5

# subtraction
print(3 - 2)  # 1

# multiplication
print(3 * 2)  # 6

# division
print(3 / 2)  # 1.5

# modulus
print(3 % 2)  # 1

# floor division
print(3 // 2)  # 1

# exponentiation
print(3 ** 2)  # 9

# Comparison Operator

# less than
if 3 < 2:
    print(True)
else:
    print(False)

# less than or equal
if 3 <= 2:
    print(True)
else:
    print(False)

# greater than
if 3 > 2:
    print(True)
else:
    print(False)

# greater than or equal
if 3 >= 2:
    print(True)
else:
    print(False)

# equal
if 3 == 2:
    print(True)
else:
    print(False)

# not equal
if 3 != 2:
    print(True)
else:
    print(False)

# logical Operator

# and
if 3 > 2 and 3 > 5:
    print(True)
else:
    print(False)

# or
if 3 > 2 or 3 > 5:
    print(True)
else:
    print(False)

# not
if not (3 > 2 and 3 > 5):
    print(True)
else:
    print(False)

# Assignment operator

# equl
num = 10

# plus and equal
num += 5  # num = num + 5

# minus and equal
num -= 5  # num = num - 5

# multiple and equal
num *= 5  # num = num * 5

# Identity operator

# is and is not
a = 123
b = "123"
print(a is b)  # false => a is int but b is str
print(a is not b)  # true => a is int but b is str

# Bitwise operator

# and
a = 10  # Ob1010
b = 8  # Ob1000
print(a & b)  # 1000 =>8 (1 value is 0,output will be 0)

# or
a = 10  # Ob1010
b = 8  # Ob1000
print(a | b)  # 1010 =>10 (1 value is 1,output will be 1)

# xor
a = 10  # Ob1010
b = 8  # Ob1000
print(a ^ b)  # 1000 =>8 (similar value will be 0)

# <<
a = 10  # Ob1010
print(a >> 2)  # 0010

# >>
a = 10  # Ob1010
print(a << 2)  # 101000

# Membership operator

# in and not in
a = "Hello"
print("e" in a)  # ture
print("a" in a)  # false
print("e" not in a)  # false
print("a" not in a)  # ture