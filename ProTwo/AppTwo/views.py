# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from AppTwo.models import User


# Create your views here.
#
def index(request):
    return render(request,'AppTwo/index.html')
def users(request):
    user_list=User.objects.order_by('first_name')
    user_dict ={'users':user_list}

    return render(request,'AppTwo/users.html',context=user_dict)
