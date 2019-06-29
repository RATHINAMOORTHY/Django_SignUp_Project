from django.shortcuts import render
from MySignUpApp import forms
from MySignUpApp import models
def index(request):
    return render(request,'index.html')
# Create your views here.
def register(request):
    form = forms.UsersModelForm
    if request.method == 'POST':
        form = forms.UsersModelForm(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
        else:
            print('Please try again')
    return render(request,'register.html',{'form':form})
