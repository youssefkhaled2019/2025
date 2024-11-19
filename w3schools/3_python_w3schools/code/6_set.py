# ================Sets===============================
# myset = {"apple", "banana", "cherry"} 
# A set is a collection which is unordered, unchangeable*, and unindexed.
# * Note: Set items are unchangeable, but you can remove items and add new items.
# Note: Sets are unordered, so you cannot be sure in which order the items will appear.
# Set items are unordered, unchangeable, and do not allow duplicate values.
# Once a set is created, you cannot change its items, but you can add new items.

# Unordered
# Unordered means that the items in a set do not have a defined order.
# Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
# Unchangeable
# Set items are unchangeable, meaning that we cannot change the items after the set has been created.
# Once a set is created, you cannot change its items, but you can remove items and add new items.

# Duplicates Not Allowed
# Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:
# thisset = {"apple", "banana", "cherry", True, 1, 2}

# print(len(thisset)) 
# set1 = {"abc", 34, True, 40, "male"} 
# thisset = set(("apple", "banana", "cherry")) # note the double round-brackets


# # Access Items
# for x in thisset:
#   print(x) 

# print("banana" in thisset)   
# print("banana" not in thisset) 

# # Add Items
# thisset = {"apple", "banana", "cherry"}
# thisset.add("orange")

# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}
# thisset.update(tropical)

# thisset = {"apple", "banana", "cherry"}
# mylist = ["kiwi", "orange"]
# thisset.update(mylist)


# Remove 
# thisset = {"apple", "banana", "cherry"}
# thisset.remove("banana")# If the item to remove does not exist, remove() will raise an error.

# thisset.discard("banana") # Note: If the item to remove does not exist, discard() will NOT raise an error.


# thisset.pop()
# thisset.clear()
# del thisset

# Join Sets
# The union() and update() methods joins all items from both sets.
# The intersection() method keeps ONLY the duplicates.
# The difference() method keeps the items from the first set that are not in the other set(s).
# The symmetric_difference() method keeps all items EXCEPT the duplicates


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}


print(set1.union(set2)) #{'b', 1, 2, 'c', 3, 'a'}
print(set1 | set2) #{1, 2, 3, 'b', 'a', 'c'}
print(set1.union(set2, set3, set4)) 
print(set1 | set2 | set3 |set4) 

# Note: Both union() and update() will exclude any duplicate items.
x = {"a", "b", "c"}
y = (1, 2, 3)
print(x.union(y))
print(x.update(y))




set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
# Keep ONLY the duplicates
# The intersection() method will return a new set, that only contains the items that are present in both sets.
print( set1.intersection(set2))#{'apple'} 
print(set1 & set2) #The & operator only allows you to join sets with sets, and not with other data types
# The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set
print(set1.intersection_update(set2)) 


# Difference
# The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
print(set1.difference(set2)) #{'banana', 'cherry'} 
print(set1 - set2)#{'banana', 'cherry'} 
# The difference_update() method will also keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set
print(set1.difference_update(set2)) 

# The symmetric_difference() method will keep only the elements that are NOT present in both sets.
print(set1.symmetric_difference(set2)) #{'google', 'banana', 'microsoft', 'cherry'}
print(set1 ^ set2) #{'google', 'banana', 'microsoft', 'cherry'}


# The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set
# Use the symmetric_difference_update() method to keep the items that are not present in both sets:
print(set1.symmetric_difference_update(set2))

# Set Methods

# Method 	                    Shortcut 	Description
# add() 	  	                            Adds an element to the set
# clear() 	  	                            Removes all the elements from the set
# copy() 	  	                            Returns a copy of the set
# difference() 	                - 	        Returns a set containing the difference between two or more sets
# difference_update() 	        -=      	Removes the items in this set that are also included in another, specified set
# discard() 	                         	Remove the specified item
# intersection()            	& 	        Returns a set, that is the intersection of two other sets
# intersection_update() 	    &= 	        Removes the items in this set that are not present in other, specified set(s)
# isdisjoint() 	                        	Returns whether two sets have a intersection or not
# issubset() 	                <= 	        Returns whether another set contains this set or not
#                           	< 	        Returns whether all items in this set is present in other, specified set(s)
# issuperset() 	                >=      	Returns whether this set contains another set or not
#   	                        > 	        Returns whether all items in other, specified set(s) is present in this set
# pop() 	                             	Removes an element from the set
# remove() 	                            	Removes the specified element
# symmetric_difference()    	^ 	        Returns a set with the symmetric differences of two sets
# symmetric_difference_update() ^= 	        Inserts the symmetric differences from this set and another
# union() 	                    | 	        Return a set containing the union of sets
# update()                  	|=      	Update the set with the union of this set and others