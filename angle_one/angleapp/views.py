from django.shortcuts import render,redirect
from smartapi import SmartConnect,SmartWebSocket 
from django.contrib.auth.models import User
import xlwings as xw
import pandas as pd
import pyotp
from django.contrib.auth import authenticate,login as loginUser,logout
from .decorator import unauthenticated_user
def test(request):
    
    """ #create object of call
    obj=SmartConnect(api_key="Ik1MXGvu")
    #login api call
    data = obj.generateSession("D50876758","2580",pyotp.TOTP("TF4PXX4D3WVPAYFPDSVN6WUFEQ").now())
    refreshToken= data['data']['refreshToken']

    #fetch the feedtoken
    feedToken=obj.getfeedToken()
    try:
        historicParam={
        "exchange": "NSE",
        "symboltoken": "3045",
        "interval": "ONE_MINUTE",
        "fromdate": "2023-05-12 09:00", 
        "todate": "2023-05-12 10:30"
        } 
        data=obj.getCandleData(historicParam)
    except Exception as e:
        print("Historic Api failed: {}".format(e.message))   
    context={
        'token':feedToken,
        'data':data
    }     

    """
    return render(request,"angleapp/index.html")

@unauthenticated_user
def login_reg(request):
    if request.method=='GET':
        return render(request,"angleapp/login_register.html")
    elif request.method=='POST':
        if 'form1' in request.POST:
            username=request.POST.get("username")
            email=request.POST.get("email")
            password=request.POST.get("password")
            user=User.objects.create_user(username,password,email)
            if user is None:
                user.save()
                return redirect('/auth')
            else:    
                return render(request,"angleapp/login_register.html")
        elif 'form2' in request.POST:
            username=request.POST.get("username")
            password=request.POST.get("password")
            print(username+" and // "+password)
            user=authenticate(request,username=username,password=password)
            if user is not None:
                loginUser(request,user)
                return redirect('/index') 
            else:
                return render(request,"angleapp/login_register.html")