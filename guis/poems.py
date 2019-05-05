import random
import requests
from tkinter import *

def get_poem():

    res=requests.get('https://api.open-notify.org/astros.json')
    data=res.json()

    authors=data['number']

    newlabel=Label(midf, text=author)
    newlabel.pack()
    
root=Tk()

topf=Frame(root)
topf.pack(fill=X)
sidebar=Frame(root)
sidebar.pack(side=RIGHT, fill=Y)
midf=Frame(root)
midf.pack()

title=Label(topf, text='POEM GENERATOR', font=('Consolas',30), fg='purple')
title.pack(fill=X)

gen_button=Button(sidebar, text='Generate Poem', command=get_poem)
gen_button.pack()

mainloop()
