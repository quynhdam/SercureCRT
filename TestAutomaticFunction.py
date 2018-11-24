#$language = "python"
#$interface = "1.0"
import os
import subprocess

#initialTab = crt.GetScriptTab()
LOG_DIRECTORY = os.path.join(
	os.path.expanduser('~'), 'LogOutputOfSpecificCommand')

LOG_FILE_TEMPLATE = os.path.join(
	LOG_DIRECTORY, "Command_%(NUM)s_Results.txt")

SCRIPT_TAB = crt.GetScriptTab()

COMMANDS = [
	"cat /etc/udhcp_lease",

	]

def Main():
	
	n = 1
	while n < 50:
		session1 = "serial-ttyusb0"
		session2 = "quynh-inspiron-3650"
		crt.Session.Disconnect()
		crt.Session.Connect("/S \"" + session1 + "\"")
		crt.Screen.Send("reboot")
		crt.Screen.Send("\r")
		# if (crt.Screen.WaitForString("ogin:", 10) != True):
		# 	crt.Screen.Send("\r")

		# else:
		Login()
		#crt.Screen.Send("echo  'Retry= \'$Retry\' --------> Pass= \'$Pass\' --------> Fail= \'$Fail\''")
				#Find_Udhcp_lease()
				#rt.Screen.Send("cat /etc/udhcp_lease > /home/quynh/LogOutputOfSpecificCommand/Command_01_Results.txt")
		LogCommand()
		crt.Session.Disconnect()
		crt.Session.Connect("/S \""+ session2 + "\"")

		crt.Screen.Send("ifconfig > /home/quynh/OutputOfCommand/Command_01_Results.txt")
		crt.Screen.Send("\r")
		crt.Screen.Send("\n")
		crt.Screen.Send("grep -r \"inet addr\" /home/quynh/OutputOfCommand/Command_01_Results.txt | cut -d \":\" -f 2 | cut -d \" \" -f 1 > /home/quynh/OutputOfCommand/IP_Local")
		crt.Screen.Send("\r")
		crt.Screen.Send("\n")
		crt.Screen.Send("cat /home/quynh/LogOutputOfSpecificCommand/Command_01_Results.txt | cut -d ' ' -f 2 > /home/quynh/OutputOfCommand/IP_Board.txt")
		crt.Screen.Send("\r")
		crt.Screen.Send("\n")
		crt.Screen.Send("\r")
		# crt.Screen.Send("s=0")
		# crt.Screen.Send("\r")
		# crt.Screen.Send("fl=0")
		# crt.Screen.Send("\r")
		crt.Screen.Send("Pass=0") 
		crt.Screen.Send("\r")
		crt.Screen.Send("Fail=0")
		crt.Screen.Send("\r")
		#crt.Screen.Send("Retry=1")
		crt.Screen.Send("\r")
		f1 = open("/home/quynh/OutputOfCommand/IP_Local","r")
		f2 = open("/home/quynh/OutputOfCommand/IP_Board.txt","r")
		count = 0
		for line2 in f2:
				for line1 in f1:
					if line1 == line2:
						count=count+1
		if count == 1:
			crt.Session.SetStatusText("Success")
			crt.Screen.Send("\r")
			crt.Screen.Send("Pass=$((Pass+1))")
			#crt.Screen.Send("echo \"$s\"")
			crt.Screen.Send("\r")
			#crt.Dialog.MessageBox("Success")
		else:
			#crt.Dialog.MessageBox("Success")
			crt.Session.SetStatusText("False")
			crt.Screen.Send("\r")
			crt.Screen.Send("Fail=`expr $Fail + 1`")
			#crt.Screen.Send("echo \"$fl\"")
			crt.Screen.Send("\r")
			#Test()
			
		f1.close()
		f2.close()
		crt.Screen.Send("\r")
		crt.Screen.Send("echo 'Success = \'$Pass\', False = \'$Fail\'' >> /home/quynh/Result.txt")
		crt.Screen.Send("\r")
		crt.Sleep(1000)
		n = n + 1
