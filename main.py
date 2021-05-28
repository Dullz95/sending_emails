import smtplib

s=smtplib.SMTP('smtp.gmail.com',587)
sender_email_id = 'abdullah.isaacs@gmail.com'
reciever_email_id = 'calvertjustin1996@gmail.com'
password = input("enter pass: ")
s.starttls()
s.login(sender_email_id,password)
message = "Shut up"
message = message + "please shut up"
s.sendmail(sender_email_id,reciever_email_id, message)
s.quit()