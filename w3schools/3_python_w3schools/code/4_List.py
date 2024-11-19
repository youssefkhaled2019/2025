
# ==================List============================
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist) 
# print(*thislist) #apple banana cherry
# print(len(thislist)) 
# thislist = list(("apple", "banana", "cherry"))

# print(thislist[1]) 
# print(thislist[-1]) 
# print(thislist[2:5]) 
# print(thislist[-4:-1])

# Change Item Value

# thislist[1] = "blackcurrant"
# thislist[1:3] = ["blackcurrant", "watermelon"] #replace 1,2

# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon"]
#["apple", "blackcurrant", "watermelon", "cherry"]

# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["watermelon"]
# ['apple', 'watermelon']

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")
# ['apple', 'banana', 'watermelon', 'cherry']


# Append 

# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange") # ['apple', 'banana', 'cherry', 'orange']
# thislist.insert(0, "orange") #['orange', 'apple', 'banana', 'cherry']

# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
#['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']
# xx=thislist+tropical
# ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)#['apple', 'banana', 'cherry', 'kiwi', 'orange']

# Remove Specified Item

# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# thislist.pop(0) #remove first item
#  thislist.pop() #Remove the last item:
# thislist.clear()
# del thislist[0]
# del thislist  deleted "thislist" variable 


# for x in thislist:
#   print(x) 

# for i in range(len(thislist)):
#   print(thislist[i]) 

# i = 0
# while i < len(thislist):
#   print(thislist[i])
#   i = i + 1

# [print(x) for x in thislist] #??


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []
# for x in fruits:
#   if "a" in x:
#     newlist.append(x)
# print(newlist)     

# newlist = [x for x in fruits if "a" in x]
# newlist = [x for x in fruits if x != "apple"]   #??
# newlist = [x if x != "banana" else "orange" for x in fruits]  #??
# print(newlist) 

# thislist.sort()
# thislist.sort(reverse = True)

# Sort the list based on how close the number is to 50:
# def myfunc(n):
#   return abs(n - 50)
# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)

# By default the sort() method is case sensitive,
#  resulting in all capital letters being sorted before lower case letters:
# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort()
# thislist.sort(key = str.lower)  #??
# thislist.reverse()

#Copy 
# mylist = thislist.copy()
# mylist = list(thislist)
# mylist = thislist[:]


# Join Lists

# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# list3 = list1 + list2

# for x in list2:
#   list1.append(x)

# list1.extend(list2)  



# List Methods

# Python has a set of built-in methods that you can use on lists.
# Method 	    Description
# append()	    Adds an element at the end of the list
# clear()	    Removes all the elements from the list
# copy()	    Returns a copy of the list
# count()	    Returns the number of elements with the specified value
# extend()	    Add the elements of a list (or any iterable), to the end of the current list
# index()	    Returns the index of the first element with the specified value
# insert()	    Adds an element at the specified position
# pop()	        Removes the element at the specified position
# remove()	    Removes the item with the specified value
# reverse()     Reverses the order of the list
# sort()	    Sorts the list