from colorama import init, Fore, Back, Style
import random
import os
import socket

init()

#colors
RED = Fore.RED
GRAY = Fore.LIGHTBLACK_EX
GREEN = Fore.GREEN

socket = socket.socket()



print(RED + "~"*50)

print(GRAY + """

██████╗░███████╗██████╗░░██████╗███████╗░█████╗░
██╔══██╗██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗
██║░░██║█████╗░░██║░░██║╚█████╗░█████╗░░██║░░╚═╝
██║░░██║██╔══╝░░██║░░██║░╚═══██╗██╔══╝░░██║░░██╗
██████╔╝███████╗██████╔╝██████╔╝███████╗╚█████╔╝
╚═════╝░╚══════╝╚═════╝░╚═════╝░╚══════╝░╚════╝░

""")

print(RED + "~"*50)
print(RED + "_"*50)

print(GRAY + "1.Scan_Port")



print(GRAY)


menu_menu = input("Choice: ")



if menu_menu == "1":

	print(RED + "~"*50)

	print(GRAY)

	host = input("Enter the host: ")
	port = int(input("Enter the port: "))

	try:
		socket.connect((host, port))
	except socket.error:
		print(RED + "[-]" + GRAY + "Port " + GRAY + "is closed")
	else:
		print(GREEN + "[+]" + GRAY + "Port " + GRAY + "is opened")