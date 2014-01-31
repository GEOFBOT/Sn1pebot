#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Sn1pebot
#
# Command Center
#
# The brain of Sn1pebot.  Runs the various functions.
#
# Copyright (c) 2014 Geoffrey "GEOFBOT" Mon (User:Sn1per)
# Distributed under the MIT License
#
# Requires Pywikibot framework (core version)

import pywikibot
import sn1pebot

# Bootup
print "==================Sn1pebot=================="
print "(c) 2014 Geoffrey \"GEOFBOT\" Mon (User:Sn1per)"
print "Distributed under the MIT License"
print
print "Command Center initializing..."

bot = sn1pebot.Bot(pywikibot.getSite(), "Sn1pebot")

# Action
print "Scanning task pages to check for work..."

#func = bot.checkFunc(["TemplateData"])

print "Run bot: " + str(bot.isRun())

print "Activating TemplateData function..."
# Shutdown sequence
print "Sn1pebot shutting down..."
