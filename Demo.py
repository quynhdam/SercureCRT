#$language = "python"
#$interface = "1.0"


def Main():
	session2 = "quynh-inspiron-3650"
	session1 = "serial-ttyusb0"
	#crt.Session.ConnectInTab("/S \""+ session2 + "\"")
	crt.Screen.Send("Pass=0") 
	crt.Screen.Send("\r")
	crt.Screen.Send("Fail=0")
	crt.Screen.Send("\r")
	crt.Screen.Send("Retry=1")
	crt.Screen.Send("\r")
	
	crt.Screen.Send("ls")
	crt.Screen.Send("\r")
	crt.Screen.Send("\r")
	crt.Screen.Send("s=0")
	crt.Screen.Send("\r")
	crt.Screen.Send("s=` expr $s + 1`")
	crt.Screen.Send("\r")
	crt.Screen.Send("echo S=$s")
	crt.Screen.Send("\r")
	crt.Screen.Send("echo  'Retry= \'$Retry\' --------> Pass= \'$Pass\' --------> Fail= \'$Fail\'' >> /home/quynh/Result.txt")
	crt.Screen.Send("\r")

	# szOutput = crt.Screen.ReadString(["error", "warning", "#"], 10)

	# index = crt.Screen.MatchIndex

	# if (index == 0):

 #   		crt.Dialog.MessageBox("Timed out!")

	# elif (index == 1):

 #   		crt.Dialog.MessageBox("Found 'error'")

	# elif (index == 2):

 #   		crt.Dialog.MessageBox("Found 'warning'")

	# elif (index == 3):

 #   		crt.Dialog.MessageBox("Found '#'")
 	#$language = "Python"

#$interface = "1.0"

 



	# send the selected text to the clipboard

	# crt.Clipboard.Text = crt.Screen.Selection

	# # Extract the selected text from the clipboard into a variable as "Text"

	# szSelection = crt.Clipboard.Text

	# # Now search on Google for the information.

	# g_szURL = "http://www.google.com/search?q=" + szSelection

	# webbrowser.open(g_szURL)
	# if (crt.Screen.WaitForString("ogin:", 10) != True):

	# 	crt.Dialog.MessageBox("Failed to detect login!")
Main()