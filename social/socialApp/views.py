from django.shortcuts import render
import requests
import json

# Create your views here.
def home(request):
    return render(
        request,
        template_name='home.html',
        context={})

def managerLogin(request):
    return render(
        request,
        template_name='manager.html',
        context={})

def customerDetails(request):
    uid = str(request.GET['uid'])
    #a call to the api to get a JSON
    param = {'uid' : uid}
    response = requests.post("http://10.11.15.55:3000/getDetails", param)
    response = response.json()
    customer_data = {'name': response[0]['name'],'dob':response[0]['dob'],'uid':response[0]['uid'],'loan':100000,'Score':-1324.75}

    return render(
        request,
        template_name='customerdetails.html',
        context=customer_data)

def customerLogin(request):
    return render(
        request,
        template_name='customerlogin.html',
        content_type={},
    )

def acknowledgement(request):
    return "<h1>Sent successfully</h1>"