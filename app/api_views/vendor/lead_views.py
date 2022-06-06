from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

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
from requests import Response
from app.serializers.vendor_serializers import GetLeadAssignSerializer
from app.common.common import format_json

def vendor_lead_data(request):
    if request.method == RequestConstants.POST:
        PAGE_SIZE = SystemConfigs.PAGE_SIZE
        PAGE_START = int(request.POST.get(RequestConstants.START))
        PAGE_SEARCH = request.POST.get(RequestConstants.SEARCH_VALUE)
        VENDOR_ID = request.user.id
        SNIPPERTS = Lead_Assign.objects.filter(vendorID=VENDOR_ID).filter(deleted_at=None)

        if PAGE_SEARCH != RequestConstants.EMPTY_VALUE:
            SNIPPERTS = SNIPPERTS.filter(Q(name=PAGE_SEARCH) | Q(email=PAGE_SEARCH)| Q(mobile_number=PAGE_SEARCH))

        SNIPPERTS = SNIPPERTS.order_by(RequestConstants.QID)[PAGE_START*PAGE_SIZE:PAGE_SIZE]            
        TOTAL = Lead_Assign.objects.filter(vendorID=VENDOR_ID).filter(deleted_at=None).count()

        serializer = GetLeadAssignSerializer(SNIPPERTS, many=True)
        
        DATA = format_json(serializer.data, status.HTTP_200_OK, ResponseMessages.SUCCESS_MSG)
        DATA[RequestConstants.PAGE]=PAGE_START
        DATA[RequestConstants.PER_PAGE]=PAGE_SIZE
        DATA[RequestConstants.RECODES_TOTAL]=TOTAL
        DATA[RequestConstants.RECODES_FILTERED]=TOTAL
        
        return HttpResponse(json.dumps(DATA))