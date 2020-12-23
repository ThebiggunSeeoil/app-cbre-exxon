
# -*- coding: utf-8 -*-
from django.conf import settings # calls the object written in settings.py
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests
from linebot.line_tamplates import *
from app.models import PersanalDetaillogin
from linebot.rich_menu_function import *
from app.models import Workfromgmail
import arrow
import datetime
from django.contrib.auth.models import Group, User
# from googleapiclient.discovery import build
# from google_auth_oauthlib.flow import InstalledAppFlow
# from google.auth.transport.requests import Request
import pickle
import os.path
import base64
import email
# from bs4 import BeautifulSoup
#0000000

Channel_access_token=settings.LINE_CHANNEL_ACCESS_TOKEN
#ddddddddd
# this is for testing
def index(request):
    return HttpResponse("test!!")
# this is code is modeified from https://github.com/line/line-bot-sdk-python
@csrf_exempt # this is used for avoid csrf request from line server
def callback(request):
    if request.method == "POST":
        payload = json.loads(request.body.decode('utf-8'))
        if payload['events'][0]['type'] == 'new_email':
            group =  Group.objects.filter()
            for I in group :
                print (I.name)
            vender=payload['events'][0]['vender']
            for I in group :
                if vender[0:5] in I.name :
                    service_id=I.id
            workorder=payload['events'][0]['workorder']
            sitename=payload['events'][0]['sitename']
            opendate=payload['events'][0]['opendate']
            description=payload['events'][0]['description']
            fm=payload['events'][0]['fm']
            # today = datetime.datetime.now().strftime("%Y-%m-%d")
            today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            print(vender)
            print(workorder)
            print(sitename)
            print(opendate)
            print(description)
            print(fm)
            save_record=Workfromgmail()
            save_record.workorder=workorder
            save_record.opended=opendate
            save_record.caller=sitename
            save_record.service_provider=vender
            save_record.service_id=service_id
            save_record.problum=description
            save_record.fm=fm
            save_record.date_create=today
            save_record.save(request)
            return HttpResponse(200)
        else : 
            payload = json.loads(request.body.decode('utf-8'))
            global Reply_token
            global User_id
            Reply_token = payload['events'][0]['replyToken']
            User_id = payload['events'][0]['source']['userId']
            #print (payload)
            if payload['events'][0]['type'] == 'follow':
                ReplyMessage(line_templates.Gressing_msg())
                return HttpResponse(200)
            if payload['events'][0]['type'] == 'message':
                message = payload['events'][0]['message']['text']
                if message == 'test':
                    ReplyMessage(line_templates.Gressing_msg())
                    return HttpResponse(200)
                if (message[0:4]).lower() == 'cbre':
                    print(message)
                    command_payload = ((payload['events'][0]['message']['text'])[0:4]).lower()+((payload['events'][0]['message']['text'])[4:])
                    code_login = (command_payload[command_payload.index('cbre') + 4:])
                    try :
                        id_user = PersanalDetaillogin.objects.filter(key_login=code_login).first()
                        if id_user != None :
                            if id_user.member_status == 'none' :
                                global name
                                global company
                                name=id_user.name
                                company=id_user.company
                                ReplyMessage(line_templates.ensure_submit(id_user))
                            else:
                                ReplyMessage(line_templates.alreadySubmit_code(id_user))
                        else :
                            ReplyMessage(line_templates.re่ject_code())        
                    except PersanalDetaillogin.DoesNotExist:
                        ReplyMessage(line_templates.re่ject_code())
                        return None 
            if payload['events'][0]['type'] == 'postback':
                message = payload['events'][0]['postback']['data']
                if message == 'register' :
                    ReplyMessage(line_templates.register_code())
                if message == 'REGISTER-OK' :
                    register_user=PersanalDetaillogin.objects.filter(name=name,company=company).update(member_status='registed',line_id=User_id)
                    ReplyMessage(line_templates.registed())
                if message == 'Data 1':
                    try :
                        id_user = PersanalDetaillogin.objects.filter(line_id=User_id).first()
                        if id_user != None :
                            if id_user.company == "CBRE":
                                Link_rich_menu_to_user(settings.CBRE_MENU,id_user.line_id)
                                updaterich_menu=PersanalDetaillogin.objects.filter(line_id=User_id).update(richmenu_id=settings.CBRE_MENU)
                                ReplyMessage(line_templates.login())
                            else:
                                Link_rich_menu_to_user(settings.CONTRACTOR_MENU,id_user.line_id)
                                updaterich_menu=PersanalDetaillogin.objects.filter(line_id=User_id).update(richmenu_id=settings.CBRE_MENU)
                                ReplyMessage(line_templates.login())
                        else:
                            ReplyMessage(line_templates.re่ject_not_register())
                            print ('NOT OK user_id')
                    except PersanalDetaillogin.DoesNotExist:
                        print ('NO DATA user_id')
                if message == 'logout' :
                    try :
                        id_user = PersanalDetaillogin.objects.filter(line_id=User_id).first()
                        if id_user != None :
                            if id_user.company == "CBRE":
                                Link_rich_menu_to_user(settings.DEFULT_RICH_MUNU,id_user.line_id)
                                updaterich_menu=PersanalDetaillogin.objects.filter(line_id=User_id).update(richmenu_id=settings.DEFULT_RICH_MUNU)
                                ReplyMessage(line_templates.logout())
                            else:
                                Link_rich_menu_to_user(settings.DEFULT_RICH_MUNU,id_user.line_id)
                                updaterich_menu=PersanalDetaillogin.objects.filter(line_id=User_id).update(richmenu_id=settings.DEFULT_RICH_MUNU)
                                ReplyMessage(line_templates.logout())
                        else:
                            print ('NOT OK user_id')
                    except PersanalDetaillogin.DoesNotExist:
                        print ('NO DATA user_id')
                return HttpResponse(200)
            
            return HttpResponse(200)


