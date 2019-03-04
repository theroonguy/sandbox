from tkinter import *

root=Tk()

topframe=Frame(root)
topframe.pack(fill=X)
bottomframe=Frame(root)
bottomframe.pack(side=BOTTOM, fill=Y)

button1 = Button(topframe, text='This is a button', bg='purple', fg='purple')
button1.pack(fill=X)
label1 = Label(root, text='This is a label', fg='purple')
label1.pack(fill=Y, side=LEFT)



'''
w = Canvas(master, width=200, height=100)
w.pack()

w.create_line(0, 0, 200, 100)
w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

w.create_rectangle(50, 25, 150, 75, fill="blue")
'''


mainloop()

