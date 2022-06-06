from multiprocessing import context
from pickle import NONE, TRUE
import uuid
from datetime import datetime
from django.conf import settings

from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib.sessions.models import Session
from django.views.decorators.csrf import csrf_exempt

from app.models import User, Lookup, Media, Verification_Token
from app.constants import HtmlViews, ContextVariables, UrlConstants, StringConstants, RequestConstants, SystemConfigs
from app.common.logger import Logger
from app import forms
from django.http import HttpResponse
from django.contrib.auth import logout, login
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.hashers import check_password
import os
from django.core.files.storage import FileSystemStorage
from ..common.helpers import Notification, notify
from django.utils.crypto import get_random_string
import json
from django.contrib import messages
import time

@csrf_exempt
def login_user(request):
    try:
        if request.user.is_authenticated:
            messages.success(request,StringConstants.USER_ALREDYLOGIN)
            return HttpResponseRedirect(UrlConstants.DASHBOARD)
        else:
            error = None
            if request.method == RequestConstants.POST:
                EMAIL = request.POST.get(RequestConstants.EMAIL)
                PASSWORD = request.POST.get(RequestConstants.PASSWORD) 
                USER_OBJ_DATA = User.objects.filter(email=EMAIL)
                if not USER_OBJ_DATA.filter(is_verify=settings.TOKEN_VERIFY_BY_USER_EMAIL).exists():    
                    messages.error(request,StringConstants.MAIL_VERIFY_USER_TOKEN)  

                    USER_OBJ = User.objects.get(email=EMAIL)
                    notify(EMAIL,None,Notification.VERIFY_AGAIN_SENT_DETAILS,USER_OBJ.is_verify,None)   

                    return render(request, HtmlViews.LOGIN)
                else:                               
                    USER_OBJ = USER_OBJ_DATA.filter(status=RequestConstants.ACTIVE)
                    if USER_OBJ.exists():
                        USER_OBJ = USER_OBJ.first()
                        if USER_OBJ.deleted_at is not None:
                            messages.error(request,StringConstants.INVALID_USER)  
                            return render(request, HtmlViews.LOGIN)
                        USERNAME = USER_OBJ.username
                        USER_DATA = authenticate(request, username=USERNAME, email=EMAIL, password=PASSWORD)

                        if USER_DATA is not None:
                            login(request,USER_DATA)
                            if USER_OBJ.basemodel_ptr_id is None:
                                UID = USER_OBJ.basemodel_ptr_id
                                USER_OBJ.last_login = datetime.now()
                                USER_OBJ.save()
                            else:
                                UID = USER_OBJ.basemodel_ptr_id
                                request.session[RequestConstants.UID] = str(UID)
                                messages.success(request,StringConstants.LOGIN_USER)
                            return HttpResponseRedirect(UrlConstants.DASHBOARD)
                        else:
                            messages.error(request,StringConstants.INVALID_USER)
                    else:
                        messages.error(request,StringConstants.USER_DISABLED)
            return render(request, HtmlViews.LOGIN)            
    except Exception as e:
        Logger.logError(StringConstants.LOG_ERROR_MESSAGE.format(str(e)))
    return render(request, HtmlViews.LOGIN)


def logout_user(request):    
    logout(request)
    messages.success(request,StringConstants.LOGOUT_USER)
    return HttpResponseRedirect(UrlConstants.LOGIN)


def change_passwords(request,token):
    context={}
    try:
        if request.user.is_authenticated:
            messages.success(request,StringConstants.USER_ALREDYLOGIN)
            return HttpResponseRedirect(UrlConstants.DASHBOARD)
        else:  
            PROFILE_OBJ = Verification_Token.objects.filter(token=token).first()
            context = { ContextVariables.USER_ID:PROFILE_OBJ.vendorID.id }
                
            if request.method == RequestConstants.POST:
                NEW_PASSWORD = request.POST.get(RequestConstants.PASSWORD)
                CONFIM_PASSWORD = request.POST.get(RequestConstants.PASSWORD_CONFIRM)
                USER_ID = request.POST.get(RequestConstants.USER_ID)

                if USER_ID is None:
                    messages.error(request,StringConstants.NO_USER_FOUND)
                    return render(request,UrlConstants.CHANGE_PASSWORD_TOKEN.format(token),context)

                if NEW_PASSWORD and CONFIM_PASSWORD and NEW_PASSWORD != CONFIM_PASSWORD:
                    messages.error(request,StringConstants.BOTH_SHOULD_BE_EQUAL)
                    return render(request,UrlConstants.CHANGE_PASSWORD_TOKEN.format(token),context)
                else:   
                    USER_OBJ = User.objects.get(id=USER_ID)
                    USER_DATA = User.objects.filter(id=USER_ID)
                    if USER_OBJ:
                        NEW_PASSWORD = make_password(NEW_PASSWORD)
                        USER_DATA.update(password=NEW_PASSWORD)   
                        messages.success(request,StringConstants.PASSWORD_RESET_SUCCESSFULLY)
                        return redirect(UrlConstants.LOGIN)
                    else:
                        messages.error(request,StringConstants.NO_USER_FOUND)
                        return render(request,UrlConstants.CHANGE_PASSWORD_TOKEN.format(token),context)
    except Exception as e:
        Logger.logError(StringConstants.LOG_ERROR_MESSAGE.format(str(e)))
    return render(request, HtmlViews.RESET_PASSWORD,context)

