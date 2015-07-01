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
import HTMLParser
import xml.etree.ElementTree as ET

h = HTMLParser.HTMLParser()

class TemplateData():
    def __init__(self, bot):
        self.bot = bot        
    def run(self):
        print "Running TemplateData function"
    def extract(self, page):
        print "Extracting template parameters from page", page.title()
        self.parsetext = pywikibot.data.api.Request(site=pywikibot.getSite(), action="parse", page=page.title(), prop=[], generatexml=True, format="json").submit()["parse"]["parsetree"]['*']
        self.tree = ET.fromstring(self.parsetext)
#        for arg in self.dom.getElementsByTagName("tplarg"):
#            print arg
        print self.parsetext
        print self.tree
        print len(self.tree)
        for item in self.tree:
            print item.text
            yield h.unescape(item.text)
#if item.tag == "tplarg":
            #    print "yoloswag"
            #    print item.text
            #    yield h.unescape(item.text.strip())
                #yield [h.unescape(self.title.text), h.unescape(''.join([str(self.defval.text)] + [xml.tostring(c) for c in self.defval.getchildren()]))]
        #print self.title, self.defval
        #print self.title.text, self.defval.text
        # self.start = [x.end() for x in re.finditer("{{{", self.text)]
        # self.end = [x.start() for x in re.finditer("}}}", self.text)]
        # for x in range(len(self.start)):
        #     yield str(self.text[self.start[x]:self.end[x]]).split('|', 2)
