# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required
from django.db import models
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from app.models import WorkPending , SiteList  , PersanalDetaillogin , WahSubmitforcontractor , Workfromgmail , type_of_work
from app.resources import SiteListResource
from django.core.paginator import Paginator, EmptyPage,InvalidPage
from django.contrib import messages
from django.db.models import Q
from django.db.models import Count
from django.db.models.functions import Lower
import json
import requests
from django.views.decorators.csrf import csrf_exempt
from app.createflexmessage import *
from linebot.views import PushMessage , send_notify
import datetime
import arrow
from django.db.models import F, Sum
# import schedule

# date = arrow.now().format('YYYY-MM-DD')
# date_new = arrow.now()
today = datetime.datetime.now().strftime("%Y-%m-%d")
tomorrow = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
@login_required(login_url="/login/")
def index(request):
    if request.user.is_authenticated:
        # สร้างไว้ป้องกันในกรณี ระบบจำ user ไว้ จะได้ direct ไปหาหน้าของตัวเอง เช่น หน้าของ ผรม
        group = request.user.groups.values_list('name', flat=True).first() #เรียกหา GroupID
        if group == 'CBRE':
            status_pending ='INPRG'
            count_today_planning_work=WahSubmitforcontractor.objects.filter(planned_date=str(today),status='in planing').count()
            count_tomorrow_planning_work=WahSubmitforcontractor.objects.filter(planned_date=str(tomorrow),status='in planing').count()
            count_wah_onsite_count=WahSubmitforcontractor.objects.filter(status='onsite').count()
            count_wah_completed_count=WahSubmitforcontractor.objects.filter(status='completed').count()
            request.session['count_tomorrow_planning_work'] = count_tomorrow_planning_work
            request.session['count_today_planning_work'] = count_today_planning_work
            request.session['count_wah_onsite_count'] = count_wah_onsite_count
            request.session['count_wah_completed_count'] = count_wah_completed_count
            submited_work=WahSubmitforcontractor.objects.filter(status='in planing') 
            today_planning_work=WahSubmitforcontractor.objects.filter(planned_date=str(today),status='in planing') 
            tomorrow_planning_work=WahSubmitforcontractor.objects.filter(planned_date=str(tomorrow),status='in planing') 
            work_at_site=WahSubmitforcontractor.objects.filter(status='onsite') 
            pendingworkdetailmycompany=WahSubmitforcontractor.objects.annotate(lower_title=Lower('status')).values('status').annotate(num=Count('status')).order_by('company')
            pendingworkdetail2=WahSubmitforcontractor.objects.filter(status='in planing').count() | WahSubmitforcontractor.objects.filter(status='onsite').count()
            count_wah_onsite=WahSubmitforcontractor.objects.filter(status='onsite')
            print (pendingworkdetail2)
            
            return render(request, "index.html",{'work_at_site':work_at_site,'tomorrow_planning_work':tomorrow_planning_work,'today_planning_work':today_planning_work ,'count_wah_onsite':count_wah_onsite,'count_today_planning_work':count_today_planning_work , 'count_tomorrow_planning_work':count_tomorrow_planning_work ,'count_wah_onsite_count':count_wah_onsite_count , 'count_wah_completed_count':count_wah_completed_count , 'submited_work':submited_work , 'pendingworkdetailmycompany':pendingworkdetailmycompany})
        else:
            return redirect("contractor") #ส่งค่าไปแสดงผลที่ index.html 
            #return redirect(request,'contractor.html',{'group':group , 'id':current_user.id}) #ส่งค่าไปแสดงผลที่ index.html 
    

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template = request.path.split('/')[-1]
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'error-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'error-500.html' )
        return HttpResponse(html_template.render(context, request))

