# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path , include
from app import views
from django.contrib import admin
admin.site.site_header = 'EXXON-CBRE TEAM THAILAND'
admin.site.site_title = 'EXXON-CBRE TEAM THAILAND'

urlpatterns = [
    re_path(r'^.*\.html', views.pages, name='pages'),
    path('', views.index, name='home'),
    path('report/contractor',views.contractorreport,name='contractor'),
    path('addrequest/<int:workorder>',views.addWAH,name='add_wah'), # รับค่าจาก contractor.html เพื่อส่งไป Submit WAH
    path('insertrequest/',views.addWAHtoDB,name='add_wah_to_db'),
    path('editwah<int:id>/',views.editwah,name='editwah'),
    path('updatewah<int:id>/',views.updatewah,name='updatewah'),
    path('seedetail<int:id>/',views.seedetail,name='seedetail'),
    path('linebot/', include('linebot.urls')),
    path('liffpage/',views.liffpage,name='liffpage'),
    path('check_userid/',views.check_userid,name='check_userid'), # รับค่าจาก javascript
    path('wahwork/',views.wahwork,name='wahwork'),
    path('liffsubmitedwahbycontractor<int:id> + <str:type>',views.liffsubmitedwahbycontractor,name='liffsubmitedwahbycontractor'),
    path('check_type_work<str:type_check>',views.check_type_work,name='check_type_work'),
    path('checkworktype_by_contractor<str:type_job>+<str:type_check>/',views.checkworktype_by_contractor,name='checkworktype_by_contractor'),
    path('checkworktoday/',views.checkworktoday,name='checkworktoday'),
    path('detail_checkworktype_by_contractor<str:type_job>+<str:type_check>/',views.detail_checkworktype_by_contractor,name='detail_checkworktype_by_contractor'),
    path('liffsubmiteddetail<str:company>+<str:type>/',views.liffsubmiteddetail,name='liffsubmiteddetail'),
    path('sendlinebot<str:company>+<str:type>+<str:workorder>/',views.sendlinebot,name='sendlinebot'),
    path('checkinwork/',views.checkinwork,name='checkinwork'),
    path('worklistforcheckin/',views.worklistforcheckin,name='worklistforcheckin'),
    path('worklistforcheckout/',views.worklistforcheckout,name='worklistforcheckout'),
    
    path('liffpage_checkin_confirme<int:id>/',views.liffpage_checkin_confirme,name='liffpage_checkin_confirme'),
    path('liffpage_checkout_confirme<int:id>/',views.liffpage_checkout_confirme,name='liffpage_checkout_confirme'),
    
    path('updatecheckindatabase<int:id>/',views.updatecheckindatabase,name="updatecheckindatabase"),
    path('updatecheckoutdatabase<int:id>/',views.updatecheckoutdatabase,name="updatecheckoutdatabase"),
    path('sendlinetocbreteam/',views.sendlinetocbreteam,name='sendlinetocbreteam'),
    path('checkoutwork/',views.checkoutwork,name='checkoutwork'),


    
    ]
