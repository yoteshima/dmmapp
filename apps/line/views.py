#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from django.shortcuts import render
from apps.line.utils import LineApi

line_api = LineApi()

def callback(request):
    content = line_api.execute_auth()
    
    token = content['access_token']
    token_type = content['token_type']

    to = "U50b1954cd81f2c346c2b501c7140e0a7"
    messages = "これってダメじゃね？"
    res  = line_api.execute_push_message(token_type=token_type, token=token, to=to, messages=messages)

    return render(request, 'line/index.html', {'res': res})
