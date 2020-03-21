#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from apps.line.utils import LineApi
from project import settings

line_api = LineApi()

@csrf_exempt
def callback(request):
    auth_info = line_api.execute_auth()
    
    token = auth_info['access_token']
    token_type = auth_info['token_type']

    request_body = json.loads(request.body)
    to = ""
    messages = ""
    try:
        to = request_body['events'][0]['source']['UserId']
        messages = request_body['events'][0]['message']['text']
    except:
        to = settings.MY_USER_ID
        messages = "error"
    pm_result = line_api.execute_push_message(token_type=token_type, token=token, to=to, messages=messages)

    display_data = {
        "res1": auth_info,
        "res2": pm_result,
        "request": messages
    }

    return render(request, 'line/index.html', {'res': display_data})
