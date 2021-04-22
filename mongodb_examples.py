import pymongo

my_client = pymongo.MongoClient("mongodb://localhost:27017/")

my_db = my_client["my_database"]

print(my_client.list_database_names())

db_list = my_client.list_database_names()
if "my_database" in db_list:
    print("exists")

my_col = my_db["customers"]

print(my_db.list_collection_names())

""" my_dict = {"name":"Marko", "address":"Savska 5"}

my_col.insert_one(my_dict)

my_dict = {"name":"Petar", "address":"Novosadska 7"}
x = my_col.insert_one(my_dict)

print(x.inserted_id) """

""" my_list = [
    {
        "name":"Ana",
        "address":"Sekspirova 11"
    },
    {
        "name":"Jana",
        "address":"Zeleznicka 20"
    },
    {
        "name":"Sofija",
        "address":"Danila Kisa 1"
    },
    {
        "name":"Janko",
        "address":"Jevrejska 14"
    }
]

x = my_col.insert_many(my_list)
print(x.inserted_ids) """

print([c for c in my_col.find()])

for c in my_col.find():
    print(c)

print("----------")

for c in my_col.find({}, {"_id": 0}):
    print(c)

print("----------")

for c in my_col.find({}, {"_id": 0, "address": 1}):
    print(c)

""" print("----------")

for c in my_col.find({}, {"name": 0, "address": 1}):
    print(c) """

my_query = {"address":"Jevrejska 14"}
r = my_col.find(my_query)

for c in r:
    print(c)

print("----")

my_query = {"address":{"$regex":"^S"}}
r = my_col.find(my_query)

for c in r:
    print(c)
print("----")
r = my_col.find().sort("name")
for x in r:
    print(x)

print("----")

r = my_col.find().sort("name", -1)
for x in r:
    print(x)

print("----")

""" my_col.delete_one({"address":"Zeleznicka 20"})

r = my_col.delete_many({"address":{"$regex":"^S"}})
print(r.deleted_count)

my_col.drop() """

my_query = {"address":"Danila Kisa 1"}
new_values = {"$set": {"address":"Futoska 2"}}
my_col.update_one(my_query, new_values)

for x in my_col.find():
    print(x)

print("----")
my_query = {"address":{"$regex":"^S"}}
new_values = {"$set": {"name":"Jovana"}}
my_col.update_many(my_query, new_values)

for x in my_col.find():
    print(x)

my_result = my_col.find().limit(5)
print("----")
for x in my_result:
    print(x)