import pymongo
from pymongo import MongoClient

cluster = MongoClient('mongodb+srv://lovelyblackish:mistura@cluster0.2yynpwg.mongodb.net/?retryWrites=true&w=majority')

db = cluster['sldd']
collection = db['employee']

post1 = {"name":"Angy", "email": "angy@gmail.com"}
post2 = {"name":"Kist", "email": "kistkist@gmail.com"}
post3 = {"name":"Amanada", "email":"Amandi@gmail.com"}



collection.insert_one(post3)
collection.update_one({"name":"Angy"}, {"$set": {"email": "kistura@gmail.com"}})
collection.delete_one(post3)

results = collection.find_one({"name": "Kist"})
print(results)