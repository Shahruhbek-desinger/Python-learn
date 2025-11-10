# thisset = {"apple", "banana", "cherry"}
# print(thisset)

# thisset = {"apple", "banana", "cherry"}
# thisset.remove("banana")
# print(thisset)

# thisset = {"apple", "banana", "cherry"}
# thisset.discard("banana")
# print(thisset)

# thisset = {"apple", "banana", "cherry"}
# x = thisset.pop()
# print(x)
# print(thisset)

# thisset = {"apple", "banana", "cherry"}
# thisset.clear()
# print(thisset)

# thisset = {"apple", "banana", "cherry"}
# del thisset
# print(thisset)

# thisset = {"apple", "banana", "cherry"}
# for x in thisset:
#   print(x)

# set1 = {"a", "b", "c", "d", "e"}
# set2 = {1, 2, 3, 4, 5, 6, 7, 8}
# set3 = set1.union(set2)
# print(set3)

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = set1 | set2
# print(set3)

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = {"John", "Elena"}
# set4 = {"apple", "bananas", "cherry"}
# myset = set1.union(set2, set3, set4)
# print(myset)

# x = {"a", "b", "c"}
# y = (1, 2, 3)
# z = x.union(y)
# print(z)

# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}
# set1.update(set2)
# print(set1)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.intersection(set2)
# print(set3)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1 & set2
# print(set3)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set1.intersection_update(set2)
# print(set1)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.difference(set2)
# print(set3)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1 - set2
# print(set3)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.symmetric_difference(set2)
# print(set3)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1 ^ set2
# print(set3)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set1.symmetric_difference_update(set2)
# print(set1)

# x = frozenset({"apple", "banana", "cherry"})
# print(x)
# print(type(x))

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict["brand"])

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2020
# }
# print(thisdict)

# thisdict = dict(name = "John", age = 36, country = "Norway")
# print(thisdict)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict["model"]
# x = thisdict.keys()
# print(x)

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
# x = car.keys()
# print(x) #before the change
# car["color"] = "white"
# print(x) #after the change

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
# x = car.values()
# print(x) #before the change
# car["year"] = 2020
# print(x) #after the change

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# if "model" in thisdict:
#   print("Yes, 'model' is one of the keys in the thisdict dictionary")

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["year"] = 2018

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.pop("model")
# print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)