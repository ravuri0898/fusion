from django import forms
from django.shortcuts import get_object_or_404

from fusion.models import *


LEAVE_TYPE = (
    ('CL', 'Casual Leave'),
    ('COL', 'Commuted Leave'),
    ('EL', 'Earned Leave'),
    ('RH', 'Restricted Holiday'),
    ('SCL', 'Special Casual Leave'),
    ('VL', 'Vacation Leave'),
)


class LoginForm(forms.Form):
    lf_UserEmail = forms.EmailField(max_length=50, widget=forms.TextInput(attrs={'type': 'email', 'placeholder': 'employee@iiitdmj.ac.in'}))
    lf_UserPassword = forms.CharField(widget=forms.TextInput(attrs={'type': 'password', 'placeholder': 'Password'}))

    def clean_message(self):
        useremail = self.cleaned_data.get('lf_UserEmail')
        userpassword = self.cleaned_data.get('lf_UserPassword')
        dbUser = get_object_or_404(Employee, empEmail=useremail, empPassword=userpassword)

        print(dbUser.pk)

        if not dbUser.pk:
            raise forms.ValidationError('The Username or Password is Incorrect!')

        return dbUser


class LeaveApplicationForm(forms.Form):
    laf_LeaveType = forms.Select(choices=LEAVE_TYPE)

