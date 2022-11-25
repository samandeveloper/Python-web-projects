# In this project we want to import selenium library and use it for automation. For instance we are going to control the url page in the chrome browser!!
# 1. check that your chrome browser is updeted
# 2. download the latest stable version of chrome from https://sites.google.com/a/chromium.org/chromedriver/home
# 3. open the zip folder and move the content (chromedriver.exe) to the same place that we have automation.py 

from selenium import webdriver 
import time 

chrome_browser = webdriver.Chrome('./chromedriver') #Drivers Address
print(chrome_browser)
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
chrome_browser.maximize_window()
#Use title
assert 'Selenium Easy Demo' in chrome_browser.title #Use assert keyword instead of print

time.sleep(5)

show_message_button = chrome_browser.find_element_by_class_name('btn-default')
# print(button)
# print(show_message_button.get_attribute('innerHTML'))	#Show the button's text

assert 'Show Message' in chrome_browser.page_source
#find the id of the input and type in the input box
user_mesasage = chrome_browser.find_element_by_id('user-message')	

#using .find_element_by_css_selector() method
user_button2 = chrome_browser.find_element_by_css_selector('#get-input>.btn')
print(user_button2)

user_mesasage.clear()
user_mesasage.send_keys('I am extra cool!')

# click on the "Show Message" button (add import time and time.sleep() in case .click() method not works)
show_message_button.click()

output_message = chrome_browser.find_element_by_id('display')
assert 'I am extra cool' in output_message.text

# close all the chrome windows 
# chrome_browser.close()  
# chrome_browser.quit()