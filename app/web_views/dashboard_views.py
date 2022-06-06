from pickle import NONE
from django.shortcuts import render
from app.constants import ContextVariables, HtmlViews
from django.contrib.auth.decorators import login_required
from app.models import User, Lookup, Media, Lead, Lead_Comment, Lead_Assign
from app.constants import HtmlViews, RequestConstants, UrlConstants, StringConstants, SystemConfigs
from django.conf import settings
from django.http import HttpResponseRedirect, JsonResponse,HttpResponse
from django.contrib import messages
from app.common.logger import Logger
from django.core.files.storage import FileSystemStorage

@login_required(login_url=UrlConstants.LOGIN)
def dashboard(request):
    try:
        NAME = request.user.name
        EMAIL = request.user.email
        ROLE = request.user.role
        USER_ID = request.user.id
        VENDOR_COUNT =  User.objects.filter(role=RequestConstants.VENDOR).count()
        LEAD_COUNT =  Lead.objects.count()
        UNASSIGN_LEAD_COUNT =  Lead_Assign.objects.filter(lead_status=settings.PENDING_STATUS_ID).count()
        ACCEPTED_LEAD_COUNT =  Lead_Assign.objects.filter(lead_status=settings.ACCEPTED_STATUS_ID).count()
        REJECTED_LEAD_COUNT =  Lead_Assign.objects.filter(lead_status=settings.REJECTED_STATUS_ID).count()
        
        VENDOR_ACCEPTED_LEAD_COUNT =  Lead_Assign.objects.filter(vendorID=USER_ID).filter(lead_status=settings.ACCEPTED_STATUS_ID).count()
        VENDOR_REJECTED_LEAD_COUNT =  Lead_Assign.objects.filter(vendorID=USER_ID).filter(lead_status=settings.REJECTED_STATUS_ID).count()
        VENDOR_PENDING_LEAD_COUNT =  Lead_Assign.objects.filter(vendorID=USER_ID).filter(lead_status=settings.PENDING_STATUS_ID).count()
        VENDOR_CLOSED_LEAD_COUNT =  Lead_Assign.objects.filter(vendorID=USER_ID).filter(lead_status=settings.CLOSED_STATUS_ID).count()

        return render(request, HtmlViews.DASHBOARD, {
            ContextVariables.NAME: NAME,
            ContextVariables.EMAIL: EMAIL,
            ContextVariables.ROLE: ROLE,
            ContextVariables.VENDOR_COUNT:VENDOR_COUNT,
            ContextVariables.LEAD_COUNT:LEAD_COUNT,
            ContextVariables.UNASSIGN_LEAD_COUNT:UNASSIGN_LEAD_COUNT,
            ContextVariables.ACCEPTED_LEAD_COUNT:ACCEPTED_LEAD_COUNT,
            ContextVariables.REJECTED_LEAD_COUNT:REJECTED_LEAD_COUNT,
            ContextVariables.VENDOR_ACCEPTED_LEAD_COUNT:VENDOR_ACCEPTED_LEAD_COUNT,
            ContextVariables.VENDOR_REJECTED_LEAD_COUNT:VENDOR_REJECTED_LEAD_COUNT,
            ContextVariables.VENDOR_PENDING_LEAD_COUNT:VENDOR_PENDING_LEAD_COUNT,
            ContextVariables.VENDOR_CLOSED_LEAD_COUNT:VENDOR_CLOSED_LEAD_COUNT
        })
    except Exception as e:
        Logger.logError(StringConstants.LOG_ERROR_MESSAGE.format(str(e)))
    return render(request, HtmlViews.DASHBOARD)

@login_required(login_url=UrlConstants.LOGIN)
def profile(request):
    try:
        USER_DATA = User.objects.get(id=request.user.id)
        USER_CATEGORY = int(USER_DATA.category)
        USER_CATERING = int(USER_DATA.catering)
        USER_MAX_CAPACITY = int(USER_DATA.max_capacity)
        USER_NUMBER_OF_EVENT = int(USER_DATA.number_of_events)
        IMAGES_LIST = list(Media.objects.select_related().filter(userID=request.user.id))
        MEDIA_URL = settings.MEDIA_URL+SystemConfigs.MEDIA_PATH_USER_LOCATION.format(request.user.id)
        MEDIA_ROOT = settings.MEDIA_ROOT+SystemConfigs.MEDIA_PATH_USER_LOCATION.format(request.user.id)
        CATEGORY_LIST = Lookup.objects.filter(type=RequestConstants.CATEGORY)         
        CATERING_LIST = Lookup.objects.filter(type=RequestConstants.CATERING)           
        MAX_CAPACITY_LIST = Lookup.objects.filter(type=RequestConstants.MAX_CAPACITY)           
        NUMBER_OF_EVENTS_LIST = Lookup.objects.filter(type=RequestConstants.NUMBER_OF_EVENT)
        return render(request, HtmlViews.PROFILE,{ContextVariables.CATEGORY_LIST:CATEGORY_LIST,ContextVariables.CATERING_LIST:CATERING_LIST,ContextVariables.MAX_CAPACITY_LIST:MAX_CAPACITY_LIST,ContextVariables.NUMBER_OF_EVENTS_LIST:NUMBER_OF_EVENTS_LIST,ContextVariables.USER_DATA:USER_DATA,ContextVariables.IMAGES_LIST:IMAGES_LIST,ContextVariables.MEDIA_URL:MEDIA_URL,ContextVariables.MEDIA_ROOT:MEDIA_ROOT,ContextVariables.USER_CATERING:USER_CATERING,ContextVariables.USER_CATEGORY:USER_CATEGORY,ContextVariables.USER_MAX_CAPACITY:USER_MAX_CAPACITY,ContextVariables.USER_NUMBER_OF_EVENT:USER_NUMBER_OF_EVENT})
    except Exception as e:
        Logger.logError(StringConstants.LOG_ERROR_MESSAGE.format(str(e)))
    return render(request, HtmlViews.PROFILE)

