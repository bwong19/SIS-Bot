from tokenize import String
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from getpass import getpass

import datetime
import os
import sys

def dismiss_warnings(browser, prompt_type: String):
    try:
        yes = browser.find_element_by_id('ctl00_contentPlaceHolder_rb{prompt_type}Yes')
        cont = browser.find_element_by_id('ctl00_contentPlaceHolder_cmdContinue')
        WebDriverWait(browser, 10)
        yes.click()
        WebDriverWait(browser, 10)
        cont.click()
        return True
    except:
        return False


try:
	usernameStr = sys.argv[1]
except BaseException:
	print("\nError: This script should be run with the following (valid) flags:\n python bot.py <jhed@jh.edu>\n")
	sys.exit(-1)
 
passwordStr = getpass()

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get(('https://sis.jhu.edu/sswf/'))
nextButton = browser.find_element_by_id('linkSignIn')
WebDriverWait(browser, 10)
nextButton.click()
WebDriverWait(browser, 10)

username = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.NAME, 'loginfmt')))
username.send_keys(usernameStr)

WebDriverWait(browser, 10)
submit1button = browser.find_element_by_id("idSIButton9")
submit1button.click()

WebDriverWait(browser, 10)
password = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.NAME, 'passwd')))
password.send_keys(passwordStr)

WebDriverWait(browser, 10)
staleElement = True

while staleElement:
    try:
        submit = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.ID, 'idSIButton9')))
        submit.click()
        staleElement = False
    except StaleElementReferenceException:
        staleElement = True

WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "aspnetForm")))

browser.get("https://sis.jhu.edu/sswf/SSS/EnrollmentCart/SSS_EnrollmentCart.aspx?MyIndex=88199")

wait = WebDriverWait(browser, 10)
selectAll = wait.until(EC.element_to_be_clickable((By.ID, 'SelectAllCheckBox')))
selectAll.click()

WebDriverWait(browser, 10)
register = browser.find_element_by_id("ctl00_contentPlaceHolder_ibEnroll")

# Wait until its 7 O'clock
while True:
    hr = datetime.datetime.now().time().hour
    min = datetime.datetime.now().time().minute
    if hr >= 7:
        browser.execute_script("arguments[0].click();", register)
        WebDriverWait(browser, 10000)
        
        warning = True
        while warning:
            warning = False
            warning |= dismiss_warnings(browser, 'Waitlist')
            warning |= dismiss_warnings(browser, 'Override')
            warning |= dismiss_warnings(browser, 'Approval')
        break

