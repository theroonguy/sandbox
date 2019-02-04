import time
import random
    
def init():
    global currentloc, n, e, s, w
    
    currentloc=0
    n=0
    e=0
    s=0
    w=0
    
    sector('Sleeping Bag', 'door', 'corner', 'wall', 'shelf', 'sleepingbag')
    action(currentloc, n, e, s, w)
    
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
    action(currentloc, n, e, s, w)
        
def loc():
    sector('Sleeping Bag', 'door', 'corner', 'wall', 'shelf', 'sleepingbag')
    
def sector(name, n, e, s, w, currentloc):
    #    global name, n, e, s, w, currentloc
    
    print(name+'\n')
    n=n
    e=e
    s=s
    w=w
    currentloc=currentloc
    
init()

'''
    action = input('')
    
    if currentloc == 'sleepingbag':
        n='door'
        w='shelf'
        s='wall'
        e='corner'

        print('sleepingbag')

    elif currentloc == 'door':
        n='outside'
        w='shelf2'
        s='sleepingbag'
        e='wall'

        print('door')

    if action == 'n':
        currentloc = n
    if action == 'w':
        currentloc = w
    if action == 's':
        currentloc = s
    if action == 'e':
        currentloc = e

    init()
        
init()
'''
