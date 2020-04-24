import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Chrome()

driver.get("http://172.20.100.43/eem/")
driver.maximize_window()
driver.switch_to.frame(1)
driver.switch_to.frame(0)
# driver.find_element(By.NAME, "user").send_keys("12057897")
# driver.find_element(By.NAME, "pwd").send_keys("159753\n")

driver.find_element_by_name('user').send_keys("12057897")
driver.find_element_by_name('pwd').send_keys('159753\n')

time.sleep(2)
driver.switch_to.frame('loginMainFrame')
driver.switch_to.frame('mainFrame')
driver.find_element_by_name('imageField1').click()

time.sleep(2)
driver.switch_to.frame('loginMainFrame')
ele = driver.find_element_by_css_selector("td:nth-child(3) .menus")
ActionChains(driver).move_to_element(ele).perform()
driver.find_element_by_css_selector("tr:nth-child(4) .submenus").click()

time.sleep(2)
driver.switch_to.frame('loginMainFrame')
driver.find_element_by_css_selector("tr:nth-child(2) .button").click()
driver.find_element_by_css_selector("form3_main_date").click()
