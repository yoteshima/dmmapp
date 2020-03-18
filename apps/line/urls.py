#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path

from apps.line.views import callback

urlpatterns = [
    path(r'callback/', callback, name='callback'),
]
