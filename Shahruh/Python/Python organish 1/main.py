# x = 5
# y = "John"
# print(x, end=" ")
# print(y)

# x = "Sally" # x is now of type str
# x = 4       # x is of type int
# print(x)

# x = str(3)    # x will be '3'
# y = int(3)    # y will be 3
# z = float(321346/10)  # z will be 3.0
# print(x, y, z)

# x = 5
# y = "John"
# print(type(x))
# print(type(y))

# myvar = "John"
# my_var = "John"
# _my_var = "John"
# myVar = "John"
# MYVAR = "John"
# myvar2 = "John"

# Har biri indexlanadi:
# x, y, z = "Orange", "Banana", "Cherry"
# print(x)
# print(y)
# print(z)

# x = y = z = "Orange"
# print(x)
# print(y)
# print(z)

# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits
# print(x)
# print(y)
# print(z)

# x = "Python is awesome"
# print(x)

# x = "Python"
# y = "is"
# z = "awesome"
# print(x, y, z)

# x = "Python "
# y = "is "
# z = "awesome"
# print(x + y + z)

# x = 5
# y = 10
# print(x + y)

# x = 5
# y = "John"
# print(x, y)

# Funksiyani Chaqirish uchun har doim funksiyani oxiriga chaqirilgan funksiyani yozish kerak !!!

# x = "awesome"

# def myfunc():
#   print("Python is " + x)

# myfunc()

# x = input()

# def myfunc():
#    print("Python is " + x)

# myfunc()

# x = "awesome"

# def myfunc():
#   x = "fantastic"
#   print("Python is " + x)

# myfunc()

# print("Python is " + x)

# def myfunc():
#   global x #golbal funksiyadan chiqib ishga tushadi
#   x = "fantastic"

# myfunc()

# print("Python is " + x)

# x = "awesome"

# def myfunc():
#   global x
#   x = "fantastic"

# myfunc()

# print("Python is " + x)

# x = complex(5.265465)
# print(x)

# MAlumotlarrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr ======================================================================================================================

# # 1. String
# x = str("Hello World")
# print("str:", x, type(x))

# # 2. Integer
# x = int(20)
# print("int:", x, type(x))

# # 3. Float
# x = float(20.5)
# print("float:", x, type(x))

# # 4. Complex
# x = complex(1j)
# print("complex:", x, type(x))

# # 5. List
# x = list(("apple", "banana", "cherry"))
# print("list:", x, type(x))

# # 6. Tuple
# x = tuple(("apple", "banana", "cherry"))
# print("tuple:", x, type(x))

# # 7. Range
# x = range(6)
# print("range:", list(x), type(x))  # list qilib chiqaramiz

# # 8. Dictionary
# x = dict(name="John", age=36)
# print("dict:", x, type(x))

# # 9. Set
# x = set(("apple", "banana", "cherry"))
# print("set:", x, type(x))

# # 10. Frozenset
# x = frozenset(("apple", "banana", "cherry"))
# print("frozenset:", x, type(x))

# # 11. Boolean
# x = bool(5)
# print("bool:", x, type(x))

# # 12. Bytes
# x = bytes(5)
# print("bytes:", x, type(x))

# # 13. Bytearray
# x = bytearray(5)
# print("bytearray:", x, type(x))

# # 14. Memoryview
# x = memoryview(bytes(5))
# print("memoryview:", x, type(x))

# ===============================================================================================================================================================================================================

# x = 35e3
# y = 12E4
# z = -87.7e100

# print(type(x))
# print(type(y))
# print(type(z))

# import -chaqirib olish random -- randomni tanlash --------------------------------------------------
# import random

# print(random.randrange(1, 1000000))

#----------------------------------------------------------------------------------------------------

# print("Hello")
# print('Hello')

# print("It's alright")
# print("He is called 'Johnny'")
# print('He is called "Johnny"')

#Kattaroq matnlar uchhun """""" 3 ta oldiga 3 ta orqaga yoziladi ---------------------------------------
# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# print(a)

# a = '''Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua.'''
# print(a)

#---------------------------------------------------------------------------------------------------

# a = "Hello, World!"
# print(a[1])

#Matnni harflarga bolib baradi ---------------------------------------------------------------------
# for x in "Nagapee bollo yaxshimisizla nagaplaa yozinglareee":
#   print(x)
#----------------------------------------------------------------------------------------------------

# len -- matnning uzunligini hisoblab beradi --------------------------------------------------------
# a = "Hello, World!"
# print(len(a))
# ---------------------------------------------------------------------------------------------------

# manttinning ichidan sozni qidiriadi ---------------------------------------------------------------
# txt = "The best things in life are 'free'!"
# print("free" in txt)

# txt = "The best things in life are free!"
# print("expensive" not in txt)

# txt = "The best things in life are free!"
# if "expensive" not in txt:
#   print("No, 'expensive' is NOT present.")

# ---------------------------------------------------------------------------------------------------

# 2-indexdan boshlab 5 indexgacha -------------------------------------------------------------------
# b = "Hello, World!"
# print(b[2:5])

# b = "Hello, World!"
# print(b[:5])

# b = "Hello, World!"
# print(b[2:])

# b = "Hello, World!"
# print(b[-5:-2])

# ---------------------------------------------------------------------------------------------------

# upper -- katta harflar bilan yoiziladi ------------------------------------------------------------
# a = "Hello, World!"
# print(a.upper())

# lower -- kichik harflar bilan yozadi
# a = "Hello, World!"
# print(a.lower())

# strip -- matnni ochiq probel __ joylarini olib tashlaydi
# a = " Hello, World! "
# print(a.strip()) # returns "Hello, World!"

# replace -- matndagi harfni ozgartirib beradi
# a = "Hello, World!"
# print(a.replace("H", "f"))

# returns ['Hello', ' World!']
# a = "Hello, World!"
# print(a.split(",")) 

#  --------------------------------------------------------------------------------------------------

# sozni sozga qoshish  ------------------------------------------------------------------------------
# a = "Hello"
# b = "World"
# c = a + b
# print(c)

# a = "Hello"
# b = "World"
# c = a + " " + b
# print(c)

# ---------------------------------------------------------------------------------------------------


# son bilan matnda yozish  --------------------------------------------------------------------------
# age = 36
# #This will produce an error:
# txt = "My name is John, I am " + age
# print(txt)

#  f -- matnga son yoza oladigan qilib yani ozgaruvchi qoshadigan qilib beradi
# age = 36
# txt = f"My name is John, I am {age}"
# print(txt)

# price = 59
# txt = f"The price is {price} dollars"
# print(txt)

# :.2f -- oxiridan .00 yani /100 ga boladi yoki ikki xona orqaga qaytaradi 
# price = 59
# txt = f"The price is {price:.2f} dollars"
# print(txt)

# txt = f"The price is {20 * 59} dollars"
# print(txt)

# txt = f"The price is {20 * 59:.2f} dollars"
# print(txt)

# ------------------------------------------------------------------------------------------------------