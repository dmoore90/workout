#! /usr/bin/env python3

import changeList

def counter():
	opt = ""
	while (opt != "*"):
		print("Type option number.")
		print("1. situps")
		print("2. chinups")
		print("3. overhead press")
		print("4. squat")
		print("5. bench press")
		print("6. deadlift")
		print("7. quit")
		print("8. change weights")
		opt = input("Option: ")

		if (opt == str(1)):		
			print("situps: ")
			sum = 0
			x = str(input("Enter rep: "))
			while (x != "*"):
				y = int(x)
				sum += y
				print(sum)
				x = input("Enter rep: ")
		elif (opt == str(2)):
			print("chinups: ")
			sum = 0
			x = str(input("Enter rep: "))
			while (x != "*"):
				y = int(x)
				sum += y
				print(sum)
				x = input("Enter rep: ")
		elif (opt == str(3)):
			print("overhead press: ")
			sum = 0
			x = str(input("Enter rep: "))
			while (x != "*"):
				y = int(x)
				sum += y
				print(sum)
				x = input("Enter rep: ")
		elif (opt == str(4)):
			print("squat: ")
			sum = 0
			x = str(input("Enter rep: "))
			while (x != "*"):
				y = int(x)
				sum += y
				print(sum)
				x = input("Enter rep: ")
		elif (opt == str(5)):
			print("bench press: ")
			sum = 0
			x = str(input("Enter rep: "))
			while (x != "*"):
				y = int(x)
				sum += y
				print(sum)
				x = input("Enter rep: ")
		elif (opt == str(6)):
			print("deadlift: ")
			sum = 0
			x = str(input("Enter rep: "))
			while (x != "*"):
				y = int(x)
				sum += y
				print(sum)
				x = input("Enter rep: ")
		elif (opt == str(7)):
			opt = "*"
		elif (opt == str(8)):
			changeList.changeList()