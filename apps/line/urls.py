#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path

from apps.line.views import post_auth

urlpatterns = [
    path(r'postauth/', post_auth, name='post_auth'),
]
