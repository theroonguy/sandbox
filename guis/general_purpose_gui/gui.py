from tkinter import *
import requests
        
def get_weather():
    output=wplace.get()
    output.strip(' ')
    
    url = 'http://api.openweathermap.org/data/2.5/weather?q={},us&appid=ac7c75b9937a495021393024d0a90c44'.format(output)
    res = requests.get(url)
    data = res.json()

    try:
        temp = data['main']['temp']
        tempF = round(((temp - 273.15) * 9/5 + 32),2)
        wind_speed = data['wind']['speed']
        description = data['weather'][0]['description']
        name = data['name']
        
        ftemp = 'Temperature: {} Degrees Fahrenheit'.format(tempF)
        fwind = 'Wind Speed: {} m/s'.format(wind_speed)
        fdesc = 'Description: {}'.format(description)
        
        label=Label(sidebar, text='Weather in {}: \n{}\n{}\n{}'.format(name, ftemp, fwind, fdesc, bg='light grey', fg='blue'), font=('Consolas',10))
        label.grid(row=2)
    except:
        Label(sidebar, text='Error').grid(row=2)
      
root=Tk()

root.geometry('1000x300')

topframe=Frame(root)
topframe.pack(fill=X)
sidebar=Frame(root, bd=1, relief=SUNKEN)
sidebar.pack(side=RIGHT, fill=Y)
midbar=Frame(root)
midbar.pack()

title = Label(topframe, text='GENERAL PURPOSE GUI', font = ('Consolas',30), fg='purple')
title.pack(fill=X)

Label(sidebar, text='WEATHER', font=('Consolas', 15), fg='blue').grid(row=0)
wplace=Entry(sidebar, width=10)
wplace.grid(row=1, column=0)
wenter=Button(sidebar, text='Enter', command=get_weather)
wenter.grid(row=1, column=1)

mainloop()
