from django import forms
import datetime
from .models import ShareDetails

class Form_Stock_Details(forms.ModelForm):
    # Company_Name = forms.CharField(required=True)
    # Date_Bought = forms.DateField(initial=datetime.date.today,required=True)
    # Share_Price = forms.FloatField(required=True)
    # Shares_Bought = forms.IntegerField(required=True)

    class Meta:
        model = ShareDetails
        fields = "__all__"