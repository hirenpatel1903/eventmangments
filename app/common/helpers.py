from email import message
from django.core.mail import send_mail
import uuid
from app.models import User, Lookup, Media
from app.constants import HtmlViews, ContextVariables, UrlConstants, StringConstants, RequestConstants, SystemConfigs
from django.conf import settings
from django.core.mail import EmailMessage
import enum
import http.client
from app.common.logger import Logger
import requests

class Notification (enum.Enum):
    FORGOT_PASSWORD = 1
    REGISTER = 2
    LEAD_ASSIGN = 3
    LEAD_ACCEPT_REJECT = 4
    VERIFY_AGAIN_SENT_DETAILS = 5

def notify(email=None,mobile_number=None,type=None,token=None,status=None,lead_name=None):
    if type == Notification.REGISTER: 
        subject = StringConstants.REGISTER_MAIL
        message= StringConstants.EMAIL_SENT_LOGIN_WITH_TOKEN.format(settings.URL,token)
    elif type == Notification.LEAD_ASSIGN:
        subject = StringConstants.LEAD_ASSIGN
        message= StringConstants.EMAIL_SENT_LOGIN.format(settings.URL)
    elif type == Notification.LEAD_ACCEPT_REJECT:
        subject = StringConstants.LEAD_ACCEPT_REJECT
        message= StringConstants.LEAD_ASSIGN_MESSAGE.format(status)
    elif type == Notification.FORGOT_PASSWORD:
        subject = StringConstants.RESET_PASSWORD
        message= StringConstants.CHANGE_PASSWORD_URL_WITH_TOKEN.format(settings.URL,token)
    elif type == Notification.VERIFY_AGAIN_SENT_DETAILS:
        subject = StringConstants.VERIFY_AGAIN_SENT_DETAILS
        message= StringConstants.VERIFY_AGAIN_SENT_DETAILS_EMAIL_SENT_LOGIN.format(settings.URL,token)
    
    email_form = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject,message,email_form,recipient_list)
    if mobile_number is not None:
        VENDOR_OBJ = User.objects.get(mobile_number=mobile_number)
        Name = VENDOR_OBJ.name
        sms_message(mobile_number,type,status,Name,lead_name)
    return True


def sms_message(mobile_number=None,type=None,status=None,Name=None,lead_name=None):

    try:
        SMS_URL=settings.TWO_FA_SMS_URL
        SMS_API_KEY=settings.TWO_FA_SMS_API_KEY
        SMS_SERVICES_NAME=settings.TWO_FA_SMS_SERVICES_NAME
        SMS_BALANCE=settings.TWO_FA_SMS_BALANCE
        TRANSACTIONAL_SMS=settings.TWO_FA_TRANSACTIONAL_SMS
        SMS_URL = SystemConfigs.SMS_SENT_TO_MESSAGE.format(SMS_URL,SMS_API_KEY,SMS_SERVICES_NAME,SMS_BALANCE,TRANSACTIONAL_SMS)

        if type == Notification.LEAD_ASSIGN:
            payload = {
                StringConstants.FROM:settings.ENTSTY,
                StringConstants.TO:mobile_number,
                StringConstants.TEMPLATE_NAME:RequestConstants.LEAD_ASSIGN_TEMPLATE_NAME,
                StringConstants.VAR1:Name,
            }
        elif type == Notification.LEAD_ACCEPT_REJECT:
            payload = {
                StringConstants.FROM:settings.ENTSTY,
                StringConstants.TO:mobile_number,
                StringConstants.TEMPLATE_NAME:RequestConstants.LEAD_DECISION_TEMPLATE_NAME,
                StringConstants.VAR1:Name,
                StringConstants.VAR2:status,
                StringConstants.VAR3:lead_name+' ('+ mobile_number +')',
            }
        response = requests.request(RequestConstants.POST, SMS_URL, data=payload)
        return True
    except Exception as e:
        Logger.logError(StringConstants.LOG_ERROR_MESSAGE.format(str(e)))
        return False
