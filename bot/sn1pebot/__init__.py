#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Sn1pebot
#
# Initialization
#
# Sn1pebot Module Initialization
#
# Copyright (c) 2014 Geoffrey "GEOFBOT" Mon (User:Sn1per)
# Distributed under the MIT License
#
# Requires Pywikibot framework (core version)

import pywikibot

from sn1pebot.templatedata import *

class Bot():
    def __init__(self, site, username):
        self.site = site
        self.username = username

    def isRun(self, page=""):
        if page != "":
            if pywikibot.Page(self.site, "User:" + self.username + "/Run/" + page + ".js").get() == "true":
                return True
            else:
                return False
        else:
            if pywikibot.Page(self.site, "User:" + self.username + "/Run.js").get() == "true":
                return True
            else:
                return False
