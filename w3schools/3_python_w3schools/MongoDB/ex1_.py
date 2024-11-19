import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = myclient["AAST"]
customers = db["customers"] 


mydict = { "name": "John", "address": "Highway 37" }

x = customers.insert_one(mydict)
print(x.inserted_id) 

# db_list=myclient.list_database_names()
# print(db_list)
# collection_list = db.list_collection_names()
# print(collection_list)