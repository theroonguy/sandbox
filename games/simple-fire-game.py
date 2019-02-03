from time import sleep

wood = 0
firelevel = 1

def action():
  global wood, firelevel
  
  action = (input('>> ')).lower()
  
  if action == 'gather wood':
    wood += 1
    print('Gathered 1 piece of wood')
    print('Wood: '+str(wood))
  elif action == 'stoke fire':
    if wood > 0:
      wood -= 1
      firelevel += 1
      print('You stoked the fire.\n-1 wood')
    else:
      print('You don\'t have enough wood.')
  elif action == 'list':
    print('\nWood: '+str(wood)+'\nFire Level: '+str(firelevel))
  elif action == 'options':
    options()
  elif action == 'quit':
    quit()
  else:
    print('Sorry, I don\'t understand what you typed. Please try again.')

  print('\n')

def options():
  print('1. gather wood -- gathers 1 wood\n2. stoke fire -- uses 1 wood to stoke fire\n3. list -- lists current wood stash and fire level\n4. options -- lists this menu\n5. quit -- quits the game')

options()  
while True:
  action()
  firelevel -= 0.2
  if firelevel == 0:
    print('Oh no! Your fire has gone out!')
