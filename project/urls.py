#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('apps.line.urls')),
    path('admin/', admin.site.urls),
]
