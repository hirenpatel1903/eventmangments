from pkgutil import get_data
from django.contrib import admin
from app.models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Lead)
admin.site.register(Media)
admin.site.register(Lookup)
admin.site.register(Lead_Assign)
admin.site.register(Verification_Token)
admin.site.register(Lead_Comment)