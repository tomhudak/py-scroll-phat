#!/usr/bin/env python

import sys
import time

import scrollphat


print("""
Scroll pHAT - Scrolling Clock
Press Ctrl+C to exit!
""")

scrollphat.set_brightness(1)

while True:
    try:
	    current = time.strftime('%H:%M')
	    scrollphat.write_string(current, 11)
        scrollphat.scroll()
        time.sleep(0.2)
    except KeyboardInterrupt:
        scrollphat.clear()
        sys.exit(-1)
