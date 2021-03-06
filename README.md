# Project Title

Automatic COVID Form Submission

## Description

This project allows users to automatically fill out their covid daily reports in an efficient manner. First on the webpage you enter your personal details. You will then be sent a message detailing how to text your symptoms. Then, reply with your symptoms and your form will be automatically submitted.

## Getting Started

### Dependancies
* Twilio
* Flask
* selenium
* requests
* ngrok

### Executing program

* First you must setup a twilio trial account
* Then utilize that account to gain access to a phone number
* While in twilio, also grab the authentication credentials
* Setup environment variables involving twilio authentication credentials
* Run the program
* Run ngrok (ngrok http 5000)
* Ngrok is used to proxy external requests to the local machine
* Copy the ngrok link under the forwarding section
* Paste that into the twilio web hook section
* Add /sms to the end of the link in that section
* Twilio has a fantastic guide at how to complete the previous steps, so feel free to check that out if you are concerned
* Run appFinal.py
* One you have connected to the webpage, enter your credentials
* You should then receive an alert on your phone detailing the steps to take to get your results
* Then respond to that text in the specified manner
* Then the form will be automatically filled out


## Acknowledgments

Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [twilio](https://www.twilio.com/docs/sms/tutorials/how-to-create-sms-conversations-python)