@login_required(login_url=UrlConstants.LOGIN)
def profile_store(request,USER_ID):
    USER_ID = int(USER_ID)
    try:        
        USER_SEL = User.objects.get(id=USER_ID)
        USER_DATA = User.objects.filter(id=USER_ID)
        if USER_SEL:
            UPDATE_NAME = request.POST.get(RequestConstants.NAME)
            UPDATE_EMAIL = request.POST.get(RequestConstants.EMAIL)
            UPDATE_CITY = request.POST.get(RequestConstants.CITY)
            UPDATE_STATE = request.POST.get(RequestConstants.STATE)
            UPDATE_COUNTRY = request.POST.get(RequestConstants.COUNTRY)
            UPDATE_ADDRESS = request.POST.get(RequestConstants.ADDRESS)
            UPDATE_DESCRIPTION = request.POST.get(RequestConstants.DESCRIPTION)
            UPDATE_MOBILE_NUMBER = request.POST.get(RequestConstants.MOBILE_NUMBER)
            UPDATE_CATEGORY = request.POST.get(RequestConstants.CATEGORY)
            UPDATE_CATERING = request.POST.get(RequestConstants.CATERING)
            UPDATE_MAX_CAPACITY = request.POST.get(RequestConstants.MAX_CAPACITY)
            UPDATE_NUMBER_OF_EVENTS = request.POST.get(RequestConstants.NUMBER_OF_EVENT)
            UPDATE_USERNAME = 'U'+ UPDATE_MOBILE_NUMBER

            USER_DATA.update(username=UPDATE_USERNAME, name=UPDATE_NAME, email=UPDATE_EMAIL, city=UPDATE_CITY,state=UPDATE_STATE,country=UPDATE_COUNTRY,address=UPDATE_ADDRESS, description=UPDATE_DESCRIPTION,mobile_number=UPDATE_MOBILE_NUMBER, category=UPDATE_CATEGORY, catering=UPDATE_CATERING, max_capacity=UPDATE_MAX_CAPACITY, number_of_events=UPDATE_NUMBER_OF_EVENTS)

            MEDIAS = request.FILES.getlist(RequestConstants.MEDIA)
            if MEDIAS:
                for MEDIA in MEDIAS:
                    MEDIA_STORE = Media.objects.create(
                        userID=User.objects.get(id=USER_ID),
                        url= MEDIA,
                        size=MEDIA.size,
                    )

                    FS = FileSystemStorage(
                        location=settings.MEDIA_ROOT+SystemConfigs.MEDIA_PATH_LOCATION.format(USER_ID)
                    )
                    
                    FILE = FS.save(MEDIA.name, MEDIA)
                    FILE_URL = FS.url(FILE)
                    
            messages.success(request,StringConstants.UPDATE_MY_PROFILE)
        return HttpResponseRedirect(UrlConstants.EDIT_PROFILE)
    except Lead.DoesNotExist:
        messages.error(request,StringConstants.SOMETHING_WRONG)
        return HttpResponseRedirect(UrlConstants.EDIT_PROFILE)


# @login_required(login_url=UrlConstants.LOGIN)
def delete_media(request, MEDIA_ID):
    MEDIA_ID = int(MEDIA_ID)
    DATA = []
    try:
        MEDIA_SEL = Media.objects.get(id=MEDIA_ID)
        USER_OBJ = User.objects.get(id=MEDIA_SEL.userID.id)
    except Lead.DoesNotExist:
        return HttpResponseRedirect(UrlConstants.EDIT_PROFILE)
    FS = FileSystemStorage(
        location=settings.MEDIA_ROOT+SystemConfigs.MEDIA_PATH_LOCATION.format(USER_OBJ)
    )
    
    # FileSystemStorage.delete(request,SystemConfigs.MEDIA_PATH_LOCATION_DELETE.format(USER_OBJ,MEDIA_SEL.url))
    MEDIA_SEL.delete()
    return JsonResponse({ContextVariables.DATA: DATA})