#!/usr/bin/env python

import sys
import time

import scrollphat

print("""
Scroll pHAT - Scrolling Text

Press Ctrl+C to exit!

""")

scrollphat.set_brightness(1)
scrollphat.write_string('weather script is going to be uploaded soon', 11)
scrollphat.scroll()
