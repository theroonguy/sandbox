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
    
def action(currentloc, n, e, s, w):
    action == input('>> ')
    
    if action == 'n':
        currentloc = n
    if action == 'e':
        currentloc = e
    if action == 's':
        currentloc = s
    if action == 'w':
        currentloc = w
    
    print(currentloc)
    loc(currentloc)
    
def loc(loc):

    if loc == 'sleepingbag':
        sleepingbag = sector('Sleeping Bag', 'door', 'corner', 'wall', 'wall', 'sleepingbag')        
    if loc == 'door':
        door = sector('Door', 'wall', 'shelf', 'sleepingbag', 'wall', 'door')
    if loc == 'shelf':
        shelf = sector('A Shelf', 'wall', 'wall', 'corner', 'door', 'shelf')
    if loc == 'corner':
        corner = sector('Corner', 'shelf', 'wall', 'wall', 'sleepingbag', 'corner')
    
def sector(name, n, e, s, w, currentloc):
    print(name+'\n')
    
    action(currentloc, n, e, s, w)
    
init()
