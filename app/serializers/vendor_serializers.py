from rest_framework import serializers
from app.models import User, Lead, Lead_Assign, Lookup

class GetVendorSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class GetLeadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lead
        fields = '__all__'

class GetLookupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lookup
        fields = '__all__'

class GetLeadAssignSerializer(serializers.ModelSerializer):
    vendorID = GetVendorSerializer(read_only=True)
    leadID = GetLeadSerializer(read_only=True)
    lead_status = GetLookupSerializer(read_only=True)

    class Meta:
        model = Lead_Assign
        fields = ['id', 'vendorID', 'leadID', 'lead_status', 'last_comments']
