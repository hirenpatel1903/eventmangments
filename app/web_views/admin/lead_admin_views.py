from multiprocessing.sharedctypes import Value
from django.contrib.auth import authenticate
from django.shortcuts import redirect, render
from app.models import User, Lead, Lead_Assign, Lead_Comment,LEAD_STATUS,Lookup
from app.constants import HtmlViews, ContextVariables, UrlConstants, StringConstants, RequestConstants, SystemConfigs
from app.common.logger import Logger
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse,HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.db.models import Q
from ...common.helpers import Notification, notify
from django.conf import settings
import json
import datetime
from django.core import serializers

@login_required(login_url=UrlConstants.LOGIN)
def index(request):
    try:
        if(request.user.role == SystemConfigs.ADMIN):
            LEAD_WHATAPP_URL = settings.WHATSAPP_URL
            LEAD_WHATAPP_MESSAGE = settings.WHATSAPP_MESSAGE
            PAGE_SIZE = SystemConfigs.PAGE_SIZE
            return render(request, HtmlViews.LEAD_INDEX,{ContextVariables.WHATSAPP_URL:LEAD_WHATAPP_URL,ContextVariables.WHATSAPP_MESSAGE:LEAD_WHATAPP_MESSAGE,ContextVariables.PAGE_SIZE:PAGE_SIZE})
        else:
            return render(request, HtmlViews.ERROR_404)
    except Exception as e:
        Logger.logError(StringConstants.LOG_ERROR_MESSAGE.format(str(e)))
    return render(request, HtmlViews.LEAD_INDEX)

@login_required(login_url=UrlConstants.LOGIN)
def create(request):
    if(request.user.role == SystemConfigs.ADMIN):
        return render(request, HtmlViews.LEAD_CREATE)
    else:
        return render(request, HtmlViews.ERROR_404)

def store(request):
    try:
        if(request.user.role == SystemConfigs.ADMIN):
            if request.method == RequestConstants.POST:
                name = request.POST.get(RequestConstants.NAME)
                email = request.POST.get(RequestConstants.EMAIL)
                description = request.POST.get(RequestConstants.DESCRIPTION)
                mobile_number = request.POST.get(RequestConstants.MOBILE_NUMBER)
                address = request.POST.get(RequestConstants.ADDRESS) 
                country = request.POST.get(RequestConstants.COUNTRY) 
                state = request.POST.get(RequestConstants.STATE) 
                city = request.POST.get(RequestConstants.CITY) 
                date_of_event = request.POST.get(RequestConstants.DATE_OF_EVENT) 
                time_of_event = request.POST.get(RequestConstants.TIME_OF_EVENT) 

                DATA = Lead(name=name,email=email,description=description,mobile_number=mobile_number,address=address,country=country,state=state,city=city,date_of_event=date_of_event,time_of_event=time_of_event)
                DATA.save()

                messages.success(request,StringConstants.LEAD_CREATE)
                return HttpResponseRedirect(UrlConstants.LEAD_INDEX)
            else:
                messages.error(request,StringConstants.SOMETHING_WRONG)
                return render(request, HtmlViews.LEAD_CREATE) 
        else:
            return render(request, HtmlViews.ERROR_404)
    except Exception as e:
        Logger.logError(StringConstants.LOG_ERROR_MESSAGE.format(str(e)))
    return render(request, HtmlViews.LEAD_CREATE) 


@login_required(login_url=UrlConstants.LOGIN)
def edit(request, LEAD_ID):
    try:
        if(request.user.role == SystemConfigs.ADMIN):
            LEAD_ID = int(LEAD_ID)
            LEAD_DATA = get_object_or_404(Lead, id=LEAD_ID)
            LEAD_ALL_DATA = Lead.objects.get(id=LEAD_ID)
            return render(request, HtmlViews.LEAD_EDIT,{ContextVariables.LEAD_ID:LEAD_ID,ContextVariables.LEAD_ALL_DATA:LEAD_ALL_DATA})
        else:
            return render(request, HtmlViews.ERROR_404)
    except Exception as e:
        Logger.logError(StringConstants.LOG_ERROR_MESSAGE.format(str(e)))
    return render(request, HtmlViews.LEAD_INDEX) 

