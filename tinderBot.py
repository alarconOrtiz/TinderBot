import sys
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import time
import random

def tinderBot(user="", passwd=""):
	url = 'https://tinder.com/'
	profile = FirefoxProfile()

	profile.set_preference("pdfjs.disabled", True)
	profile.set_preference("dom.webnotifications.enabled", True)
	profile.set_preference("geo.enabled", True)
	profile.set_preference("geo.provider.use_corelocation", True)
	profile.set_preference("geo.prompt.testing", True)
	profile.set_preference("geo.prompt.testing.allow", True)
	profile.set_preference("geo.wifi.uri", "path-to-loglatjson\\geo-location-ITPL.json")
	profile.set_preference("profile.default_content_setting_values.notifications", True)

	driver = webdriver.Firefox(profile)
	driver.get(url)

    #login into tinder
	login_tinder(driver, user, passwd)

	#permision Tinder
	avai =  driver.find_element_by_css_selector('button.Ov\(h\):nth-child(1)')
	avai.click()

	try:
		alert = driver.switch_to.alert
		alert.accept()
	except :
		print("ERROR : closing notification permesion")

	time.sleep(3)

	avai = driver.find_element_by_css_selector('button.Ell:nth-child(1) > span:nth-child(1)')
	avai.click()

    #Starting search 
	search_match(driver,odd=0.9)

def login_tinder(driver, user, passwd):
	time.sleep(5)
	loggin_FB = driver.find_elements_by_xpath('//*[text()=\'Inicia sesión con Facebook\']')

	if loggin_FB :
		loggin_FB[0].click()
	else:
		mas_opciones = driver.find_element_by_css_selector('button.Td\(u\):nth-child(3)')
		mas_opciones.click()
		time.sleep(1)
		loggin_FB = driver.find_elements_by_xpath('//*[text()=\'Inicia sesión con Facebook\']')
		loggin_FB[0].click()
	
	#boton cookies
	cookies_accept = driver.find_element_by_css_selector('.Pt\(8px\) > div:nth-child(1) > button:nth-child(1) > span:nth-child(1)')
	cookies_accept.click()
	
	time.sleep(3)
	
	driver.switch_to.window(driver.window_handles[1])
	user_fb = driver.find_element_by_css_selector('#email')
	user_fb.send_keys(user)

	pass_fb = driver.find_element_by_css_selector('#pass')
	pass_fb.send_keys(passwd)

	entrar_fb = driver.find_element_by_xpath('//*[@id="u_0_0"]')
	entrar_fb.click()

	driver.implicitly_wait(30)
	
	driver.switch_to.window(driver.window_handles[0])
	

def search_match(driver,odd):
	like = 0
	dislike = 0
	while True:
		time.sleep(5)
		if random.random() < odd:
			likeBt = driver.find_element_by_css_selector('div.Mx\(a\):nth-child(4) > button:nth-child(1) > span:nth-child(1) > svg:nth-child(1) > path:nth-child(1)')
			likeBt.click()
			print("Like ", like)
			like +=1
		else:
			dislikeBT = driver.find_element_by_css_selector('div.Sq\(70px\):nth-child(2) > button:nth-child(1) > span:nth-child(1) > svg:nth-child(1) > path:nth-child(1)')
			dislikeBT.click()
			print("disLike ", dislike)
			dislike +=1
		

def clickButtonJS(driver,xpath):
	try:
		button = driver.find_element_by_xpath(xpath)
		button.click()
		return True
	except:
		return False 
	

if __name__ == '__main__':
	user = sys.argv[1]
	passwd = sys.argv[2]
	print("Iniciando tinderBot de >> {} ".format(user))
	tinderBot(user,passwd)