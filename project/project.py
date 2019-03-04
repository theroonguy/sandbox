from tkinter import *

root=Tk()

topframe=Frame(root)
topframe.pack(fill=X)
bottomframe=Frame(root)
bottomframe.pack(side=BOTTOM, fill=Y)
middleframe=Frame(root)
middleframe.pack()

button1 = Button(topframe, text='This is a button', bg='purple', fg='purple')
button1.pack(fill=X)
label1 = Label(root, text='This is a label', fg='purple')
label1.pack(fill=Y, side=LEFT)

name = Label(middleframe, text='NAME')
password = Label(middleframe, text='PASSWORD')
entry1 = Entry(middleframe)
entry2 = Entry(middleframe)

name.grid(row=0)
password.grid(row=1)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

'''
w = Canvas(master, width=200, height=100)
w.pack()

w.create_line(0, 0, 200, 100)
w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

w.create_rectangle(50, 25, 150, 75, fill="blue")
'''


mainloop()

