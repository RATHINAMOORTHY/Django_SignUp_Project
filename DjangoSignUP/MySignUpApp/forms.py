from django import forms
from MySignUpApp import models
class UsersModelForm(forms.ModelForm):
    class Meta():
        model = models.UsersModel
        fields = '__all__'