global str
@csrf_exempt
def forgot_password(request):
    context = {}
    try:
        if request.user.is_authenticated:
            messages.success(request,StringConstants.USER_ALREDYLOGIN)
            return HttpResponseRedirect(UrlConstants.DASHBOARD)
        else:  
            if request.method == RequestConstants.POST:
                EMAIL_FILED = request.POST.get(RequestConstants.EMAIL)
                if not User.objects.filter(email=EMAIL_FILED).first():
                    messages.error(request,StringConstants.NOT_FOUND_EMAIL)
                    return redirect(UrlConstants.FORGOT_PASSWORD)

                USER_OBJ = User.objects.get(email=EMAIL_FILED)
                TOKEN = str(uuid.uuid4())

                profile_all_data = Verification_Token.objects.filter(vendorID=USER_OBJ)
                if not profile_all_data:
                    USER_ID = USER_OBJ
                    TOKEN_VALUE = TOKEN
                    DATA = Verification_Token(vendorID=USER_ID,token=TOKEN_VALUE)
                    DATA.save()
                else:
                    Verification_Token.objects.filter(vendorID=USER_OBJ).update(token=TOKEN)
                    
                MOBILE_NUMBER = None
                notify(EMAIL_FILED,MOBILE_NUMBER,Notification.FORGOT_PASSWORD,TOKEN)  

                messages.success(request,StringConstants.EMAIL_IS_SENT)
                return redirect(UrlConstants.FORGOT_PASSWORD)            
    except Exception as e:
        Logger.logError(StringConstants.LOG_ERROR_MESSAGE.format(str(e)))
        messages.error(request,StringConstants.SOMETHING_WRONG)  
    return render(request, HtmlViews.FORGOT_PASSWORD,context)