def LogCommand():
	
	if not os.path.exists(LOG_DIRECTORY):
		os.mkdir(LOG_DIRECTORY)

	if not os.path.isdir(LOG_DIRECTORY):
		crt.Dialog.MessageBox(
			"Log output directory %r is not a directory" % LOG_DIRECTORY)
		return

	if not SCRIPT_TAB.Session.Connected:
		crt.Dialog.MessageBox(
			"Not Connected.  Please connect before running this script.")
		return
	SCRIPT_TAB.Screen.IgnoreEscape = True
	SCRIPT_TAB.Screen.Synchronous = True
	while True:
		if not SCRIPT_TAB.Screen.WaitForCursor(1):
			break
	
	rowIndex = SCRIPT_TAB.Screen.CurrentRow
	colIndex = SCRIPT_TAB.Screen.CurrentColumn - 1

	prompt = SCRIPT_TAB.Screen.Get(rowIndex, 0, rowIndex, colIndex)
	prompt = prompt.strip()

	for (index, command) in enumerate(COMMANDS):
		command = command.strip()

		logFileName = LOG_FILE_TEMPLATE % {"NUM" : NN(index + 1, 2)}
		
		SCRIPT_TAB.Screen.Send(command + '\r')

		SCRIPT_TAB.Screen.WaitForString('\r', 1)
		SCRIPT_TAB.Screen.WaitForString('\n', 1)

		result = SCRIPT_TAB.Screen.ReadString(prompt)
		result = result.strip()
		
		filep = open(logFileName, 'wb+')


		filep.write(result + os.linesep)
		
		filep.close()

	
	LaunchViewer(LOG_DIRECTORY)


def LaunchViewer(filename):
	try:
		os.startfile(filename)
	except AttributeError:
		subprocess.call(['open', filename])


def NN(number, digitCount):
	format = "%0" + str(digitCount) + "d"
	return format % number

def Login():
	crt.Screen.Synchronous = True
	if crt.Screen.WaitForString("ogin:", 100) != True:
	 	crt.Screen.Send("\r")
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
    	crt.Screen.Send("\r")
    	crt.Screen.Synchronous = False

def Compare():
	crt.Screen.Send("\r")
	crt.Screen.Send("s=0")
	crt.Screen.Send("\r")
	crt.Screen.Send("fl=0")
	crt.Screen.Send("\r")
	f1 = open("/home/quynh/OutputOfCommand/IP_Local","r")
	f2 = open("/home/quynh/OutputOfCommand/IP_Board.txt","r")
	count = 0
	for line2 in f2:
			for line1 in f1:
				if line1 == line2:
					count=count+1
	if count == 1:
		crt.Session.SetStatusText("Success")
		crt.Screen.Send("\r")
		crt.Screen.Send("s=$((s+1))")
		#crt.Screen.Send("echo \"$s\"")
		crt.Screen.Send("\r")
		#crt.Dialog.MessageBox("Success")
	else:
		#crt.Dialog.MessageBox("Success")
		crt.Session.SetStatusText("False")
		crt.Screen.Send("\r")
		crt.Screen.Send("fl=`expr $fl + 1`")
		#crt.Screen.Send("echo \"$fl\"")
		crt.Screen.Send("\r")
		#Test()
		
	f1.close()
	f2.close()
	crt.Screen.Send("\r")
	crt.Screen.Send("echo Success = $s, False = $fl")
	crt.Screen.Send("\r")

def Star_Test():
	while True:
		if not crt.Screen.WaitForString("ogin: ", 20):
			#crt.Screen.Send(chr(10) + chr(13))
			crt.Screen.Send("\r")
		else:
			break
		crt.Screen.Send("\r")
		crt.Screen.Send("\r")
		crt.Screen.Send("\r")
		Login()
		crt.Screen.Send("\r")
		crt.Screen.Send("\r")
		crt.Screen.Send("\r")
def Find_Udhcp_lease():
	crt.Screen.Send("\n")
	crt.Screen.Send("ps | grep dhcp")
	crt.Screen.Send("\n")
	crt.Screen.Send("cat /etc/mac.conf")
	crt.Screen.Send("\n")
	crt.Screen.Send("cat /etc/fwver.conf")
	false = 0
	paSS = 1
	pending = 0
	interval =10
	mLimit = 18
	while True:
		# crt.Screen.Send("cat /etc/udhcp_lease")
		# crt.Screen.Send("\n")
		if not crt.Screen.WaitForString("192.168.1.",1):
			pending = pending + 1
			crt.Sleep(interval*100)
			if pending == mLimit:
				crt.Screen.Send("ps | grep dhcp")
				crt.Screen.Send("\n")
				crt.Screen.Send("cat /tmp/dhcpTmp.log")
				crt.Screen.Send("\n")
				crt.Screen.Send("cat /tmp/dhcp.log")
				crt.Screen.Send("\n")
				crt.Screen.Send ("ps | grep dhcp") 
				false = false + 1
		else:
			crt.Screen.Send("echo DHCP OK")
			paSS = paSS + 1
			break

Main()