def ReplyMessage(TextMessage):
    Token=Channel_access_token
    Reply_token_line=Reply_token
    LINE_API = 'https://api.line.me/v2/bot/message/reply'
    # print('line API {}'.format(TextMessage))
    Authorization = 'Bearer {}'.format(Token)
    # print(Authorization)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': Authorization
    }

    data = {
        "replyToken": Reply_token_line,
        "messages": [TextMessage], }

    data = json.dumps(data)
    # print('data to line {}'.format(data))
    r = requests.post(LINE_API, headers=headers, data=data)
    print(r)
    return 200

def PushMessage(push_new_messasge,user_id):
    Token=Channel_access_token
    LINE_API = 'https://api.line.me/v2/bot/message/push'
    # print('line API {}'.format(push_new_messasge))

    Authorization = 'Bearer {}'.format(Token)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': Authorization
    }

    data = {
        "to": user_id,
        "messages": [push_new_messasge], }

    # print('data to line {}'.format(data))
    data = json.dumps(data)
    r = requests.post(LINE_API, headers=headers, data=data)
    print(r)
    return 200
    
def send_notify(message, token):
    try:
        Token = 'Bearer ' + token

        LINE_ACCESS_TOKEN = Token
        url = 'https://notify-api.line.me/api/notify'
        token = LINE_ACCESS_TOKEN
        headers = {'content-type': 'application/x-www-form-urlencoded', 'Authorization': LINE_ACCESS_TOKEN}
        r = requests.post(url, headers=headers, data={'message': message})
        print
        r.text
    except  requests.ConnectionError as err:
        print("Connected to Line notify fail")


def PushMessage_group(push_new_messasge, Token, group_id_site):
    LINE_API = 'https://api.line.me/v2/bot/message/push'
    Authorization = 'Bearer {}'.format(Token)  ##ที่ยาวๆ
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': Authorization
    }

    data = {
        "to": group_id_site,
        "messages": [push_new_messasge], }
    data = json.dumps(data)
    r = requests.post(LINE_API, headers=headers, data=data)
    return 200