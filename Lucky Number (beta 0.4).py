import time
import os
import platform
import sys
import string
from builtins import input
import random
import datetime
from common import *




#The Questions
def LNG():
	clear()
	total = 0
	name = input('What is your name?\n \n')
	clear()
	print('Hello, ' + string.capwords(name))
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
		total += 4
	clear()
	print('Thank you for trying the beta... More to come soon.')
	
	
	

#Asks user if they want to play the game
def intro():
	clear()
	print('Beta version:\nv0.4\n\nIf you notice a bug, fill out an Issue report on my Github\n')
	input('***Press any key to continue...***\n\n')
	clear()
	print('Hello and Welcome to the "Lucky Number Game"')
	time.sleep(3)
	clear()
	ready = input('Are you Ready to play the game?\n\n[yes/no]\n\n')
	if "y" in ready.lower():
		LNG()
	elif "n" in ready.lower():
		notready()
	else:
		print('Invalid response detected... Restarting...')
		time.sleep(2)
		intro()

#Exits program if user answers "No" to above function's question
def notready():
	clear()
	print('Fine have it your way')
	time.sleep(2)
	exit()
	
intro()


	
