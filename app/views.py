from django.shortcuts import render
from app.constants import HtmlViews

# Create your views here.

def error_404_view(request,exception):
    return render(request,HtmlViews.ERROR_404)