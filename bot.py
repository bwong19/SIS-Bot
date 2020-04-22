from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.support.ui import Select 
import datetime
import os 
import sys

EMAILFIELD = (By.ID, "i0116")
PASSWORDFIELD = (By.ID, "i0118")
NEXTBUTTON = (By.ID, "idSIButton9")

try:
	usernameStr = sys.argv[1]
	passwordStr = sys.argv[2]
except BaseException:
	print("\nError: This script should be run with the following (valid) flags:\n python bot.py <jhed@jh.edu> SIS_Password\n")
	sys.exit(-1)

browser = webdriver.Chrome()
browser.get(('https://sis.jhu.edu/sswf/'))

nextButton = browser.find_element_by_id('linkSignIn')
nextButton.click()

WebDriverWait(browser, 10).until(EC.element_to_be_clickable(EMAILFIELD)).send_keys(usernameStr)
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(NEXTBUTTON)).click()
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(PASSWORDFIELD)).send_keys(passwordStr)
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(NEXTBUTTON)).click()


WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "aspnetForm")))
browser.get("https://sis.jhu.edu/sswf/SSS/EnrollmentCart/SSS_EnrollmentCart.aspx?MyIndex=88199")


WebDriverWait(browser, 10).until(lambda d: d.find_element_by_id('SelectAllCheckBox'))
selectAll = browser.find_element_by_id("SelectAllCheckBox")
selectAll.click()

WebDriverWait(browser, 10).until(lambda d: d.find_element_by_id('ctl00_contentPlaceHolder_ibEnroll'))
register = browser.find_element_by_id("ctl00_contentPlaceHolder_ibEnroll")

# Wait until its 7 O'clock
while True:
    current_hour = datetime.datetime.now().time().hour
    current_time = datetime.datetime.now()

    time = current_time.strftime("%H:%M:%S")
    print(time, end="\r")

    try:
        alert = browser.switch_to.alert
        alert.accept()
    except:
        pass

    if current_hour >= 7:
        register.click()
        WebDriverWait(browser, 10000)
        clear = False
        while warning:
            warning = False
            try:
                yes = browser.find_element_by_id('ctl00_contentPlaceHolder_rbWaitlistYes')
                cont = browser.find_element_by_id('ctl00_contentPlaceHolder_cmdContinue')
                yes.click()
                WebDriverWait(browser, 10)
                cont.click()
                warning = True
            except:
                pass
            try:
                yes = browser.find_element_by_id('ctl00_contentPlaceHolder_rbOverrideYes')
                cont = browser.find_element_by_id('ctl00_contentPlaceHolder_cmdContinue')
                yes.click()
                WebDriverWait(browser, 10)
                cont.click()
                warning = True
            except:
                pass
            try:
                yes = browser.find_element_by_id('ctl00_contentPlaceHolder_rbApprovalYes')
                cont = browser.find_element_by_id('ctl00_contentPlaceHolder_cmdContinue')
                yes.click()
                WebDriverWait(browser, 10)
                cont.click()
                warning = True
            except:
                pass
        break