def register(request):
    try:   
        if request.user.is_authenticated:
            messages.success(request,StringConstants.USER_ALREDYLOGIN)
            return HttpResponseRedirect(UrlConstants.DASHBOARD)
        else:     
            if request.method == RequestConstants.GET:
                CATEGORY_LIST = Lookup.objects.filter(type=RequestConstants.CATEGORY)  
                CATERING_LIST = Lookup.objects.filter(type=RequestConstants.CATERING)           
                MAX_CAPACITY_LIST = Lookup.objects.filter(type=RequestConstants.MAX_CAPACITY)           
                NUMBER_OF_EVENTS_LIST = Lookup.objects.filter(type=RequestConstants.NUMBER_OF_EVENT)  
                TERMS_OF_USE_URL = settings.TERMS_OF_USE_URL         
                PRIVACY_POLICY_URL = settings.PRIVACY_POLICY_URL
                return render(request, HtmlViews.REGISTER, {ContextVariables.CATEGORY_LIST:CATEGORY_LIST,ContextVariables.CATERING_LIST:CATERING_LIST,ContextVariables.MAX_CAPACITY_LIST:MAX_CAPACITY_LIST,ContextVariables.NUMBER_OF_EVENTS_LIST:NUMBER_OF_EVENTS_LIST,ContextVariables.TERMS_OF_USE_URL:TERMS_OF_USE_URL,ContextVariables.PRIVACY_POLICY_URL:PRIVACY_POLICY_URL})
            elif request.method == RequestConstants.POST:
                NAME = request.POST.get(RequestConstants.NAME)
                EMAIL = request.POST.get(RequestConstants.EMAIL)
                ADDRESS = request.POST.get(RequestConstants.ADDRESS)
                COUNTRY = request.POST.get(RequestConstants.COUNTRY)
                STATE = request.POST.get(RequestConstants.STATE)
                CITY = request.POST.get(RequestConstants.CITY)
                DESCRIPTION = request.POST.get(RequestConstants.DESCRIPTION)
                MOBILE_NUMBER = request.POST.get(RequestConstants.MOBILE_NUMBER)
                CATEGORY = request.POST.get(RequestConstants.CATEGORY)
                CATERING = request.POST.get(RequestConstants.CATERING)
                MAX_CAPACITY = request.POST.get(RequestConstants.MAX_CAPACITY)
                NUMBER_OF_EVENTS = request.POST.get(RequestConstants.NUMBER_OF_EVENT)
                PASSWORD = make_password(request.POST.get(RequestConstants.PASSWORD))
                ROLE = RequestConstants.VENDOR
                STATUS = RequestConstants.DISABLE
                USERNAME = 'U'+ MOBILE_NUMBER

                Data = User(username=USERNAME,name=NAME,password=PASSWORD,role=ROLE,email=EMAIL,address=ADDRESS,country=COUNTRY,state=STATE,city=CITY,description=DESCRIPTION,mobile_number=MOBILE_NUMBER,category=CATEGORY,catering=CATERING,max_capacity=MAX_CAPACITY,number_of_events=NUMBER_OF_EVENTS,status=STATUS)
                Data.save()
                
                TOKEN = str(uuid.uuid4())
                USER_OBJ = User.objects.get(email=EMAIL)

                if USER_OBJ:
                    User.objects.filter(email=USER_OBJ.email).update(is_verify=TOKEN)

                notify(EMAIL,MOBILE_NUMBER,Notification.REGISTER,TOKEN)            
                
                MEDIAS = request.FILES.getlist(RequestConstants.MEDIA)
                for MEDIA in MEDIAS:
                    MEDIA_STORE = Media.objects.create(
                        userID=User.objects.last(),
                        url= MEDIA,
                        size=MEDIA.size,
                    )

                    USER_LAST_ID = User.objects.last().id
                    FS = FileSystemStorage(
                        location=settings.MEDIA_ROOT+SystemConfigs.MEDIA_PATH_LOCATION.format(USER_LAST_ID)
                    )
                    
                    FILE = FS.save(MEDIA.name, MEDIA)
                    FILE_URL = FS.url(FILE)
                
                messages.success(request,StringConstants.REGISTER_USER)            
                return HttpResponseRedirect(UrlConstants.LOGIN)
    except Exception as e:
        Logger.logError(StringConstants.LOG_ERROR_MESSAGE.format(str(e)))
        messages.error(request,StringConstants.SOMETHING_WRONG)
        return HttpResponseRedirect(UrlConstants.REGISTER)


@csrf_exempt
def change_password(request):
    try:
        context = {}
        USER_OBJ = User.objects.filter(basemodel_ptr_id=request.user.id)
        if len(USER_OBJ)>0:
            DATA = User.objects.get(basemodel_ptr_id=request.user.id)
            context[ContextVariables.DATA] = DATA
        if request.method == RequestConstants.POST:
            CURRENT_PASSWORD = request.POST.get(RequestConstants.CURRENT_PASSWORD)
            NEW_PAASWORD = request.POST.get(RequestConstants.PASSWORD)        
            USER_DATA_OBJ = User.objects.get(id=request.user.id)
            EMAIL_USER = USER_DATA_OBJ.email
            
            CHECK_DATA = USER_DATA_OBJ.check_password(CURRENT_PASSWORD)
            if CHECK_DATA:
                USER_DATA_OBJ.set_password(NEW_PAASWORD)
                USER_DATA_OBJ.save()            
                
                messages.success(request,StringConstants.PASSWORD_CHANGED)
                USER_DATA = User.objects.get(email=EMAIL_USER)
                login(request,USER_DATA)
            else:
                context[StringConstants.CURRENT_PASSWORD] = CURRENT_PASSWORD
                context[StringConstants.PASSWORD] = NEW_PAASWORD
                messages.error(request,StringConstants.CURRENT_PASSWORD_NOT_MATCH)

        return render(request, HtmlViews.CHANGE_PASSWORD,context)
    except Exception as e:
        Logger.logError(StringConstants.LOG_ERROR_MESSAGE.format(str(e)))
    return HttpResponseRedirect(UrlConstants.CHANGE_PASSWORD)


