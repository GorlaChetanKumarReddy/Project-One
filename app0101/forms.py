from django import forms
from app0101.models import new_shedule_class_model,user_register

class shedule_classess(forms.ModelForm):
    date = forms.DateField(widget=forms.SelectDateWidget)
    time = forms.CharField(widget=forms.TimeInput)
    class Meta:
        model = new_shedule_class_model
        fields = '__all__'

class user_register_form(forms.ModelForm):
    Password = forms.CharField(widget=forms.PasswordInput,min_length=8)
    Contact_No = forms.IntegerField(min_value=1111111111)
    class Meta:
        model = user_register
        fields = '__all__'