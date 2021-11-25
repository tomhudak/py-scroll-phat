#!/usr/bin/env python

import argparse
import requests
import sys
import time

import scrollphat


parser = argparse.ArgumentParser()
parser.add_argument('--time', type=bool, help='If enabled, shows time in 24hr HH:MM format', required=True)
parser.add_argument('--city', type=str, help='Name of the city to get weather data from', required=True)
parser.add_argument('--owkey', type=str, help='OpenWeather API key')
parser.add_argument('--aqikey', type=str, help='Air Quality Index API key')
args = parser.parse_args()

if not(args.owkey or args.aqikey):
    parser.error('You need to specify at least one API key to show weather data')

print('Scroll pHAT - Weather started...Press Ctrl+C to exit!')

refresh_interval = 300

scrollphat.set_brightness(1)

def get_temp():
    if not (args.owkey):
        return ''

    openWeatherApiUrl = 'https://api.openweathermap.org/data/2.5/weather'
    urlParams = {
        'q': args.city,
        'appid': args.owkey,
        'units': "metric",
    }
    try:
        r = requests.get(url = openWeatherApiUrl, params = urlParams)
        data = r.json()
    except Exception:
        return ''

    temp = data['main']['temp']
    return str(int(round(temp, 0))) + chr(248) + "C"
  
def get_pollution():
    if not (args.aqikey):
        return ''

    waqiApiUrl = 'https://api.waqi.info/feed/' + args.city + '/'
    urlParams = {
        'token': args.aqikey,
    }
    try:
        r = requests.get(url = waqiApiUrl, params = urlParams)
        data = r.json()
    except Exception:
        return ''

    pollution = data['data']['iaqi']['pm10']['v']
    return "pm" + str(pollution)

def get_time(current_time):
    if not (args.time):
        return ''
    return time.strftime('%H:%M', time.localtime(current_time))

def scroll_once(text):
    text = str(text)
    scrollphat.write_string(text, 11)
    length = scrollphat.buffer_len()
    for i in range(length):
        scrollphat.scroll()
    	time.sleep(0.1)
#    scrollphat.clear()



#init before first loop
current_time = time.time()
next_get_time = 0


# Temperature degree char needed to be defined separately
scrollphat.font[248] = [3, 3]

while True:
    try:
        if(current_time > next_get_time):
            temperature = get_temp();
            pollution = get_pollution();
            next_get_time = time.time() + refresh_interval;
            #print(time.strftime('%H:%M:%S', time.localtime(next_get_time)))

        current_time = time.time()
        timestr = get_time(current_time)
            
        scroll_once(temperature + ' ' + pollution + ' ' + timestr) 
        time.sleep(0.12)

    except KeyboardInterrupt:
        scrollphat.clear()
        sys.exit(-1)