from flask import Flask, render_template, redirect, url_for, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
from send import *
import datetime as dt 

app = Flask(__name__)

# route for handling the login page logic
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST': 
        number = request.form['number']
        firstname = request.form['firstname']
        email = request.form['email']
        lastname = request.form['lastname']
        x = person(lastname, firstname, number, email)
        phoneNumberDict[number] = x
        #sendToAllNumbers(x, phoneNumberDict, greeting)
        return render_template('Login.html')
    elif request.method == 'GET': 
        return render_template('Login.html')

@app.route('/sms', methods=['GET', 'POST'])
def sms():
    """
    Twilio utilizes this route to send data about incoming messages
    """
    incoming_msg = request.values.get('Body', '').lower()
    from_number = request.values.get('From')
    responded = False
    symptomsList = []
    message = ''
    resp = MessagingResponse()
    resp.message(message)
    symptoms = incoming_msg.split(',')
    for i in symptoms:
        if isinstance(int(i), int):
            symptomsList.append(i)

    if len(symptomsList) > 0:
        #figure out name
        number = from_number[2:12]
        for i in phoneNumberDict:
            if i == number:
                fillOutForm(symptomsList, phoneNumberDict[i])
    
    return str(resp)


if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug = True)
    
