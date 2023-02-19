from django.shortcuts import render, redirect
from django.http import HttpResponse
from studentstudyportal import settings
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from .tokens import generate_token
from django.core.mail import EmailMessage
from django.contrib.auth import logout
from dashboard.models import Homework, ToDo

# Create your views here.

def UserRegistrationView(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username=request.POST.get('username')
            email=request.POST.get('email')
            password1=request.POST.get('password1')
            password2=request.POST.get('password2')

            if password1 != password2:
                messages.warning(request,"Passwords didn't match!!!")
            
            myuser=User.objects.create_user(username, email, password1)
            myuser.is_active=False
            myuser.save()
            messages.success(request,"You Successfully Created Account. We have send comfirmation email")

            # Welcome Email !!!!!!!!!!!!!!!!!!!!!!!!!!
            subject="Welcome to Student Study Portal"
            message="Hello "+myuser.username+" !!!!\n"+"Welcome to Student Study Portal!!\nThank you for visiting our website.\nWe have also send you confirmation email, Please confirm your email in order to activat your account."+"Thank you,\nPratik Deshmukh"
            from_email=settings.EMAIL_HOST_USER
            to_email_list=[myuser.email]
            send_mail(subject, message, from_email, to_email_list, fail_silently=True)


            # Confirmation Email !!!!!!!!!!!!!!!!!!!!!
            print(myuser.id)
            current_site = get_current_site(request)
            subject2 = "Welcome to Student Study Portal-Login"
            message2 = render_to_string('user/emailcomfirmation.html',{
                'name' : myuser.username,
                'domain' : current_site.domain,
                'uid' : urlsafe_base64_encode(force_bytes(myuser.id)),
                'token' : generate_token.make_token(myuser)

            })
            print(urlsafe_base64_encode(force_bytes(myuser.id)))
            email = EmailMessage(
                subject2,
                message2,
                settings.EMAIL_HOST_USER,
                [myuser.email],
            )
            email.fail_silently = True
            email.send()
            return redirect('login')
        


    else:
        form=UserRegistrationForm()
    context={
        'form':form
    }
    return render(request,'user/register.html',context)

def activate(request, uidb64, token):
    try:
        uid =  force_str(urlsafe_base64_decode(uidb64))
        print(uid)
        print(User.objects.get(id=uid))
        myuser = User.objects.get(id=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        messages.success(request,"Your account successfully activated")
        return redirect('login')

    else:
        return render(request,'activationfail.html')



def ProfileView(request):
    homeworks = Homework.objects.filter(is_finish=False, user=request.user)
    todos = ToDo.objects.filter(status=False, user=request.user)
    print(len(homeworks))
    print(len(todos))
    if len(homeworks) == 0:
        homework_done = True
    else:
        homework_done = False

    if len(todos) == 0:
        todo_done = True
    else:
        todo_done = False

    context={
        'homeworks':homeworks,
        'homework_done':homework_done,
        'todos':todos,
        'todo_done':todo_done,
    }
    return render(request,'user/profile.html', context)