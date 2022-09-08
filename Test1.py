import pymongo

client = pymongo.MongoClient("mongodb+srv://ram143srvs:Ram143srvs@ramesh.9hyxhe9.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name": "Ramesh",
    "email": "ram143srvs@gmail.com",
    "surname": "Rayala"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)