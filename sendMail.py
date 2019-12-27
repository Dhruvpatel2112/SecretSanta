import smtplib 

def sendMails(dict1):
    #connecion and login
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls() 
    s.login("sintprd@gmail.com", "simbaproject")
    
    for name in dict1:
        message = 'Hi, You are secret Sanata for '+name
        # sending the mail 
        s.sendmail("sintprd@gmail.com", dict1[name], message)
        print('Email :'+dict1[name]+'secret santa for : '+name)  
    s.quit()
