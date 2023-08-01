from django.urls import path
from .views import *

urlpatterns = [

    #URL for Related Page
    path('adomx/', adomx, name='adomx'),
    path('show/', show, name='show'),
    path('dtable/', dtable, name='dtable'),
    path('form/', form, name='form'),
    path('details/', details, name='details'),

    #URL for Athentication
    path('user_login/', user_login, name='user_login'),
    path('user_logout/', user_logout, name='user_logout'),
    path('register/', register, name='register'),
    path('reset_pass/', reset_pass, name='reset_pass'),

    #URL for E-Mail Verification
    path('success/', success, name='success'),
    path('token_send/', token_send, name='token_send'),
    path('error/', error, name='error'),
    path('verify/<auth_token>/', verify, name='verify')
]
