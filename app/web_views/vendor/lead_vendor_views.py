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
def index_lead_vendor(request):
    try:
        if(request.user.role == SystemConfigs.VENDOR):
            LEAD_WHATAPP_URL = settings.WHATSAPP_URL
            LEAD_WHATAPP_MESSAGE = settings.WHATSAPP_MESSAGE            
            PAGE_SIZE = SystemConfigs.PAGE_SIZE
            return render(request, HtmlViews.VENDOR_LEAD_INDEX,{ContextVariables.WHATSAPP_URL:LEAD_WHATAPP_URL,ContextVariables.WHATSAPP_MESSAGE:LEAD_WHATAPP_MESSAGE,ContextVariables.PAGE_SIZE:PAGE_SIZE})
        else:
            return render(request, HtmlViews.ERROR_404)
    except Exception as e:
        Logger.logError(StringConstants.LOG_ERROR_MESSAGE.format(str(e)))
    return render(request, HtmlViews.VENDOR_LEAD_INDEX) 

@login_required(login_url=UrlConstants.LOGIN)
def view_lead_vendor(request, LEAD_ASSIGN_ID):
    try:
        LEAD_ASSIGN_SINGLE_ID = LEAD_ASSIGN_ID
        LEAD_ASSIGN_ID = int(LEAD_ASSIGN_ID)
        LEAD_DATA = get_object_or_404(Lead_Assign, id=LEAD_ASSIGN_ID)
        DATA_VIEW = Lead_Assign.objects.get(id=LEAD_ASSIGN_SINGLE_ID)  
        
        if DATA_VIEW.lead_status.value == RequestConstants.STATUS_PENDING:
            STATUS_LIST = Lookup.objects.filter(type=RequestConstants.LEAD_STATUS).filter(value__in=[RequestConstants.ACCEPTED,RequestConstants.REJECTED])
        else:
            STATUS_LIST = Lookup.objects.filter(type=RequestConstants.LEAD_STATUS).filter(~Q(value__in=[RequestConstants.ACCEPTED,RequestConstants.REJECTED,RequestConstants.STATUS_PENDING]))

        return render(request, HtmlViews.VENDOR_LEAD_VIEW,{ContextVariables.LEAD_ASSIGN_ID:LEAD_ASSIGN_ID,ContextVariables.DATA_VIEW:DATA_VIEW,ContextVariables.STATUS_LIST:STATUS_LIST})  
    except Exception as e:
        Logger.logError(StringConstants.LOG_ERROR_MESSAGE.format(str(e)))
    return render(request, HtmlViews.VENDOR_LEAD_INDEX) 
    
    
def store_lead_vendor(request, LEAD_ASSIGN_ID):
    LEAD_ASSIGN_ID = int(LEAD_ASSIGN_ID)
    try:
        LEAD_SINGLE_DATA = Lead_Assign.objects.get(id =LEAD_ASSIGN_ID)
        if LEAD_SINGLE_DATA:
            LEAD_ID = request.POST.get(RequestConstants.LEAD_ID)
            LEAD_ASSIGN_VAR_ID = request.POST.get(RequestConstants.LEAD_ASSIGN_ID)
            VENDOR_ID = request.POST.get(RequestConstants.VENDOR_ID)
            STATUS = request.POST.get(RequestConstants.STATUS)
            COMMENT = request.POST.get(RequestConstants.COMMENT)
            LOOK_OBJ = Lookup.objects.get(id=STATUS)

            LEAD_DATA = Lead_Assign.objects.filter(id=LEAD_ASSIGN_ID).filter(vendorID=VENDOR_ID).filter(leadID=LEAD_ID)
            LEAD_DATA.update(lead_status=STATUS,last_comments=COMMENT)
            
            LEAD_ID = Lead.objects.get(id=LEAD_ID) 
            LEAD_ASSIGN_OBJ = Lead_Assign.objects.get(id=LEAD_ASSIGN_VAR_ID) 
            VENDOR_OBJ = User.objects.get(id=VENDOR_ID) 
            DATA = Lead_Comment(leadID=LEAD_ID,leadAssignedId=LEAD_ASSIGN_OBJ,vendorID=VENDOR_OBJ,status=LOOK_OBJ,comments=COMMENT)
            DATA.save()   

            EMAIL_FILED = VENDOR_OBJ.email
            MOBILE_NUMBER = VENDOR_OBJ.mobile_number
            STATUS_LEAD=LOOK_OBJ.value
            LEAD_NAME = LEAD_ID.name

            notify(EMAIL_FILED,MOBILE_NUMBER,Notification.LEAD_ACCEPT_REJECT,'',STATUS_LEAD,LEAD_NAME)
            
            messages.success(request,StringConstants.VENDOR_LEAD_STATUS_UPDATE)
            return HttpResponseRedirect(UrlConstants.VENDOR_LEAD_INDEX)
        else:
            messages.error(request,StringConstants.SOMETHING_WRONG)            
            return render(UrlConstants.VENDOR_LEAD_VIEW_ID.format(LEAD_ASSIGN_ID))
    except Lead.DoesNotExist:
        error = StringConstants.SOMETHING_WRONG
        return HttpResponseRedirect(UrlConstants.VENDOR_LEAD_INDEX, {ContextVariables.ERROR: error})

