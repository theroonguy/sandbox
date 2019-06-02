from tkinter import *
import requests
import random
import datetime

root=Tk()

        
################### INIT ########################################

def get_date():
    now = datetime.datetime.now()
    return now.year, now.month, now.day

def get_coords():

    place = prayer_place.get()
    place.strip(' ')
    
    url = 'https://api.opencagedata.com/geocode/v1/json?q={}&key=3243e87472484e1c8471c7614a21734c'.format(place)
    res = requests.get(url)
    data = res.json()

    lat = data['results'][0]['geometry']['lat']
    lng = data['results'][0]['geometry']['lng']
    totalresults = data['total_results']

    status = 1
    
    if totalresults > 1:
        output = 0

    return lat, lng, status
    
root.geometry('1000x300')

root_topf=Frame(root)
root_topf.pack(fill=X)
root_rightbar=Frame(root, bd=2, relief=SUNKEN)
root_rightbar.pack(side=RIGHT, fill=Y)
root_leftbar=Frame(root, bd=2, relief=SUNKEN)
root_leftbar.pack(side=LEFT, fill=Y)
root_midf=Frame(root)
root_midf.pack()

poemgen=Frame(root_leftbar, bd=1, relief=SUNKEN)
poemgen.pack(side=LEFT)
quitbutton=Frame(root_rightbar, bd=1, relief=SUNKEN)
quitbutton.grid(row=5)
weather=Frame(root_rightbar, bd=1, relief=SUNKEN)
weather.grid(row=0, column=0)
prayertime=Frame(root_rightbar, bd=1, relief=SUNKEN)
prayertime.grid(row=0, column=1)

root_title = Label(root_topf, text='GENERAL PURPOSE GUI', font = ('Consolas',30), fg='purple')
root_title.pack(fill=X)


################### WEATHER #####################################

def get_weather():
    output=weather_place.get()
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
        
        label=Label(weather, text='Weather in {}: \n{}\n{}\n{}'.format(name, ftemp, fwind, fdesc, bg='light grey', fg='blue'), font=('Consolas',10))
        label.grid(row=2)
    except:
        Label(weather, text='Error').grid(row=2)
        
Label(weather, text='WEATHER', font=('Consolas', 15), fg='blue').grid(row=0)
weather_place=Entry(weather, width=10)
weather_place.grid(row=1, column=0)
weather_enter=Button(weather, text='Enter', command=get_weather)
weather_enter.grid(row=1, column=1)


################### POEM GENERATOR ##############################


def get_author():

    clear_poem()

    res=requests.get('http://poetrydb.org/author')
    data=res.json()
    
    authors=data['authors']
    rand_author=authors[random.randint(0, 128)]
    

    
    get_poem(rand_author)
    
def get_poem(rand_author):
    global textlabel, authorlabel

    poemnum=0
    
    res=requests.get('http://poetrydb.org/author/{}'.format(rand_author))
    data=res.json()
    
    poems=data[0:]
    
    for word in poems:
        poemnum+=1
        
    rand_poemnum=random.randint(0, poemnum-1)
    
    poem_lines=poems[rand_poemnum]['lines']
    poem_title=poems[rand_poemnum]['title']

    
    final=[]
    for word in poem_lines:
        final.append(word)
        final.append('\n')
        
    authorlabel=Label(poem_midf, text='{} written by {}'.format(poem_title, rand_author))
    authorlabel.grid(row=0, column=0)
    
    textlabel=Label(poem_midf, text=' '.join(final))
    textlabel.grid(row=1, column=0)

def clear_poem():

    try:
        authorlabel.grid_forget()
        textlabel.grid_forget()
    except:
        print('no poems')

poem_topf=Frame(poemgen)
poem_topf.pack(fill=X)
poem_sidebar=Frame(poemgen)
poem_sidebar.pack(side=RIGHT, fill=Y)

poem_midf=Frame(poemgen)
poem_midf.pack()

poem_title=Label(poem_topf, text='POEM GENERATOR', font=('Consolas',15), fg='blue')
poem_title.pack(fill=X)

poem_gen_button=Button(poem_sidebar, text='Generate Poem', command=get_author)
poem_gen_button.pack()

################### PRAYER TIMES ##############################

def get_timings():

    year = get_date()[0]
    month = get_date()[1]
    day = get_date()[2]

    lat = get_coords()[0]
    lng = get_coords()[1]
    coordstatus = get_coords()[2]
    
    url = 'https://api.aladhan.com/v1/calendar?latitude={}&longitude={}&method=2&month={}&year={}&day={}'.format(lat, lng, month, year, day)
    res = requests.get(url)
    data = res.json()
    
    f = data['data'][0]['timings']['Fajr']
    d = data['data'][0]['timings']['Dhuhr']
    a = data['data'][0]['timings']['Asr']
    m = data['data'][0]['timings']['Maghrib']
    i = data['data'][0]['timings']['Isha']
    
    Label(prayertime, text='''
Fajr: {}
Dhuhr: {}
Asr: {}
Maghrib: {}
Isha: {}'''.format(f, d, a, m, i)).grid(row=2)
        
Label(prayertime, text='PRAYERS', font=('Consolas', 15), fg='blue').grid(row=0)
prayer_place=Entry(prayertime, width=10)
prayer_place.grid(row=1, column=0)
prayer_enter=Button(prayertime, text='Enter', command=get_timings)
prayer_enter.grid(row=1, column=1)

################### QUIT BUTTON ##############################

qbutton = Button(quitbutton, text='QUIT', command=quit)
qbutton.pack()

mainloop()
