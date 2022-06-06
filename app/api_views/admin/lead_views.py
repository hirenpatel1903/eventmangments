from multiprocessing.sharedctypes import Value
from django.contrib.auth import authenticate
from django.shortcuts import redirect, render
from app.models import User, Lead, Lead_Assign, Lead_Comment,LEAD_STATUS,Lookup
from app.constants import HtmlViews, ContextVariables, UrlConstants, StringConstants, RequestConstants, SystemConfigs, ResponseMessages
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
from app.common.common import format_json
from app.serializers.vendor_serializers import GetLeadSerializer
from rest_framework import status

@login_required(login_url=UrlConstants.LOGIN)
def data(request):
    if(request.user.role == SystemConfigs.ADMIN):
        if request.method == RequestConstants.POST:
            PAGE_SIZE = SystemConfigs.PAGE_SIZE
            PAGE_START = int(request.POST.get(RequestConstants.START))
            PAGE_SEARCH = request.POST.get(RequestConstants.SEARCH_VALUE)
            SNIPPERTS = Lead.objects.all()

            if PAGE_SEARCH != RequestConstants.EMPTY_VALUE:
                SNIPPERTS = SNIPPERTS.filter(Q(name=PAGE_SEARCH) | Q(email=PAGE_SEARCH)| Q(mobile_number=PAGE_SEARCH)| Q(city=PAGE_SEARCH))

            SNIPPERTS = SNIPPERTS.order_by(RequestConstants.QID)[PAGE_START*PAGE_SIZE:PAGE_SIZE]            
            TOTAL = Lead.objects.all().order_by(RequestConstants.QID).count()
            
            serializer = GetLeadSerializer(SNIPPERTS, many=True)
            
            DATA = format_json(serializer.data, status.HTTP_200_OK, ResponseMessages.SUCCESS_MSG)
            DATA[RequestConstants.PAGE]=PAGE_START
            DATA[RequestConstants.PER_PAGE]=PAGE_SIZE
            DATA[RequestConstants.RECODES_TOTAL]=TOTAL
            DATA[RequestConstants.RECODES_FILTERED]=TOTAL
    
            return HttpResponse(json.dumps(DATA))
    else:
        return render(request, HtmlViews.ERROR_404)
  