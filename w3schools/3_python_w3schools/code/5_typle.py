# =================================Tuples====================================
# A tuple is a collection which is ordered and unchangeable.
# Tuple items are [ordered], [unchangeable], and [allow duplicate] values.
# Tuple items are indexed, the first item has index [0], the second item has index [1]
# Ordered
   # When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
# Unchangeable
   # Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.


# mytuple = ("apple", "banana", "cherry", "apple", "cherry")
# # tuple1 = ("abc", 34, True, 40, "male") 

# # thistuple = ("apple",) # a tuple
# # print(type(thistuple))
# # thistuple = ("apple") #NOT a tuple
# # print(type(thistuple)) 

# # thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets

# # Access Tuple Items
# print(mytuple[1])
# print(mytuple[-1])
# print(mytuple[2:5])
# print(mytuple[-4:-1])


# thistuple = ("apple", "banana", "cherry")
# if "apple" in thistuple:
#   print("Yes, 'apple' is in the fruits tuple") 



# # Update Tuples
# # Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.
# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)
# print(x)

# # Add Items
# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.append("orange")
# thistuple = tuple(y)
# # or
# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y

# print(thistuple)


# # Remove Items
# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.remove("apple")
# thistuple = tuple(y)
# # or
# thistuple = ("apple", "banana", "cherry")
# del thistuple
# print(thistuple) #this will raise an error because the tuple no longer exist








# When we create a tuple, we normally assign values to it. This is called "packing" 
# fruits = ("apple", "banana", "cherry") #packing
# we are also allowed to extract the values back into variables. This is called "unpacking":
# (green, yellow, red) = fruits

# Note: The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.
# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# (green, yellow, *red) = fruits #??

# If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.
# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
# (green, *tropic, red) = fruits #??
# print(green)
# print(tropic)
# print(red)





# Loop Through a Tuple
# thistuple = ("apple", "banana", "cherry")
# for x in thistuple:
#   print(x) 

# for i in range(len(thistuple)):
#   print(thistuple[i]) 

# i = 0
# while i < len(thistuple):
#   print(thistuple[i])
#   i = i + 1   


# Join Two Tuples
# tuple1 = ("a", "b" , "c")
# tuple2 = (1, 2, 3)
# tuple3 = tuple1 + tuple2  #??


fruits = ("apple", "banana", "cherry")
# mytuple = fruits * 2 #Multiply Tuples


print(fruits.count("apple"))
print(fruits.index("apple"))