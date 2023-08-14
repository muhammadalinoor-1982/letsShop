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
                return redirect('error')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid User Name or Password....!! Please Tray again')
    return render(request, 'Accounts/pages/Auth/login.html')
# End Login

# Start Logout
def user_logout(request):
    logout(request)
    messages.info(request, 'You are logged out')
    return redirect('user_login')
# End Logout

# Start Registration
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
                        first_name  =First_name,
                        last_name   =Last_name,
                        username    =UserName,
                        email       =Email,
                        password    =Pass)

                # Start Password Hashing
                    user.set_password(Pass)
                # End Password Hashing

                # Start Generate Token
                    auth_token = str(uuid.uuid4())
                # End Generate Token

                # Start Save Registration Credentials with a Token in the Database
                    prof_obj = Profile.objects.create(user=user, auth_token=auth_token)
                    prof_obj.save()
                # End Save Registration Credentials with a Token in the Database

                # Start Sent Email with Token
                    send_mail_reg(Email, auth_token)
                # End Sent Email with Token

                    #messages.success(request, 'Account has been created')
                    return redirect('success')
                else:
                    messages.error(request, 'Your Given Password not matched With Confirm Password')

    return render(request, 'Accounts/pages/Auth/registration.html')
# End Registration

def success(request):
    return render(request, 'Accounts/pages/emailVerification/success.html')

def token_send(request):
    return render(request, 'Accounts/pages/emailVerification/token_send.html')

def error(request):
    return render(request, 'Accounts/pages/emailVerification/error.html')

# Start Email Sending Process for Email Verification
def send_mail_reg(Email, auth_token):
    subject = 'Your Account Authentication Link'
    message = f'Hi..!! Please Click The Link to Verify Your Account  http://127.0.0.1:8000/Accounts/verify/{auth_token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [Email]
    send_mail(subject, message, email_from, recipient_list)
# End Email Sending Process for Email Verification

# Start Email Verification Process
def verify(request, auth_token):
    prof_obj = Profile.objects.filter(auth_token=auth_token).first()
    prof_obj.is_verified = True
    prof_obj.save()
    messages.success(request, 'Congratulations...!!!!   Your Account has been verified')
    return redirect('user_login')
# End Email Verification Process

def reset_pass(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            user_prof = User.objects.get(email=email)
            if user_prof:
                res_prof = Profile.objects.get(user=user_prof)
                auth_token = res_prof.auth_token
                send_mail_reset(email, auth_token)
                return redirect('success_reset')
            else:
                messages.error(request, 'Email Address Not Found')
                return redirect('reset_pass')
    return render(request, 'Accounts/pages/Auth/reset_pass.html')

def success_reset(request):
    return render(request, 'Accounts/pages/emailVerification/success_reset.html')

# Start Email Sending Process for Reset Password
def send_mail_reset(Email, auth_token):
    subject = 'Your Password Reset Link'
    message = f'Hi..!! Please Click The Link to Reset Your Password  http://127.0.0.1:8000/Accounts/Reset_user_pass/{auth_token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [Email]
    send_mail(subject, message, email_from, recipient_list)
# End Email Sending Process for Reset Password

def Reset_user_pass(request, auth_token):
    profile_obj = Profile.objects.filter(auth_token=auth_token).first()
    if profile_obj:
        if request.method == 'POST':
            pass0 = request.POST.get('pass')
            pass1 = request.POST.get('pass1')
            if pass0:
                if pass0 == pass1:
                    user = profile_obj.user
                    user.set_password(pass0)
                    user.save()
                    messages.success(request, 'Your Password Has Been Reset Successfully')
                    return redirect('user_login')
                else:
                    messages.error(request, 'Retype Password Has Not Been Matched')
            else:
                messages.error(request, 'Password Should Not Be Blank')

    return render(request, 'Accounts/pages/Auth/new_pass.html')

def userDetails(request):
    user = request.user
    add = Address.objects.filter(user=user)
    return render(request, 'Accounts/pages/my_profile/user_details.html', locals())

















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
