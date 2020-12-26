#! /usr/bin/env python3

def wList(x, w):
	f = open("data.txt", "a")
	# exercise = input("enter ex: ")
	f.write("{}".format(x))
	# weight = input("enter weight: ")
	f.write("{}\n".format(w))
	f.close()

workoutlist = {
	"situps: ": "bodyweight", "chinups: ": "bodyweight", 
	"overhead press: ": "bodyweight", "squat: ":"bodyweight", 
	"bench press: ": "bodyweight", "deadlift: ": "bodyweight",
	"---":"----"
	}

for k,v in workoutlist.items():
	wList(k,v)

