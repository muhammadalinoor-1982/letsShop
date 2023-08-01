import uuid
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from .models import *


def user_login(request):
    if request.method == 'POST':
        UserName = request.POST.get('username')
        Pass = request.POST.get('password')
        if len(Pass) == 0:
            messages.error(request, 'Password should not be BLANK..!!')
            return redirect('user_login')
        user = authenticate(username=UserName, password=Pass)
        if user:
            prof = Profile.objects.get(user=user)
            if prof.is_verified == True:
                login(request, user)
                return redirect('pro')
            else:
                prof.is_verified == False
                messages.error(request, 'Please verify your Email')
                return redirect('error')
        else:
            messages.error(request, 'Invalid User Name or Password....!! Please Tray again')
            return redirect('user_login')
    return render(request, 'Accounts/pages/Auth/login.html')

def user_logout(request):
    logout(request)
    messages.info(request, 'You are logged out')
    return redirect('user_login')

def register(request):
    if request.method == 'POST':
        First_name = request.POST.get('first')
        Last_name  = request.POST.get('last')
        UserName   = request.POST.get('name')
        Email      = request.POST.get('email')
        Pass       = request.POST.get('pass')
        Pass1      = request.POST.get('pass1')

        if UserName is not None:

            # Start Name Validation
            for i in UserName:
                if i in ['@', '#', '$', '%', '&', '()', '=', '{}', '[]']:
                    messages.warning(request, 'Please Remove Special Characters')
                    return redirect('register')
            # End Name Validation

            # Start Name Unique
            if User.objects.filter(username=UserName).exists():
                messages.warning(request, 'Given User Name Already been Exist...!!!  Please Try Other One')
            # End Name Unique

            # Start Email Unique
            elif User.objects.filter(email=Email).exists():
                messages.warning(request, 'Given Email Already been Exist...!!!  Please Try Other One')
            # End Email Unique

            else:
                # Start Check Password Matching
                if Pass == Pass1:
                # End Check Password Matching

                    user = User.objects.create_user(
                        first_name=First_name,
                        last_name=Last_name,
                        username=UserName,
                        email=Email,
                        password=Pass)

                # Start Password Hashing
                    user.set_password(Pass)
                # End Password Hashing

                    auth_token = str(uuid.uuid4())
                    prof_obj = Profile.objects.create(user=user, auth_token=auth_token)
                    prof_obj.save()
                    send_mail_reg(Email, auth_token)
                    #messages.success(request, 'Account has been created')
                    return redirect('success')
                else:
                    messages.error(request, 'Your Given Password not matched With Confirm Password')
            '''
            print('\n'f' Your First Name: {First_name}. '
                  '\n'f' Your Last Name: {Last_name}. '
                  '\n'f' Your Full Name: {UserName}. '
                  '\n'f' Your Email: {Email}. '
                  '\n'f' Your Password: {Pass}. '
                  '\n'f' Your Confirm Password: {Pass1}.')
                  '''
    return render(request, 'Accounts/pages/Auth/registration.html')

def success(request):
    return render(request, 'Accounts/pages/emailVerification/success.html')

def token_send(request):
    return render(request, 'Accounts/pages/emailVerification/token_send.html')

def error(request):
    return render(request, 'Accounts/pages/emailVerification/error.html')

def send_mail_reg(Email, auth_token):
    subject = 'Your Account Authentication Link'
    message = f'Hi..!! Please Click The Link to Verify Your Account  http://127.0.0.1:8000/Accounts/verify/{auth_token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [Email]
    send_mail(subject, message, email_from, recipient_list)

def verify(request, auth_token):
    prof_obj = Profile.objects.filter(auth_token=auth_token).first()
    prof_obj.is_verified = True
    prof_obj.save()
    messages.success(request, 'Congratulations...!!!!   Your Account has been verified')
    return redirect('user_login')

def reset_pass(request):
    if request.method == 'POST':
        Email = request.POST.get('email')
        Pass  = request.POST.get('pass')
        Pass1 = request.POST.get('pass1')

    return render(request, 'Accounts/pages/Auth/reset_pass.html')




















def adomx(request):
    return render(request, 'Accounts/layout/master.html')

def show(request):
    return render(request, 'Accounts/pages/related/show.html')

def dtable(request):
    return render(request, 'Accounts/pages/related/dtable.html')

def form(request):
    return render(request, 'Accounts/pages/related/form.html')

def details(request):
    return render(request, 'Accounts/pages/related/details.html')
