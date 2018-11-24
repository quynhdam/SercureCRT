#$language = "python"
#$interface = "1.0"

import os
import subprocess
initialTab = crt.GetScriptTab()
LOG_DIRECTORY_BOARD = os.path.join(
	os.path.expanduser('~'), 'LogOutputOfSpecificCommand')

LOG_FILE_TEMPLATE_BOARD = os.path.join(
	LOG_DIRECTORY_BOARD, "Command_%(NUM)s_Results.txt")

SCRIPT_TAB_BOARD = crt.GetScriptTab()
COMMANDS_BOARD = [
	"cat /etc/udhcp_lease",
	]
LOG_DIRECTORY_LOCAL = os.path.join(
	os.path.expanduser('~'), 'OutputOfCommand')

LOG_FILE_TEMPLATE_LOCAL = os.path.join(
	LOG_DIRECTORY_LOCAL, "Command_%(NUM)s_Results.txt")

SCRIPT_TAB_LOCAL = crt.GetScriptTab()

COMMANDS_LOCAL = [
	"ifconfig",
	"grep -r \"inet addr\" /home/quynh/OutputOfCommand/Command_01_Results.txt | cut -d \":\" -f 2 | cut -d \" \" -f 1 > /home/quynh/OutputOfCommand/IP_Local",

	]
def Main():
	Login()
	LogCommand()
	LogCommand2()
	Compare()
	# errorMessages = ""

	# sessionsFileName = os.path.expanduser("~") + "/SessionList.txt"
	# if not os.path.exists(sessionsFileName):
	# 	crt.Dialog.MessageBox(
	# 		"Session list file not found:\n\n" +
	# 		sessionsFileName + "\n\n" +
	# 		"Create a session list file as described in the description of " +
	# 		"this script code and then run the script again.")
	# 	return

	# sessionFile = open(sessionsFileName, "r")
	# sessionsArray = []

	# for line in sessionFile:
	# 	session = line.strip()
	# 	if session:
	# 		sessionsArray.append(session)

	# sessionFile.close()

	
	# for session in sessionsArray:

	# 		try:
	# 			crt.Session.Connect("/S \"" + session + "\"")
	# 		except SecureCRT.ScriptError:
	# 			error = crt.GetLastErrorMessage()

	# 		if crt.Session.Connected:
	# 			if crt.GetScriptTab().Session.Path == sessionsArray[0]:
	# 				crt.Screen.Synchronous = True

	# 				while True:				
	# 					if not crt.Screen.WaitForCursor(1):
	# 						break
					
	# 				row = crt.Screen.CurrentRow
	# 				prompt = crt.Screen.Get(row, 0, row, crt.Screen.CurrentColumn - 1)
	# 				prompt = prompt.strip()
	# 				Login()
	# 				LogCommand()
	# 			else:
	# 				LogCommand2()
	# 				Compare()
	# 				while crt.Session.Connected == True:
	# 					crt.Sleep(100)
	# 					crt.Sleep(1000)
	# 				else:
	# 					errorMessages = errorMessages + "\n" + "*** Error connecting to " + session + ": " + error
	# 					if errorMessages == "":
	# 						crt.Dialog.MessageBox("Tasks completed.  No Errors were detected.")
	# 					else:
	# 						crt.Dialog.MessageBox("Tasks completed.  The following errors occurred:\n" + errorMessages)
	# 						crt.Quit()
def Login():
	crt.Screen.Synchronous = True
	if not crt.Screen.WaitForString("ogin: ", 2):
		crt.Screen.Send
    	crt.Screen.Send("\n")
    	crt.Screen.WaitForString("ogin: ")
    	crt.Screen.Send("ambit")
    	crt.Sleep(10)
    	crt.Screen.Send("\n")
    	crt.Screen.WaitForString("assword: ")
    	crt.Screen.Send("ambitdebug")
    	crt.Sleep(10)
    	crt.Screen.Send("\n")
    	crt.Screen.WaitForString("gpon$")
    	crt.Screen.Send("retsh foxconn168!")
    	crt.Sleep(100)
    	crt.Screen.Send("\n")
    	crt.Screen.Synchronous = False

def LaunchViewer(filename):
	try:
		os.startfile(filename)
	except AttributeError:
		subprocess.call(['open', filename])


def NN(number, digitCount):
	format = "%0" + str(digitCount) + "d"
	return format % number
def LogCommand():
	if not os.path.exists(LOG_DIRECTORY_BOARD):
		os.mkdir(LOG_DIRECTORY_BOARD)

	if not os.path.isdir(LOG_DIRECTORY_BOARD):
		crt.Dialog.MessageBox(
			"Log output directory %r is not a directory" % LOG_DIRECTORY_BOARD)
		return

	if not SCRIPT_TAB_BOARD.Session.Connected:
		crt.Dialog.MessageBox(
			"Not Connected.  Please connect before running this script.")
		return

	SCRIPT_TAB_BOARD.Screen.IgnoreEscape = True
	SCRIPT_TAB_BOARD.Screen.Synchronous = True

	
	while True:
		if not SCRIPT_TAB_BOARD.Screen.WaitForCursor(1):
			break
	
	rowIndex = SCRIPT_TAB_BOARD.Screen.CurrentRow
	colIndex = SCRIPT_TAB_BOARD.Screen.CurrentColumn - 1

	prompt = SCRIPT_TAB_BOARD.Screen.Get(rowIndex, 0, rowIndex, colIndex)
	prompt = prompt.strip()

	for (index, command) in enumerate(COMMANDS_BOARD):
		command = command.strip()

	
		logFileName = LOG_FILE_TEMPLATE_BOARD % {"NUM" : NN(index + 1, 2)}
		
	
		SCRIPT_TAB_BOARD.Screen.Send(command + '\r')

		
		SCRIPT_TAB_BOARD.Screen.WaitForString('\r', 1)
		SCRIPT_TAB_BOARD.Screen.WaitForString('\n', 1)

		result = SCRIPT_TAB_BOARD.Screen.ReadString(prompt)
		result = result.strip()
		
		filep = open(logFileName, 'wb+')
		

		
		filep.write(result + os.linesep)
		
		
		filep.close()
		LaunchViewer(LOG_DIRECTORY_BOARD)

	return
