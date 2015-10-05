from django.core.mail import send_mail

__author__ = 'mohammad'


# here is a security problem
# hacker at first reset password request
# then server send email via port 25
# hacker listen to port 25 and then sniff the password reset link !!!
# we must use SSL


def sendMail(subject, message, addresses):

    send_mail(subject, message, 'me@morabaa.ir', addresses)