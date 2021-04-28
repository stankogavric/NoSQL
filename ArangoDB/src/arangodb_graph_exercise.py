import json
from typing import Collection
from pyArango.connection import *
from pyArango.graph import EdgeDefinition, Graph
from pyArango.collection import Edges, Field, Collection

conn = Connection(username="root", password="root")
#db = conn.createDatabase(name="gameOfThrones")
db = conn["gameOfThrones"]


class Characters(Collection):
    _fields = {
        "name": Field(),
        "surname": Field()
    }


class ChildOf(Edges):
    pass


class gameOfThrones(Graph):
    _edgeDefinitions = (EdgeDefinition(
        edgesCollection="ChildOf", fromCollections=["Characters"], toCollections=["Characters"]), )

    _orphanedCollections = []


g = db.createGraph("gameOfThrones")

data = []
with open("ArangoDB/data/characters.json", "r", encoding="utf-8") as f:
    data = json.load(f)

relations = []
with open("ArangoDB/data/relations.json", "r", encoding="utf-8") as f:
    relations = json.load(f)

vertices = []
for d in data:
    try:
        surname = d["surname"]
    except Exception:
        d["surname"]=""
    v = g.createVertex("Characters", {"name":d["name"], "surname":d["surname"], "_key": (d["name"]+d["surname"]).lower().replace(" ", "") })
    v.save()
    vertices.append(v)

for r in relations:
    parent = [v for v in vertices if v["name"]==r["parent"]["name"] and v["surname"]==r["parent"]["surname"]][0]["_id"]
    child = [v for v in vertices if v["name"]==r["child"]["name"] and v["surname"]==r["child"]["surname"]][0]["_id"]
    g.link("ChildOf", child, parent, {})


for v in vertices:
    if v["name"]=="Ned" and v["surname"]=="Stark":
        g.deleteVertex(v)
