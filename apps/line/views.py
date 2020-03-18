#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from django.shortcuts import render
from apps.line.utils import LineApi

line_api = LineApi()

def callback(request):
    auth_info = line_api.execute_auth()
    
    token = auth_info['access_token']
    token_type = auth_info['token_type']

    to = "U50b1954cd81f2c346c2b501c7140e0a7"
    messages = "これってダメじゃね？"
    pm_result = line_api.execute_push_message(token_type=token_type, token=token, to=to, messages=messages)

    display_data = {
        "res1": auth_info,
        "res2": pm_result
    }

    return render(request, 'line/index.html', {'res': display_data})
