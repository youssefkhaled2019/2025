# MongoDB stores data in JSON-like documents, which makes the database very flexible and scalable.
# You can download a free MongoDB database at https://www.mongodb.com.
# Or get started right away with a MongoDB cloud service at https://www.mongodb.com/cloud/atlas.
#========================================
# python -m pip install pymongo 
#========================================

# docker run --rm --name my-mongo -it -p 27017:27017 mongo:latest
#========================================


# DATABASE = {
#     'default': {
#         'ENGINE': 'djongo',
#         'NAME': 'your-database-name',
#         'CLIENT': {
#             'host': 'mongodb://mongodb:27017',
#             'username': 'root',
#             'password': 'mongoadmin',
#             'authSource': 'admin',
#             'authMechanism': 'SCRAM-SHA-1',
#         }
#     }
# }

#========================================
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

dblist=myclient.list_database_names()
print(dblist)
# if "mydatabase" in dblist:
#   print("The database exists.")

# =========================================
# Creating a Collection == table
# Important: In MongoDB, a collection is not created until it gets content!

# mycol = mydb["customers"]  
# collist = mydb.list_collection_names()
# if "customers" in collist:
#   print("The collection exists.")

# =========================================
# Insert Into Collection
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]

# mydict = { "name": "John", "address": "Highway 37" }

# x = mycol.insert_one(mydict)
# print(x.inserted_id) 



# mylist = [
#   { "name": "Amy", "address": "Apple st 652"},
#   { "name": "Hannah", "address": "Mountain 21"},
#   { "name": "Michael", "address": "Valley 345"},
#   { "name": "Sandy", "address": "Ocean blvd 2"},
#   { "name": "Betty", "address": "Green Grass 1"},
#   { "name": "Richard", "address": "Sky st 331"},
#   { "name": "Susan", "address": "One way 98"},
#   { "name": "Vicky", "address": "Yellow Garden 2"},
#   { "name": "Ben", "address": "Park Lane 38"},
#   { "name": "William", "address": "Central st 954"},
#   { "name": "Chuck", "address": "Main Road 989"},
#   { "name": "Viola", "address": "Sideway 1633"}
# ]
# mylist = [
#   { "_id": 1, "name": "John", "address": "Highway 37"},
#   { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
#   { "_id": 3, "name": "Amy", "address": "Apple st 652"},
#   { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
#   { "_id": 5, "name": "Michael", "address": "Valley 345"},
#   { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
#   { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
#   { "_id": 8, "name": "Richard", "address": "Sky st 331"},
#   { "_id": 9, "name": "Susan", "address": "One way 98"},
#   { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
#   { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
#   { "_id": 12, "name": "William", "address": "Central st 954"},
#   { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
#   { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
# ]

# x = mycol.insert_many(mylist)
# print(x.inserted_ids) 
# =========================================
# # Find==select
# x = mycol.find_one() #the first occurrence in the selection.
# print(x) 


# # The find() method returns all occurrences in the selection.
# for x in mycol.find():
#   print(x) 

# =========================================
# You are not allowed to specify both 0 and 1 values in the same object 
# (except if one of the fields is the _id field). If you specify a field with the value 0,
#  all other fields get the value 1, and vice versa:

#  mycol.find({},{ "address": 0 }):
# for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
#   print(x) 


# =========================================
# find the documents where starts with the letter "S" or higher (alphabetically)
# myquery = { "address": { "$gt": "S" } }

# Find documents where the address starts with the letter "S":
# myquery = { "address": { "$regex": "^S" } }

# myquery = { "address": "Park Lane 38" }
# mydoc = mycol.find(myquery)
# for x in mydoc:
#   print(x)   

# =========================================
# Sort 
# sort("name", 1) #ascending
# sort("name", -1) #descending 
# mydoc = mycol.find().sort("name", -1)

# for x in mydoc:
#   print(x) 
# =========================================
# Delete Document
# myquery = { "address": "Mountain 21" }
# Note: If the query finds more than one document, only the first occurrence is deleted.
# x=mycol.delete_one(myquery) 
# print(x.deleted_count, " documents deleted.") 


# myquery = { "address": {"$regex": "^S"} }
# x = mycol.delete_many(myquery)
# print(x.deleted_count, " documents deleted.") 


# x = mycol.delete_many({})
# print(x.deleted_count, " documents deleted.") 
# =========================================

# # Delete Collection
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]
# # The drop() method returns true if the collection was dropped successfully, and false if the collection does not exist.
# mycol.drop() 

# =========================================
# Update Collection
# Note: If the query finds more than one record, only the first occurrence is updated.
# myquery = { "address": "Valley 345" }
# newvalues = { "$set": { "address": "Canyon 123" } }

# mycol.update_one(myquery, newvalues)

# #print "customers" after the update:
# for x in mycol.find():
#   print(x) 

# To update all documents that meets the criteria of the query, use the update_many() method.
# myquery = { "address": { "$regex": "^S" } }
# newvalues = { "$set": { "name": "Minnie" } }
# x = mycol.update_many(myquery, newvalues)
# print(x.modified_count, "documents updated.") 

# =========================================
# limit
# myresult = mycol.find().limit(5)

#print the result:
# for x in myresult:
#   print(x) 

# =========================================
