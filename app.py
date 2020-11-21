from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from datetime import datetime


def isWordPresent(sentence, word):
    s = sentence.split(" ")
    for i in s:
        if (i == word):
            return True
    return False


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')

    # Create reply
    resp = MessagingResponse()
    resp.message("You said: {}".format(msg))


    print(msg)
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    note = open("notes.txt", "a")
    word = "#note"

    if (isWordPresent(msg, word)):
        msg = msg.replace("#note", '')
        note.write(dt_string+"\n"+msg)
        note.write("\n\n")
        note.close
        resp.message("Your note has been saved.")
    else:
        print("No notes\n")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
