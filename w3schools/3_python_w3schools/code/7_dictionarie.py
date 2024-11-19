# ===================Dictionary=========================
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
thisdict["brand"]
# When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.
# Unordered means that the items do not have a defined order, you cannot refer to an item by using an index.
# Duplicates Not Allowed

# xx = dict(name = "John", age = 36, country = "Norway")

x = thisdict["model"]
 #thisdict.get("model")

# thisdict.keys()  
# thisdict.values() 
# thisdict.items()

# Change Values
thisdict["color"] = "white"
# The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.
thisdict.update({"year": 2020}) 

# Adding Items
thisdict["color_xx"] = "red"

# Removing Items
thisdict.pop("model")
del thisdict["model"]
del thisdict["model"]



for x in thisdict:
  print(thisdict[x]) 

for x in thisdict.values():
  print(x) 

for x in thisdict.keys():
  print(x) 

for x, y in thisdict.items():
  print(x, y)


# copy
mydict = thisdict.copy()  
mydict = dict(thisdict)


# Nested Dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
# or
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
} 


#  print(myfamily["child2"]["name"]) 

# Loop Through Nested Dictionaries
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])

# Dictionary Methods
# Method 	    Description
# clear()	    Removes all the elements from the dictionary
# copy()	    Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	        Returns the value of the specified key
# items()	    Returns a list containing a tuple for each key value pair
# keys()	    Returns a list containing the dictionary's keys
# pop()	        Removes the element with the specified key
# popitem()	    Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	    Updates the dictionary with the specified key-value pairs
# values()	    Returns a list of all the values in the dictionary
