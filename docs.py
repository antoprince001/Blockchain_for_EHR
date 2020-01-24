import pymongo

doc={
    '_id':'ADM00' ,
    'name':'',
    'passwd': '1234',
    'timestamp':'0'
}


client = pymongo.MongoClient()
db = client.test
mydb=client["Blockchain"]

mycol=mydb["Nodes"]


y=mycol.insert_one(doc)
print(y)
