#$language = "python"
#$interface = "1.0"
import os
import subprocess
LOG_DIRECTORY_LOCAL = os.path.join(
	os.path.expanduser('~'), 'OutputOfCommand')

LOG_FILE_TEMPLATE_LOCAL = os.path.join(
	LOG_DIRECTORY_LOCAL, "Command_%(NUM)s_Results.txt")

SCRIPT_TAB_LOCAL = crt.GetScriptTab()

COMMANDS_LOCAL = [
	"ifconfig",
	"grep -r \"inet addr\" /home/quynh/OutputOfCommand/Command_01_Results.txt | cut -d \":\" -f 2 | cut -d \" \" -f 1 > /home/quynh/OutputOfCommand/IP_Local",
	"cat /home/quynh/LogOutputOfSpecificCommand/Command_01_Results.txt | cut -d ' ' -f 2 > /home/quynh/OutputOfCommand/IP_Board.txt",

	]
	
def Main():
	LogCommand()
	Compare()
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
	
def LaunchViewer(filename):
	try:
		os.startfile(filename)
	except AttributeError:
		subprocess.call(['open', filename])
def NN(number, digitCount):
	format = "%0" + str(digitCount) + "d"
	return format % number 
def LogCommand():
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

Main()

