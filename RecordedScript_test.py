# $language = "python"
# $interface = "1.0"

# This automatically generated script may need to be
# edited in order to work correctly.

def Main():
	crt.Screen.Synchronous = True
	crt.Screen.Send(chr(10) + chr(13))
	crt.Screen.WaitForString("login: ")
	crt.Screen.Send("ambit" + chr(10) + "ambitdebug" + chr(10) + "retsh foxconn168!" + chr(10) + chr(10) + chr(10) + chr(10) + chr(10) + chr(10) + chr(10) + chr(10) + chr(10))

Main()
