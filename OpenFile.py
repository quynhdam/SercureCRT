import os
def Main():
	f1 = open("/home/quynh/OutputOfCommand/test","r")
	f2 = open("/home/quynh/OutputOfCommand/test.txt","r")
	for line2 in f2:
		for line1 in f1:
			if line1 == line2:
				print("Success")
			else:
				print("False")
	f1.close()
	f2.close()
Main()
