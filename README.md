# scroll-phat-examples
My collection of scripts that is utilizing Scroll pHAT

I have also created a post on how to kick start with Scroll pHAT on https://tomhudak.github.io/

## clock.py

Displays scrolling text that shows the current time of the Raspberry Pi in HH:MM (24hr) format.

### Usage

```bash
python clock.py
```

For info on setup please check out my post linked above.

## weather.py
**Going to be uploaded soon.**

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
- `--time` - displays time if provided
- `--ow-key <api key>` - OpenWeather API key (required for temperature display)
- `--aqi-key <api key>` - Air Quality API key (required for pollution display)
- `--help` - Displays help for command line swiches

### Usage

```bash
python weather.py --city <city name> [--time] [--ow-key <api key>] [--aqi-key <api key>]
```

### Contribution

Found a bug, or are you extending this? Feel free to contatct me, open a PR or an issue!