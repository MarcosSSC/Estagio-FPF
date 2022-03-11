import smtplib, ssl
import requests

results = requests.get('https://jsonplaceholder.typicode.com/users')

users = results.json()

userlist =[]

for n in users:
    variable = n.get('name')
    userlist.append(variable)

names = ','.join(userlist)

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "marcos.teste.fpf@gmail.com"  # Enter your address
receiver_email = "osenias.oliveira@fpf.com"  # Enter receiver address
password = input("Type your password and press enter: ")
message = f"""\
Subject: Usuarios
{names}
"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)

