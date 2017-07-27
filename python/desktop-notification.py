#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Simplest notification solution for Mac and Linux desktop.
# May not be the best way in production as theres many ways to go about it with
# other libraries.

import sys
import os
import subprocess

def notify(title, text):

    if sys.platform == "linux" or sys.platform == "linux2":
        linux_notify(title, text)

    elif sys.platform == "darwin":
        mac_notify(title, text)

    else:
        print("NOTIFICATION: " + title)
        print(text)

def mac_notify(title, text):
    os.system("""osascript -e 'display notification "{}" with title "{}"'""".format(text, title))

def linux_notify(title, text):
    subprocess.Popen(['notify-send', title + text])


notify("Hello", "Heres an alert")
