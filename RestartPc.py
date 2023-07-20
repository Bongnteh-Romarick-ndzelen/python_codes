import os

choice = input('Restart your computer ? (y or n) ')
if choice == 'y' or 'Y':
      os.system('shotdown /r')
else:
      print('Exiting the Program doing Nothing ')