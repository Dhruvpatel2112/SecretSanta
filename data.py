import json
import random
import smtplib
from Shuffle import *
from sendMail import *

f = open("./Participent_data.json", "r")


dic1=json.load(f)
# keys = list(dic1.keys())
# random.shuffle(keys)
# shuffle_dic2 = dict(zip(keys, dic1.values()))



ShuffledDict=shuffle_fun(dic1)
# print(dic1)

# print(shuffle_dic2)
sendMails(ShuffledDict)
##mail module
# server=smtplib.SMTP('smtp.gmail.com:587')
# server.ehlo()
# server.starttls()

# message='Subject:{}\n\n{}'.format(subject,msg)
# server.sendmail()




