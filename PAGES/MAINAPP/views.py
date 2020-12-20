from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def registerView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print("Data is valid, adding user ...")
            form.save()
            print('User added')
            return redirect('login')

    else:
        form = UserCreationForm()

    context = {'form':form}
    template_name = 'MAINAPP/register.html'
    return render(request, template_name, context)

def loginView(request):
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pass']

        print(u,p)
        print(request.POST)
        user = authenticate(username=u,password=p)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            print("invalid credentials")
            messages.error(request,"Invalid Credential")
            template_name = 'MAINAPP/login.html'
            return render(request,template_name)
    else:
        context = {}
        template_name = "MAINAPP/login.html"
        return render(request,template_name,context)

def home(request):
    template_name = "MAINAPP/home.html"
    return render(request,template_name)

@login_required(login_url='login')
def product(request):
    template_name = "MAINAPP/product.html"
    return render(request,template_name)

def logoutView(request):
    logout(request)
    return redirect('login')

def view1(request):
    #resp = HttpResponse("Hello")
    resp = render(request,template_name="MAINAPP/v1.html")
    if request.method == 'POST':
        n = request.POST['name']
        print(n)
    #resp.set_cookie("rn",'1')
        resp.set_cookie('name',n,max_age=20)
        resp.set_cookie('marks',100,max_age=20)
    return resp
def view2(request):
    n = request.COOKIES.get('name','none')
    m = request.COOKIES.get('marks',0)
    #r = request.COOKIES.get('rn',0)
    #context = {'name':n,'rn':r}
    context = {'name':n,'marks':m}
    return render(request,template_name="MAINAPP/v2.html",context=context)
def view3(request):
    cnt = int(request.COOKIES.get('visits',0))
    cnt = cnt + 1
    resp = render(request,'MAINAPP/v3.html',{'count':cnt})
    resp.set_cookie('visits',str(cnt))
    return resp