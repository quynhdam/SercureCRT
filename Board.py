#$language = "python"
#$interface = "1.0"

import os
#import "/home/quynh/.vandyke/SecureCRT/Cores/Example.py"
import sys
sys.path.append('/home/quynh/.vandyke/SecureCRT/Cores/Example.py')
from Example.py import LogCommand
from Example.py import Compare
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
def Main():
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
	LogCommand()
	Example.LogCommand()
	Example.Compare()
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

Main()
