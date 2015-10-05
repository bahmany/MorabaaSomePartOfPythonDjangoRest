from asq.initiators import query
from django.test import TestCase

# Create your tests here.


objs = [
    {"id": "1", "name":"ali11"}
    ,{"id":"2", "name":"ali12"}
    ,{"id":"3", "name":"ali13"}
    ,{"id":"4", "name":"ali14"}
    ,{"id":"5", "name":"ali15"}
    ,{"id":"6", "name":"ali16"}
    ,{"id":"7", "name":"ali17"}
]



 # found = [i for i in objs if i["id"] == "2"]

for i in objs:
    if i["id"] == "2":
        i["name"] = "rrrrrrrrrrrrreza"



found = query(objs).select(lambda x:x["id"])

print (found)