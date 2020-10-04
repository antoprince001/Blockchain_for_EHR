import os
from flask import Flask, render_template, request
import pymongo,base64,

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


client = pymongo.MongoClient("mongodb+srv://Antony:A8939469555@blockchainehr-kpbxk.mongodb.net/test?retryWrites=true&w=majority")
db = client.test
mydb=client["XRAY"]

mycol=mydb["Nodes"]



@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload", methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)
        imagepic=open(destination, "rb") 
        f = imagepic.read()
        strs=base64.b64encode(f)
        #print b[0]
        val={
            'imagearr':strs,
            'destination':destination
        }
        y=mycol.insert_one(val)
    return render_template("complete.html",posts=val)

if __name__ == '__main__':
    app.run(port=5000, debug=True)