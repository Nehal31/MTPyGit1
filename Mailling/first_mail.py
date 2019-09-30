import smtplib

MAIL_SERVER = 'smtp.gmail.com:587'
USER_EMAIL = 'nehal31.test01@gmail.com'
PASSWORD = 'password.test'

with smtplib.SMTP(MAIL_SERVER) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(USER_EMAIL, PASSWORD)

    subject = "Test Python mail"
    msg_body = "Hi,\nThis is a test mail.\nThanks"

    msg = f'Subject : {subject}\n\n{msg_body}'

    smtp.sendmail(USER_EMAIL, USER_EMAIL, msg)
    print("Done")


