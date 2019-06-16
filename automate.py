from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome('C:\\Users\\DELL\\Downloads\\Compressed\\chromedriver_win32_2\\chromedriver')
browser.get('http://facebook.com')
email_field = browser.find_element_by_id('email')
password_field = browser.find_element_by_id('pass')
btn_login = browser.find_element_by_id('loginbutton')

email_field.send_keys('enter your email')
password_field.send_keys('enter your password')

btn_login.click();
