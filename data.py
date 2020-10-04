
import pymongo

Blockchain=[{
    '_id':'PAT00' ,
    'first':'Genesis',
    'second':'Block',
    'patientid':'00000',
    'passwd': '1234',
    'age':0,
    'address':'None',
    'aadhar':000000000000,
    'record':[],
    'prevhash':0,
    'hash':'0d5514737fd838222d35a956c72519be12c5f38339d05aee054824f941d74c93'   
}]


client = pymongo.MongoClient("mongodb+srv://Antony:A8939469555@blockchainehr-kpbxk.mongodb.net/test?retryWrites=true&w=majority")
db = client.test
mydb=client["Blockchain"]

mycol=mydb["Blockhead"]


y=mycol.insert_many(Blockchain)
print(y)
