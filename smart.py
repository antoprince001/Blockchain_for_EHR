import pymongo,dns

'''contract={
    '_id':'PAT003REC01' ,
    'accesssors': 'DOC1',
    'owner':'PAT001',
    'timestamp':'0',
    'record':'',
    'status':-1

}'''


client = pymongo.MongoClient("mongodb+srv://Antony:A8939469555@blockchainehr-kpbxk.mongodb.net/test?retryWrites=true&w=majority")
db = client.test
mydb=client["Blockchain"]

#mycol=mydb["SMART_CONTRACT"]

myview=mydb['SMART_CONTRACT']
myquery = {
    'owner':'PAT008', 
    'accessor':'DOC1',
    'record': 'PAT001REC1'}
#newvalues = { "$set": {"status": 1 } }

#y=myview.update_one(myquery, newvalues)
#y=myview.find(myquery)
#myquery = {'accesssors':{'id':'DOC1','status': 1}}
my=myview.find_one(myquery)
if( str(my)=='None'):
    print('Dont')
else:
    print('trouble')
#print(my)
#Insert to contract
#y=mycol.insert_one(contract)

print(my)
 