import sys
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time

def tinderBot(user="",password=""):
	url = 'https://tinder.com/'
	binary = FirefoxBinary()
	driver = webdriver.Firefox()
	driver.get(url)

    #login into tinder
    login_tinder(driver, user, passwd)

    #Starting search 
    search_match(driver, odd)
	
    driver.implicitly_wait(10)

	#Navigate to the application home page and loggin
	driver.get(url)
	driver.implicitly_wait(10)

	user_field = driver.find_element_by_id('login')
	user_field.clear()
	user_field.send_keys(user)

	pass_field = driver.find_element_by_id('passwd')
	pass_field.clear()
	pass_field.send_keys(password)

	entrer_button = driver.find_element_by_id('nsg-x1-logon-button')
	entrer_button.click()

	driver.implicitly_wait(15)
	#Enter in a register schedule application
	register_app_button = driver.find_element_by_link_text('Registro de Jornada')
	driver.find_element_by_xpath
	register_app_button.click()

	driver.implicitly_wait(20)
	time.sleep(15)
	# Hacemos foco sobre la nueva pestaña
	driver.switch_to.window(driver.window_handles[1])

	inicio_jornada_button = driver.find_element_by_css_selector('button.c-button')
	inicio_jornada_button.click()

if __name__ == '__main__':
	user = sys.argv[1]
	passwd = sys.argv[2]
	print("Iniciando tinderBot de >> {} ".format(user))
	tinderBot(user,passwd)

search_match(driver)
    pass
login_tinder(driver,user, passwd)
    x_button = driver.find_element_by_xpath('/html/body/div[2]/div/div/button')
	x_button.click()

	inicia_session = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button/span')
	inicia_session.click()

	facebook_session = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/span/div[2]/button/span[2]')
	facebook_session.click()

	driver.switch_to.window(driver.window_handles[1])
	
	user_fb = driver.find_element_by_css_selector('#email')
	user_fb.send_keys(user)

	pass_fb = driver.find_element_by_css_selector('#pass')
	pass_fb.send_keys(passwd)

	entrar_fb = driver.find_element_by_xpath('//*[@id="u_0_0"]')
	entrar_fb.click()
	
	driver.implicitly_wait(60)

