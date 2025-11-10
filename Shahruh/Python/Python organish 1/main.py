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

# \" Salom \" matnni ortasiga yozish usuli -------------------------------------------------------------
# txt = "We are the so-called \"Vikings\" from the north."
# print(txt)

# \n -- keyingi qatorga qoyish uchun
# txt = "We are the so-called Vikings \n from the north."
# print(txt)

# \r -- ozidan keyingi gapni oqiydi agar gap yoq bolsa odidagi gapni 23ta joyni oqiydi
# txt = "We are the auth so lived so-called Vikings\r from the north."
# print(txt)

# \t -- ortadan probeel ( ___ ) ochadi
# txt = "We are the so-called Vikings\t from the north."
# print(txt)

# \b -- oxiridan 1 ta harf ochiradi
# txt = "We are the so-called Vikings\b from the north."
# print(txt)

# \f -- ♀ qizlar belgisini qoyib beradi
# txt = "We are the so-called Vikings\f from the north."
# print(txt)

# txt = "We are the so-called Vikings \xhh from the north."
# print(txt)


# Boolen operatorlar tekshiruv operatorlari ----------------------------------------------------------------------
# print(10 > 9)
# print(10 == 9)
# print(10 < 9)

# if va else ------------------------------------------------------------------------------------------------------
# a = 200
# b = 33
# if b > a:
#   print("b is greater than a")
# else:
#   print("b is not greater than a")

# print(bool('Hello'))
# print(bool("15"))

# a = bool(False)
# b = bool(None)
# c = bool(0)
# d = bool("")
# e = bool(())
# f = bool([])
# g = bool({})

# print(a, b, c, d, e, f, g)

# class myclass():
#   def __len__(self):
#     return 2

# myobj = myclass()
# print(bool(myobj))

# def myFunction() :
#   return True

# print(myFunction())

# def myFunction() :
#   return True

# if myFunction():
#   print("YES!")
# else:
#   print("NO!")

# x = 200
# print(isinstance(x, int))

# sum1 = 100 + 50      # 150 (100 + 50)
# sum2 = sum1 + 250    # 400 (150 + 250)
# sum3 = sum2 + sum2   # 800 (400 + 400)

# sum1 = 100 / 50      # 150 (100 + 50)
# sum2 = 5 % 2    # 400 (150 + 250)
# sum3 = 2 **3   # 800 (400 + 400)
# sum4 = 6 // 3   # 800 (400 + 400)

# print(sum1, sum2, sum3, sum4)

# x = 15
# y = 4

# print(x + y)
# print(x - y)
# print(x * y)
# print(x / y)
# print(x % y)
# print(x ** y)
# print(x // y)

# x = 12
# y = 5

# print(x / y)

# numbers = [1, 2, 3, 4, 5, 6, 7, 100, 1020]
# count = len(numbers)
# if count > 3:
#     print(f"List has {count} elements")

# if (count := len(numbers)) > 3:
#     print(f"List has {count} elements")

# x = 5
# print(x)
# x+=3
# print(x)
# x-=3
# print(x)
# x*=3
# print(x)
# x/=3
# print(x)
# x%=3
# print(x)
# x&=3
# print(x)
# x//=3
# print(x)
# x**=3
# print(x)
# x|=3
# print(x)
# x^=3
# print(x)
# x>>=3
# print(x)
# x<<=3
# print(x)

# x= 5
# y = 4
# print(x!=y)
# print(x==y)
# print(x>=y)
# print(x<=y)

# x = 5

# print(1 < x < 10)

# print(1 < x and x < 10)

# x = ["apple", "banana"]
# y = ["apple", "banana"]
# z = x

# print(x is z)
# print(x is y)
# print(x == y)

# x = ["apple", "banana"]
# y = ["apple", "banana"]

# print(x is not y)

# x = [1, 2, 3]
# y = [1, 2, 3]

# print(x == y)
# print(x is y)

# fruits = ["apple", "banana", "cherry"]

# print("pineapple" not in fruits)

# text = "Hello World"

# print("H" in text)
# print("hello" in text)
# print("z" not in text)

# a = str("Hello World")
# print(a.isalpha())

# yosh = input("Yoshinngizni yozing: ")
# ism = input("Isminggizni yozing: ")
# sonmi = yosh.isalnum()
# ism2 = str(ism).strip()
# print(ism2)
# harf = ism2.isalpha()

# mal = dict(name=b , age=a)

# if harf == True and sonmi == True:
#     print(f"Sizning yoshinggiz {yosh} va isminggiz {ism.title()}")
# else:
#     print("Isminggizni va Yoshinggizni togri yozing")


a = 5
b = 4

# & -- and
# if a & b: 
#     print("true")

# | -- or
# if a | b: 
#     print("true")

# ^ -- XOR
# if a ^ b: 
#     print("true")

# listlar -------------------------------------------------------------------------------------------
# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["watermelon"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(1, "orange")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)

# ------------------------------------------------------------------------------------------------------

# thislist = ["apple", "banana", "cherry"]
# thislist.pop(1)
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.pop()
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# del thislist

# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#   print(x)

# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#   print(thislist[i])

# thislist = ["apple", "banana", "cherry"]
# i = 0
# while i < len(thislist):
#   print(thislist[i])
#   i = i + 1

# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist]

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#   if "a" in x:
#     newlist.append(x)

# print(newlist)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x for x in fruits if "a" in x] # ichida a harfi borlarni oladi

# print(newlist)