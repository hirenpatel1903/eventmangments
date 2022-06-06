from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from urllib import response
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, JsonResponse,HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app.constants import ResponseMessages, StringConstants, RequestConstants, SystemConfigs
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
from app.common.common import format_json
from app.serializers.vendor_serializers import GetVendorSerializer

class VendorDetail(APIView):
    def data(request):
        if(request.user.role == SystemConfigs.ADMIN):
            if request.method == RequestConstants.POST:
                PAGE_SIZE = SystemConfigs.PAGE_SIZE
                PAGE_START = int(request.POST.get(RequestConstants.START))
                PAGE_SEARCH = request.POST.get(RequestConstants.SEARCH_VALUE)
                SNIPPERTS = User.objects.filter(role=RequestConstants.VENDOR)

                if PAGE_SEARCH != RequestConstants.EMPTY_VALUE:
                    SNIPPERTS = SNIPPERTS.filter(Q(name=PAGE_SEARCH) | Q(email=PAGE_SEARCH)| Q(mobile_number=PAGE_SEARCH))

                SNIPPERTS = SNIPPERTS.order_by(RequestConstants.QID)[PAGE_START*PAGE_SIZE:PAGE_SIZE]            
                TOTAL = User.objects.filter(role=RequestConstants.VENDOR).count()
                
                serializer = GetVendorSerializer(SNIPPERTS, many=True)
                
                DATA = format_json(serializer.data, status.HTTP_200_OK, ResponseMessages.SUCCESS_MSG)
                DATA[RequestConstants.PAGE]=PAGE_START
                DATA[RequestConstants.PER_PAGE]=PAGE_SIZE
                DATA[RequestConstants.RECODES_TOTAL]=TOTAL
                DATA[RequestConstants.RECODES_FILTERED]=TOTAL
        
                return HttpResponse(json.dumps(DATA))
