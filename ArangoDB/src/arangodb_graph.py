from typing import Collection
from pyArango.connection import *
from pyArango.graph import EdgeDefinition, Graph
from pyArango.collection import Edges, Field, Collection

conn = Connection(username="root", password="root")
# db = conn.createDatabase(name="graph")
db = conn["graph"]


class Female(Collection):
    _fields = {
        "name": Field()
    }


class Male(Collection):
    _fields = {
        "name": Field()
    }


class Relation(Edges):
    _fields = {
        "type": Field()
    }


class social(Graph):
    _edgeDefinitions = (EdgeDefinition(
        edgesCollection="Relation", fromCollections=["Female", "Male"], toCollections=["Female", "Male"]), )

    _orphanedCollections = []


g = db.createGraph("social")

a = g.createVertex("Female", {"name": "Ana", "_key": "ana"})
b = g.createVertex("Female", {"name": "Jana", "_key": "jana"})
c = g.createVertex("Male", {"name": "Marko", "_key": "marko"})
d = g.createVertex("Male", {"name": "Janko", "_key": "janko"})

a.save()
b.save()
c.save()
d.save()

g.link("Relation", a, c, {"type": "married", "_key":"anaAndMarko"})
g.link("Relation", b, d, {"type": "married", "_key":"janaAndJanko"})
g.link("Relation", a, b, {"type": "friend", "_key":"anaAndJana"})
g.link("Relation", c, d, {"type": "friend", "_key":"markoAndJanko"})

print(g.traverse(a, direction="outbound", maxDepth=1))

g.deleteVertex(c)
