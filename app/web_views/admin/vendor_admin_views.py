from urllib import response
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, JsonResponse,HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app.constants import HtmlViews, ContextVariables, UrlConstants, StringConstants, RequestConstants, SystemConfigs
from django.core.serializers import serialize
from app.constants import HtmlViews
from app.models import User, Lookup,Media
import json
from django.shortcuts import get_object_or_404
from app.common.logger import Logger
from django.conf import settings
from django.core.paginator import Paginator
import math
from functools import reduce
from django.db.models import Q

@login_required(login_url=UrlConstants.LOGIN)
def index(request):
    try:
        if(request.user.role == SystemConfigs.ADMIN):
            VENDOR_ALL_DATA = User.objects.filter(role=RequestConstants.VENDOR).order_by(RequestConstants.QID)            
            PAGE_SIZE = SystemConfigs.PAGE_SIZE
            return render(request, HtmlViews.VENDOR_INDEX,{ContextVariables.VENDOR_ALL_DATA:VENDOR_ALL_DATA,ContextVariables.PAGE_SIZE:PAGE_SIZE})
        else:
            return render(request, HtmlViews.ERROR_404)
    except Exception as e:
        Logger.logError(StringConstants.LOG_ERROR_MESSAGE.format(str(e)))
    return render(request, HtmlViews.VENDOR_INDEX)

@login_required(login_url=UrlConstants.LOGIN)
def change_status(request):
    if(request.user.role == SystemConfigs.ADMIN):
        try:
            USER_ID = request.POST.get(RequestConstants.ID)
            USER_STATUS = request.POST.get(RequestConstants.STATUS_VALUE)
            USER_DATA = User.objects.filter(id=USER_ID)
            DATA = []  
            if USER_STATUS==RequestConstants.ACTIVE:
                status=RequestConstants.STATUS
                USER_DATA.update(status=RequestConstants.DISABLE)
            elif USER_STATUS==RequestConstants.DISABLE:
                status=RequestConstants.STATUS
                USER_DATA.update(status=RequestConstants.ACTIVE)
                
            return JsonResponse({ContextVariables.DATA: DATA})
        except Exception as e:
            Logger.logError(SystemConfigs.LOG_ERROR_MESSAGE.format(str(e)))
        return render(request, HtmlViews.VENDOR_INDEX)
    else:
        return render(request, HtmlViews.ERROR_404)

@login_required(login_url=UrlConstants.LOGIN)
def view(request, vendor_id):
    if(request.user.role == SystemConfigs.ADMIN):
        try:
            VENDOR_ID = int(vendor_id)
            VENDOR_DATA = get_object_or_404(User, id=VENDOR_ID)
            VENDOR_ALL_DATA = User.objects.get(id=VENDOR_ID)
            if VENDOR_ALL_DATA:
                CATEGORY = Lookup.objects.get(id=VENDOR_ALL_DATA.category)
                CATERING = Lookup.objects.get(id=VENDOR_ALL_DATA.catering)
                MAX_CAPACITY = Lookup.objects.get(id=VENDOR_ALL_DATA.max_capacity)
                NUMBER_OF_EVENTS = Lookup.objects.get(id=VENDOR_ALL_DATA.number_of_events)
                USER_OBJ = User.objects.get(id=VENDOR_ALL_DATA.id)
                IMAGES_LIST = list(Media.objects.select_related().filter(userID=USER_OBJ.id))

                MEDIA_URL = settings.MEDIA_URL+SystemConfigs.MEDIA_PATH_USER_LOCATION.format(USER_OBJ.id)
                MEDIA_ROOT = settings.MEDIA_ROOT+SystemConfigs.MEDIA_PATH_USER_LOCATION.format(USER_OBJ.id)
            
            return render(request, HtmlViews.VENDOR_VIEW,{ContextVariables.VENDOR_ALL_DATA:VENDOR_ALL_DATA,ContextVariables.CATEGORY:CATEGORY,ContextVariables.CATERING:CATERING,ContextVariables.MAX_CAPACITY:MAX_CAPACITY,ContextVariables.NUMBER_OF_EVENTS:NUMBER_OF_EVENTS,ContextVariables.IMAGES_LIST:IMAGES_LIST,ContextVariables.MEDIA_URL:MEDIA_URL,ContextVariables.MEDIA_ROOT:MEDIA_ROOT})
        except Exception as e:
            Logger.logError(SystemConfigs.LOG_ERROR_MESSAGE.format(str(e)))
        return render(request, HtmlViews.VENDOR_INDEX)
    else:
        return render(request, HtmlViews.ERROR_404)

