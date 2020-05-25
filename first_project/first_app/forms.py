from django import forms
from django.contrib.admin.widgets import AdminDateWidget
import datetime
from .models import ShareDetails

class Form_Stock_Details(forms.ModelForm):
    company_name = forms.CharField(required=True,label='Company Name')
    date_bought = forms.DateField(initial=datetime.date.today,required=True,widget=AdminDateWidget,label='Date Bought')
    share_price = forms.FloatField(required=True,label='Share Price')
    shares_bought = forms.IntegerField(required=True,label='Quantity')

    class Meta:
        model = ShareDetails
        fields = ['company_name','date_bought','share_price','shares_bought']