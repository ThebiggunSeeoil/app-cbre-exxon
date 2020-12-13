# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from app.models import SiteList,WorkPending,PersanalDetaillogin,WahSubmitforcontractor
#from app.resources import WorkPending_resource

# Register your models here.

@admin.register(SiteList)
class SiteListAdmin(ImportExportModelAdmin):
    list_display = ("customer", "pbl", "internal_order", "eng_name","name","regiter_name","area","tm","am","moso","moso_type","cat_type")
    #list_editable=['eng_name','pbl'] # ทำให้ Edit ข้อมูลต่างๆได้ 
    list_per_page=30 #กำหนดให้แสดงรายการสินค้่าใน Admin
    pass

@admin.register(WorkPending)
class WorkPendingAdmin(ImportExportModelAdmin):
    list_display = ("workorder","priority","status", "opended", "startwork", "completedwork","caller","building_location","service_provider","equipment_code","failure_code","problem_code","work_type","problum")
    #list_editable=['eng_name','pbl'] # ทำให้ Edit ข้อมูลต่างๆได้ 
    list_per_page=30 #กำหนดให้แสดงรายการสินค้่าใน Admin
    #resource_class = WorkPending_resource
    pass

@admin.register(WahSubmitforcontractor)
class WorkPendingAdmin(ImportExportModelAdmin):
    list_display = ("workorder","company","opended", "status", "startwork", "completedwork","caller","wah_status","timestramp","planned_date","job_description","fls_mame_1","fls_phone","management","remark","type_job","jla_ra","any_ssw","physical","fm")
    #list_editable=['eng_name','pbl'] # ทำให้ Edit ข้อมูลต่างๆได้ 
    list_per_page=30 #กำหนดให้แสดงรายการสินค้่าใน Admin
    #resource_class = WorkPending_resource
    pass

@admin.register(PersanalDetaillogin)
class PersanalDetailloginAdmin(ImportExportModelAdmin):
    list_display = ("name","position", "company", "company_id", "key_login","line_id","group_id","member_status","timestramp")
    #list_editable=['eng_name','pbl'] # ทำให้ Edit ข้อมูลต่างๆได้ 
    list_per_page=30 #กำหนดให้แสดงรายการสินค้่าใน Admin
    #resource_class = WorkPending_resource
    pass
    
    
#admin.site.register(SiteList)
#admin.site.register(WorkPending)