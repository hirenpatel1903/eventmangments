import base64
from app.constants import RequestConstants

def is_login(uid):
    if uid == "":
        return False
    else:
        return True


def format_json(data, code, message):
    if data == {}:
        data = None
    return dict(code=code, message=message, data=data)


def validate_phone(phone):
    if 9 < len(phone) < 15:
        return True
    else:
        return False


def clearSessionFlashMessages(request):
    SESSION_DATA = {}
    if RequestConstants.FLASH_SUCCESS_MSG in request.session:
        SESSION_DATA[RequestConstants.FLASH_SUCCESS_MSG] = request.session[RequestConstants.FLASH_SUCCESS_MSG]
        request.session[RequestConstants.FLASH_SUCCESS_MSG] = ""
    if RequestConstants.FLASH_ERROR_MSG in request.session:
        SESSION_DATA[RequestConstants.FLASH_ERROR_MSG] = request.session[RequestConstants.FLASH_ERROR_MSG]
        request.session[RequestConstants.FLASH_ERROR_MSG] = ""

    return SESSION_DATA


def filter_data(data):
    try:
        data._mutable = True
        del data["csrfmiddlewaretoken"]
    except:
        pass

    data = dict(data)

    filtered_data = {}

    for key, val in data.items():
        filtered_data[key] = val[0]

    return filtered_data

def convert_base_64(input_data):
    return base64.b64encode(str(input_data).encode('utf-8'))

def decode_base_64(input_data):
    try:
        return base64.b64decode(input_data).decode()
    except Exception as e:
        return ""