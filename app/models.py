from datetime import datetime
from pyexpat import model
from django.conf import settings

from django.contrib.auth.models import AbstractUser
from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(default=datetime.now)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    updated_at = models.DateTimeField(default=datetime.now)
    updated_by = models.CharField(max_length=10, null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted_by = models.CharField(max_length=10, null=True, blank=True)

Role = (
    ("ADMIN", "ADMIN"),
    ("VENDOR", "VENDOR"),
    ("CUSTOMER", "CUSTOMER")
)

STATUS = (
    ("ACTIVE", "ACTIVE"),
    ("DISABLE", "DISABLE")
)

# Create your models here.
class User(AbstractUser,BaseModel):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100,blank=True, null=True)
    role = models.CharField(max_length=10, choices=Role, default='VENDOR')
    email = models.EmailField(blank=False, null=False, unique=True)
    address = models.CharField(max_length=255,blank=True, null=True)
    country = models.CharField(max_length=50,blank=True, null=True)
    state = models.CharField(max_length=50,blank=True, null=True)
    city = models.CharField(max_length=50,blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    mobile_number = models.CharField(max_length=15, unique=True, blank=True, null=True)
    category = models.CharField(max_length=10, blank=True, null=True)
    catering = models.CharField(max_length=10, blank=True, null=True)
    max_capacity = models.CharField(max_length=10, blank=True, null=True)
    number_of_events = models.CharField(max_length=10, blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS, default='ACTIVE')
    is_verify = models.CharField(max_length=250,blank=True, null=True)


    def __str__(self):
        return "{}-{}-{}".format(self.name, self.email, self.role)

    def get_data(self):
        return {
            "id":self.id,
            "name":self.name,
            "password":self.password,
            "role":self.role,
            "email":self.email,
            "address":self.address,
            "country":self.country,
            "state":self.state,
            "city":self.city,
            "description":self.description,
            "mobile_number":self.mobile_number,
            "category":self.category,
            "catering":self.catering,
            "max_capacity":self.max_capacity,
            "number_of_events":self.number_of_events,
            "status":self.status,
        }


class Media(BaseModel):
    userID = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    url = models.CharField(max_length=255)
    size = models.IntegerField(default=0)

    def __str__(self):
        return self.url


LEAD_STATUS = (
    ("1", "Accepted"),
    ("2", "Rejected"),
    ("3", "New"),
    ("4", "Called and research in progress"),
    ("5", "Called and customer declined services"),
    ("6", "Customer didn't respond"),
    ("7", "Quote sent"),
    ("8", "Event finalized"),
    ("9", "Advance received"),
    ("10", "Event completed"),
    ("11", "Invoice paid in full"),
    ("12", "Closed"),
    ("13", "Unassign"),
)

class Lead(BaseModel):
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField(blank=False, null=False)
    description = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=50,blank=True, null=True)
    state = models.CharField(max_length=50,blank=True, null=True)
    city = models.CharField(max_length=50,blank=True, null=True)
    vendor_count = models.IntegerField(default=0)
    date_of_event = models.DateField(settings.DATE_INPUT_FORMATS, blank=True, null=True)
    time_of_event = models.TimeField(settings.TIME_INPUT_FORMATS, blank=True, null=True)

    def get_data(self):
        return {
            "id":self.id,
            "name":self.name,
            "mobile_number":self.mobile_number,
            "email":self.email,
            "description":self.description,
            "address":self.address,
            "country":self.country,
            "state":self.state,
            "city":self.city,
        }


LOOKUP_TYPE = (
    ("category", "Category"),
    ("catering", "Catering"),
    ("max_capacity", "Max Capacity"),
    ("number_of_events", "Number of Events"),
    ("lead_status", "Lead Status")
)

class Lookup(BaseModel):
    type = models.CharField(max_length=100, choices=LOOKUP_TYPE, blank=True, null=True)
    value = models.CharField(max_length=100, blank=True, null=True)
    numeric_value = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return "{}-{}-{}".format(self.id,self.type, self.value)

    class Meta:
        db_table = 'app_lookup'
    
    def get_data(self):
        return {
            "type":self.type,
            "value":self.value,
            "numeric_value":self.numeric_value,
        }

class Lead_Assign(BaseModel):
    vendorID = models.ForeignKey(User,related_name='vendorID', on_delete=models.CASCADE, blank=True, null=True)
    leadID = models.ForeignKey(Lead, on_delete=models.CASCADE, blank=True, null=True)
    lead_status=models.ForeignKey(Lookup, on_delete=models.CASCADE, blank=True, null=True)
    last_status_updated_time=models.DateTimeField(default=datetime.now)
    last_comments = models.CharField(max_length=200, blank=True, null=True)

    def get_data(self):
        return {
            "vendorID":self.vendorID.get_data(),
            "leadID":self.leadID.get_data(),
            "lead_status":self.lead_status.get_data(),
            "last_status_updated_time":self.last_status_updated_time,
            "last_comments":self.last_comments,
        }

class Lead_Comment(BaseModel):
    leadID = models.ForeignKey(Lead, on_delete=models.CASCADE, blank=True, null=True)
    leadAssignedId = models.ForeignKey(Lead_Assign, on_delete=models.CASCADE, blank=True, null=True)
    vendorID = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    status=models.ForeignKey(Lookup, on_delete=models.CASCADE, blank=True, null=True)
    comments = models.CharField(max_length=200, blank=True, null=True)
    datetime=models.DateTimeField(default=datetime.now)

    def __str__(self):
        return "{}-{}-{}".format(self.leadID, self.leadAssignedId, self.vendorID)

class Verification_Token(BaseModel):
    vendorID = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=100)

    def __str__(self):
        return self.email.email

