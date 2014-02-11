#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Sn1pebot
#
# TemplateData Function
#
# Extracts parameters from template definitions
# and generates basic TemplateData.
#
# Copyright (c) 2014 Geoffrey "GEOFBOT" Mon (User:Sn1per)
# Distributed under the MIT License
#
# Requires Pywikibot framework (core version)

import pywikibot
import re

class TemplateData():
    def __init__(self, bot):
        self.bot = bot        
    def run(self):
        print "Running TemplateData function"
    def extract(self, page):
        print "Extracting template parameters from page", page.title()
        self.text = page.get()
        self.start = [x.end() for x in re.finditer("{{{", self.text)]
        self.end = [x.start() for x in re.finditer("}}}", self.text)]
        for x in range(len(self.start)):
            yield str(self.text[self.start[x]:self.end[x]]).split('|', 2)
