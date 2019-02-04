import time
import random

def init():
    global n, s, e, w, currentloc
    
    currentloc='sleepingbag'
    action()

def action():
    action == input('>> ')
    
def sector(n, e, s, w, currentloc):
    global n, e, s, w, currentloc
    
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
