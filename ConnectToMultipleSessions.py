#$language = "Python"
#$interface = "1.0"


import os

def main():
	errorMessages = ""

	sessionsFileName = os.path.expanduser("~") + "/SessionList.txt"
	if not os.path.exists(sessionsFileName):
		crt.Dialog.MessageBox(
			"Session list file not found:\n\n" +
			sessionsFileName + "\n\n" +
			"Create a session list file as described in the description of " +
			"this script code and then run the script again.")
		return

	sessionFile = open(sessionsFileName, "r")
	sessionsArray = []

	for line in sessionFile:
		session = line.strip()
		if session:
			sessionsArray.append(session)

	sessionFile.close()

	
	for session in sessionsArray:

		

		try:
			crt.Session.Connect("/S \"" + session + "\"")
			SessionName = crt.GetScriptTab.caption
		except SecureCRT.ScriptError:
			error = crt.GetLastErrorMessage()

		if crt.Session.Connected:
			crt.Screen.Synchronous = True

			while True:				
				if not crt.Screen.WaitForCursor(1):
					break
			
			row = crt.Screen.CurrentRow
			prompt = crt.Screen.Get(row, 0, row, crt.Screen.CurrentColumn - 1)
			prompt = prompt.strip()

			crt.Screen.Send("ls -l\n")
			
			crt.Screen.WaitForString(prompt)

			crt.Screen.Send("pwd\n")
			
			crt.Screen.WaitForString(prompt)

			crt.Screen.Send("who\n")
		
			crt.Screen.WaitForString(prompt)

			crt.Session.Disconnect()
			
			while crt.Session.Connected == True:
				crt.Sleep(100)

			crt.Sleep(1000)
		else:
			errorMessages = errorMessages + "\n" + "*** Error connecting to " + session + ": " + error

	if errorMessages == "":
		crt.Dialog.MessageBox("Tasks completed.  No Errors were detected.")
	else:
		crt.Dialog.MessageBox("Tasks completed.  The following errors occurred:\n" + errorMessages)

	crt.Quit()

main()