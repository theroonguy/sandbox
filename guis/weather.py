from tkinter import *
import requests
import re


root=Tk()

url = 'http://iphone.halalfire.com/bot_prayerspace.php?l={}&uuid=1&key=O2A8Uo5ACzEXW7NnPYPX'.format('austin')
res = requests.get(url)
data = res.json()
    
status_text = data['data']['status_text']
photo = data['data']['photo_url']
name = data['data']['name']
placetype = data['data']['type']
address = data['data']['address']
city = data['data']['city']
state = data['data']['state']
zipcode = data['data']['zip']
phone = data['data']['phone']
distance = data['data']['distance']
desc = data['data']['desc']
zabihah_url = data['data']['url']
    

topframe=Frame(root)
topframe.pack()

state = Label(topframe, text=state, fg='blue')
city = Label(topframe, text=city, fg='blue')
distance = Label(topframe, text=distance, fg='blue')

state.grid(row=0)
city.grid(row=1)
distance.grid(row=2)

