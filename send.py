from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from twilio.rest import Client 
import datetime as dt

sent = 0
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)
phoneNumberDict = {}
greeting = 'Hello nameHere and welcome to the automated covid symptoms checker. Do you have any symptoms?\nInput your symptoms as comma-separated numbers, following the below legend. \n0: No symptoms\n1: Fever or chills\n2: Cough\n3: Shortness of breath or difficulty breathing\n4:Fatigue\n5:Muscle or body aches\n6: Headache (unlike your usual headaches)\n7: New Loss of Taste or Smell\n8: Sore Throat\n9: Congestion or runny nose\n10:Nausea or vomiting\n11: Diarrhea"'
symptomsList = []
symptomsDictionary = {
    "0": "QID22-21-label",
    "1": "QID22-1-label",
    "2": "QID22-2-label",
    "3": "QID22-3-label",
    "4": "QID22-4-label",
    "5": "QID22-5-label",
    "6": "QID22-6-label",
    "7": "QID22-7-label",
    "8": "QID22-8-label",
    "9": "QID22-9-label",
    "10": "QID22-10-label",
    "11": "QID22-21-label",
}

class person:
    """
    Just a class for saving data about people signed up for the automated covid response
    """
    def __init__(self, lastname, firstname, number, email):
        self.lastname = lastname
        self.firstname = firstname
        self.number = number
        self.email = email

def sendAll():
    """
    easier way to send all
    """
    if len(phoneNumberDict) > 0:
        sendToAllNumbers(phoneNumberDict, greeting)
        return True
    return False

def fillOutForm(symptoms, person):
    """
    Fills out the covid form on bobsons website then tells the person that it has been done.
    """
    PATH = "/home/dev/Downloads/chromedriver"
    driver = webdriver.Chrome(PATH)
    driver.get("http://babson.qualtrics.com/jfe/form/SV_d76vBw9YUNfXY4l")
    for s in symptoms:
        driver.find_element_by_id(f"{symptomsDictionary[s]}").click()

    first_name = driver.find_element_by_xpath("//input[@name=\"QR~QID19~TEXT\"]")\
        .send_keys(person.firstname)
    last_name = driver.find_element_by_xpath("//input[@name=\"QR~QID25~TEXT\"]")\
        .send_keys(person.lastname)
    email_address = driver.find_element_by_xpath("//input[@name=\"QR~QID20~TEXT\"]")\
        .send_keys(person.email)
    mobile_phone_number = driver.find_element_by_xpath("//input[@name=\"QR~QID21~TEXT\"]")\
        .send_keys(person.number)

    driver.find_element_by_xpath("//input[@name=\"NextButton\"]").click()

    sendSMS('Your COVID form has been filled out', person)

def sendSMS(message, person):
    """
    Send an sms message using the provided message and a person object
    """
    number = person.number
    print(number)
    if number[0] != '+':
        numbers = '+1' + str(number)

    messages = client.messages.create(body=message, from_='+12549442411', to=numbers)
    #throws an error, need this to override
    try:
        print(messages.sid)
    except AttributeError:
        pass

def customizedGreeting(name, nameToReplace, message):
    """
    Cteate a customized message by putting a name into the greeting string
    """
    t = message.replace(nameToReplace, name)
    return t

def sendToAllNumbers(numberDictionary, message):
    """
    Send a message to all people stored in the dictionary
    """
    for i in numberDictionary:
        y = numberDictionary[i]
        msg = customizedGreeting(y.firstname, 'nameHere', message)
        sendSMS(msg, numberDictionary[i])

