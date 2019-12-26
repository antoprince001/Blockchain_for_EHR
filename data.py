
import pymongo,pprint

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
''',
{
    '_id':'PAT01',
    'first':'Aathitya',
    'second':'Sriram',
    'passwd': '1234',
    'age':18,
    'record':[],
    'patientid':'00001',
    'address':'chennai',
    'aadhar':312412451136,
    'prevhash':'8c91f74e15a53a94b096419a57662bef769c3f15f0bdaef4c4c2ead29430763e',
    'hash':'969464686ebce37246efb1e196c163edce036bd5c24e54adf3071972c41f997e'   
},{
    '_id':'PAT02',
    'first':'Abirami',
    'second':'Somasundaram',
    'record':[],
    'passwd': '12324',
    'age':18,
    'address':'chennai',
    'aadhar':312412451135,
    'prevhash':'969464686ebce37246efb1e196c163edce036bd5c24e54adf3071972c41f997e',
    'hash':'ca701d2be90ccb1d11abe7ea42528800678bc203ed982b31908fce133b66fec1'
}
,'''



myclient=pymongo.MongoClient()

mydb=myclient["Blockchain"]

mycol=mydb["Blockhead"]


y=mycol.insert_many(Blockchain)
print(y)
'''


myclient = pymongo.MongoClient()
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "addres":'trial' }
#mycol.insert_one(myquery)
myd =[]
mydoc= mycol.find(myquery)

for doc in mydoc:
    myd.append(doc)

print(myd)'''