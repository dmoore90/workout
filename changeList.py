#! /usr/bin/env python3

def changeList():
	workoutdict = {}
	ex = ""
	w = ""
	lines = []
	lines1 = []
	exercises = []
	weights = []
	wd = {}
	newLine = ""
	f = open("data.txt", "r")
	for i in f.readlines():
		lines.append(i)	
	for i in lines:
		line = i
		newLine = line.strip('\n')
		lines1.append(newLine)
	for i in lines1:
		for j in i:
			if (j != ":"):
				ex += j
			elif (j == ":"):
				exercises.append(ex)
				ex = ""
		ex = ""
	for i in lines1:
		for j in i:
			w += j
			if (j == " "):
				w = ""
		weights.append(w)
		w + ""
	i = 0
	while (i < len(exercises)):
		workoutdict[exercises[i]] = weights[i]
		i += 1


	opt = ""
	while (opt != "*"):
		for k,v in workoutdict.items():
			print(k, v)
		print("Press 1 for situps weight: ")
		print("Press 2 for chinups weight: ")
		print("Press 3 for overheadpress weight: ")
		print("press 4 for squats: ")
		print("Press 5 for bench press weight: ")
		print("Press 6 for deadlift: ")
		print("Press * to quit:")
		opt = input("Enter option number: ")
		if (opt == "1"):
			for k,v in workoutdict.items():
				if (k == "situps"):
					workoutdict[k] = input("enter new weight: ")
		elif (opt == "2"):
			for k,v in workoutdict.items():
				if (k == "chinups"):
					workoutdict[k] = input("enter new weight: ")
		elif (opt == "3"):
			for k,v in workoutdict.items():
				if (k == "overhead press"):
					workoutdict[k] = input("enter new weight: ")
		elif (opt == "4"):
			for k,v in workoutdict.items():
				if (k == "squats"):
					workoutdict[k] = input("enter new weight: ")
		elif (opt == "5"):
			for k,v in workoutdict.items():
				if(k == "bench press"):
					workoutdict[k] = input("enter new weight: ")
		elif (opt == "6"):
			for k,v in workoutdict.items():
				if (k == "deadlift"):
					workoutdict[k] = input("enter new weight: ")
		elif (opt == "*"):
			opt = "*"

	for k,v in workoutdict.items():
		f = open("data.txt", "a")
		# exercise = input("enter ex: ")
		f.write("{}: ".format(k))
		# weight = input("enter weight: ")
		f.write("{}\n".format(v))
		f = open("data.txt", "a")
		f.close()