from tkinter import *
import requests

def init():
    root=Tk()

    topframe=Frame(root)
    topframe.pack(fill=X)
    sidebar=Frame(root)
    sidebar.pack(side=RIGHT, fill=Y)
    
    title = Label(topframe, text='GENERAL PURPOSE GUI', fg='purple')
    title.pack(fill=X)
    
    sidebar = Label(sidebar, text='{}\n{}\n{}'.format(get_weather()[0], get_weather()[1], get_weather()[2]), bg='light grey', fg='purple')
    sidebar.pack(fill=Y)

    print(get_weather()[0])
    
def get_weather():
    output = 'austin'
    
    url = 'http://api.openweathermap.org/data/2.5/weather?q={},us&appid=ac7c75b9937a495021393024d0a90c44'.format(output)
    res = requests.get(url)
    data = res.json()
    
    temp = data['main']['temp']
    tempF = round(((temp - 273.15) * 9/5 + 32),2)
    wind_speed = data['wind']['speed']
    description = data['weather'][0]['description']
    name = data['name']
    
    ftemp = 'Temperature: {} Degrees Fahrenheit'.format(tempF)
    fwind = 'Wind Speed: {} m/s'.format(wind_speed)
    fdesc = 'Description: {}'.format(description)
    
    return ftemp, fwind, fdesc

init()

mainloop()
