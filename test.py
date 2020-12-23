#! /usr/bin/env python3

# with open("data.txt") as f:
# 	read_data = f.read()
# 	print(read_data)
# f.closed

exercise = ""
weight = ""
line = ""
f = open("data.txt", "r")
for x in f.readline():
	line += x

while (x in line and x != ":"):
	exercise += line
	
print(exercise)
f.closed

