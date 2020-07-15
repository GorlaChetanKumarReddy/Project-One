from django import forms
from app0101.models import new_shedule_class_model

class shedule_classess(forms.ModelForm):
    date = forms.DateField(widget=forms.SelectDateWidget)
    time = forms.CharField(widget=forms.TimeInput)
    class Meta:
        model = new_shedule_class_model
        fields = '__all__'