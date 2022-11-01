# py-scroll-phat
My collection of Python scripts that is utilizing Scroll pHAT

I have also created a post on how to kick start with Scroll pHAT at https://tomhudak.github.io/blog/2021-11-25-create-a-digital-clock-from-scratch-with-scroll-phat-and-raspberry-pi/

## clock.py

Displays scrolling text that shows the current time of the Raspberry Pi in HH:MM (24hr) format.

### Usage

```bash
python clock.py
```

For info on setup please check out my post linked above.

## weather.py

Displays a scrolling text that shows 
- the current temperature (in celsius) 
- pollution (pmi10)
- time (HH:MM format, 24hr)

### Setup OpenWeather API for temperature data

The temperature is from OpenWeather's [Current Weather API](https://openweathermap.org/api). To use that you need to [register](https://home.openweathermap.org/users/sign_up), and obtain an API key. Please make sure that this data is still available as a free tier before you register.

### Setup Air Quality API for pollution data

The pollution is obtained from World's Air Pollution: Real-time Air Quality Index. [https://waqi.info/](https://waqi.info/). It is using the API of [https://aqicn.org/api/](https://aqicn.org/api/), please follow the instructions here to obtain a data-token.

### Switches

- `--city <city name>` - **required**, the city to locate the weather info
- `--time <True|False>` - displays time
- `--idokep <True|False>` - Use idokep.hu for fetching temperature
- `--owkey <api key>` - OpenWeather API key (required for temperature display if --idokep is not True)
- `--aqikey <api key>` - Air Quality API key (required for pollution display)
- `--help` - Displays help for command line swiches

### Usage

```bash
python weather.py --city <city name> [--time] [--ow-key <api key>] [--aqi-key <api key>]
```

Example
```bash
python weather.py --time True --city Budapest --owkey 12345de2bdf12a123e456acc5a2c3dea --aqikey aff3ea0e8e12a34d2b9a9455bf3bcf1234f6da7a
```

### Further improvements
- Fahrenheit temperature
- 12h time format
- Error handling if API keys are wrong
- Error handling if the input city is nonexistent

## Contribution

Found a bug, or do you want to improve the above scripts? Feel free to contact me, open a PR or an issue!
