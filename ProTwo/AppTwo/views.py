# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from AppTwo.forms import NewUserForm


# Create your views here.
#
def index(request):
    return render(request,'AppTwo/index.html')

def users(request):

    form = NewUserForm()

    if request.method == "POST":

        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

        else:
            print('ERROR FORM Invalid')

    return render(request,'AppTwo/users.html',{'form':form})
