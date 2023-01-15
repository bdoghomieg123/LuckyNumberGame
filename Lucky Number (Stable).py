import time
import os 
import platform 
import string 
from builtins import input 
import random
import datetime


opsys = platform.system()

#clears output
def clear():
	if opsys == 'Linux':
		os.system('clear')
	elif opsys == 'Windows':
		os.system('cls')

def restart():
	if opsys == 'Linux':
		os.system('Python3 Lucky Number (Stable).py')
	elif opsys == 'Windows':
		os.system('python Lucky Number (Stable).py')
	
clear()

print('Hello and Welcome to the "Lucky Number Game"')
print('\nv0.3')
input('\n***Press any key to continue...***')
total = 0
clear()
ready = input("Are you Ready to play the game? \n \nPlease input 'y' or 'n' ")
																					

if "y" in ready.lower():
	clear()
	name = input('What is your name? \n \n')
	clear()
	print('Hello, ' + string.capwords(name))
	time.sleep(3)
	clear()
	if len(name) > 5:
		total += random.randint(1,100)
	else:
		total += random.randint(0,5)
	movie = input("What is your favorite movie?" + '\n \n')
	total += random.randint(1,30)
	clear()
	color = input('What is your favorite color?' + '\n \n')
	clear()
	if color.lower() == "blue":
		print('I love the color Blue!')
		total += random.randint(2,19)
		time.sleep(2)
	else:
		print("Ahhh %s... That's a nice color..." % (color))
		total -= 5
		time.sleep(2)
	clear()
	place = input('What Fictional City Would you Like to Visit? \n \n')
	total += random.randint(1,20)
	clear()
	phone = input('Which do you like better: Apple or Android? \n \n')
	if phone == "Android":
		total += 12
	elif phone == "Apple":
		total += 5
	clear()
	print("Your Lucky number is: %s" % (total))
	print('\n\n\n\n\n\nContent is under development. Project To Be continuted...')



elif "n" in ready.lower():
	clear()
	print("Alrighty then. have a nice day I guess...")
	exit(42069)


else:
	clear()
	print("Okay? Have a nice day.")
	time.sleep(2)
	exit(404)