def update(request, LEAD_ID):
    if(request.user.role == SystemConfigs.ADMIN):
        LEAD_ID = int(LEAD_ID)
        try:
            LEAD_SEL = Lead.objects.get(id = LEAD_ID)
            LEAD_DATA = Lead.objects.filter(id=LEAD_ID)
            if LEAD_SEL:
                UPDATE_NAME = request.POST.get(RequestConstants.NAME)
                UPDATE_MOBILE_NUMBER = request.POST.get(RequestConstants.MOBILE_NUMBER)
                UPDATE_EMAIL = request.POST.get(RequestConstants.EMAIL)
                UPDATE_DESCRIPTION = request.POST.get(RequestConstants.DESCRIPTION)            
                UPDATE_ADDRESS = request.POST.get(RequestConstants.ADDRESS)
                UPDATE_COUNTRY = request.POST.get(RequestConstants.COUNTRY)
                UPDATE_STATE = request.POST.get(RequestConstants.STATE)
                UPDATE_CITY = request.POST.get(RequestConstants.CITY)
                UPDATE_DATE_OF_EVENT = request.POST.get(RequestConstants.DATE_OF_EVENT)
                UPDATE_TIME_OF_EVENT = request.POST.get(RequestConstants.TIME_OF_EVENT)

                LEAD_DATA.update(name=UPDATE_NAME, mobile_number=UPDATE_MOBILE_NUMBER, email=UPDATE_EMAIL, description=UPDATE_DESCRIPTION,address=UPDATE_ADDRESS,country=UPDATE_COUNTRY,state=UPDATE_STATE, city=UPDATE_CITY, date_of_event=UPDATE_DATE_OF_EVENT, time_of_event=UPDATE_TIME_OF_EVENT)
                messages.success(request,StringConstants.LEAD_UPDATE)

            return HttpResponseRedirect(UrlConstants.LEAD_INDEX)
        except Lead.DoesNotExist:
            messages.error(request,StringConstants.SOMETHING_WRONG)
            return HttpResponseRedirect(UrlConstants.LEAD_EDIT)
    else:
        return render(request, HtmlViews.ERROR_404)

@login_required(login_url=UrlConstants.LOGIN)
def delete(request, LEAD_ID):
    try:
        if(request.user.role == SystemConfigs.ADMIN):
            LEAD_ID = int(LEAD_ID)
            DATA = []
            try:
                LEAD_SEL = Lead.objects.get(id = LEAD_ID)
            except Lead.DoesNotExist:
                return HttpResponseRedirect(UrlConstants.LEAD_INDEX)
            LEAD_SEL.delete()
            messages.success(request,StringConstants.DELETED_RECORED)
            return JsonResponse({ContextVariables.DATA: DATA})
        else:
            return render(request, HtmlViews.ERROR_404)
    except Exception as e:
        Logger.logError(StringConstants.LOG_ERROR_MESSAGE.format(str(e)))
    return render(request, HtmlViews.LEAD_INDEX) 

@login_required(login_url=UrlConstants.LOGIN)
def assign(request, LEAD_ID):
    try:
        CONTEXT = {}
        LEAD_SINGLE_ID=LEAD_ID
        LEAD_ID = int(LEAD_ID)
        LEAD_ALL_DATA = Lead.objects.get(id=LEAD_ID)
        USER_ALL_DATA = User.objects.filter(role=RequestConstants.VENDOR).filter(status=RequestConstants.ACTIVE)
        ASSIGN_ALL_DATA = list(Lead_Assign.objects.select_related().filter(leadID=LEAD_SINGLE_ID))

        return render(request, HtmlViews.LEAD_ASSIGN,{ContextVariables.LEAD_ID:LEAD_ID,ContextVariables.LEAD_ALL_DATA:LEAD_ALL_DATA,ContextVariables.USER_ALL_DATA:USER_ALL_DATA,ContextVariables.CONTEXT: CONTEXT,ContextVariables.ASSIGN_ALL_DATA: ASSIGN_ALL_DATA})
    except Exception as e:
        Logger.logError(StringConstants.LOG_ERROR_MESSAGE.format(str(e)))
    return render(request, HtmlViews.LEAD_INDEX) 


