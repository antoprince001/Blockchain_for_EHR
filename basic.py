from flask import Flask,render_template,request,url_for,session,redirect
import json,sqlite3
from time import time
from hashlib import sha256
import datetime,time,pymongo
from passlib.context import CryptContext
import requests
import os

#session['user']='Genesis'
'''Blockchain=[{
        'index':'0',
        'patientid':'00000',
        'first': '',
        'last': '',
        'doctor id': '',
        'Dor': '12-13-2019',
        'Age': '',
        'haemo':'',
        'blood':'',

         
    }]'''

login_status=0
app= Flask(__name__)
app.secret_key = 'PATREC Authentication'



#Password encryption scheme
pwd_context = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=30000
)

#Sessio variables
class sessionlog:
    def __init__(self):
        self.username=''
        self.id=''

sess=sessionlog()


def encrypt_password(password):
    return pwd_context.encrypt(password)

def check_encrypted_password(password, hashed):
    return pwd_context.verify(password, hashed)

#Mongodb setup
client = pymongo.MongoClient("mongodb+srv://Antony:A8939469555@blockchainehr-kpbxk.mongodb.net/test?retryWrites=true&w=majority")

mydb=client["Blockchain"]

mycol=mydb["Blockhead"]


'''hashset=[]
ind=-1
patdoc= mycol.find()
for x in patdoc:
    hashset.append(x['hash'])
    ind=ind+1

class index:
    index=ind
    def getindex(self):
        self.index=int(self.index+1)
        return self.index

idv=index()'''

@app.route('/')
@app.route('/home')
def home():
    return render_template('welcome.html')

#MEDREC form creation
@app.route('/create', methods=['POST'])
def createblock():
    pid=request.form['pid']
    doc= request.form['doc']
    blood= request.form['blood']
    pp= request.form['pp']
    fast= request.form['fast']
    serum= request.form['serum']
    tot=request.form['tot']
    thdl=request.form['thdl']
    ldl=request.form['ldl']
    rbc=request.form['rbc']
    pulse=request.form['pulse']
    myrow=mydb[pid]
    patdoc= myrow.find()
    ind=-1
    for x in patdoc:
        prev=x['hash']
        ind=ind+1
    ts=time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    block={
        '_id':pid+'REC'+str(ind+1),
        'doc':doc,
        'gluc':pp,
        'glucf':fast,
        'serum':serum,
        'blood':blood,
        'chol': tot,
        'thdl':thdl,
        'ldl':ldl,
        'rbc':rbc,
        'pulse':pulse,
        'prev': prev,
        'timestamp':st


    }

    block_string = json.dumps(block, sort_keys=True) 
    hashval=sha256(block_string.encode()).hexdigest()
    block={
        '_id': pid+'REC'+str(ind+1),
        'doc':doc,
        'gluc':pp,
        'glucf':fast,
        'serum':serum,
        'blood':blood,
        'chol': tot,
        'thdl':thdl,
        'ldl':ldl,
        'rbc':rbc,
        'pulse':pulse,
        'prev': prev,
        'hash':hashval,
        'timestamp':st

    }
    myrow.insert_one(block)
    return render_template('newrec.html',post=block)

@app.route('/domain')
def domain():
    return render_template('domain.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')




@app.route('/patient')
def patient():
    return render_template('patient.html')

@app.route('/patientlog')
def patientlog():
    return render_template('patientlog.html')

@app.route('/patientver',methods=['POST'])
def patientverify():
    userid=request.form['PID']
    pwd=request.form['pwd']
    patquery = { "_id": userid }
    
    patdoc= mycol.find(patquery)
    for x in patdoc:
        if check_encrypted_password(pwd,x['passwd']):
            sess.username = userid
            return render_template('patdash.html')

    return render_template('patientlog.html')

