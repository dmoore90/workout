#! /usr/bin/env python3

# def wList(x, w):
# 	f = open("data.txt", "a")
# 	# exercise = input("enter ex: ")
# 	f.write("{}".format(x))
# 	# weight = input("enter weight: ")
# 	f.write("{}\n".format(w))
# 	f.close()

# exercises = {
# 	"situps: ": "bodyweight", "chinups: ": "bodyweight", 
# 	"overhead press: ": "bodyweight", "squats: ":"bodyweight", 
# 	"bench press: ": "bodyweight", "deadlift: ": "bodyweight",
# 	"---":"----"
# 	}



def readValues():
	ex = ""
	w = ""
	lines = []
	lines1 = []
	exercises = []
	weights = []
	workoutdict = {}
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
				
	print(weights)
	print("---")
	print(exercises)

readValues()

# def changeVal():
# 	a = ""
# 	while (a != "*"):
# 		print("Press 1 for situps weight: ")
# 		print("Press 2 for chinups weight: ")
# 		print("Press 3 for overheadpress weight: ")
# 		print("press 4 for squats: ")
# 		print("Press 5 for bench press weight: ")
# 		print("Press 6 for deadlift: ")
# 		print("Press * to quit:")
# 		a = input("Enter option number: ")
# 		if (a == "1"):
# 			print("true")
# 			for k,v in exercises.items():
# 				if (k == "situps: "):
# 					exercises["situps"] = input("enter new weight: ")
# 		elif (a == "2"):
# 			for k,v in exercises.items():
# 				if (k == "chinups: "):
# 					v = input("enter new weight: ")
# 		elif (a == "3"):
# 			for k,v in exercises.items():
# 				if (k == "overhead press: "):
# 					v = input("enter new weight: ")
# 		elif (a == "4"):
# 			for k,v in exercises.items():
# 				if (k == "squats: "):
# 					v = input("enter new weight: ")
# 		elif (a == "5"):
# 			for k,v in exercises.items():
# 				if(k == "bench press: "):
# 					v = input("enter new weight: ")
# 		elif (a == "6"):
# 			for k,v in exercises.items():
# 				if (k == "deadlift: "):
# 					v = input("enter new weight: ")
# 		elif (a == "*"):
# 			a = "*"

# def printList():
# 	for k,v in exercises.items():
# 		wList(k,v)

# printList()
# changeVal()
