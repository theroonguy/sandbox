from tkinter import *

root=Tk()

topframe=Frame(root)
topframe.pack(fill=X)
middleframe=Frame(root)
middleframe.pack()
bottomframe=Frame(root)
bottomframe.pack(side=BOTTOM, fill=Y)
sidebar=Frame(root)
middleframe.pack(side=RIGHT, fill=Y)

title = Label(topframe, text='TITLE', fg='purple')
label1 = Label(sidebar, text='This is a sidebar', fg='purple')
label1.pack(fill=Y)

name = Label(middleframe, text='NAME')
password = Label(middleframe, text='PASSWORD')
entry1 = Entry(middleframe)
entry2 = Entry(middleframe)

name.grid(row=0)
password.grid(row=1)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

button1 = Button(middleframe, text='This is a button', bg='purple', fg='white')
button1.grid(row=0, column=2)

'''
w = Canvas(master, width=200, height=100)
w.pack()

w.create_line(0, 0, 200, 100)
w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

w.create_rectangle(50, 25, 150, 75, fill="blue")
'''


mainloop()

