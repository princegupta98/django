from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        # fields = '__all__'
        fields = (
            "f_name",
            "l_name",
            "photo",
            "designation",
            "email_address",
            "phone_number"
        )
        labels = {
            'f_name':'First Name',
            'l_name':'Last Name',
            "designation": "Position",
            "email_address":"Email",
            "phone_number":"Phone",
        }

    def __init__(self, *args, **kwargs):    
        super(EmployeeForm, self).__init__(*args, **kwargs)