def assign_store(request, LEAD_ID):
    try:
        LEAD_ID = int(LEAD_ID)
        LEAD_GET_ID = request.POST.get(RequestConstants.LEAD_ID)
        USER_LIST = request.POST.getlist(RequestConstants.USER_ID)
        for USER_ID in USER_LIST:
            USER_OBJ = User.objects.get(id=USER_ID)
            LEAD_OBJ = Lead.objects.get(id=LEAD_GET_ID)
            PENDING_LEAD_STATUS = Lookup.objects.get(id=settings.PENDING_STATUS_ID)
            if not Lead_Assign.objects.filter(vendorID=USER_OBJ, leadID=LEAD_OBJ).exists():
                DATA = Lead_Assign.objects.create(
                    vendorID=USER_OBJ,
                    leadID=LEAD_OBJ,
                    lead_status = PENDING_LEAD_STATUS
                )

                EMAIL_FILED = USER_OBJ.email
                MOBILE_NUMBER = USER_OBJ.mobile_number

                notify(EMAIL_FILED,MOBILE_NUMBER,Notification.LEAD_ASSIGN) 
                messages.success(request,StringConstants.LEAD_ASSIGN)
            else:
                LEAD_ID = LEAD_GET_ID
                messages.error(request,StringConstants.LEAD_ASSIGN_ALREDY)
        return redirect(StringConstants.URL_LEAD_ASSIGN, LEAD_ID=LEAD_GET_ID)
    except Exception as e:
        Logger.logError(StringConstants.LOG_ERROR_MESSAGE.format(str(e)))
    return render(request, HtmlViews.LEAD_INDEX) 

def assign_delete(request, assign_id):
    ASSIGN_ID = int(assign_id)
    DATA = []
    try:
        lead_asggin_id = Lead_Assign.objects.get(id = ASSIGN_ID)
    except Lead.DoesNotExist:
        return render(UrlConstants.LEAD_ASSIGN_ID.format(ASSIGN_ID))
    lead_asggin_id.delete()
    return JsonResponse({ContextVariables.DATA: DATA})

@login_required(login_url=UrlConstants.LOGIN)
def view(request, LEAD_ID):
    try:
        LEAD_SINGLE_ID = LEAD_ID
        LEAD_ID = int(LEAD_ID)
        LEAD_DATA = get_object_or_404(Lead, id=LEAD_ID)
        LEAD_ALL_DATA = Lead.objects.get(id=LEAD_ID)
        ASSIGN_VENDOR_ALL_DATA = list(Lead_Assign.objects.select_related().filter(leadID=LEAD_SINGLE_ID))
        return render(request, HtmlViews.LEAD_VIEW,{ContextVariables.LEAD_ID:LEAD_ID,ContextVariables.LEAD_ALL_DATA:LEAD_ALL_DATA,ContextVariables.ASSIGN_VENDOR_ALL_DATA:ASSIGN_VENDOR_ALL_DATA})
    except Exception as e:
        Logger.logError(StringConstants.LOG_ERROR_MESSAGE.format(str(e)))
    return render(request, HtmlViews.LEAD_INDEX) 

def comment_list(request,ASSIGN_ID,LEAD_ID):
    LEAD_ASSIGN_LIST = get_object_or_404(Lead_Assign, id=ASSIGN_ID)
    LEAD_ASSIGN_OBJ= Lead_Assign.objects.get(id=ASSIGN_ID)
    LEAD_OBJ = Lead.objects.get(id=LEAD_ID)
    LEAD_ASSIGN_ID = LEAD_ASSIGN_OBJ.id
    LEAD_ID = LEAD_OBJ.id
    data = list(Lead_Comment.objects.select_related().filter(leadAssignedId=LEAD_ASSIGN_ID).filter(leadID=LEAD_OBJ))
    context={
        RequestConstants.COMMENT_LIST: data
    }
    return render(request,HtmlViews.LEAD_MODAL, locals())

@login_required(login_url=UrlConstants.LOGIN)
def change_status(request):
    LEAD_ASSIGN_ID = request.POST.get(RequestConstants.ID)
    LEAD_ASSIGN_DELETE_STATUS = request.POST.get(RequestConstants.DELETE_VAL)
    LEAD_ASSIGN_DATA = Lead_Assign.objects.filter(id=LEAD_ASSIGN_ID)
    DATA = []  
    if LEAD_ASSIGN_DELETE_STATUS == RequestConstants.NONE:
        deleted_at=RequestConstants.DELETED_AT
        LEAD_ASSIGN_DATA.update(deleted_at=datetime.date.today())
    elif LEAD_ASSIGN_DELETE_STATUS is not None:
        deleted_at=RequestConstants.DELETED_AT
        LEAD_ASSIGN_DATA.update(deleted_at=None)
        
    return JsonResponse({ContextVariables.DATA: DATA})