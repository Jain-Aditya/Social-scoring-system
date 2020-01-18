from django.shortcuts import render

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
    uid = request.GET['uid']
    #a call to the api to get a JSON

    customer_data = {'name':'Achilles','dob':'1/1/1980','uid':19320,'loan':100000,'Score':-1324.75}

    customer_transactions={'traffic-challana'}
    return render(
        request,
        template_name='customerdetails.html',
        context={'details':customer_data,
                'transactions':customer_transactions,
        })

def customerLogin(request):
    return render(
        request,
        template_name='customerlogin.html',
        content_type={},
    )