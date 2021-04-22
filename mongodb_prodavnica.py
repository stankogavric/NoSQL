import pymongo
from bson.objectid import ObjectId
import datetime

my_client = pymongo.MongoClient("mongodb://localhost:27017/")

prodavnica = my_client["prodavnica"]

artikli = prodavnica["artikli"]
porudzbine = prodavnica["porudzbine"]

for a in artikli.find({"broj_artikala": {"$gt": 7}}, {"_id": 0, "naziv": 1}):
    print(a)

print("----")

for a in artikli.find({"_id": ObjectId("5e0e293b7bf8582054b53cae")}, {"_id": 0, "naziv": 1}):
    print(a)

print("----")

# artikli.update_many({"$and":[{"naziv":{"$regex":"^P"}}, {"broj_artikala":{"$gt":6}}]}, {"$inc":{"broj_artikala":-7}})

# r = artikli.delete_many({"broj_artikala": {"$eq": 0}})
# print(r.deleted_count)

for p in porudzbine.find({"ime_prezime": {"$regex": ".*Peric.*"}}):
    print(p)

porudzbine.insert_one({"id_artikla": ObjectId("5e0e289200bc1b20545a43a3"), "ime_prezime": "Bojan Petrović",
                   "broj_artikala": 7, "datum_nar": datetime.datetime(2021, 4, 19), "datum_isp": datetime.datetime(2021, 4, 21)})
