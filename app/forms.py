from xml.dom.minidom import Attr
from django import forms
from django.core import validators
from .models import Lead
from app.constants import HtmlViews, ContextVariables, UrlConstants, StringConstants, RequestConstants

# #Sign In Validations
class SignIn(forms.Form):
    email = forms.EmailField(help_text = StringConstants.WRITE_YOUR_EMAIL, )
    password = forms.CharField(widget = forms.PasswordInput)


#Forgot Password Validation
class ForgotPassword(forms.Form):
    email = forms.EmailField(help_text = StringConstants.ENTER_YOUR_MAIL, )

class LeadCreate(forms.ModelForm):
    class Meta:
        model = Lead
        fields = '__all__'