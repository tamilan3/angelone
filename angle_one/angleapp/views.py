from django.shortcuts import render
from smartapi import SmartConnect,SmartWebSocket 
import xlwings as xw
import pandas as pd
import pyotp
def test(request):
    
    #create object of call
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
    return render(request,"angleapp/index.html",context)
