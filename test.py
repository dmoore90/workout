#! /usr/bin/env python3

def changeWeight(e, w):
	f = open("data.txt", "w")
	f.write(e + ":" + w) 
	f.closed

def rFile():
	f = open("data.txt", "r")
	print(f.read())
	f.closed

exercise = input("Enter exercise: ")
weight = input("Enter weight: ")

changeWeight(exercise, weight)
rFile()