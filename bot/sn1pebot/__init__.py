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

class Bot():
    def __init__(self, site, username):
        self.site = site
        self.username = username

    def isRun(self, page=""):
        if page != "":
            if eval(pywikibot.Page(self.site, "User:" + self.username + "/Run/" + page).get()):
                return True
            else:
                return False
        else:
            if eval(pywikibot.Page(self.site, "User:" + self.username + "/Run").get()):
                return True
            else:
                return False
