import time
import random
    
def init():
    global currentloc, n, e, s, w, descs
    
    currentloc=0
    n=0
    e=0
    s=0
    w=0

    descs = []

    options()
    loc('sleepingbag')
    
def options():
    print('''
1. 'n', 's', 'e', and 'w' for movement
2. 'o' or 'options' for options
3. 'q' or 'quit' for quit
''')
    
def action(cl, n, e, s, w):
    action = input('>> ')
    
    if action == 'n':
        if n != 'wall':
            cl = n
    elif action == 'e':
        if e != 'wall':
            cl = e
    elif action == 's':
        if s != 'wall':
            cl = s
    elif action == 'w':
        if w != 'wall':
            cl = w

    elif action == 'l':
        loc(cl)

    elif action == 'o' or action == 'options':
        options()
    elif action == 'q' or action == 'quit':
        quit()

    else:
        print('Sorry, I didn\'t understand.')

        
    loc(cl)
    
def loc(loc):

    # PUT CODE HERE
    
    if loc == 'start':
        sector('TITLE', 'n', 'e', 's', 'w', 'ID','DESC')        
    
def sector(name, n, e, s, w, currentloc, desc):
    global descs

    print(name+'\n')

    if desc in descs:
        print('')
    else:
        descs.append(desc)
        print(desc)

    action(currentloc, n, e, s, w)
