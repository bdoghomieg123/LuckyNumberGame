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
print('\n v1.1')
input('\n***Press any key to continue...***')
total = 0
clear()
ready = input('Are you Ready to play the game? \n \n')
assert isinstance(ready,str)
#Begining of Game

if "y" in ready.lower():
	clear()
	name = input('What is your name? \n \n')
	assert isinstance(name,str)
	clear()
	print('Hello, ' + string.capwords(name))
	if len(name) > 5:
		total += random.randint(1,100)
	else:
		total += random.randint(0,5)
	movie = input("(1/3)What is your favorite movie?" + '\n \n')
	assert isinstance(movie,str)
	total += random.randint(1,30)
	clear()
	color = input('(2/3)What is your favorite color?' + '\n \n')
	assert isinstance(color,str)
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
	place = input('(3/3)What Fictional City Would you Like to Visit? \n \n')
	assert isinstance(place,str)
	total += random.randint(1,20)
	phone = input('Which do you like better: Apple or Android? \n \n')
	assert isinstance(phone,str)
	clear()
	if phone == "Android":
		total += 12
	elif phone == "Apple":
		total += 4
	
	
	
#Don't code below this line... Code is a dead-end past this line
elif "n" in ready.lower():
	clear()
	print('Fine. have it your way')
	time.sleep(2)
	clear()
	exit()
else:
	print('Invalid response detected... Exiting...')
	
	
