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
from sn1pebot.dupecite import *

class Bot():
    def __init__(self, site, username):
        self.site = site
        self.username = username

    def isRun(self, page=""):
        runpage = ""
        if page != "":
            runpage = pywikibot.Page(self.site, "User:" + self.username + "/Run/" + page + ".js")
        else:
            runpage = pywikibot.Page(self.site, "User:" + self.username + "/Run.js")

        if runpage.exists() and runpage.get() == "true":
            return True
        else:
            return False
