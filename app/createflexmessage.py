import datetime
class creatinglinemessages ():
    def summary_by_contractor(data,date_today,planned_date):
        Main_data = {"type": "flex",
                            "altText": "Flex Message",
                            "contents":
                                {
                                    "type": "carousel",
                                    "contents":[{
                            "type": "bubble",
                            "size": "giga",
                            "hero": {
                                "type": "image",
                                "url": "https://seeoil-web.com/cbre/Picture/CBRE-Logo.jpg",
                                "align": "center",
                                "gravity": "bottom",
                                "size": "full",
                                "aspectRatio": "20:7",
                                "aspectMode": "cover",
                                "action": {
                                "type": "uri",
                                "label": "Line",
                                "uri": "https://linecorp.com/"
                                },
                                "position": "relative"
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "Summary Report All Contractor",
                                    "weight": "bold",
                                    "size": "sm",
                                    "color": "#225508FF",
                                    "align": "center",
                                    "contents": []
                                },
                                {
                                    "type": "text",
                                    "text": str(date_today),
                                    "weight": "bold",
                                    "size": "sm",
                                    "color": "#225508FF",
                                    "align": "center",
                                    "contents": []
                                },
                                {
                                    "type": "text",
                                    "text": "Planned on " + planned_date,
                                    "weight": "bold",
                                    "size": "sm",
                                    "color": "#225508FF",
                                    "align": "center",
                                    "contents": []
                                },
                                {
                                    "type": "separator",
                                    "margin": "sm",
                                    "color": "#165C3CFF"
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "spacing": "sm",
                                    "margin": "xs",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": "SP",
                                        "weight": "bold",
                                        "size": "xs",
                                        "contents": []
                                    },
                                    {
                                        "type": "text",
                                        "text": "WR",
                                        "weight": "bold",
                                        "size": "xs",
                                        "align": "center",
                                        "position": "relative",
                                        "contents": []
                                    },
                                    {
                                        "type": "text",
                                        "text": "SB",
                                        "weight": "bold",
                                        "size": "xs",
                                        "align": "center",
                                        "contents": []
                                    },
                                    {
                                        "type": "text",
                                        "text": "PA",
                                        "weight": "bold",
                                        "size": "xs",
                                        "align": "center",
                                        "contents": []
                                    },
                                    {
                                        "type": "text",
                                        "text": "TD-PD",
                                        "weight": "bold",
                                        "size": "xs",
                                        "align": "center",
                                        "contents": []
                                    }
                                    ]
                                },
                                
                                
                                {
                                    "type": "separator",
                                    "margin": "md",
                                    "color": "#165C3CFF"
                                },
                                {
                                    "type": "text",
                                    "text": "SP : Providor Name , WR : Work received today",
                                    "size": "xxs",
                                    "align": "center",
                                    "margin": "sm",
                                    "contents": []
                                },
                                {
                                    "type": "text",
                                    "text": "SB : Submitted Work , PA : Work All Pending",
                                    "size": "xxs",
                                    "align": "center",
                                    "margin": "xs",
                                    "contents": []
                                },
                                {
                                    "type": "text",
                                    "text": "TD-PD : Work Planned on 28-12-2020",
                                    "size": "xxs",
                                    "align": "center",
                                    "margin": "xs",
                                    "contents": []
                                }
                                ]
                            }
                            }

                                        ]

                                }}

        for I in data :
            name = I['name']
            if 'new_work_today' not in I :
                new_work_today = '0'
            else :
                new_work_today = I['new_work_today']
            if 'today_submit' not in I :
                today_submit = '0'
            else :
                today_submit = I['today_submit']
            if 'todaypending' not in I :
                todaypending = '0'
            else :
                todaypending = I['todaypending']
            if 'planned_today' not in I :
                planned_today = '0'
            else :
                planned_today = I['planned_today']

            # print (name)
            # print (new_work_today)
            # print (today_submit)
            # print (todaypending)
            # print (planned_today)
            
            content_data = {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                        {
                                            "type": "text",
                                            "text": name,
                                            "size": "xs",
                                            "align": "start",
                                            "contents": []
                                        },
                                        {
                                            "type": "text",
                                            "text": str(new_work_today),
                                            "size": "xs",
                                            "align": "center",
                                            "position": "relative",
                                            "contents": []
                                        },
                                        {
                                            "type": "text",
                                            "text": str(today_submit),
                                            "size": "xs",
                                            "align": "center",
                                            "contents": []
                                        },
                                        {
                                            "type": "text",
                                            "text": str(todaypending),
                                            "size": "xs",
                                            "align": "center",
                                            "contents": []
                                        },
                                        {
                                            "type": "text",
                                            "text": str(planned_today),
                                            "size": "xs",
                                            "align": "center",
                                            "contents": []
                                        }
                                        ]
                                    }
            Main_data['contents']['contents'][0]['body']['contents'].insert(-4,content_data)
        return Main_data   
    def submit_notify(request):
        
        planned_date=request.POST.get('planned_date')
        caller=request.POST.get('caller')
        job_description=request.POST.get('job_description')
        workorder=request.POST.get('workorder')
        company=request.POST.get('company') 
        fls_mame_1=request.POST.get('fls_mame_1')
        fls_mame_2=request.POST.get('fls_mame_2')
        
        
        data = {'\n'+'SUBMIT WAH TYPE'+'\n'
                        +'Contractor : ' + company + '\n' 
                        + 'SiteName : ' + caller + '\n'
                        + 'WorkOrder '+ workorder + '\n'
                        + 'WorkDetail : ' + job_description + '\n'
                        + 'Planned : ' + planned_date + '\n'
                        + 'fls_mame_1 : ' + fls_mame_1 + '\n'
                        + 'fls_mame_2 : ' + fls_mame_2 }
        return data
    def updatedsubmit_notify(request):
        
        planned_date=request.POST.get('planned_date')
        caller=request.POST.get('caller')
        job_description=request.POST.get('job_description')
        workorder=request.POST.get('workorder')
        company=request.POST.get('company') 
        fls_mame_1=request.POST.get('fls_mame')
        
        
        
        data = {'\n'+'UPDATED DATE WAH'+'\n'
                        +'Contractor : ' + company + '\n' 
                        + 'SiteName : ' + caller + '\n'
                        + 'WorkOrder '+ workorder + '\n'
                        + 'WorkDetail : ' + job_description + '\n'
                        + 'Planned : ' + planned_date + '\n'
                        + 'fls_mame : ' + fls_mame_1 + '\n'
                        }
        return data
    def checkout_notify(data):
        for I in data :
                # Title = (I['Title'])
                print (I)
                workorder = I.workorder
                company= I.company
                opended = I.opended
                status = I.status
                startwork = I.startwork
                completedwork = I.completedwork
                caller = I.caller
                wah_status = I.wah_status
                timestramp = I.timestramp
                planned_date = I.planned_date
                job_description = I.job_description
                fls_mame = I.fls_mame_1
                fls_startwork = I.fls_startwork
                fls_completedwork = I.fls_completedwork
                fls_phone = I.fls_phone
                management = I.management
                remark = I.remark
                type_job = I.type_job
                jla_ra = I.jla_ra
                any_ssw = I.any_ssw
                physical = I.physical
                fm = I.fm
                startwork=I.startwork

                print (workorder)
                print (company)
                print (opended)
                print (status)
                print (startwork)
                print (completedwork)
                print (caller)
                print (wah_status)
                print (timestramp)
                print (planned_date)
                print (job_description)
                print (fls_mame)
                print (fls_phone)
                print (management)
                print (remark)
                print (type_job)
                print (jla_ra)
                print (any_ssw)
                print (physical)
                print (fm)
        data = {'\n'+'CHECKOUT WAH TYPE'+'\n'
                        +'Contractor : ' + company + '\n' 
                        + 'SiteName : ' + caller + '\n'
                        + 'WorkOrder '+ workorder + '\n'
                        + 'CheckIn Name : ' + fls_startwork + '\n'
                        + 'CheckOut Name : ' + fls_completedwork + '\n'
                        + 'CheckIn Time : ' + str(startwork.strftime("%d-%m-%Y %H:%M")) + '\n'
                        + 'CheckOut Time : ' + str(completedwork.strftime("%d-%m-%Y %H:%M"))}
        return data
    def checkin_notify(data):
        for I in data :
                # Title = (I['Title'])
                print (I)
                workorder = I.workorder
                company= I.company
                opended = I.opended
                status = I.status
                startwork = I.startwork
                completedwork = I.completedwork
                caller = I.caller
                wah_status = I.wah_status
                timestramp = I.timestramp
                planned_date = I.planned_date
                job_description = I.job_description
                fls_mame = I.fls_mame_1
                fls_startwork = I.fls_startwork
                fls_phone = I.fls_phone
                management = I.management
                remark = I.remark
                type_job = I.type_job
                jla_ra = I.jla_ra
                any_ssw = I.any_ssw
                physical = I.physical
                fm = I.fm
                startwork=I.startwork

                print (workorder)
                print (company)
                print (opended)
                print (status)
                print (startwork)
                print (completedwork)
                print (caller)
                print (wah_status)
                print (timestramp)
                print (planned_date)
                print (job_description)
                print (fls_mame)
                print (fls_phone)
                print (management)
                print (remark)
                print (type_job)
                print (jla_ra)
                print (any_ssw)
                print (physical)
                print (fm)
        data = {'\n'+'CHECKIN WAH TYPE'+'\n'
                        +'Contractor : ' + company + '\n' 
                        + 'SiteName : ' + caller + '\n'
                        + 'WorkOrder '+ workorder + '\n'
                        + 'CheckIn Name : ' + fls_startwork + '\n'
                        + 'CheckIn Time : ' + str(startwork.strftime("%d-%m-%Y %H:%M"))}
        return data
    def wahsubmit (count_wah_submit_detail,type):
        print ('insile createline')
        if type == 'in planing' :
            data = count_wah_submit_detail
            arry_contants = []
            data_wah = {"type": "flex",
                                            "altText": "Flex Message",
                                            "contents":     
                                            {
                                        "type": "carousel",
                                        "contents": 
                                            
                                            arry_contants
                                        
                                        }       }
            for I in data :
                # Title = (I['Title'])
                print (I)
                workorder = I.workorder
                company= I.company
                opended = I.opended
                status = I.status
                startwork = I.startwork
                completedwork = I.completedwork
                caller = I.caller
                wah_status = I.wah_status
                timestramp = I.timestramp
                planned_date = I.planned_date.strftime("%d-%m-%Y %H:%M")
                job_description = I.job_description
                fls_mame = I.fls_mame_1
                fls_phone = I.fls_phone
                management = I.management
                remark = I.remark
                type_job = I.type_job
                jla_ra = I.jla_ra
                any_ssw = I.any_ssw
                physical = I.physical
                fm = I.fm

                print (workorder)
                print (company)
                print (opended)
                print (status)
                print (startwork)
                print (completedwork)
                print (caller)
                print (wah_status)
                print (timestramp)
                print (planned_date)
                print (job_description)
                print (fls_mame)
                print (fls_phone)
                print (management)
                print (remark)
                print (type_job)
                print (jla_ra)
                print (any_ssw)
                print (physical)
                print (fm)

                contents_submit_wah = {
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://seeoil-web.com/cbre/Picture/CBRE-Logo.jpg",
                    "align": "center",
                    "gravity": "bottom",
                    "size": "full",
                    "aspectRatio": "20:7",
                    "aspectMode": "cover",
                    "action": {
                    "type": "uri",
                    "label": "Line",
                    "uri": "https://linecorp.com/"
                    },
                    "position": "relative"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "WAH - DETAIL OF WORK",
                        "weight": "bold",
                        "size": "xl",
                        "color": "#225508FF",
                        "align": "center",
                        "contents": []
                    },
                    {
                        "type": "separator",
                        "margin": "xs",
                        "color": "#E42424FF"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "none",
                        "margin": "xs",
                        "contents": [
                        {
                            "type": "text",
                            "text": "Contractor :",
                            "weight": "bold",
                            "size": "xs",
                            "color": "#045221FF",
                            "margin": "sm",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": company,
                            "size": "xxs",
                            "color": "#045221FF",
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "none",
                        "margin": "xs",
                        "contents": [
                        {
                            "type": "text",
                            "text": "PlanedDate :",
                            "weight": "bold",
                            "size": "xs",
                            "color": "#045221FF",
                            "margin": "sm",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": str(planned_date),
                            "size": "xxs",
                            "color": "#045221FF",
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "none",
                        "margin": "xs",
                        "contents": [
                        {
                            "type": "text",
                            "text": "WorkOrder :",
                            "weight": "bold",
                            "size": "xs",
                            "color": "#045221FF",
                            "margin": "sm",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": workorder,
                            "size": "xxs",
                            "color": "#045221FF",
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "text",
                            "text": "SiteName :",
                            "weight": "bold",
                            "size": "xs",
                            "color": "#045221FF",
                            "margin": "sm",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": caller,
                            "size": "xxs",
                            "color": "#045221FF",
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "none",
                        "margin": "xs",
                        "contents": [
                        {
                            "type": "text",
                            "text": "JobDescriptions :",
                            "weight": "bold",
                            "size": "xs",
                            "color": "#045221FF",
                            "margin": "sm",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": job_description,
                            "size": "xxs",
                            "color": "#045221FF",
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "none",
                        "margin": "xs",
                        "contents": [
                        {
                            "type": "text",
                            "text": "FlsName :",
                            "weight": "bold",
                            "size": "xs",
                            "color": "#045221FF",
                            "margin": "sm",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": fls_mame,
                            "size": "xxs",
                            "color": "#045221FF",
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "none",
                        "margin": "xs",
                        "contents": [
                        {
                            "type": "text",
                            "text": "MobilePhoneFLS :",
                            "weight": "bold",
                            "size": "xs",
                            "color": "#045221FF",
                            "margin": "sm",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": fls_phone,
                            "size": "xxs",
                            "color": "#045221FF",
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "none",
                        "margin": "xs",
                        "contents": [
                        {
                            "type": "text",
                            "text": "MangementName :",
                            "weight": "bold",
                            "size": "xs",
                            "color": "#045221FF",
                            "margin": "sm",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": management,
                            "size": "xxs",
                            "color": "#045221FF",
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "none",
                        "margin": "xs",
                        "contents": [
                        {
                            "type": "text",
                            "text": "TypeOfJob :",
                            "weight": "bold",
                            "size": "xs",
                            "color": "#045221FF",
                            "margin": "sm",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": type_job,
                            "size": "xxs",
                            "color": "#045221FF",
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "none",
                        "margin": "xs",
                        "contents": [
                        {
                            "type": "text",
                            "text": "JLA/RAReviewed :",
                            "weight": "bold",
                            "size": "xs",
                            "color": "#045221FF",
                            "margin": "sm",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": jla_ra,
                            "size": "xxs",
                            "color": "#045221FF",
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "none",
                        "margin": "xs",
                        "contents": [
                        {
                            "type": "text",
                            "text": "WorkerInvolved ? : ",
                            "weight": "bold",
                            "size": "xs",
                            "color": "#045221FF",
                            "margin": "sm",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": any_ssw,
                            "size": "xxs",
                            "color": "#045221FF",
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "none",
                        "margin": "xs",
                        "contents": [
                        {
                            "type": "text",
                            "text": "Observation ? :",
                            "weight": "bold",
                            "size": "xs",
                            "color": "#045221FF",
                            "margin": "sm",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": physical,
                            "size": "xxs",
                            "color": "#045221FF",
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "none",
                        "margin": "xs",
                        "contents": [
                        {
                            "type": "text",
                            "text": "CBRE FM : ",
                            "weight": "bold",
                            "size": "xs",
                            "color": "#045221FF",
                            "margin": "sm",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": fm,
                            "size": "xxs",
                            "color": "#045221FF",
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "none",
                        "margin": "xs",
                        "contents": [
                        {
                            "type": "text",
                            "text": "Remarks :",
                            "weight": "bold",
                            "size": "xs",
                            "color": "#045221FF",
                            "margin": "sm",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": remark,
                            "size": "xxs",
                            "color": "#045221FF",
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    }
                    ]
                }
                }
                arry_contants.append(contents_submit_wah)
            return data_wah
        if type == 'onsite' :
            data = count_wah_submit_detail
            arry_contants = []
            data_wah = {"type": "flex",
                                            "altText": "Flex Message",
                                            "contents":     
                                            {
                                        "type": "carousel",
                                        "contents": 
                                            
                                            arry_contants
                                        
                                        }       }
            for I in data :
                # Title = (I['Title'])
                print (I)
                workorder = I.workorder
                company= I.company
                opended = I.opended
                status = I.status
                startwork = I.startwork
                completedwork = I.completedwork
                caller = I.caller
                wah_status = I.wah_status
                timestramp = I.timestramp
                planned_date = I.planned_date
                job_description = I.job_description
                fls_mame = I.fls_mame_1
                fls_phone = I.fls_phone
                management = I.management
                remark = I.remark
                type_job = I.type_job
                jla_ra = I.jla_ra
                any_ssw = I.any_ssw
                physical = I.physical
                fm = I.fm

                print (workorder)
                print (company)
                print (opended)
                print (status)
                print (startwork)
                print (completedwork)
                print (caller)
                print (wah_status)
                print (timestramp)
                print (planned_date)
                print (job_description)
                print (fls_mame)
                print (fls_phone)
                print (management)
                print (remark)
                print (type_job)
                print (jla_ra)
                print (any_ssw)
                print (physical)
                print (fm)

                contents_submit_wah = {
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://seeoil-web.com/cbre/Picture/CBRE-Logo.jpg",
                    "align": "center",
                    "gravity": "bottom",
                    "size": "full",
                    "aspectRatio": "20:7",
                    "aspectMode": "cover",
                    "action": {
                    "type": "uri",
                    "label": "Line",
                    "uri": "https://linecorp.com/"
                    },
                    "position": "relative"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "WAH - DETAIL OF WORK",
                        "weight": "bold",
                        "size": "xl",
                        "color": "#225508FF",
                        "align": "center",
                        "contents": []
                    },
                    {
                        "type": "separator",
                        "margin": "xs",
                        "color": "#E42424FF"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "none",
                        "margin": "xs",
                        "contents": [
                        {
                            "type": "text",
                            "text": "Contractor :",
                            "weight": "bold",
                            "size": "xs",
                            "color": "#045221FF",
                            "margin": "sm",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": company,
                            "size": "xxs",
                            "color": "#045221FF",
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "none",
                        "margin": "xs",
                        "contents": [
                        {
                            "type": "text",
                            "text": "PlanedDate :",
                            "weight": "bold",
                            "size": "xs",
                            "color": "#045221FF",
                            "margin": "sm",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": str(planned_date),
                            "size": "xxs",
                            "color": "#045221FF",
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "none",
                        "margin": "xs",
                        "contents": [
                        {
                            "type": "text",
                            "text": "WorkOrder :",
                            "weight": "bold",
                            "size": "xs",
                            "color": "#045221FF",
                            "margin": "sm",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": workorder,
                            "size": "xxs",
                            "color": "#045221FF",
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "text",
                            "text": "SiteName :",
                            "weight": "bold",
                            "size": "xs",
                            "color": "#045221FF",
                            "margin": "sm",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": caller,
                            "size": "xxs",
                            "color": "#045221FF",
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "none",
                        "margin": "xs",
                        "contents": [
                        {
                            "type": "text",
                            "text": "JobDescriptions :",
                            "weight": "bold",
                            "size": "xs",
                            "color": "#045221FF",
                            "margin": "sm",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": job_description,
                            "size": "xxs",
                            "color": "#045221FF",
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "none",
                        "margin": "xs",
                        "contents": [
                        {
                            "type": "text",
                            "text": "FlsName :",
                            "weight": "bold",
                            "size": "xs",
                            "color": "#045221FF",
                            "margin": "sm",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": fls_mame,
                            "size": "xxs",
                            "color": "#045221FF",
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "none",
                        "margin": "xs",
                        "contents": [
                        {
                            "type": "text",
                            "text": "MobilePhoneFLS :",
                            "weight": "bold",
                            "size": "xs",
                            "color": "#045221FF",
                            "margin": "sm",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": fls_phone,
                            "size": "xxs",
                            "color": "#045221FF",
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "none",
                        "margin": "xs",
                        "contents": [
                        {
                            "type": "text",
                            "text": "MangementName :",
                            "weight": "bold",
                            "size": "xs",
                            "color": "#045221FF",
                            "margin": "sm",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": management,
                            "size": "xxs",
                            "color": "#045221FF",
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "none",
                        "margin": "xs",
                        "contents": [
                        {
                            "type": "text",
                            "text": "TypeOfJob :",
                            "weight": "bold",
                            "size": "xs",
                            "color": "#045221FF",
                            "margin": "sm",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": type_job,
                            "size": "xxs",
                            "color": "#045221FF",
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "none",
                        "margin": "xs",
                        "contents": [
                        {
                            "type": "text",
                            "text": "JLA/RAReviewed :",
                            "weight": "bold",
                            "size": "xs",
                            "color": "#045221FF",
                            "margin": "sm",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": jla_ra,
                            "size": "xxs",
                            "color": "#045221FF",
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "none",
                        "margin": "xs",
                        "contents": [
                        {
                            "type": "text",
                            "text": "WorkerInvolved ? : ",
                            "weight": "bold",
                            "size": "xs",
                            "color": "#045221FF",
                            "margin": "sm",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": any_ssw,
                            "size": "xxs",
                            "color": "#045221FF",
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "none",
                        "margin": "xs",
                        "contents": [
                        {
                            "type": "text",
                            "text": "Observation ? :",
                            "weight": "bold",
                            "size": "xs",
                            "color": "#045221FF",
                            "margin": "sm",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": physical,
                            "size": "xxs",
                            "color": "#045221FF",
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "none",
                        "margin": "xs",
                        "contents": [
                        {
                            "type": "text",
                            "text": "CBRE FM : ",
                            "weight": "bold",
                            "size": "xs",
                            "color": "#045221FF",
                            "margin": "sm",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": fm,
                            "size": "xxs",
                            "color": "#045221FF",
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "none",
                        "margin": "xs",
                        "contents": [
                        {
                            "type": "text",
                            "text": "Remarks :",
                            "weight": "bold",
                            "size": "xs",
                            "color": "#045221FF",
                            "margin": "sm",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": remark,
                            "size": "xxs",
                            "color": "#045221FF",
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "none",
                        "margin": "xs",
                        "contents": [
                        {
                            "type": "text",
                            "text": "CheckIn Time :",
                            "weight": "bold",
                            "size": "xs",
                            "color": "#045221FF",
                            "margin": "sm",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": str(startwork),
                            "size": "xxs",
                            "color": "#045221FF",
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    }
                    ]
                }
                }
                arry_contants.append(contents_submit_wah)
            return data_wah
    def linedetailcheck (detail_checkin,type):
        if type == 'completed' :
            
            for I in detail_checkin :
                # Title = (I['Title'])
                print (I)
                workorder = I.workorder
                company= I.company
                opended = I.opended
                status = I.status
                startwork = I.startwork
                completedwork = I.completedwork.strftime("%d-%m-%Y %H:%M")
                caller = I.caller
                wah_status = I.wah_status
                timestramp = I.timestramp
                planned_date = I.planned_date.strftime("%d-%m-%Y %H:%M")
                job_description = I.job_description
                fls_mame = I.fls_mame_1
                fls_startwork = I.fls_startwork
                fls_phone = I.fls_phone
                management = I.management
                remark = I.remark
                type_job = I.type_job
                jla_ra = I.jla_ra
                any_ssw = I.any_ssw
                physical = I.physical
                fm = I.fm
                startwork=I.startwork.strftime("%d-%m-%Y %H:%M")

                print (workorder)
                print (company)
                print (opended)
                print (status)
                print (startwork)
                print (completedwork)
                print (caller)
                print (wah_status)
                print (timestramp)
                print (planned_date)
                print (job_description)
                print (fls_mame)
                print (fls_phone)
                print (management)
                print (remark)
                print (type_job)
                print (jla_ra)
                print (any_ssw)
                print (physical)
                print (fm)
            
                data = {
                                                    "type": "flex",
                                                    "altText": "Flex Message",
                                                    "contents": {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "url": "https://seeoil-web.com/cbre/Picture/CBRE-Logo.jpg",
                        "align": "center",
                        "gravity": "bottom",
                        "size": "full",
                        "aspectRatio": "20:7",
                        "aspectMode": "cover",
                        "action": {
                        "type": "uri",
                        "label": "Line",
                        "uri": "https://linecorp.com/"
                        },
                        "position": "relative"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "รายละเอียดของงาน",
                            "weight": "bold",
                            "size": "xl",
                            "color": "#225508FF",
                            "align": "center",
                            "contents": []
                        },
                        {
                            "type": "separator",
                            "margin": "xs",
                            "color": "#E42424FF"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "spacing": "none",
                            "margin": "xs",
                            "contents": [
                            {
                                "type": "text",
                                "text": "ผู้รับเหมา :",
                                "weight": "bold",
                                "size": "xs",
                                "color": "#045221FF",
                                "margin": "sm",
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": company,
                                "size": "xxs",
                                "color": "#045221FF",
                                "align": "start",
                                "margin": "none",
                                "wrap": True,
                                "contents": []
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "spacing": "none",
                            "margin": "xs",
                            "contents": [
                            {
                                "type": "text",
                                "text": "เลขแจ้งซ่อม :",
                                "weight": "bold",
                                "size": "xs",
                                "color": "#045221FF",
                                "margin": "sm",
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": workorder,
                                "size": "xxs",
                                "color": "#045221FF",
                                "align": "start",
                                "margin": "none",
                                "wrap": True,
                                "contents": []
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": "สถานี :",
                                "weight": "bold",
                                "size": "xs",
                                "color": "#045221FF",
                                "margin": "sm",
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": caller,
                                "size": "xxs",
                                "color": "#045221FF",
                                "align": "start",
                                "margin": "none",
                                "wrap": True,
                                "contents": []
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "spacing": "none",
                            "margin": "xs",
                            "contents": [
                            {
                                "type": "text",
                                "text": "รายละเอียดงาน :",
                                "weight": "bold",
                                "size": "xs",
                                "color": "#045221FF",
                                "margin": "sm",
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": job_description,
                                "size": "xxs",
                                "color": "#045221FF",
                                "align": "start",
                                "margin": "none",
                                "wrap": True,
                                "contents": []
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "spacing": "none",
                            "margin": "xs",
                            "contents": [
                            {
                                "type": "text",
                                "text": "ช่างที่เข้าทำงาน :",
                                "weight": "bold",
                                "size": "xs",
                                "color": "#045221FF",
                                "margin": "sm",
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": fls_startwork,
                                "size": "xxs",
                                "color": "#045221FF",
                                "align": "start",
                                "margin": "none",
                                "wrap": True,
                                "contents": []
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "spacing": "none",
                            "margin": "xs",
                            "contents": [
                            {
                                "type": "text",
                                "text": "เบอร์โทรช่าง :",
                                "weight": "bold",
                                "size": "xs",
                                "color": "#045221FF",
                                "margin": "sm",
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": fls_phone,
                                "size": "xxs",
                                "color": "#045221FF",
                                "align": "start",
                                "margin": "none",
                                "wrap": True,
                                "contents": []
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "spacing": "none",
                            "margin": "xs",
                            "contents": [
                            {
                                "type": "text",
                                "text": "CBRE FM : ",
                                "weight": "bold",
                                "size": "xs",
                                "color": "#045221FF",
                                "margin": "sm",
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": fm,
                                "size": "xxs",
                                "color": "#045221FF",
                                "align": "start",
                                "margin": "none",
                                "wrap": True,
                                "contents": []
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "spacing": "none",
                            "margin": "xs",
                            "contents": [
                            {
                                "type": "text",
                                "text": "วันที่เข้าจบงาน :",
                                "weight": "bold",
                                "size": "xs",
                                "color": "#045221FF",
                                "margin": "sm",
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": str(startwork),
                                "size": "xxs",
                                "color": "#045221FF",
                                "align": "start",
                                "margin": "none",
                                "wrap": True,
                                "contents": []
                            }
                            ]
                        }
                        ]
                    }
                    }
                                                                    }

                return data
        if type == 'onsite' :
            
            for I in detail_checkin :
                # Title = (I['Title'])
                print (I)
                workorder = I.workorder
                company= I.company
                opended = I.opended
                status = I.status
                startwork = I.startwork.strftime("%d-%m-%Y %H:%M")
                completedwork = I.completedwork
                caller = I.caller
                wah_status = I.wah_status
                timestramp = I.timestramp
                planned_date = I.planned_date.strftime("%d-%m-%Y %H:%M")
                job_description = I.job_description
                fls_mame = I.fls_mame_1
                fls_startwork = I.fls_startwork
                fls_phone = I.fls_phone
                management = I.management
                remark = I.remark
                type_job = I.type_job
                jla_ra = I.jla_ra
                any_ssw = I.any_ssw
                physical = I.physical
                fm = I.fm
                startwork=I.startwork.strftime("%d-%m-%Y %H:%M")

                print (workorder)
                print (company)
                print (opended)
                print (status)
                print (startwork)
                print (completedwork)
                print (caller)
                print (wah_status)
                print (timestramp)
                print (planned_date)
                print (job_description)
                print (fls_mame)
                print (fls_phone)
                print (management)
                print (remark)
                print (type_job)
                print (jla_ra)
                print (any_ssw)
                print (physical)
                print (fm)
            
                data = {
                                                    "type": "flex",
                                                    "altText": "Flex Message",
                                                    "contents": {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "url": "https://seeoil-web.com/cbre/Picture/CBRE-Logo.jpg",
                        "align": "center",
                        "gravity": "bottom",
                        "size": "full",
                        "aspectRatio": "20:7",
                        "aspectMode": "cover",
                        "action": {
                        "type": "uri",
                        "label": "Line",
                        "uri": "https://linecorp.com/"
                        },
                        "position": "relative"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "รายละเอียดของงาน",
                            "weight": "bold",
                            "size": "xl",
                            "color": "#225508FF",
                            "align": "center",
                            "contents": []
                        },
                        {
                            "type": "separator",
                            "margin": "xs",
                            "color": "#E42424FF"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "spacing": "none",
                            "margin": "xs",
                            "contents": [
                            {
                                "type": "text",
                                "text": "ผู้รับเหมา :",
                                "weight": "bold",
                                "size": "xs",
                                "color": "#045221FF",
                                "margin": "sm",
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": company,
                                "size": "xxs",
                                "color": "#045221FF",
                                "align": "start",
                                "margin": "none",
                                "wrap": True,
                                "contents": []
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "spacing": "none",
                            "margin": "xs",
                            "contents": [
                            {
                                "type": "text",
                                "text": "เลขแจ้งซ่อม :",
                                "weight": "bold",
                                "size": "xs",
                                "color": "#045221FF",
                                "margin": "sm",
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": workorder,
                                "size": "xxs",
                                "color": "#045221FF",
                                "align": "start",
                                "margin": "none",
                                "wrap": True,
                                "contents": []
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": "สถานี :",
                                "weight": "bold",
                                "size": "xs",
                                "color": "#045221FF",
                                "margin": "sm",
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": caller,
                                "size": "xxs",
                                "color": "#045221FF",
                                "align": "start",
                                "margin": "none",
                                "wrap": True,
                                "contents": []
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "spacing": "none",
                            "margin": "xs",
                            "contents": [
                            {
                                "type": "text",
                                "text": "รายละเอียดงาน :",
                                "weight": "bold",
                                "size": "xs",
                                "color": "#045221FF",
                                "margin": "sm",
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": job_description,
                                "size": "xxs",
                                "color": "#045221FF",
                                "align": "start",
                                "margin": "none",
                                "wrap": True,
                                "contents": []
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "spacing": "none",
                            "margin": "xs",
                            "contents": [
                            {
                                "type": "text",
                                "text": "ช่างที่เข้าทำงาน :",
                                "weight": "bold",
                                "size": "xs",
                                "color": "#045221FF",
                                "margin": "sm",
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": fls_startwork,
                                "size": "xxs",
                                "color": "#045221FF",
                                "align": "start",
                                "margin": "none",
                                "wrap": True,
                                "contents": []
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "spacing": "none",
                            "margin": "xs",
                            "contents": [
                            {
                                "type": "text",
                                "text": "เบอร์โทรช่าง :",
                                "weight": "bold",
                                "size": "xs",
                                "color": "#045221FF",
                                "margin": "sm",
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": fls_phone,
                                "size": "xxs",
                                "color": "#045221FF",
                                "align": "start",
                                "margin": "none",
                                "wrap": True,
                                "contents": []
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "spacing": "none",
                            "margin": "xs",
                            "contents": [
                            {
                                "type": "text",
                                "text": "CBRE FM : ",
                                "weight": "bold",
                                "size": "xs",
                                "color": "#045221FF",
                                "margin": "sm",
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": fm,
                                "size": "xxs",
                                "color": "#045221FF",
                                "align": "start",
                                "margin": "none",
                                "wrap": True,
                                "contents": []
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "spacing": "none",
                            "margin": "xs",
                            "contents": [
                            {
                                "type": "text",
                                "text": "วันที่เข้าทำงาน :",
                                "weight": "bold",
                                "size": "xs",
                                "color": "#045221FF",
                                "margin": "sm",
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": str(startwork),
                                "size": "xxs",
                                "color": "#045221FF",
                                "align": "start",
                                "margin": "none",
                                "wrap": True,
                                "contents": []
                            }
                            ]
                        }
                        ]
                    }
                    }
                                                                    }

                return data
        if type == 'admin2' :
            for I in detail_checkin :
                # Title = (I['Title'])
                print (I)
                workorder = I.workorder
                company= I.company
                opended = I.opended
                status = I.status
                startwork = I.startwork
                completedwork = I.completedwork.strftime("%d-%m-%Y %H:%M")
                caller = I.caller
                wah_status = I.wah_status
                timestramp = I.timestramp
                planned_date = I.planned_date.strftime("%d-%m-%Y %H:%M")
                job_description = I.job_description
                fls_mame = I.fls_mame_1
                fls_startwork = I.fls_startwork
                fls_completedwork = I.fls_completedwork
                fls_phone = I.fls_phone
                management = I.management
                remark = I.remark
                type_job = I.type_job
                jla_ra = I.jla_ra
                any_ssw = I.any_ssw
                physical = I.physical
                fm = I.fm
                startwork=I.startwork.strftime("%d-%m-%Y %H:%M")

                print (workorder)
                print (company)
                print (opended)
                print (status)
                print (startwork)
                print (completedwork)
                print (caller)
                print (wah_status)
                print (timestramp)
                print (planned_date)
                print (job_description)
                print (fls_mame)
                print (fls_phone)
                print (management)
                print (remark)
                print (type_job)
                print (jla_ra)
                print (any_ssw)
                print (physical)
                print (fm)
            
                data = {
                                                    "type": "flex",
                                                    "altText": "Flex Message",
                                                    "contents": {
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://seeoil-web.com/cbre/Picture/CBRE-Logo.jpg",
                    "align": "center",
                    "gravity": "bottom",
                    "size": "full",
                    "aspectRatio": "20:7",
                    "aspectMode": "cover",
                    "action": {
                    "type": "uri",
                    "label": "Line",
                    "uri": "https://linecorp.com/"
                    },
                    "position": "relative"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "CHECKOUT WAH NOTIFY",
                        "weight": "bold",
                        "size": "xl",
                        "color": "#225508FF",
                        "align": "center",
                        "contents": []
                    },
                    {
                        "type": "separator",
                        "margin": "xs",
                        "color": "#E42424FF"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "none",
                        "margin": "xs",
                        "contents": [
                        {
                            "type": "text",
                            "text": "Contractor :",
                            "weight": "bold",
                            "size": "xs",
                            "color": "#045221FF",
                            "margin": "sm",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": company,
                            "size": "xxs",
                            "color": "#045221FF",
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "none",
                        "margin": "xs",
                        "contents": [
                        {
                            "type": "text",
                            "text": "PlanedDate :",
                            "weight": "bold",
                            "size": "xs",
                            "color": "#045221FF",
                            "margin": "sm",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": str(planned_date),
                            "size": "xxs",
                            "color": "#045221FF",
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "none",
                        "margin": "xs",
                        "contents": [
                        {
                            "type": "text",
                            "text": "WorkOrder :",
                            "weight": "bold",
                            "size": "xs",
                            "color": "#045221FF",
                            "margin": "sm",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": workorder,
                            "size": "xxs",
                            "color": "#045221FF",
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "text",
                            "text": "SiteName :",
                            "weight": "bold",
                            "size": "xs",
                            "color": "#045221FF",
                            "margin": "sm",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": caller,
                            "size": "xxs",
                            "color": "#045221FF",
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "none",
                        "margin": "xs",
                        "contents": [
                        {
                            "type": "text",
                            "text": "JobDescriptions :",
                            "weight": "bold",
                            "size": "xs",
                            "color": "#045221FF",
                            "margin": "sm",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": job_description,
                            "size": "xxs",
                            "color": "#045221FF",
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "none",
                        "margin": "xs",
                        "contents": [
                        {
                            "type": "text",
                            "text": "FlsName CheckIn :",
                            "weight": "bold",
                            "size": "xs",
                            "color": "#045221FF",
                            "margin": "sm",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": fls_startwork,
                            "size": "xxs",
                            "color": "#045221FF",
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    },{

                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "none",
                        "margin": "xs",
                        "contents": [
                        {
                            "type": "text",
                            "text": "FlsName CheckOut :",
                            "weight": "bold",
                            "size": "xs",
                            "color": "#045221FF",
                            "margin": "sm",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": fls_completedwork,
                            "size": "xxs",
                            "color": "#045221FF",
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "none",
                        "margin": "xs",
                        "contents": [
                        {
                            "type": "text",
                            "text": "MobilePhoneFLS :",
                            "weight": "bold",
                            "size": "xs",
                            "color": "#045221FF",
                            "margin": "sm",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": fls_phone,
                            "size": "xxs",
                            "color": "#045221FF",
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "none",
                        "margin": "xs",
                        "contents": [
                        {
                            "type": "text",
                            "text": "MangementName :",
                            "weight": "bold",
                            "size": "xs",
                            "color": "#045221FF",
                            "margin": "sm",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": management,
                            "size": "xxs",
                            "color": "#045221FF",
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "none",
                        "margin": "xs",
                        "contents": [
                        {
                            "type": "text",
                            "text": "TypeOfJob :",
                            "weight": "bold",
                            "size": "xs",
                            "color": "#045221FF",
                            "margin": "sm",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": type_job,
                            "size": "xxs",
                            "color": "#045221FF",
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "none",
                        "margin": "xs",
                        "contents": [
                        {
                            "type": "text",
                            "text": "JLA/RAReviewed :",
                            "weight": "bold",
                            "size": "xs",
                            "color": "#045221FF",
                            "margin": "sm",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": jla_ra,
                            "size": "xxs",
                            "color": "#045221FF",
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "none",
                        "margin": "xs",
                        "contents": [
                        {
                            "type": "text",
                            "text": "WorkerInvolved ? : ",
                            "weight": "bold",
                            "size": "xs",
                            "color": "#045221FF",
                            "margin": "sm",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": any_ssw,
                            "size": "xxs",
                            "color": "#045221FF",
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "none",
                        "margin": "xs",
                        "contents": [
                        {
                            "type": "text",
                            "text": "Observation ? :",
                            "weight": "bold",
                            "size": "xs",
                            "color": "#045221FF",
                            "margin": "sm",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": physical,
                            "size": "xxs",
                            "color": "#045221FF",
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "none",
                        "margin": "xs",
                        "contents": [
                        {
                            "type": "text",
                            "text": "CBRE FM : ",
                            "weight": "bold",
                            "size": "xs",
                            "color": "#045221FF",
                            "margin": "sm",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": fm,
                            "size": "xxs",
                            "color": "#045221FF",
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "none",
                        "margin": "xs",
                        "contents": [
                        {
                            "type": "text",
                            "text": "Remarks :",
                            "weight": "bold",
                            "size": "xs",
                            "color": "#045221FF",
                            "margin": "sm",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": remark,
                            "size": "xxs",
                            "color": "#045221FF",
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "none",
                        "margin": "xs",
                        "contents": [
                        {
                            "type": "text",
                            "text": "CheckIn Time",
                            "weight": "bold",
                            "size": "xs",
                            "color": "#045221FF",
                            "margin": "sm",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": str(startwork),
                            "size": "xxs",
                            "color": "#045221FF",
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "none",
                        "margin": "xs",
                        "contents": [
                        {
                            "type": "text",
                            "text": "CheckOut Time",
                            "weight": "bold",
                            "size": "xs",
                            "color": "#045221FF",
                            "margin": "sm",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": str(completedwork),
                            "size": "xxs",
                            "color": "#045221FF",
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    }
                    ]
                }
                }
                                                                    }

                return data
            print("OK")
        if type == 'admin' :
            for I in detail_checkin :
                # Title = (I['Title'])
                print (I)
                workorder = I.workorder
                company= I.company
                opended = I.opended
                status = I.status
                startwork = I.startwork.strftime("%d-%m-%Y %H:%M")
                completedwork = I.completedwork
                caller = I.caller
                wah_status = I.wah_status
                timestramp = I.timestramp
                planned_date = I.planned_date.strftime("%d-%m-%Y %H:%M")
                job_description = I.job_description
                fls_mame = I.fls_mame_1
                fls_startwork = I.fls_startwork
                fls_phone = I.fls_phone
                management = I.management
                remark = I.remark
                type_job = I.type_job
                jla_ra = I.jla_ra
                any_ssw = I.any_ssw
                physical = I.physical
                fm = I.fm
                startwork=I.startwork.strftime("%d-%m-%Y %H:%M")

                print (workorder)
                print (company)
                print (opended)
                print (status)
                print (startwork)
                print (completedwork)
                print (caller)
                print (wah_status)
                print (timestramp)
                print (planned_date)
                print (job_description)
                print (fls_mame)
                print (fls_phone)
                print (management)
                print (remark)
                print (type_job)
                print (jla_ra)
                print (any_ssw)
                print (physical)
                print (fm)
            
                data = {
                                                    "type": "flex",
                                                    "altText": "Flex Message",
                                                    "contents": {
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://seeoil-web.com/cbre/Picture/CBRE-Logo.jpg",
                    "align": "center",
                    "gravity": "bottom",
                    "size": "full",
                    "aspectRatio": "20:7",
                    "aspectMode": "cover",
                    "action": {
                    "type": "uri",
                    "label": "Line",
                    "uri": "https://linecorp.com/"
                    },
                    "position": "relative"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "CHECK IN WAH NOTIFY",
                        "weight": "bold",
                        "size": "xl",
                        "color": "#225508FF",
                        "align": "center",
                        "contents": []
                    },
                    {
                        "type": "separator",
                        "margin": "xs",
                        "color": "#E42424FF"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "none",
                        "margin": "xs",
                        "contents": [
                        {
                            "type": "text",
                            "text": "Contractor :",
                            "weight": "bold",
                            "size": "xs",
                            "color": "#045221FF",
                            "margin": "sm",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": company,
                            "size": "xxs",
                            "color": "#045221FF",
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "none",
                        "margin": "xs",
                        "contents": [
                        {
                            "type": "text",
                            "text": "PlanedDate :",
                            "weight": "bold",
                            "size": "xs",
                            "color": "#045221FF",
                            "margin": "sm",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": str(planned_date),
                            "size": "xxs",
                            "color": "#045221FF",
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "none",
                        "margin": "xs",
                        "contents": [
                        {
                            "type": "text",
                            "text": "WorkOrder :",
                            "weight": "bold",
                            "size": "xs",
                            "color": "#045221FF",
                            "margin": "sm",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": workorder,
                            "size": "xxs",
                            "color": "#045221FF",
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "text",
                            "text": "SiteName :",
                            "weight": "bold",
                            "size": "xs",
                            "color": "#045221FF",
                            "margin": "sm",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": caller,
                            "size": "xxs",
                            "color": "#045221FF",
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "none",
                        "margin": "xs",
                        "contents": [
                        {
                            "type": "text",
                            "text": "JobDescriptions :",
                            "weight": "bold",
                            "size": "xs",
                            "color": "#045221FF",
                            "margin": "sm",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": job_description,
                            "size": "xxs",
                            "color": "#045221FF",
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "none",
                        "margin": "xs",
                        "contents": [
                        {
                            "type": "text",
                            "text": "FlsName :",
                            "weight": "bold",
                            "size": "xs",
                            "color": "#045221FF",
                            "margin": "sm",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": fls_mame,
                            "size": "xxs",
                            "color": "#045221FF",
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "none",
                        "margin": "xs",
                        "contents": [
                        {
                            "type": "text",
                            "text": "MobilePhoneFLS :",
                            "weight": "bold",
                            "size": "xs",
                            "color": "#045221FF",
                            "margin": "sm",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": fls_phone,
                            "size": "xxs",
                            "color": "#045221FF",
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "none",
                        "margin": "xs",
                        "contents": [
                        {
                            "type": "text",
                            "text": "MangementName :",
                            "weight": "bold",
                            "size": "xs",
                            "color": "#045221FF",
                            "margin": "sm",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": management,
                            "size": "xxs",
                            "color": "#045221FF",
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "none",
                        "margin": "xs",
                        "contents": [
                        {
                            "type": "text",
                            "text": "TypeOfJob :",
                            "weight": "bold",
                            "size": "xs",
                            "color": "#045221FF",
                            "margin": "sm",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": type_job,
                            "size": "xxs",
                            "color": "#045221FF",
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "none",
                        "margin": "xs",
                        "contents": [
                        {
                            "type": "text",
                            "text": "JLA/RAReviewed :",
                            "weight": "bold",
                            "size": "xs",
                            "color": "#045221FF",
                            "margin": "sm",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": jla_ra,
                            "size": "xxs",
                            "color": "#045221FF",
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "none",
                        "margin": "xs",
                        "contents": [
                        {
                            "type": "text",
                            "text": "WorkerInvolved ? : ",
                            "weight": "bold",
                            "size": "xs",
                            "color": "#045221FF",
                            "margin": "sm",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": any_ssw,
                            "size": "xxs",
                            "color": "#045221FF",
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "none",
                        "margin": "xs",
                        "contents": [
                        {
                            "type": "text",
                            "text": "Observation ? :",
                            "weight": "bold",
                            "size": "xs",
                            "color": "#045221FF",
                            "margin": "sm",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": physical,
                            "size": "xxs",
                            "color": "#045221FF",
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "none",
                        "margin": "xs",
                        "contents": [
                        {
                            "type": "text",
                            "text": "CBRE FM : ",
                            "weight": "bold",
                            "size": "xs",
                            "color": "#045221FF",
                            "margin": "sm",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": fm,
                            "size": "xxs",
                            "color": "#045221FF",
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "none",
                        "margin": "xs",
                        "contents": [
                        {
                            "type": "text",
                            "text": "Remarks :",
                            "weight": "bold",
                            "size": "xs",
                            "color": "#045221FF",
                            "margin": "sm",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": remark,
                            "size": "xxs",
                            "color": "#045221FF",
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "spacing": "none",
                        "margin": "xs",
                        "contents": [
                        {
                            "type": "text",
                            "text": "CheckIn Time",
                            "weight": "bold",
                            "size": "xs",
                            "color": "#045221FF",
                            "margin": "sm",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": str(startwork),
                            "size": "xxs",
                            "color": "#045221FF",
                            "align": "start",
                            "margin": "none",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    }
                    ]
                }
                }
                                                                    }

                return data
            print("OK")