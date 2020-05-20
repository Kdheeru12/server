from django.conf import settings
from .models import Orders
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.core.mail import send_mail
import random
from .orders import OrderForm
from .forms import Ordersforms
from django.core.files.storage import FileSystemStorage
# Create your views here.
def homepage(request):
    return redirect('letsconnect')
def signup(request):
    if request.method == 'POST':
        global first_name
        global last_name
        global email
        global password
        global phonenumber
        first_name = request.POST['first']
        last_name = request.POST['last']
        email = request.POST['email']
        phonenumber = request.POST['phonenum']
        password = request.POST['password']
        globals()['first_name']=first_name
        globals()['last_name'] = last_name
        globals()['email'] = email
        globals()['password'] = password
        globals()['phonenumber'] = phonenumber
        if User.objects.filter(username=phonenumber).exists():
            messages.info(request,'PhoneNumber Taken')
            return redirect('signup')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email taken')
            return redirect('signup')
        else:
            global otp
            otp = random.randint(100000,999999)
            otp1 = str(otp)
            print(otp, otp1)
            globals()['otp'] = otp1
            #user = User.objects.create_user(username=phonenumber,password=password,email=email,first_name=first_name,last_name=last_name)
            #user.save()
            send_mail('Regarding Login Into the WEBSITE',
            'Hello '  + first_name+ '  otp for login is: ' + otp1,
            'letsconnectsociety@gmail.com',
            [email],
            fail_silently=False,
            )
            print('mail sent')
            user = User.objects.create_user(username=phonenumber,password=password,email=email,first_name=first_name,last_name=last_name)
            user.save()
            return redirect('login')
        return render(request,'signup.html')
    else:
        return render(request,'signup.html')
def signuppage(request):
    return render(request,'signup.html')
def login(request):
    if request.method == 'POST':
        password = request.POST['password']
        email = request.POST['email']
        user = auth.authenticate(username=email,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'test.html')
            
        else:
            messages.info(request,'invalid phone or password')
            return redirect('/login')
    else:
        return render(request,'test.html')
def letsconnect(request):
        return render(request,'index.html')
def logout(request):
    auth.logout(request)
    return redirect('login')
def verification(request):
    if request.method == 'POST':
        email_otp = request.POST['Email_otp'] 
        messages.info(request,'otp verified')
       
        print('user logined')
        return redirect('login')
    else:
        return redirect('signup')
def place_orders(request):
    if request.method == 'POST':
        upload = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(upload.name, upload)
        uploaded_file_url = fs.url(filename)
        name = request.POST["name"]
        phonenumber = request.POST["phonenumber"]
        alt_number = request.POST["alt_number"]
        address = request.POST["address"]
        landmark = request.POST["landmark"]
        print(address)
        orders = Orders(name=name,phonenumber=phonenumber,alt_number=alt_number,address=address,ordered=uploaded_file_url,landmark=landmark) 
        orders.save()
        return redirect('orders')
    else:
        return redirect('signup')
def orders(request):
    if request.method == 'POST':
        phonenumber = request.POST["phonenumber"]
        print(phonenumber)
        orders=Orders.objects.filter(phonenumber=phonenumber)
        return render(request,"orders.html",{'orders':orders})
    else:
        return render(request,'dd.html')
def test(request):

    if request.method == "POST":
        upload = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(upload.name, upload)
        uploaded_file_url = fs.url(filename)

    return render(request, 'saved.html')