def LogCommand2():
	if not os.path.exists(LOG_DIRECTORY_LOCAL):
		os.mkdir(LOG_DIRECTORY_LOCAL)

	if not os.path.isdir(LOG_DIRECTORY_LOCAL):
		crt.Dialog.MessageBox(
			"Log output directory %r is not a directory" % LOG_DIRECTORY_LOCAL)
		return

	if not SCRIPT_TAB_LOCAL.Session.Connected:
		crt.Dialog.MessageBox(
			"Not Connected.  Please connect before running this script.")
		return

	SCRIPT_TAB_LOCAL.Screen.IgnoreEscape = True
	SCRIPT_TAB_LOCAL.Screen.Synchronous = True

	
	while True:
		if not SCRIPT_TAB_LOCAL.Screen.WaitForCursor(1):
			break
	
	rowIndex = SCRIPT_TAB_LOCAL.Screen.CurrentRow
	colIndex = SCRIPT_TAB_LOCAL.Screen.CurrentColumn - 1

	prompt = SCRIPT_TAB_LOCAL.Screen.Get(rowIndex, 0, rowIndex, colIndex)
	prompt = prompt.strip()

	for (index, command) in enumerate(COMMANDS_LOCAL):
		command = command.strip()

	
		logFileName = LOG_FILE_TEMPLATE_LOCAL % {"NUM" : NN(index + 1, 2)}
		
	
		SCRIPT_TAB_LOCAL.Screen.Send(command + '\r')

		
		SCRIPT_TAB_LOCAL.Screen.WaitForString('\r', 1)
		SCRIPT_TAB_LOCAL.Screen.WaitForString('\n', 1)

		result = SCRIPT_TAB_LOCAL.Screen.ReadString(prompt)
		result = result.strip()
		
		filep = open(logFileName, 'wb+')

		
		filep.write(result + os.linesep)
		
		
		filep.close()

	LaunchViewer(LOG_DIRECTORY_LOCAL)
	return
def Compare():
	f1 = open("/home/quynh/OutputOfCommand/IP_Local","r")
	f2 = open("/home/quynh/OutputOfCommand/IP_Board.txt","r")
	count = 0
	for line2 in f2:
			for line1 in f1:
				if line1 == line2:
					count=count+1
	if count == 1:
		crt.Dialog.MessageBox("Success")
	else:
		crt.Dialog.MessageBox("False")
			# for line1 in f1:
			# 	if line1==line2:
			# 		crt.Dialog.MessageBox("Success")
			# 	else:
			# 		crt.Dialog.MessageBox("False")
	f1.close()
	f2.close()
# def SendCommandToTabs():
# 	command = crt.Dialog.Prompt("Enter command to be sent to all tabs:",
#                                     "Send To All Connected Tabs",
#                                     "ifconfig",
#                                     False)
# 	if command == "": return

# 	skippedTabs = ""
# 	for i in range(1, crt.GetTabCount()+1):
# 		tab = crt.GetTab(i)
# 		tab.Activate()
# 		# Skip tabs that aren't connected
# 		if tab.Session.Connected == True:
# 			tab.Screen.Send(command + "\n")
# 		else:
# 			if skippedTabs == "":
# 				skippedTabs = str(i)
# 			else:
# 				skippedTabs = skippedTabs + "," + str(i)

# 	initialTab.Activate()
# def CompareIP():
# 	#command = crt.Dialog.Prompt("Enter IP to compare:"," ", False)
# 	# if command == "": return
# 	# skippedTabs = ""
# 	#os.system("cat /home/quynh/LogOutputOfSpecificCommand/Command_01_Results.txt | cut -d \' \' -f 2 > test")
# 	#file = "/home/quynh/LogOutputOfSpecificCommand/Command_01_Results.txt"
# 	#os.system("check = $(cat /home/quynh/LogOutputOfSpecificCommand/Command_01_Results.txt | cut -d \' \' -f 2) > test")
# 	#os.system("\"$check\" > test")
# 	crt.Screen.Send("cat /home/quynh/LogOutputOfSpecificCommand/Command_01_Results.txt | cut -d \' \' -f 2 > test.txt")
# 	#os.system(command)
# 	ipcheck = crt.Dialog.Prompt("Enter IP local to check:","Enter in this:","",False)
# 	if ipcheck == "":
# 		crt.Dialog.MessageBox("Enter IP again")
# 	else:
# 		for line in open("/home/quynh/LogOutputOfSpecificCommand/test.txt","r"):
# 			if line == ipcheck:
# 				crt.Screen.MessageBox("Success")
# 				return True
# 			else:
# 				crt.Screen.Send("reboot")
# 				crt.Sleep(10)
# 				crt.Screen.Send("\n")
# 				return

Main()


