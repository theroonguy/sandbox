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

    #Start Location
    loc('bedroom')
    
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

    elif action == 'l':
        loc(cl)

    elif action == 'options':
        options()
    elif action == 'quit':
        quit()

    else:
        print('Sorry, I didn\'t understand.')

        
    loc(cl)
    
def loc(loc):

	 if loc == 'bedroom':
        sector('Room', 'wall', 'wall', 'wall', 'hallway', 'bedroom','A bedroom with two beds.')        
	 elif loc == 'hallway':
        sector('Hallway', 'bathroom', 'bedroom', 'wall', 'room', 'hallway', 'I enter into a hallway, dimly lit from unclear windows.')
	 elif loc == 'bathroom':
        sector('Bathroom', 'wall', 'wall', 'hallway', 'wall', 'bathroom','A bathroom.')        
	 elif loc == 'room':
        sector('A Large Room', 'wall', 'hallway', 'stairtop', 'wall', 'room', 'A larger room than the bedroom, with a smashed tv on the ground.')
	 elif loc == 'stairtop':
        sector('Top of Stairs', 'room', 'stairbottom', 'wall', 'wall', 'stairtop','The top of a staircase leading down to the east into darkness.')        
    
	 elif loc == 'stairbottom':
        sector('Bottom of Stairs', 'int1', 'kitchen', 'living room', 'stairtop', 'stairbottom', 'The bottom of a staircase.')
	 elif loc == 'int1':
        sector('Intersection', 'door', 'wall', 'stairbottom', 'dining', 'int1','I stand at an intersection.')        
	 elif loc == 'door':
        sector('A Boarded Door', 'wall', 'wall', 'int1', 'wall', 'door', 'A boarded door, impossible to get through with my bare hands.')
	 elif loc == 'dining':
        sector('Dining Room', 'office', 'int1', 'wall', 'bathroom2', 'dining', 'A dining room, with a large table in the center, nothing on it.')
	 elif loc == 'office':
        sector('Office', 'wall', 'wall', 'dining', 'wall', 'office','An office.')        
	 elif loc == 'bathroom2':
        sector('Another Bathroom', 'wall', 'dining', 'wall', 'wall', 'bathroom2', 'Another bathroom, almost pitch dark.')

	 elif loc == 'kitchen':
        sector('Kitchen', 'balcony', 'wall', 'wall', 'stairbottom', 'kitcen', 'A kitchen.')
	 elif loc == 'int1':
        sector('Intersection', 'door', 'wall', 'stairbottom', 'dining', 'int1','I stand at an intersection.')        
	 elif loc == 'door':
        sector('A Boarded Door', 'wall', 'wall', 'int1', 'wall', 'door', 'A boarded door, impossible to get through with my bare hands.')

def sector(name, n, e, s, w, currentloc, desc):
    global descs

    print(name+'\n')

    if desc in descs:
        print('')
    else:
        descs.append(desc)
        print(desc)

    action(currentloc, n, e, s, w)
