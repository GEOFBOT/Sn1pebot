#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Sn1pebot
#
# Duplicate Citation removal
#
# Checks and fixes duplicate citations
#
# Copyright (c) 2014 Geoffrey "GEOFBOT" Mon (User:Sn1per)
# Distributed under the MIT License
#
# Requires Pywikibot framework (core version)

import pywikibot
import mwparserfromhell as mwph

class DupeCite():
    def __init__(self, bot):
        self.bot = bot        
    def run(self):
        print("Running DupeCite function")
    def getRefs(self, page):
        print("Extracting refs from page", page.title())
        self.text = mwph.parse(page.get())
        for tag in self.text.filter_tags():
            if tag.tag == 'ref':
                yield tag
    def sortRefs(self, page):
        print("Sorting refs from page", page.title())
        refs = []
        rawRefs = list(self.getRefs(page))
        for rawRef in rawRefs:
            refDict = {}
            name = ""
            content = rawRef.contents
            for attr in rawRef.attributes:
                if attr.name == "name":
                    name = attr.value
                    break
            refDict["name"] = name
            refDict["content"] = content
            refs.append(refDict);
        return refs
        
