import pymongo

doc={
    '_id':'ADM00' ,
    'name':'',
    'passwd': '1234',
    'timestamp':'0'
}


client = pymongo.MongoClient("mongodb+srv://Antony:A8939469555@blockchainehr-kpbxk.mongodb.net/test?retryWrites=true&w=majority")
db = client.test
mydb=client["Blockchain"]

mycol=mydb["Nodes"]


y=mycol.insert_one(doc)
print(y)