@app.route('/patcreate',methods=['POST'])
def patcreate():
    block_data = request.form['usr']
    first=request.form['usr']
    second=request.form['lsn']
    passwd= request.form['pwd']
    passwd=encrypt_password(passwd)
    age=request.form['age']
    addres=request.form['add']
    #aadhar=request.form['Aadhar']
    ts=time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    myrow=mydb['Blockhead']
    patdoc= myrow.find()
    ind=-1
    for x in patdoc:
        prev=x['hash']
        ind=ind+1
    i='PAT'+ind
    block={
    '_id':i,
    'timestamp':st,
    'first': first,
    'second':second,
    'passwd': passwd,
    'address':addres,
    #'aadhar':aadhar,
    'prevhash':prev
}
    block_string = json.dumps(block, sort_keys=True) 
    hashval=sha256(block_string.encode()).hexdigest()
    #session['user']=first
    block={
    '_id':i,
    'timestamp':st,
    'first': first,
    'second':second,
    'passwd': passwd,
    'address':addres,
    'record':i+'REC',
    #'aadhar':aadhar,
    'prevhash':prev,
    'hash': hashval
}
    '''
    ima=open(file, "rb")
    f = ima.read()
    b = bytearray(f)'''
    myrow=mydb[i]
    rec={
        '_id':i+'REC'+'00',
        'doc':'',
        'gluc':0,
        'glucf':0,
        'serum':0,
        'blood':0,
        'chol': 0,
        'thdl':0,
        'ldl':0,
        'rbc':0,
        'pulse':'',
        'prev': '0',

    }
    block_s = json.dumps(rec, sort_keys=True) 
    hashrec=sha256(block_s.encode()).hexdigest()
    rec={
        '_id':i+'REC'+'00',
        'doc':'',
        'gluc':0,
        'glucf':0,
        'serum':0,
        'blood':0,
        'chol': 0,
        'thdl':0,
        'ldl':0,
        'rbc':0,
        'pulse':'',
        'timestamp':'',
        'prev': '0',
        'hash':hashrec
    }

    myrow.insert_one(rec)
    mycol.insert_one(block)
    Blockc=[]
    Bloc=mycol.find()
    for i in Bloc:
        Blockc.append(i)
    return render_template('patcreate.html',posts=Blockc)

@app.route('/patdash')
def patdash():
    return render_template('patdash.html')




@app.route('/patacc')
def view():
    patquery = { "_id": sess.username }
    
    patdoc= mycol.find_one(patquery)
    
    return render_template('patmyacc.html',post=patdoc)

@app.route('/viewrec')
def viewrec():
    myrow=mydb[sess.username]
    recs=myrow.find()
    records=[]
    for x in recs:
        records.append(x)
    records.pop(0)
    return render_template('records.html',posts=records)
        


@app.route('/doctor')
def doctor():
    return render_template('doctor.html')

@app.route('/doclog')
def doclog():
    return render_template('doctorlog.html')
@app.route('/docdash')
def docdash():
    return render_template('docdash.html')

@app.route('/docver',methods=['POST'])
def docverify():
    nam=request.form['n']
    ts=time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    passwd= request.form['pwd']
    passwd=encrypt_password(passwd)
    myrow=mydb['Nodes']
    patdoc= myrow.find()
    ind=-1
    for x in patdoc:
        if(x['_id'].find('DOC')):
            ind=ind+1
    doc={
        '_id':'DOC'+str(ind+1),
        'timestamp':st,
        'password':passwd,
        'name':nam
    }
    sess.username=doc['_id']
    myrow.insert_one(doc)
    return render_template('docdash.html')

@app.route('/doclogover',methods=['POST'])
def doclogver():
    userid=request.form['DID']
    pwd=request.form['pwd']
    patquery = { "_id": userid }
    myrow=mydb['Nodes']
    patdoc= myrow.find(patquery)
    for x in patdoc:
        if check_encrypted_password(pwd,x['password']):
            sess.username = userid
            return render_template('docdash.html')
    return render_template('doctorlog.html')

@app.route('/docview')
def docview():
    return render_template('docview.html')
@app.route('/medrec')
def medrec():
    return render_template('medrec.html')

@app.route('/myacc')
def myacc():
    patquery = { "_id": sess.username }
    myrow=mydb['Nodes']
    patdoc= myrow.find_one(patquery)
    
    return render_template('myacc.html',post=patdoc)

