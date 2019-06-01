from tkinter import *
import requests
import random

root=Tk()

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

        
################### INIT ########################################


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
weather=Frame(root_rightbar, bd=1, relief=SUNKEN)
weather.pack(side=RIGHT)
prayertime=Frame(root_leftbar, bd=1, relief=SUNKEN)
prayertime.pack(side=RIGHT)

root_title = Label(root_topf, text='GENERAL PURPOSE GUI', font = ('Consolas',30), fg='purple')
root_title.pack(fill=X)


################### WEATHER #####################################


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

def get_prayer():

    url = 'https://api.aladhan.com/v1/calendar?latitude=39&longitude=-77&method=2&month=6&year=2019&day=1'
    res = requests.get(url)
    data = res.json()
    
    try:
        fajr = data['data'][0]['timings']
        print(fajr)
    except:
        print('error')
        
Label(prayertime, text='PRAYERS', font=('Consolas', 15), fg='blue').grid(row=0)
prayer_place=Entry(prayertime, width=10)
prayer_place.grid(row=1, column=0)
prayer_enter=Button(prayertime, text='Enter', command=get_prayer)
prayer_enter.grid(row=1, column=1)


mainloop()
