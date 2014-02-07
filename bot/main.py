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

# Bootup with fancy ASCII art
print
print "  /$$$$$$              /$$                       /$$                   /$$    "
print " /$$__  $$           /$$$$                      | $$                  | $$    "
print "| $$  \__/ /$$$$$$$ |_  $$    /$$$$$$   /$$$$$$ | $$$$$$$   /$$$$$$  /$$$$$$  "
print "|  $$$$$$ | $$__  $$  | $$   /$$__  $$ /$$__  $$| $$__  $$ /$$__  $$|_  $$_/  "
print " \____  $$| $$  \ $$  | $$  | $$  \ $$| $$$$$$$$| $$  \ $$| $$  \ $$  | $$    "
print " /$$  \ $$| $$  | $$  | $$  | $$  | $$| $$_____/| $$  | $$| $$  | $$  | $$ /$$"
print "|  $$$$$$/| $$  | $$ /$$$$$$| $$$$$$$/|  $$$$$$$| $$$$$$$/|  $$$$$$/  |  $$$$/"
print " \______/ |__/  |__/|______/| $$____/  \_______/|_______/  \______/    \___/  "
print "                            | $$                                              "
print "                            | $$                                              "
print "                            |__/                                              "
print 
print "=============================================================================="
print "=============================================================================="
print
print "(c) 2014 Geoffrey \"GEOFBOT\" Mon (User:Sn1per)"
print "Distributed under the MIT License"
print
print "Command Center initializing..."
print

bot = sn1pebot.Bot(pywikibot.getSite(), "Sn1pebot")
td = sn1pebot.TemplateData(bot)


# Action
print "Scanning task pages to check for work..."

#func = bot.checkFunc(["TemplateData"])

run = [bot.isRun(), bot.isRun("TemplateData")]

print
print "Run bot: " + str(run[0])

if run[0]:
    print "- TemplateData: " + str(run[1])
    if run[1]:
        print
        td.run()
else:
    print "Bot disabled, quitting..."

# Shutdown sequence
print
print "Sn1pebot shutting down..."
