#!/usr/bin/env python3

#lettergrade = float(input("What is your numeric score? "))

#if lettergrade > 101:
#	keepgoing = lettergrade
#	if keepgoing > 101:
#		keepgoing
	#else
		#break
while True: 
	lettergrade = float(input("What is your numeric score? "))
	if lettergrade >= 101:
		lettergrade
#		return
	break

if lettergrade >= 90 and lettergrade <= 100:
	print("A")
elif lettergrade >= 80 and lettergrade <=89:
	print("B")
elif lettergrade >= 70 and lettergrade <=79:
	print("C")
elif lettergrade >=60 and lettergrade <=69:
	print("D")
elif lettergrade <= 59:
	print("F")

#elif lettergrade >= 100:
#	print("no")

#return lettergrade

#if lettergrade <= int(100) or lettergrade >= int(90):
#	print("A")
#elif lettergrade <= 89 or lettergrade >= 80:
#	print("B")
#elif lettergrade >= 70 or <=79:
#	print("C")
#elif lettergrade >= 60 or <=69:
#	print("D")
#else lettergrade <= 59:
#	print("F")

