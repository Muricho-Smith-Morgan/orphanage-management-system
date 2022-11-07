from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Help
from django import forms


class SignUpForm(UserCreationForm):
    class Meta:
      model = User
      fields = ('username', 'password1', 'password2')
      


class EditForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'type': 'email'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'type': 'tel'}))
    help_offered = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}))
     
    
    
    class Meta:
        model = Help
        fields = '__all__'

class EditCaseInfoForm(forms.ModelForm):
  
    name = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'type': 'email'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'type': 'tel'}))
    help_offered = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}))
     
    class Meta:
        model = Help
        fields = '__all__'