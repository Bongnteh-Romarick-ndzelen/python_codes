import os
 
choice = input("Shotdown Your Computer ? (Y or N) ")
if choice == 'y' or 'Y':
       os.system("shutdown /s")
       
else:
      print("Exiting the Program doig nothing")