def export(request):
    SiteList_resource = SiteListResource()
    WorkPending_resource= SiteListResource()
    dataset = SiteList_resource.export()
    dataset = WorkPending_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="member.csv"'
    response = HttpResponse(dataset.json, content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="persons.json"'
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="persons.xls"'
    return response

def contractorreport_ (request) :
    #สร้างการเชื่อมต่อ sql ที่นี่ 
    if request.user.is_authenticated:
        contractor = request.user.groups.values_list('name', flat=True).first() #เรียกหา GroupID
        # contractor='KVM ENGINEERING CO.,LTD'
        status_pending ='INPRG'
        status_completed = 'COMP'
        pendingworks=Workfromgmail.objects.filter(service_provider=contractor, status=status_pending) # ดึงอีเมลล์จากฐานข้อมูล เงื่อนไข คือ อีเมลล์ตรงกัน
        pendingcount=Workfromgmail.objects.filter(status=status_pending,service_provider=contractor).count()
        completedcount=Workfromgmail.objects.filter(status=status_completed,service_provider=contractor).count()
        wah_submited=WahSubmitforcontractor.objects.filter(company=contractor,status="in planing")
        wah_submitedcount=WahSubmitforcontractor.objects.filter(company=contractor,status="in planing").count()
        wah_onsite=WahSubmitforcontractor.objects.filter(company=contractor,status="onsite").count()
        wah_completed=WahSubmitforcontractor.objects.filter(company=contractor,status="completed").count()
        
        # print ('CompletedWork',wah_completed)
        
        #print (current_user.id)
        paginator=Paginator(pendingworks,5) #ตั้งค่าให้แสดง 4 รายการต่อหน้า
        try :
            page=int(request.GET.get('page','1'))
        except:
            page=1

        try:
            workpendingperpage=paginator.page(page)
        except (EmptyPage,InvalidPage):
            workpendingperpage=paginator.page(paginator.num_pages)
        
    return render(request,'contractor.html',{'pendings':workpendingperpage ,'wahsubmits':wah_submited,'pendingcount':pendingcount,'completedcount':completedcount ,'wahsubited':wah_submitedcount ,'wah_onsite':wah_onsite , 'wah_completed':wah_completed})

def contractorreport(request) :
    #สร้างการเชื่อมต่อ sql ที่นี่ 
    if request.user.is_authenticated:
        contractor_id = request.user.groups.values_list('id', flat=True).first() #เรียกหา GroupID
        contractor = request.user.groups.values_list('name', flat=True).first() #เรียกหา GroupID
        contractor_initials_name = request.user.groups.values_list('initials_name', flat=True).first() #เรียกหา GroupID
        request.session['contractor_id'] = contractor_id
        request.session['contractor'] = contractor
        request.session['contractor_initials_name'] = contractor_initials_name
        # contractor='KVM ENGINEERING CO.,LTD'
        pendingworks=Workfromgmail.objects.filter(service_id=request.session['contractor_id'],status_submit__isnull=True) # ดึงอีเมลล์จากฐานข้อมูล เงื่อนไข คือ อีเมลล์ตรงกัน
        pendingcount=Workfromgmail.objects.filter(service_id=request.session['contractor_id'],status_submit__isnull=True).count()
        # completedcount=WorkPending.objects.filter(status=status_completed,service_provider=contractor).count()
        wah_submited=WahSubmitforcontractor.objects.filter(company_id=request.session['contractor_id'],status="in planing")
        wah_submitedcount=WahSubmitforcontractor.objects.filter(company_id=request.session['contractor_id'],status="in planing").count()
        wah_onsite=WahSubmitforcontractor.objects.filter(company_id=request.session['contractor_id'],status="onsite").count()
        wah_completed=WahSubmitforcontractor.objects.filter(company_id=request.session['contractor_id'],status="completed").count()
        # print ('CompletedWork',wah_completed)
        
        #print (current_user.id)
        paginator=Paginator(pendingworks,5) #ตั้งค่าให้แสดง 4 รายการต่อหน้า
        try :
            page=int(request.GET.get('page','1'))
        except:
            page=1

        try:
            workpendingperpage=paginator.page(page)
        except (EmptyPage,InvalidPage):
            workpendingperpage=paginator.page(paginator.num_pages)
        
    return render(request,'contractor.html',{'pendings':workpendingperpage ,'wahsubmits':wah_submited,'pendingcount':pendingcount,'completedcount':wah_completed ,'wahsubited':wah_submitedcount ,'wah_onsite':wah_onsite , 'wah_completed':wah_completed})

    


@login_required(login_url='singIn') # เป็นการบังคับให้ login ก่อนทำการกดสักซื้อ
def addWAH(request,workorder):
    # status_pending ='INPRG'
    # global contractor_id
    # contractor = request.user.groups.values_list('name', flat=True).first() #เรียกหา GroupID
    # contractor_id = request.user.groups.values_list('id', flat=True).first() #เรียกหา GroupID
    description=Workfromgmail.objects.filter(service_id=request.session['contractor_id'], workorder=workorder)
    pendingcount=Workfromgmail.objects.filter(service_id=request.session['contractor_id']).count()
    wah_submitedcount=WahSubmitforcontractor.objects.filter(company_id=request.session['contractor_id'],wah_status="submited").count()
    wah_onsite=WahSubmitforcontractor.objects.filter(company_id=request.session['contractor_id'],status="onsite").count()
    wah_completed=WahSubmitforcontractor.objects.filter(company_id=request.session['contractor_id'],status="completed").count()
    fm_detail=PersanalDetaillogin.objects.filter(company='CBRE')
    worktype_detail=type_of_work.objects.all()
    fls_detail=PersanalDetaillogin.objects.filter(company_id=request.session['contractor_id'])
    for workdescription in description :
        print (workdescription)
        work_detail= (workdescription.problum)
        sitename = (workdescription.caller)
    print (workorder)
    print (description)
    # new_wah.save()
    
    return render (request,'submit_wah.html',{'worktype_detail':worktype_detail,'workorder':workorder , 'contractor':request.session['contractor'], 'workdetail':work_detail , 'sitename':sitename,'wahsubited':wah_submitedcount ,'wah_onsite':wah_onsite , 'wah_completed':wah_completed , 'pendingcount':pendingcount , 'fm_detail':fm_detail ,"fls_detail":fls_detail})

@login_required(login_url='singIn') # เป็นการบังคับให้ login ก่อนทำการกดสักซื้อ
def addWAHtoDB(request):
    open_work = open
    wah_status = 'submited'
    status_onsite='in planing'
    print('inside addwahtodb')
    if request.method == "POST" :
        print('inside post method')
        if request.POST.get('planned_date') and request.POST.get('caller') and request.POST.get('job_description') and request.POST.get('workorder') and request.POST.get('company') and request.POST.get('fls_mame_1') and request.POST.get('fls_mame_2') and request.POST.get('fls_phone') and request.POST.get('management') and request.POST.get('remark') and request.POST.get('type_job') and request.POST.get('jla_ra') and request.POST.get('any_ssw') and request.POST.get('physical') and request.POST.get('fm'):
            workorder = request.POST.get('workorder')
            contractor = request.POST.get('company')
            token=PersanalDetaillogin.objects.filter(name=request.POST.get('fls_mame_1')).values_list('group_id')[0][0]
            print('Token is',token)
            fls_id_1 = PersanalDetaillogin.objects.filter(name=request.POST.get('fls_mame_1')).values_list('id')[0][0]
            fls_id_2 = PersanalDetaillogin.objects.filter(name=request.POST.get('fls_mame_2')).values_list('id')[0][0]
            print ('fls name is ')
            save_record=WahSubmitforcontractor()
            save_record.planned_date=request.POST.get('planned_date')
            save_record.caller=request.POST.get('caller')
            save_record.job_description=request.POST.get('job_description')
            save_record.workorder=request.POST.get('workorder')
            save_record.company=request.POST.get('company') 
            save_record.fls_mame_1=request.POST.get('fls_mame_1')
            save_record.fls_mame_2=request.POST.get('fls_mame_2')
            save_record.fls_id_1=fls_id_1
            save_record.fls_id_2=fls_id_2
            save_record.fls_phone=request.POST.get('fls_phone')
            save_record.management=request.POST.get('management')
            save_record.remark=request.POST.get('remark')
            save_record.type_job=request.POST.get('type_job')
            save_record.jla_ra=request.POST.get('jla_ra')
            save_record.any_ssw=request.POST.get('any_ssw')
            save_record.physical=request.POST.get('physical')
            save_record.fm=request.POST.get('fm')
            save_record.openned=open_work
            save_record.wah_status=wah_status
            save_record.status=status_onsite
            save_record.company_id=request.session['contractor_id']
            save_record.initials_name=request.session['contractor_initials_name']
            save_record.save(request)
            udpate_pending_to_submitted=Workfromgmail.objects.filter(workorder=workorder).update(status_submit='yes')
            data_3=creatinglinemessages.submit_notify(request)
            send_notify(data_3,token)
            #return redirect(request,'contractor')

            return redirect('contractor')

@login_required(login_url='singIn') # เป็นการบังคับให้ login ก่อนทำการกดสักซื้อ
def editwah (request,id):
    print ('id is ',id)
    # contractor = request.user.groups.values_list('name', flat=True).first() #เรียกหา GroupID
    workforedit=WahSubmitforcontractor.objects.filter(company=request.session['contractor'], id=id)
    for workforedit in workforedit :
        id=workforedit.id
        workorder=workforedit.workorder
        company=workforedit.company
        opended=workforedit.opended
        status=workforedit.status
        startwork=workforedit.startwork
        completedwork=workforedit.completedwork
        caller=workforedit.caller
        wah_status=workforedit.wah_status
        planned_date=workforedit.planned_date
        job_description=workforedit.job_description
        fls_mame=workforedit.fls_mame_1
        fls_phone=workforedit.fls_phone
        management=workforedit.management
        remark=workforedit.remark
        type_job=workforedit.type_job
        jla_ra=workforedit.jla_ra
        any_ssw=workforedit.any_ssw
        physical=workforedit.physical
        fm=workforedit.fm
       
       
    return render (request,'edit_submitwah.html',{'id':id,'workorder':workorder ,'company':company ,'opended':opended , 'status':status , 'startwork':startwork , 'completedwork':completedwork , 'caller':caller , 'wah_status':wah_status , 'planned_date':planned_date , 'job_description':job_description , 'fls_mame':fls_mame , 'fls_phone':fls_phone , 'management':management , 'remark':remark , 'type_job':type_job , 'jla_ra':jla_ra , 'any_ssw':any_ssw , 'physical':physical , 'fm':fm })

@login_required(login_url='singIn') # เป็นการบังคับให้ login ก่อนทำการกดสักซื้อ
def updatewah (request,id):
    if request.method == "POST" : 
        if  request.POST.get('fls_mame') :
            print ('fls name is',request.POST.get('fls_mame'))
            token=PersanalDetaillogin.objects.filter(name=request.POST.get('fls_mame')).values_list('group_id')[0][0]
            print ('Token is',token)
        if request.POST.get('planned_date') :
            print (request.POST.get('planned_date'))
            ID = request.POST.get('id')
            planned_update= request.POST.get('planned_date')
            udpatedatawah=WahSubmitforcontractor.objects.filter(id=id).update(planned_date=planned_update)
            data_3=creatinglinemessages.updatedsubmit_notify(request)
            send_notify(data_3,token)
        
            return redirect('contractor')

@login_required(login_url='singIn') # เป็นการบังคับให้ login ก่อนทำการกดสักซื้อ
def seedetail (request,id):
    print ('id is ',id)
    contractor = request.user.groups.values_list('name', flat=True).first() #เรียกหา GroupID
    workforedit=WahSubmitforcontractor.objects.filter(id=id)
    for workforedit in workforedit :
        id=workforedit.id
        workorder=workforedit.workorder
        company=workforedit.company
        opended=workforedit.opended
        status=workforedit.status
        startwork=workforedit.startwork
        completedwork=workforedit.completedwork
        caller=workforedit.caller
        wah_status=workforedit.wah_status
        planned_date=workforedit.planned_date
        job_description=workforedit.job_description
        fls_mame=workforedit.fls_mame_1
        fls_phone=workforedit.fls_phone
        management=workforedit.management
        remark=workforedit.remark
        type_job=workforedit.type_job
        jla_ra=workforedit.jla_ra
        any_ssw=workforedit.any_ssw
        physical=workforedit.physical
        fm=workforedit.fm 
    return render (request,'seedetailofwork.html',{'count_wah_completed_count':request.session['count_wah_completed_count'],'count_wah_onsite_count':request.session['count_wah_onsite_count'],'count_tomorrow_planning_work':request.session['count_tomorrow_planning_work'],'count_today_planning_work':request.session['count_today_planning_work'],'workorder':workorder ,'company':company ,'opended':opended , 'status':status , 'startwork':startwork , 'completedwork':completedwork , 'caller':caller , 'wah_status':wah_status , 'planned_date':planned_date , 'job_description':job_description , 'fls_mame':fls_mame , 'fls_phone':fls_phone , 'management':management , 'remark':remark , 'type_job':type_job , 'jla_ra':jla_ra , 'any_ssw':any_ssw , 'physical':physical , 'fm':fm })

def liffpage (requests):
    return render (requests,'liffpagelogin.html')

@csrf_exempt
def check_userid(request):
    if request.method == "POST" : 
        # global user_id
        user_id=request.POST['user_id']
        request.session['user_id'] = user_id
        return HttpResponse('OK')
        
def wahwork(request):
    company_id = PersanalDetaillogin.objects.filter(line_id=request.session['user_id']).values_list('company_id')[0][0]
    request.session['company_id'] = company_id
    group = Group.objects.filter(id=company_id).values_list('name')[0][0]
    if group == 'CBRE':
        count_wah_submitedcount=WahSubmitforcontractor.objects.filter(status='in planing').count()
        count_wah_onsite_count=WahSubmitforcontractor.objects.filter(status='onsite').count()
    return render (request,'liffinformationwah.html',{"count_wah_submitedcount":count_wah_submitedcount , "count_wah_onsite_count":count_wah_onsite_count , "company_id":company_id})

def liffsubmitedwahbycontractor(request,id,type):
    if id == 3 :
        wahs_submited=WahSubmitforcontractor.objects.filter(status=type).values('company').annotate(dcount=Count('company'))
        print(wahs_submited)
    else:
        print(id) #Pass for contractor
    return render (request,'liffsubmitedwahbycontractor.html',{'wah_submited_detail':wahs_submited , "type":type})

def check_type_work(request,type_check):
    company_id = PersanalDetaillogin.objects.filter(line_id=request.session['user_id']).values_list('company_id')[0][0]
    request.session['company_id'] = company_id
    imcomming_work=Workfromgmail.objects.filter(date=today,notify_contractor__isnull=True).values('service_provider').annotate(dcount=Count('service_provider'))
    # print ('incomming is',imcomming_work)
    # print (type_check)
    today_check = datetime.datetime.now().strftime("%Y-%m-%d")
    tomorrow_check = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    if request.session['company_id'] == 3 :
        if type_check == 'main_check':
            worktype_detail=WahSubmitforcontractor.objects.filter(status='in planing').values('type_job').annotate(dcount=Count('type_job'))
        if type_check == 'today':
            worktype_detail=WahSubmitforcontractor.objects.filter(status='in planing',planned_date=today_check).values('type_job').annotate(dcount=Count('type_job'))
        if type_check == 'tomorrow':
            worktype_detail=WahSubmitforcontractor.objects.filter(status='in planing',planned_date=tomorrow_check).values('type_job').annotate(dcount=Count('type_job'))
        if type_check == 'incomming':
            # เป็นการ Query ข้อมูลในตารางเดียวกันและให้ระบบ sum ข้อมูลที่เหมือนกันในแต่ละเงื่อนไขได้เลย
            # worktype_detail=Workfromgmail.objects.filter(completed_work__isnull=True).values('service_provider').annotate(date_open=Count('date', filter=Q(date=today))).annotate(submit=Count('status_submit')).annotate(todaypending=Count('date', filter=Q(date=today,status_submit__isnull=True))).annotate(notify=Count('notify_contractor')).annotate(pending=Count('date', filter= ~Q(status_submit='yes')))
            worktype_detail=Workfromgmail.objects.filter(date=today).values('date').annotate(date_open=Count('date', filter=Q(date=today))).annotate(submit=Count('status_submit')).annotate(todaypending=Count('date', filter=Q(date=today,status_submit__isnull=True)))
            # print(worktype_detail)
        if type_check == 'submitted_check':
            data_1 = []
            data_2 = Workfromgmail.objects.filter(completed_work__isnull=True).values('initials_name').annotate(new_work_today=Count('date', filter=Q(date=today_check))).annotate(today_submit=Count('status_submit',filter=Q(status_submit='yes'))).annotate(todaypending=Count('date', filter=Q(status_submit__isnull=True)))
            data_3 = WahSubmitforcontractor.objects.filter(planned_date=tomorrow,status='in planning').values('initials_name').annotate(planned_today=Count('planned_date',))
            today_date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
            tomorrow_date = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%d-%m-%Y")
            # print ('data 2 is',data_2)
            # print ('data 3 is',data_3)
            # print ('today is',today_date)
            for name in Group.objects.values_list('initials_name'):
               data = {'name':(name[0])}
               if data['name'] == 'CBRE':
                   print ('Cancel CBRE')
               else :
                   data_1.append(data)
            for guest_new in data_2:
                for name in data_1:
                    if (name['name'] == guest_new['initials_name']):
                        name['new_work_today'] = guest_new['new_work_today']
                        name['today_submit'] = guest_new['today_submit']
                        name['todaypending'] = guest_new['todaypending']
            for guest_new in data_3 :
                for name in data_1:
                    if(name['name'] == guest_new['initials_name']):
                        name['planned_today'] = guest_new['planned_today']
            print (data_1)
            data_line=creatinglinemessages.summary_by_contractor(data_1,today_date,tomorrow_date)
            # print (json.dumps(data_line))
            return render (request,'showsubmitcheck.html',{"data":json.dumps(data_line),'today_date':today_date,'final':data_1}) 
    else:
        print(id) #Pass for contractor
    return render (request,'showcheckworkbytype.html',{'worktype_detail':worktype_detail,'type':type_check})
    
def checkworktype_by_contractor(request,type_job,type_check):
    print (type_check)
    if type_check == 'incomming':
        print ('type job is',type_job)
        details=Workfromgmail.objects.filter(completed_work__isnull=True).values('service_provider').annotate(date_open=Count('date', filter=Q(date=today))).annotate(submit=Count('status_submit')).annotate(todaypending=Count('date', filter=Q(date=today,status_submit__isnull=True))).annotate(notify=Count('notify_contractor')).annotate(pending=Count('date', filter= ~Q(status_submit='yes')))
        return render (request,'worktype_by_contractor.html',{'details':details ,'type_job':type_job ,'type':type_check})
        # return HttpResponse (200)
    else :
        details=WahSubmitforcontractor.objects.filter(type_job=type_job,status='in planing').values('company').annotate(dcount=Count('company'))
        return render (request,'worktype_by_contractor.html',{'details':details ,'type_job':type_job ,'type':type_check})

def detail_checkworktype_by_contractor(request,type_job,type_check):
    type = 'in planing'
    details=WahSubmitforcontractor.objects.filter(status='in planing',type_job=type_job) 
    data=creatinglinemessages.wahsubmit(details,type)
    return render (request,'worktype_by_contractor_detail.html',{'type':type_check,'details':details , 'type_job':type_job , "data":json.dumps(data)})
    
def checkworktoday(request):
    details=WahSubmitforcontractor.objects.filter(status='in planing',planned_date=today) 
    print(details)
    return HttpResponse (200)


def liffsubmiteddetail(request,company,type):
    count_wah_submit_detail=WahSubmitforcontractor.objects.filter(status=type,company=company)
    data=creatinglinemessages.wahsubmit(count_wah_submit_detail,type)
    return render (request,'liffsubmitedwahdetail.html',{"count_wah_submit_detail":count_wah_submit_detail , "type":type , "data":json.dumps(data)})

def sendlinebot(request,company,type,workorder):
    return render (request,'liffsubmitedwahdetail.html',{"count_wah_submit_detail":count_wah_submit_detail , "type":type })

def checkinwork (request):
    return render (request,'liffpage_checkin_login.html')

def checkoutwork (request):
    return render (request,'liffpage_checkout_login.html')

def worklistforcheckin(request):
    fls_line_id=PersanalDetaillogin.objects.filter(line_id=request.session['user_id']).values_list('id')[0][0]
    work_detail=WahSubmitforcontractor.objects.filter(Q(fls_id_1=fls_line_id) | Q(fls_id_2=fls_line_id) ,startwork__isnull=True)
    #work_detail=WahSubmitforcontractor.objects.filter(Q(fls_id_1=fls_line_id) | Q(fls_id_2=fls_line_id) )
    if work_detail.exists():
        return render (request,'liffpage_checkin_detail.html',{"work_detail":work_detail ,"type":'OK'})
    else:
        return render (request,'liffpage_checkin_detail.html',{"work_detail":work_detail ,"type":'NOK'})

def worklistforcheckout(request):
    fls_line_id=PersanalDetaillogin.objects.filter(line_id=request.session['user_id']).values_list('id')[0][0]
    work_detail=WahSubmitforcontractor.objects.filter(Q(fls_id_1=fls_line_id) | Q(fls_id_2=fls_line_id) ,status='onsite')
    
    #work_detail=WahSubmitforcontractor.objects.filter(Q(fls_id_1=fls_line_id) | Q(fls_id_2=fls_line_id) )
    if work_detail.exists():
        return render (request,'liffpage_checkout_detail.html',{"work_detail":work_detail ,"type":'OK'})
    else:
        return render (request,'liffpage_checkout_detail.html',{"work_detail":work_detail ,"type":'NOK'})

def liffpage_checkin_confirme(request,id):
    type='onsite'
    fls_line_id=PersanalDetaillogin.objects.filter(line_id=request.session['user_id']).values_list('id')[0][0]
    work_detail=WahSubmitforcontractor.objects.filter(Q(fls_id_1=fls_line_id) | Q(fls_id_2=fls_line_id),startwork__isnull=True,id=id)
    #work_detail=WahSubmitforcontractor.objects.filter(Q(fls_id_1=fls_line_id) | Q(fls_id_2=fls_line_id))
    return render (request,'liffpage_checkin_confirme.html',{"work_detail":work_detail })

def liffpage_checkout_confirme(request,id):
    fls_line_id=PersanalDetaillogin.objects.filter(line_id=request.session['user_id']).values_list('id')[0][0]
    work_detail=WahSubmitforcontractor.objects.filter(Q(fls_id_1=fls_line_id) | Q(fls_id_2=fls_line_id),completedwork__isnull=True,id=id)
    #work_detail=WahSubmitforcontractor.objects.filter(Q(fls_id_1=fls_line_id) | Q(fls_id_2=fls_line_id))
    return render (request,'liffpage_checkout_confirme.html',{"work_detail":work_detail })
    

def updatecheckindatabase(request,id,workorder):
    # print('Work ID is ',id)
    type='onsite'
    type_1='admin'
    type_2='fm'
    today_checkin = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
    fls_startwork=PersanalDetaillogin.objects.filter(line_id=request.session['user_id']).values_list('name')[0][0]
    updatedatawah=WahSubmitforcontractor.objects.filter(id=id).update(startwork=today_checkin,status='onsite',fls_startwork=fls_startwork)
    udpate_pending_to_status_work=Workfromgmail.objects.filter(workorder=workorder).update(completed_work='onsite')
    work_detail_to_line=WahSubmitforcontractor.objects.filter(id=id)
    global data_2
    global data_3
    data_1=creatinglinemessages.linedetailcheck(work_detail_to_line,type)
    data_2=creatinglinemessages.linedetailcheck(work_detail_to_line,type_1)
    data_3=creatinglinemessages.checkin_notify(work_detail_to_line)
    for I in work_detail_to_line :
        fm_name = I.fm
        request.session['fm_name'] = fm_name
    admin_data=PersanalDetaillogin.objects.filter(user_type='admin')
    token=PersanalDetaillogin.objects.filter(line_id=request.session['user_id']).values_list('group_id')[0][0]
    for I in admin_data :
        data_admin=I.line_id
        send_line_to_cbre=PushMessage(data_2,data_admin)
        # print (send_line_to_cbre)
    
    fm_data=PersanalDetaillogin.objects.filter(name=request.session['fm_name']).values_list('line_id')[0][0]
    # print (fm_data)
    send_line_to_fm=PushMessage(data_2,fm_data)
    send_notify(data_3,token)
    return render(request,'completedcheckin.html',{"data":json.dumps(data_1)})

def updatecheckoutdatabase(request,id,workorder):
    print('Work ID is ',id)
    type='completed'
    type_1='admin'
    type_1='admin2'
    today_checkout = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
    fls_startwork=PersanalDetaillogin.objects.filter(line_id=request.session['user_id']).values_list('name')[0][0]
    updatedatawah=WahSubmitforcontractor.objects.filter(id=id).update(completedwork=today_checkout,status='completed',fls_completedwork=fls_startwork)
    udpate_pending_to_status_work=Workfromgmail.objects.filter(workorder=workorder).update(completed_work='completed')
    work_detail_to_line=WahSubmitforcontractor.objects.filter(id=id)
    global data_2
    global data_3
    data_1=creatinglinemessages.linedetailcheck(work_detail_to_line,type)
    data_2=creatinglinemessages.linedetailcheck(work_detail_to_line,type_1)
    data_3=creatinglinemessages.checkout_notify(work_detail_to_line)
    admin_data=PersanalDetaillogin.objects.filter(user_type='admin')
    token=PersanalDetaillogin.objects.filter(line_id=request.session['user_id']).values_list('group_id')[0][0]
    for I in admin_data :
        data_admin=I.line_id
        send_line_to_cbre=PushMessage(data_2,data_admin)
        # print (send_line_to_cbre)
    
    fm_data=PersanalDetaillogin.objects.filter(name=request.session['fm_name']).values_list('line_id')[0][0]
    # print (fm_data)
    send_line_to_fm=PushMessage(data_2,fm_data)
    send_notify(data_3,token)
    return render(request,'completedcheckout.html',{"data":json.dumps(data_1)})

def sendlinetocbreteam(request):
    admin_data=PersanalDetaillogin.objects.filter(user_type='admin')
    token=PersanalDetaillogin.objects.filter(line_id=request.session['user_id']).values_list('group_id')[0][0]
    for I in admin_data :
        data_admin=I.line_id
        send_line_to_cbre=PushMessage(data_2,data_admin)
        # print (send_line_to_cbre)
    
    fm_data=PersanalDetaillogin.objects.filter(name=request.session['fm_name']).values_list('line_id')[0][0]
    # print (fm_data)
    send_line_to_fm=PushMessage(data_2,fm_data)
        
    
    send_notify(data_3,token)
    return HttpResponse(200)











    
