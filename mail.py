from flask_mail import Mail, Message
from flask import Flask



app =Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'antoprince001@gmail.com'
app.config['MAIL_PASSWORD'] = 'gboyilovemylife100%'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)


@app.route("/")
def index():
   msg = Message('Hello', sender = 'antoprince001@gmail.com', recipients = ['hemuhema2000@gmail.com','hinduabisundaram@gmail.com'])
   msg.body = "PATREC Contract created"
   mail.send(msg)
   return "Sent"

if __name__ == '__main__':
   app.run(debug = True)