from flask import Flask
from flask_mail import Mail, Message


app1 = Flask(__name__)

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'nareshd.jmu@gmail.com',
    "MAIL_PASSWORD": 'yzixhtvwgazeqofx'
}

app1.config.update(mail_settings)
mail = Mail(app1)

def mailSend(bodymsg="",eml=""):
	try:
		with app1.app_context():
			msg = Message(subject="List of restaurants",
                      sender=app1.config.get("MAIL_USERNAME"),
                      recipients=["nareshdogra@rediffmail.com"],
                      body=bodymsg)
			mail.send(msg)
	except Exception as e:
		return(str(e)) 