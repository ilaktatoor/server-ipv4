#https://accounts.google.com/DisplayUnlockCaptcha
#creating a program that sends the public ip to some email so they can conect to the ssh server that i host
#in case that the ip changes or the internet restart, it will wait 4 min before send the new ip 

import smtplib
from requests import get
import time
import urllib.request

from requests.models import requote_uri

EMAIL_ADDRES="servermckali@gmail.com"
EMAIL_PASSWORD="emma1200"
EMAIL_TO=['cristobalschmidt001@gmail.com','yamilyaber@hotmail.com','cemmnuelaxa@gmail.com']


def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True 
    except:
        return False


def request():
    try:
        ping =  get('https://api.ipify.org').text
        return True
    except:
        return False

while True:
    time.sleep(10)
    if connect()==False:
        print('not connected')
    else:
        print('connected')
        time.sleep(120)#time for the modem and internet to start
        
        if request() == True:
            ip =  get('https://api.ipify.org').text
            old_ip = ''
            if old_ip != ip:
                old_ip = ip
                time.sleep(120)#time in seconds
                server = smtplib.SMTP_SSL("smtp.gmail.com",465)

                server.login(EMAIL_ADDRES,EMAIL_PASSWORD)
                server.sendmail(EMAIL_ADDRES,EMAIL_TO,ip)
                print('email sent')
                server.quit()
        