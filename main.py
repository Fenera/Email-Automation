import smtplib
import os


#sender email & receiver email
email_s = input('Enter your email: ')
email_r = input('Enter the email of the receiver: ')

app_password = os.environ.get('app_password')


#subject and body of email
subject = input('Enter the subject: ')
body = input('Enter the body of the email: ')

text = f'{subject} \n\n {body}'

#create a server connection
#the email is the address of the SMTP server provided by Gmail
#Port 587
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

#authenticate your email account with SMTP server
server.login(email_s, app_password)

#send email
server.sendmail(email_s, email_r, text)

print('The email has been sent')