@csrf_exempt
def check_mobilenumber(request):
    try:
        IS_AVAIABLE = StringConstants.TRUE_VALUE
        MOBILE_NUMBER = request.POST.get(RequestConstants.MOBILE_NUMBER)
        if MOBILE_NUMBER:
            try: 
                CH_DATA = User.objects.filter(mobile_number=MOBILE_NUMBER)
                if CH_DATA:
                    User.objects.filter(mobile_number=MOBILE_NUMBER)
                    IS_AVAIABLE = StringConstants.FALSE_VALUE
            except User.DoesNotExit:
                IS_AVAIABLE = StringConstants.TRUE_VALUE
        return HttpResponse(IS_AVAIABLE)
    except Exception as e:
        Logger.logError(StringConstants.LOG_ERROR_MESSAGE.format(str(e)))
    return HttpResponse(StringConstants.FALSE_VALUE)

@csrf_exempt
def check_email(request):
    try:
        IS_AVAIABLE = StringConstants.TRUE_VALUE
        CHECK_EMAIL = request.POST.get(RequestConstants.EMAIL)
        if CHECK_EMAIL:
            try:
                CH_DATA = User.objects.filter(email=CHECK_EMAIL)
                if CH_DATA:
                    User.objects.filter(email=CHECK_EMAIL)
                    IS_AVAIABLE = StringConstants.FALSE_VALUE
            except User.DoesNotExit:
                IS_AVAIABLE = StringConstants.TRUE_VALUE
        return HttpResponse(IS_AVAIABLE)
    except Exception as e:
        Logger.logError(StringConstants.LOG_ERROR_MESSAGE.format(str(e)))
    return HttpResponse(StringConstants.FALSE_VALUE)

@csrf_exempt
def check_user_mobilenumber(request):
    try:
        IS_AVAIABLE = StringConstants.TRUE_VALUE
        MOBILE_NUMBER = request.POST.get(RequestConstants.MOBILE_NUMBER)
        USER_ID = request.POST.get(RequestConstants.USER_ID)
        if MOBILE_NUMBER:
            try: 
                CH_DATA = User.objects.filter(mobile_number=MOBILE_NUMBER).filter(id=USER_ID)
                if not CH_DATA:
                    User.objects.filter(mobile_number=MOBILE_NUMBER)
                    IS_AVAIABLE = StringConstants.FALSE_VALUE
            except User.DoesNotExit:
                IS_AVAIABLE = StringConstants.TRUE_VALUE
        return HttpResponse(IS_AVAIABLE)
    except Exception as e:
        Logger.logError(StringConstants.LOG_ERROR_MESSAGE.format(str(e)))
    return HttpResponse(StringConstants.FALSE_VALUE)

@csrf_exempt
def check_user_email(request):
    try: 
        IS_AVAIABLE = StringConstants.TRUE_VALUE
        CHECK_EMAIL = request.POST.get(RequestConstants.EMAIL)
        USER_ID = request.POST.get(RequestConstants.USER_ID)
        if CHECK_EMAIL:
            try:
                CH_DATA = User.objects.filter(email=CHECK_EMAIL).filter(id=USER_ID)
                if not CH_DATA:
                    User.objects.filter(email=CHECK_EMAIL)
                    IS_AVAIABLE = StringConstants.FALSE_VALUE
            except User.DoesNotExit:
                IS_AVAIABLE = StringConstants.TRUE_VALUE
        return HttpResponse(IS_AVAIABLE)
    except Exception as e:
        Logger.logError(StringConstants.LOG_ERROR_MESSAGE.format(str(e)))
    return HttpResponse(StringConstants.FALSE_VALUE)


def login_usercheck(request,token):
    try:
        USER_OBJ = User.objects.filter(is_verify=token).first()

        if USER_OBJ:
            User.objects.filter(email=USER_OBJ.email).update(is_verify=settings.TOKEN_VERIFY_BY_USER_EMAIL)
            messages.success(request,StringConstants.USER_VERIFY)
            return HttpResponseRedirect(UrlConstants.LOGIN)
        else:
            messages.error(request,StringConstants.USER_NOT_VERIFY)
            return HttpResponseRedirect(UrlConstants.LOGIN)
    except Exception as e:
        Logger.logError(StringConstants.LOG_ERROR_MESSAGE.format(str(e)))
        messages.error(request,StringConstants.SOMETHING_WRONG)  
    return render(request, HtmlViews.LOGIN)

def contact_details(request):
    WHATSAPP_URL = settings.WHATSAPP_URL
    WHATSAPP_MESSAGE = settings.WHATSAPP_MESSAGE
    return render(request, HtmlViews.CONTACT_DETAILS,{ContextVariables.WHATSAPP_URL:WHATSAPP_URL,ContextVariables.WHATSAPP_MESSAGE:WHATSAPP_MESSAGE})
