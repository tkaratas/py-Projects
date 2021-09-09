"""Notify Germany and Turkey Covid Datas"""
from notifypy import Notify
import requests
import datetime

covidDataTurkey = None
covidDataGermany = None
notification = Notify()

try:
    covidDataTurkey = requests.get(
        'https://corona-rest-api.herokuapp.com/Api/turkey')
    covidDataGermany = requests.get(
        'https://corona-rest-api.herokuapp.com/Api/germany')
except:
    print("No connection. Check your internet connection or try it again.")


def covidNotificationDE(title):
    data = covidDataGermany.json()['Success']
    notification.title = title
    notification.message = "Total Cases: {totalcases}\nToday Cases: {todaycases}\nToday Deaths: {todaydeaths}\nRecovered: {recovered}\nActive: {active}".format(
        totalcases=data['cases'], todaycases=data['todayCases'], todaydeaths=data['todayDeaths'], recovered=data['recovered'], active=data['active'])
    notification.icon = "C:/Users/karat/Desktop/covid.jpg"
    notification.send()


def covidNotificationTR(title):
    data = covidDataTurkey.json()['Success']
    notification.title = title
    notification.message = "Total Cases: {totalcases}\nToday Cases: {todaycases}\nToday Deaths: {todaydeaths}\nRecovered: {recovered}\nActive: {active}".format(
        totalcases=data['cases'], todaycases=data['todayCases'], todaydeaths=data['todayDeaths'], recovered=data['recovered'], active=data['active'])
    notification.icon = "C:/Users/karat/Desktop/covid.jpg"
    notification.send()


# while True:
if (covidDataGermany != None):
    today = datetime.date.today()
    title = "Covid Mitteilung am {}".format(today)
    covidNotificationDE(title)

if (covidDataTurkey != None):
    now = datetime.date.today()
    title = "Covid Bildirimi {}".format(today)
    covidNotificationTR(title)

# time.sleep(60*60*24)
