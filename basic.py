from flask import Flask,render_template,request,url_for,session
import json,sqlite3
from time import time
from hashlib import sha256
import datetime,time

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

index=2
Blockchain=[{
    'first':'Genesis',
    'second':'Block',
    'patientid':'00000',
    'passwd': '1234',
    'age':0,
    'address':'None',
    'aadhar':000000000000,
    'index':0,
    'prevhash':0,
    'hash':'8c91f74e15a53a94b096419a57662bef769c3f15f0bdaef4c4c2ead29430763e'   
},
{
    'first':'Aathitya',
    'second':'Sriram',
    'passwd': '1234',
    'age':18,
    'patientid':'00001',
    'address':'chennai',
    'aadhar':312412451136,
    'index':1,
    'prevhash':'8c91f74e15a53a94b096419a57662bef769c3f15f0bdaef4c4c2ead29430763e',
    'hash':'969464686ebce37246efb1e196c163edce036bd5c24e54adf3071972c41f997e'   
},{
    'first':'Abirami',
    'second':'Somasundaram',
    'passwd': '12324',
    'age':18,
    'address':'chennai',
    'aadhar':312412451135,
    'index':2,
    'prevhash':'969464686ebce37246efb1e196c163edce036bd5c24e54adf3071972c41f997e',
    'hash':'ca701d2be90ccb1d11abe7ea42528800678bc203ed982b31908fce133b66fec1'
}
]

patientrec=[
    {

    }
]

login_status=0
app= Flask(__name__)





@app.route('/')
@app.route('/home')
def home():
    return render_template('welcome.html')



@app.route('/create', methods=['POST'])
def createblock():
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
    prevhash='8c91f74e15a53a94b096419a57662bef769c3f15f0bdaef4c4c2ead29430763e'
    
    index=4
    block={
        'name':'Aathitya',
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
        'prev': prevhash,
        'index':index

    }
    block_string = json.dumps(block, sort_keys=True) 
    hashval=sha256(block_string.encode()).hexdigest()
    block={
        'name':'Aathitya',
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
        'prev': prevhash,
        'hash':hashval,
        'index':index

    }
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

@app.route('/patcreate',methods=['POST'])
def patcreate():
    block_data = request.form['usr']
    first=request.form['usr']
    second=request.form['lsn'],
    passwd= request.form['pwd'],
    age=request.form['age'],
    addres=request.form['add'],
    #aadhar=request.form['Aadhar']
    #ts=time.time()
    #st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    block={
    #'timestamp':st,
    'first': first,
    'second':second,
    'passwd': passwd,
    'address':addres,
    #'aadhar':aadhar,
    'prevhash':Blockchain[-1]['hash']
}
    block_string = json.dumps(block, sort_keys=True) 
    hashval=sha256(block_string.encode()).hexdigest()
    #session['user']=first
    block={
    'index':Blockchain[-1]['index']+1,
    #'timestamp':st,
    'first': first,
    'second':second,
    'passwd': passwd,
    'address':addres,
    #'aadhar':aadhar,
    'prevhash':Blockchain[-1]['hash'],
    'hash': hashval
}
    Blockchain.append(block)
    return render_template('patcreate.html',posts=Blockchain)

@app.route('/patdash')
def patdash():
    return render_template('patdash.html')



@app.route('/viewrec')
def view():
    return render_template('prevblock.html',post=Blockchain[-1])



@app.route('/doctor')
def doctor():
    return render_template('doctor.html')

@app.route('/doclog')
def doclog():
    return render_template('doctorlog.html')
@app.route('/docdash')
def docdash():
    return render_template('docdash.html')

@app.route('/medrec')
def medrec():
    return render_template('medrec.html')







@app.route('/hospital')
def hospital():
    return render_template('hospital.html')

@app.route('/adminlog')
def adminlog():
    return render_template('hospitallog.html')

@app.route('/admindash')
def admindash():
    return render_template('admindash.html')







@app.route('/organ_donor')
def donor():
    return render_template('organ.html')


@app.route('/viewmore')
def insure():
    return render_template('insure.html')


if __name__=='__main__':
    app.run(debug=True)