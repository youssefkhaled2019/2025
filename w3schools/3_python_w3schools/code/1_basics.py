# import sys
# print(sys.version)
# >>> python python.py

# import platform
# x = platform.system()
# x = dir(platform)
# print(x) 
# ==============================================
# x = str(3)    # x will be '3'
# y = int(3)    # y will be 3
# z = float(3)  # z will be 3.0 
# c = complex(x)
# bool("Hello")
# x = 1    # int
# y = 2.8  # float
# z = 1j   # complex #3+5j
# x = 35e3   # <class 'float'>
# y = 12E4   # <class 'float'>
# x, y, z = "Orange", "Banana", "Cherry"
# x = y = z = "Orange"
# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits
# ==============================================
# x = "awesome"
# def myfunc():
#   x = "fantastic"
#   print("Python is " + x)
#   myfunc()
# print("Python is " + x) 

# x = "awesome"
# def myfunc():
#   global x
#   x = "fantastic"
# myfunc()
# print("Python is " + x) 




# def myfunc():
#   global x
#   x = "fantastic"
# myfunc()
# print("Python is " + x)
# ====================modules==========================


import mymodule
import mymodule as mx
from mymodule import person1

mymodule.greeting("Jonathan")
a = mymodule.person1["age"]
print(a) 

a = mx.person1["age"]

print (person1["age"])
# ==============================================
# import random
# print(random.randrange(1, 10)) 


# ==============================================
# Text Type: 	    str
# Numeric Types: 	int, float, complex
# Sequence Types: 	list, tuple, range
# Mapping Type: 	dict
# Set Types: 	    set, frozenset
# Boolean Type: 	bool
# Binary Types: 	bytes, bytearray, memoryview
# None Type: 	    NoneType


# x = range(6) #range
# x = b"Hello" 	#bytes
# x = bytearray(5) 	#bytearray
# x = memoryview(bytes(5)) 	#memoryview
# x = None 	#NoneType
# x = ("apple", "banana", "cherry") 	tuple
# x = {"name" : "John", "age" : 36} 	dict
# x = {"apple", "banana", "cherry"} 	set

# x = complex(1j) 	complex
# x = list(("apple", "banana", "cherry"))
# x = tuple(("apple", "banana", "cherry"))
# x = dict(name="John", age=36)
# x = set(("apple", "banana", "cherry"))
# x = bool(5)
# x = frozenset({"apple", "banana", "cherry"}) 	frozenset
# x = bytearray(5) 	                            bytearray
# x = memoryview(bytes(5)) 	                    memoryview
# x = None 	                                    NoneType
# x = bytes(5) 	#bytes


# =======================bool=======================
# print(bool(False)) #False
# print(bool(None))#False
# print(bool(0))#False
# print(bool(""))#False
# print(bool(()))#False
# print(bool([]))#False
# print(bool({}))#False

# class myclass():
#   def __len__(self):
#     return 0
# myobj = myclass()
# print(bool(myobj))#False


# x = 200
# y="200"
# print(isinstance(x, int))#True    #??
# print(isinstance(y, int))#False
# ======================if-else========================

a = 200
b = 33
c = 500

# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")
# else:
#   print("a is greater than b")


# if a > b: print("a is greater than b") 

# print("A") if a > b else print("B") 

# print("A") if a > b else print("=") if a == b else print("B") 

# if a > b and c > a:print("Both conditions are True")

# if a > b or a > c:print("At least one of the conditions is True")

# if not a > b:print("a is NOT greater than b")

# if b > a:pass
# =======================while=======================
# i = 1
# while i < 6:
#   print(i)
#   if i == 2:
#     print(i)
#     continue
#   if i == 3:
#     print(i)
#     break
#   i += 1 
# else:
#   print("i is no longer less than 6")  
# ======================for========================
# fruits = ["apple", "banana", "cherry"]
# adj = ["red", "big", "tasty"]

# for x in fruits:
#   if x == "banana":
#     break
#   if x == "apple":
#     continue
#   print(x)

# for x in range(6):#range(2, 30, 3)
#   print(x)

# for x in range(6):
#   if x == 3: break
#   print(x)
# else:
#   print("Finally finished!") 

# for x in adj:
#   for y in fruits:
#     print(x, y)
# ====================== try-except ========================
# try:
#   print(x)
# except:
#   print("An exception occurred") 


# try:
#   print(x)
# except NameError:
#   print("Variable x is not defined")
# except:
#   print("Something else went wrong")   


# try:
#   print("Hello")
# except:
#   print("Something went wrong")
# else:
#   print("Nothing went wrong")  

# try:
#   print(x)
# except:
#   print("Something went wrong")
# finally:
#   print("The 'try except' is finished") 


# x = -1
# if x < 0:
#   raise Exception("Sorry, no numbers below zero")  #??  

# x = "hello"
# if not type(x) is int:
#   raise TypeError("Only integers are allowed")