from selenium import webdriver
from selenium.webdriver.common.keys import Keys
PATH = "/Users/aidansuljic/Downloads/chromedriver 2"
driver = webdriver.Chrome(PATH)
driver.get("http://babson.qualtrics.com/jfe/form/SV_d76vBw9YUNfXY4l")
first_name = "Aidan"
last_name = "Suljic"
email_address = "asuljic1@babson.edu"
mobile_phone_number = "8472191797"
symptoms = input("Do you have any symptoms?\nInput your symptoms as comma-separated numbers, following the below legend. \n0: No symptoms\n1: Fever or chills\n2: Cough\n3Shortness of breath or difficulty breathing\n4:Fatigue\n5:Muscle or body aches\n6: Headache (unlike your usual headaches)\n7: New Loss of Taste or Smell\n8: Sore Throat\n9: Congestion or runny nose\n10:Nausea or vomiting\n11: Diarrhea")
symptoms = symptoms.split(',')
symptomsDictionary = {
    "0": "QR~QID22~21",
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
    "11": "/html/body/div[3]/div/form/div/div[2]/div[1]/div[3]/div[1]/div[12]/div[3]/div/fieldset/div/ul/li[12]/span/label",
}
for s in symptoms:
    driver.find_element_by_xpath(f"//input[@name='{symptomsDictionary[s]}']").click()


first_name = driver.find_element_by_xpath("//input[@name=\"QR~QID19~TEXT\"]")\
    .send_keys(first_name)
last_name = driver.find_element_by_xpath("//input[@name=\"QR~QID25~TEXT\"]")\
    .send_keys(last_name)
email_address = driver.find_element_by_xpath("//input[@name=\"QR~QID20~TEXT\"]")\
    .send_keys(email_address)
mobile_phone_number = driver.find_element_by_xpath("//input[@name=\"QR~QID21~TEXT\"]")\
    .send_keys(mobile_phone_number)

    
   


driver.find_element_by_xpath("//input[@name=\"NextButton\"]").click()






