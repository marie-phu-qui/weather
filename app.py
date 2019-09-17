import requests
import datetime

def get_woeid(city):
    woeid = requests.get('https://www.metaweather.com/api/location/search/?query='+str(city)).json()[0]['woeid']
    return woeid

def print_meteo(city):
    woeid = get_woeid(city)
    # today = datetime
    print(requests.get('https://www.metaweather.com/api/location/'+str(woeid)+'/2019/9/17').json()[0])

print_meteo('wellington')