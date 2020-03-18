#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from django.shortcuts import render
from apps.line.utils import LineApi

line_api = LineApi()

def post_auth(request):
    content = line_api.execute_auth()
    return render(request, 'line/index.html', {'res': content})
