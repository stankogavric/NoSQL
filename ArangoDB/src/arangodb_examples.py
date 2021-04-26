from pyArango.connection import *

conn = Connection(username="root", password="root")

#db = conn.createDatabase("school")
db = conn["school"]

#studentsCollection = db.createCollection(name="Students")
studentsCollection = db["Students"]
print(db["Students"])

doc1 = studentsCollection.createDocument()
doc1["name"] = "Marko Markovic"
doc1["_key"] = "markomarkovic"
print(doc1)
#doc1.save()

doc2 = studentsCollection.createDocument()
doc2["firstname"] = "Ana"
doc2["lastname"]="Anic"
doc2._key = "anaanic"
print(doc2)
#doc2.save()

students = [("Petar", "Petrovic", 9.0), ("Janko", "Jankovic", 8.5), ("Ivana", "Ivanic", 9.5), ("Mis", "Misic", 7.7)]

for (first, last, gpa) in students:
    doc = studentsCollection.createDocument()
    doc["name"] = "%s %s" % (first, last)
    doc["gpa"] = gpa
    doc["year"] = 2017
    doc._key = "".join([first, last]).lower()
    #doc.save()

def report_gpa(document):
    print(document["name"])
    print(document["gpa"])

ivana = studentsCollection["ivanaivanic"]
#report_gpa(ivana)

def update_gpa(document, new_gpa):
    document["gpa"] = new_gpa
    document.save()

def top(gpa):
    for student in studentsCollection.fetchAll():
        if student["gpa"] is not None and student["gpa"] >= gpa:
            print(student["name"])

#top(9.0)

""" mis = studentsCollection["mismisic"]
mis.delete()
print(mis) """

aql = "FOR x IN Students RETURN x.name"
result = db.AQLQuery(aql)
#print(result)


doc = {"_key": "mismisic", "name":"Mis Misic", "gpa":7.7}
bind = {"doc":doc}
aql = "INSERT @doc INTO Students LET newDoc = NEW RETURN newDoc"
# result = db.AQLQuery(aql, bindVars=bind)
print(result)


doc = {"gpa":10.0}
bind = {"doc":doc, "key":"mismisic"}
aql = "UPDATE @key WITH @doc in Students LET updated = NEW return updated"
result = db.AQLQuery(aql, bindVars=bind)
print(result)

