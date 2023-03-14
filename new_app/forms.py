from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import DateInput

from new_app.models import Login, CustomerRegister, Stock


class DateInput(forms.DateInput):
    input_type = 'date'




class Login_Form(UserCreationForm):
    class Meta:
        model = Login
        fields = ("username","password1","password2")



class CustomerRegisterForm(forms.ModelForm):
    dob = forms.DateField(widget=DateInput)
    class Meta:
        model = CustomerRegister
        fields = '__all__'
        exclude = 'user',



class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = '__all__'