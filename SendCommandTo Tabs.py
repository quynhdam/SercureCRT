# $language = "python"
# $interface = "1.0"

# Get a reference to the tab that was active when this script was launched.
initialTab = crt.GetScriptTab()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def Main():
	# Ask user what command should be sent to each tabs
	command = crt.Dialog.Prompt("Enter command to be sent to all tabs:",
                                    "Send To All Connected Tabs",
                                    "ls -al",
                                    False)
	if command == "": return

	# Give the user a chance to review the command and cancel if they notice
	# something wrong.
	response = crt.Dialog.MessageBox("Are you sure you want to send the\
following command to __ALL__ tabs?\n\n" + command,
                                         "Send Command To All Tabs - Confirm",
                                         BUTTON_YESNO)

	if response != IDYES:
		return

	# Activate each tab in order from left to right, and issue the command in
	# each "connected" tab...
	skippedTabs = ""
	for i in range(1, crt.GetTabCount()+1):
		tab = crt.GetTab(i)
		tab.Activate()
		# Skip tabs that aren't connected
		if tab.Session.Connected == True:
			tab.Screen.Send("ifconfig" + "\n")
		else:
			if skippedTabs == "":
				skippedTabs = str(i)
			else:
				skippedTabs = skippedTabs + "," + str(i)

	# Now, activate the original tab on which the script was started
	initialTab.Activate()

	# Determine if there were any skipped tabs, and prepare a message for
	# displaying at the end.
	if skippedTabs != "":
		skippedTabs = "\n\nThe following tabs did not receive the command because\n\
they were not connected at the time:\n\t" + skippedTabs

	crt.Dialog.MessageBox("The following command was sent to all \
connected tabs:\n\t" + command + skippedTabs)

Main()