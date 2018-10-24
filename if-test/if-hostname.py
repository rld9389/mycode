#!/usr/bin/env python3
#hostname = 'MTG'

#if hostname == 'MTG':
#	print('The hostname was found to be mtg')


#accept input from user
hostnameinput = input('What is your hostname? ')

if hostnameinput == "mtg" or "MTG" or "mTG" or "MTg" or "mTg" or "MtG":
#if hostname is anything then go to next
#	hostnameinput == True
	print("hostname matches expected config")
#prints if true

elif hostnameinput: # if any data is provided, this will test true
   print('Looks like the IP address was set') # indented under if

else: # if data is NOT provided
   print('You did not provide input.') # indented under else


#elif hostnameinput != "mtg" or "MTG" or "mTG" or "MTg" or "mTg" or "MtG":
#	print(hostnameinput)
#	exit()

print("Exiting the script.")



