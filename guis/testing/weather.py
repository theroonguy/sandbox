from tkinter import *
import requests
import re


root=Tk()

topframe = Frame(root)
topframe.pack(side=TOP)
bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)

def place(place):

    url = 'http://iphone.halalfire.com/bot_prayerspace.php?l={}&uuid=1&key=O2A8Uo5ACzEXW7NnPYPX'.format(place)
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

    state = Label(root, text=state, fg='blue')
    city = Label(root, text=city, fg='blue')
    distance = Label(root, text=distance, fg='blue')
    
    state.grid(row=0)
    city.grid(row=1)
    distance.grid(row=2)

austin_button = Button(topframe, text='Austin', command=place('austin'))

austin_button.grid(row=0, column=0)


mainloop()
