from django.http import HttpResponseRedirect
from django.shortcuts import render
from app import forms
from django.core.cache import cache
from django.http import HttpResponse
from django.views.decorators.cache import never_cache
from app.constants import StringConstants

@never_cache
def clear_cache(request):
    cache.clear()
    return HttpResponse(StringConstants.CACHE_CLEAR_SUCCESSFULLY)