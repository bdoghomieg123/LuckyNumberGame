import os 
import platform
import time



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