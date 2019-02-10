import time
import random
    
def init():
    global currentloc, n, e, s, w, descs, locs
    
    currentloc=0
    n=0
    e=0
    s=0
    w=0

    descs = []

    options()
    locs = []
    
def options():
    print('''
1. 'n', 's', 'e', and 'w' for movement
2. 'o' or 'options' for options
3. 'quit' for quit
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

#    elif action == 'l':
#        loc(cl)

    elif action == 'options':
        options()
    elif action == 'quit':
        quit()

    else:
        print('Sorry, I didn\'t understand.')

        
    sector(cl, n, e, s, w, cl)

    
def loc(loc):
    global locs


    locs.append(loc)

    print(locs)

    start(locs)
    

def sector(name, n, e, s, w, currentloc, desc=''):

    print(name+'\n')
    action(currentloc, n, e, s, w)

'''
    if desc in descs:
        print('')
    else:
        descs.append(desc)
        print(desc)
'''

def start(locs):
    sector(locs[0])
