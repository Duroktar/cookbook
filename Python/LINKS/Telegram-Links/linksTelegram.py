import os
import time
import pickle
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By



t = 2

#
# service_log_path = "{}/chromedriver.log".format('C:/Users/traBpUkciP/cookbook/cookbook/Python/LINKS/Telegram-Links')
# service_args = ['--verbose']
# path = "C:\\ChromeDriver\\chromedriver.exe"
# os.environ["webdriver.chrome.driver"] = path
# options = Options()
# options.add_argument('user-data-dir=C:\\Users\\traBpUkciP\\AppData\\Local\\Google\\Chrome\\User Data\\default')
# driver = webdriver.Chrome(executable_path=path,
#                           chrome_options=options,
#                           service_args=service_args,
#                           service_log_path=service_log_path)

path = "C:\PhantomJS\bin\phantomjs.exe"
driver = webdriver.PhantomJS()

try:
    driver.get('https://web.telegram.org/#/login')
    # webdriver.ChromeOptions.

    time.sleep(2)
    driver.get_screenshot_as_file('screen.png')
    country_field = driver.find_element_by_class_name('md-input-label')
    # phone = raw_input('Enter your phone number: ')
    # phone_field.send_keys(phone)
    country_field.click()
    time.sleep(2)
    country_box = driver.find_element_by_class_name('ng-touched')
    country_box.click()
    country_box.send_keys('canada')
    country_box.send_keys(Keys.RETURN)
    phone_field = driver.find_element_by_name('phone_number').send_keys("5064499926")
    phone_field.send_keys(Keys.RETURN)
    driver.get_screenshot_as_file('screen2.png')

    time.sleep(t)
    confirm_box = driver.find_element_by_class_name('btn-md-primary')
    confirm_box.send_keys(Keys.RETURN)
    driver.get_screenshot_as_file('screen3.png')

    time.sleep(t)
    code = raw_input('Enter your Telegram Code: ')
    enter_code_box = driver.find_element_by_name('phone_code')
    enter_code_box.send_keys(code)
    enter_code_box.send_keys(Keys.RETURN)
    driver.get_screenshot_as_file('screen4.png')
    print driver.session_id
    driver.get_screenshot_as_png()
    raw_input("Press Enter")
    driver.quit()
    quit()
except Exception as e:
    driver.quit()
    print e


def main():
    raw_input('Press a key to exit')
    quit()
    return

try:

    # clear_terminal_screen()
    print "***Logged in to Facebook***"
    while True:
        main()
except KeyboardInterrupt:
    pass
