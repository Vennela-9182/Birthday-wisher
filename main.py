from_email = "kambalapallysirivennela@gmail.com"
app_password = "dozu ckrx nliq rcmx"

import datetime as dt
from email.mime.multipart import MIMEMultipart
import pandas
import smtplib
now=dt.datetime.now()
month=now.month
day=now.day
today=(month,day)

data=pandas.read_csv("birthdays.csv")
birthday_dic={(row['month'],row['day']):row  for (index,row) in data.iterrows()}
if today in birthday_dic:
    birthday_person=birthday_dic[today]
    with open("letter_templates/letter_1.txt") as f1:

        letter=f1.read()
    letter=letter.replace("name",birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(user=from_email,password=app_password)
        connection.sendmail(from_addr=from_email,to_addrs=birthday_person['email'],msg=letter)
        print("email is sent ")










