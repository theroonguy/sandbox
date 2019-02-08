import time
import random
    
def init():
    global currentloc, n, e, s, w
    
    currentloc=0
    n=0
    e=0
    s=0
    w=0
    
    loc('sleepingbag')
    
def action(cl, n, e, s, w):
    action = input('>> ')
    
    if action == 'n':
        cl = n
    elif action == 'e':
        cl = e
    elif action == 's':
        cl = s
    elif action == 'w':
        cl = w
    
    loc(cl)
    
def loc(loc):

    if loc == 'sleepingbag':
        sector('Sleeping Bag', 'door', 'corner', 'wall', 'wall', 'sleepingbag')        
    elif loc == 'door':
        sector('Door', 'wall', 'shelf', 'sleepingbag', 'wall', 'door')
    elif loc == 'shelf':
        sector('A Shelf', 'wall', 'wall', 'corner', 'door', 'shelf')
    elif loc == 'corner':
        sector('Corner', 'shelf', 'wall', 'wall', 'sleepingbag', 'corner')
    
def sector(name, n, e, s, w, currentloc):
    print(name+'\n')
    
    action(currentloc, n, e, s, w)
    
init()
