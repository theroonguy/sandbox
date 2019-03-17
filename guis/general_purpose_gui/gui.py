from tkinter import *
import requests

root=Tk()

topframe=Frame(root)
topframe.pack(fill=X)
sidebar=Frame(root)
sidebar.pack(side=RIGHT, fill=Y)

title = Label(topframe, text='GENERAL PURPOSE GUI')
title.pack(fill=X)

sidebar = Label(sidebar, text='Sidebar')
sidebar.pack(fill=Y)

output = 'austin'

url = 'http://api.openweathermap.org/data/2.5/weather?q={},us&appid=ac7c75b9937a495021393024d0a90c44'.format(output)
res = requests.get(url)
data = res.json()

temp = data['main']['temp']
tempF = round(((data['main']['temp'] - 273.15) * 9/5 + 32),2)
wind_speed = data['wind']['speed']
description = data['weather'][0]['description']
name = data['name']
main = data['weather']['main']

ftemp = 'Temperature: {} Degrees Fahrenheit'.format(tempF)
fwind = 'Wind Speed: {} m/s'.format(wind_speed)
fdesc = 'Description: {}'.format(description)

print(ftemp)
mainloop()
