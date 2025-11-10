# thistuple = ("apple", "banana", "cherry", "apple", "cherry")
# print(thistuple)

# thistuple = ("apple", "banana", "cherry")
# print(len(thistuple))

# thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
# print(thistuple)

# thistuple = ("apple", "banana", "cherry")
# if "apple" in thistuple:
#   print("Yes, 'apple' is in the fruits tuple")

# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)

# print(x)

# fruits = ("apple", "banana", "cherry")

# (green, yellow, red) = fruits

# print(green)
# print(yellow)
# print(red)

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

# (green, yellow, *red) = fruits

# print(green)
# print(yellow)
# print(red)

# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

# (green, *tropic, red) = fruits

# print(green)
# print(tropic)
# print(red)

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1