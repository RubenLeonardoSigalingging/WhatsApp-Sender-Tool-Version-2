#!/usr/bin/env python3


# Created By: Ruben Leonardo Sigalingging.
# Created On: Saturday, June 25, 2022, 12:41 PM.
# Function: WhatsApp Messaging Tool, Using Python


# Dibuat Oleh: Ruben Leonardo Sigalingging.
# Dibuat Pada: Sabtu, 25 Juni 2022, 12:41.
# Fungsi: Alat Pesan WhatsApp, Menggunakan Python


# Send a WhatsApp Message to a Contact at 1:30 PM
# Kirim Pesan WhatsApp ke Kontak pada 13:30
def sender(created_by="Ruben Leonardo Sigalingging."):
	import pywhatkit
	# https://pypi.org/project/pywhatkit/
	from os import system
	system("chmod 777 WhatsAppSenderToolV2.py")
	system("clear")
	system("pip install pywhatkit")
	from pyfiglet import figlet_format
	tema=figlet_format("PyWhatKit",font="slant")
	print(tema)
	print("[!] Created By: Ruben Leonardo Sigalingging.")
	print("[!] Created On: Saturday, June 25, 2022, 12:41 PM.")
	print("[!] Function: WhatsApp Messaging Tool, Using Python.\n")


	phone_number=input("[!] Enter Phone Number: ")
	message=input("[!] Enter Message: ")
	hour=input("[!] Enter Hour: ")
	hour=int(hour)
	minute=input("[!] Enter Minutes: ")
	minute=int(minute)
	print("")
	pywhatkit.sendwhatmsg(phone_number,message,hour,minute)
# sender()


# Kirim Gambar ke Grup dengan Caption as Hello
def whatsapp_sender_tools_v2(created_by="Ruben Leonardo Sigalingging."):
	import pywhatkit
	# https://pypi.org/project/pywhatkit/
	from os import system
	system("chmod 777 WhatsAppSenderToolV2.py")
	system("clear")
	system("pip install pywhatkit")
	from pyfiglet import figlet_format
	tema=figlet_format("PyWhatKit",font="slant")
	print(tema)
	print("[!] Created By: Ruben Leonardo Sigalingging.")
	print("[!] Created On: Saturday, June 25, 2022, 12:41 PM.")
	print("[!] Function: WhatsApp Messaging Tool, Using Python.\n")


	phone_number=input("[!] Enter Phone Number: ")
	image=input("[!] Input Image File: ")
	print("")
	pywhatkit.sendwhats_image(phone_number,image)
# whatsapp_sender_tools_v2()


# Kirim Pesan WhatsApp ke Grup pada 12:00 AM
def whatsapp_sender_tools_v3(created_by="Ruben Leonardo Sigalingging."):
	import pywhatkit
	# https://pypi.org/project/pywhatkit/
	from os import system
	system("chmod 777 WhatsAppSenderToolV2.py")
	system("clear")
	system("pip install pywhatkit")
	from pyfiglet import figlet_format
	tema=figlet_format("PyWhatKit",font="slant")
	print(tema)
	print("[!] Created By: Ruben Leonardo Sigalingging.")
	print("[!] Created On: Saturday, June 25, 2022, 12:41 PM.")
	print("[!] Function: WhatsApp Messaging Tool, Using Python.\n")


	group=input("[!] Enter Group Name: ")
	message=input("[!] Input Message: ")
	hour=input("[!] Enter Hour: ")
	hour=int(hour)
	minute=input("[!] Enter Minutes: ")
	minute=int(minute)
	print("")
	pywhatkit.sendwhatmsg_to_group(group,message,hour,minute)
# whatsapp_sender_tools_v3()


# Play a Video on YouTube
def whatsapp_sender_tools_v4(created_by="Ruben Leonardo Sigalingging."):
	import pywhatkit
	# https://pypi.org/project/pywhatkit/
	from os import system
	system("chmod 777 WhatsAppSenderToolV2.py")
	system("clear")
	system("pip install pywhatkit")
	from pyfiglet import figlet_format
	tema=figlet_format("PyWhatKit",font="slant")
	print(tema)
	print("[!] Created By: Ruben Leonardo Sigalingging.")
	print("[!] Created On: Saturday, June 25, 2022, 12:41 PM.")
	print("[!] Function: WhatsApp Messaging Tool, Using Python.\n")


	# Putar Video di YouTube
	link=input("[!] YouTube Video Link: ")
	pywhatkit.playonyt(link)
# whatsapp_sender_tools_v4()


# Tanya user
def whatsapp_sender_tools(created_by="Ruben Leonardo Sigalingging"):
	# https://pypi.org/project/pywhatkit/
	from os import system
	system("chmod 777 WhatsAppSenderToolV2.py")
	system("clear")
	system("pip install pywhatkit")
	from pyfiglet import figlet_format
	tema=figlet_format("PyWhatKit",font="slant")
	print(tema)
	print("[!] Created By: Ruben Leonardo Sigalingging.")
	print("[!] Created On: Saturday, June 25, 2022, 12:41 PM.")
	print("[!] Function: WhatsApp Messaging Tool, Using Python.\n")


	print("[1] Send A WhatsApp Message To A Contact")
	print("[2] Send An Image To A Group With The Caption")
	print("[3] Send A WhatsApp Message To A Group")
	print("[4] Play A Video On YouTube")
	print("\n")
	tanya=int(input("[!] Enter Your Choices: "))
	print("\n")
	if tanya == 1:
		sender()


	elif tanya == 2:
		whatsapp_sender_tools_v2()


	elif tanya == 3:
		whatsapp_sender_tools_v3()


	elif tanya == 4:
		whatsapp_sender_tools_v4()
whatsapp_sender_tools()