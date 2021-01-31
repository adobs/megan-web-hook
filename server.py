from twilio.rest import Client
from twilio.twiml.messaging_response import Body, Message, Redirect, MessagingResponse
from flask import Flask, request, render_template, redirect, flash, session
import os

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "ABCDEF")


@app.route("/sms", methods=['POST'])
def sms():
    return render_template("sms.html")

@app.route("/voice", methods=['GET', 'POST'])
def voice():
    return render_template("voice.html")


if __name__ == "__main__":
    
    PORT = int(os.environ.get("PORT", 5000))
    DEBUG = "NO_DEBUG" not in os.environ

    app.run(debug=DEBUG, host="0.0.0.0", port=PORT)
