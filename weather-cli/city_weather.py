#!/usr/bin/env python
# -*- encoding: utf8 -*-
import argparse
import requests
from datetime import date

METAWEATHER_API_URL = "https://www.metaweather.com/api"


class MetaweatherApiUnreachableException(Exception):
    pass


class LocationUnknownException(Exception):
    pass


def fetch_location_woeid(city):
    location_search = requests.get("{api_url}/location/search/?query={city}".format(api_url=METAWEATHER_API_URL, city=city))
    if location_search.ok:
        locations = location_search.json()
        if len(locations) > 0:
            return locations[0]['woeid']
        else:
            raise LocationUnknownException
    raise MetaweatherApiUnreachableException


def fetch_today_weather(woeid):
    weather_request = requests.get("{api_url}/location/{woeid}/{date}".format(api_url=METAWEATHER_API_URL, woeid=woeid, date=date.today().strftime("%Y/%m/%d")))
    if weather_request.ok:
        return weather_request.json()
    raise MetaweatherApiUnreachableException


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Is tomorrow rainy?')
    parser.add_argument('city', nargs=1)
    args = parser.parse_args()
    city = args.city[0]
    woeid = fetch_location_woeid(city)
    weather = fetch_today_weather(woeid)
    from pprint import pprint
    pprint(weather)
    if any(w['weather_state_abbr'] in ['lr', 'hr', 's'] for w in weather):
        print("It will or had already rained today!")
    else:
        print("Weather is clear today")
