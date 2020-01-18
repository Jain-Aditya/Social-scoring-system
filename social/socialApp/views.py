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
        template_name='managerlogin.html',
        context={})

def customerLogin(request):
    return render(
        request,
        template_name='customerlogin.html',
        context={})