@app.route('/access',methods=['POST'])
def access():
    pid=request.form['PID']
    did=sess.username
    '''url = "https://www.fast2sms.com/dev/bulk"

    querystring = {"authorization":"4FzGm7K6haHIMiAJfuNsSwv50rT8cROE2UBCkP9yp3bZdXDlQqC0jLU1HVkQYE3sNdph24AIztabBcTO","sender_id":"PATREC","language":"english","route":"qt","numbers":"9789862702","message":"Doctor has requested for your record."}

    headers = {
    'cache-control': "no-cache"
    }

    response=requests.request("GET", url, headers=headers, params=querystring)'''
    myval=mydb['SMART_CONTRACTS']
    ts=time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    con={
    'accessor':did,
    'owner': pid,
    'timestamp':st,
    'record':pid+'REC',
    'status':0

    }
    myval.insert_one(con)
    return render_template('docdash.html')

@app.route('/hospital')
def hospital():
    return render_template('hospital.html')

@app.route('/adminlog')
def adminlog():
    return render_template('hospitallog.html')

@app.route('/admindash')
def admindash():
    return render_template('admindash.html')

@app.route('/admver',methods=['POST'])
def admverify():
    nam=request.form['n']
    ts=time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    passwd= request.form['pwd']
    passwd=encrypt_password(passwd)
    myrow=mydb['Nodes']
    patdoc= myrow.find()
    ind=0
    for x in patdoc:
        ind=ind+1
    doc={
        '_id':'ADM'+str(ind+1),
        'timestamp':st,
        'password':passwd,
        'name':nam
    }
    sess.username=doc['_id']
    myrow.insert_one(doc)
    return render_template('admindash.html')

@app.route('/admlogover',methods=['POST'])
def admlogver():
    userid=request.form['AID']
    pwd=request.form['pwd']
    patquery = { "_id": userid }
    myrow=mydb['Nodes']
    patdoc= myrow.find(patquery)
    for x in patdoc:
        if check_encrypted_password(pwd,x['password']):
            sess.username = userid
            return render_template('admindash.html')
    return render_template('hospitallog.html')

@app.route('/accesslog')
def accesslog():
    mycli=mydb['SMART_CONTRACTS']
    query={"owner":sess.username}
    mydata=mycli.find(query)
    block=[]
    for x in mydata:
        if x['_id']!="CON00":
            block.append(x)
            sess.id=x['accessor']
    return render_template('accesslog.html',posts=block)
    

@app.route('/available')
def available():
    myquery=patquery = { "accessor": sess.username }
    myview=mydb['SMART_CONTRACTS']
    Blockc=[]
    rec={
        'doc':'Pending',
        'gluc':0,
        'glucf':0,
        'serum':0,
        'blood':0,
        'chol': 0,
        'thdl':0,
        'ldl':0,
        'rbc':0,
        'pulse':'',
        'timestamp':'',
        'prev': '0',
        'hash':'Pending'
    }
    mydat=myview.find(myquery)
    for x in mydat:
        if x['status']==1:
            mydata=mydb[x['owner']]
            mycl=mydata.find()
            for y in mycl:
                Blockc.append(y)
        elif x['status']==0:
            Blockc.append(rec)

    return render_template('available.html',posts=Blockc)
#bAPP_ROOT = os.path.dirname(os.path.abspath(__file__))


'''@app.route("/upload", methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT, 'images/')

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)

    return render_template("complete.html")'''


@app.route('/organ_donor')
def donor():
    return render_template('organ.html')


@app.route('/viewmore')
def insure():
    return render_template('insure.html')

@app.route('/authorize')
def authorize():
    myview=mydb['SMART_CONTRACTS']
    myquery = { 'accessor': sess.id ,
                'owner':sess.username }
    newvalues = { "$set": { "status": 1 } }
    mycol.update_one(myquery, newvalues)
    return redirect(url_for('accesslog'))

@app.route('/deny')
def decline():
    myview=mydb['SMART_CONTRACTS']
    myquery = { 'accessor': sess.id ,
                'owner':sess.username }
    newvalues = { "$set": { "status": 0 } }
    mycol.update_one(myquery, newvalues)
    return redirect(url_for('accesslog'))

@app.route('/logout')
def logout():
    sess.username=''
    return render_template('domain.html')

if __name__=='__main__':
    app.run(debug=True)