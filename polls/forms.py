from django import forms
from polls.models import PollingUnit,AnnouncedPuResults


class PollingUnitForm(forms.ModelForm):
    class Meta:
        model = PollingUnit
        fields = ['polling_unit_id','ward_id','lga_id','uniquewardid','polling_unit_number','polling_unit_name','polling_unit_description','lat','long','entered_by_user','date_entered','user_ip_address']
        
class PollingUnitResultForm(forms.ModelForm):
    class Meta:
        model = AnnouncedPuResults
        fields = ['polling_unit_uniqueid','party_abbreviation','party_score','entered_by_user','date_entered','user_ip_address']
        