from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://formy-project.herokuapp.com/')
import time


# first_name = driver.find_element(By.NAME,'firstname')
# first_name.send_keys('George')
# driver.find_element(By.ID, 'sex-0').click()
# driver.find_element(By.ID, 'exp-0').click()
# last_name = driver.find_element(By.NAME,'lastname')
# last_name.send_keys('Carp')
# date = driver.find_element(By.NAME,'datapicker')
# date.send_keys('23.12.2022')
# driver.find_element(By.LINK_TEXT, 'Checkbox').click()
# driver.find_element(By.ID, 'checkbox-2').click()
# driver.find_element(By.LINK_TEXT,'Datepicker').click()
# time.sleep(3)
# driver.find_element(By.ID,'datepicker').click()
# driver.find_element(By.LINK_TEXT,'new-tab-button').click()
# time.sleep(3)
# driver.find_element(By.PARTIAL_LINK_TEXT, 'Disabled').click()
# time.sleep(3)
# driver.find_element(By.PARTIAL_LINK_TEXT, 'Enabled').click()
# time.sleep(3)
# driver.find_element(By.PARTIAL_LINK_TEXT,'Drag').click()
# time.sleep(3)
# driver.find_element(By.ID,'box').click()
# time.sleep(3)


# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.get('http://www.seleniumframework.com/Practiceform/')
# import time
#
# driver.get('http://www.seleniumframework.com/Practiceform/')
# driver.find_element(By.NAME, 'email').send_keys('asass@ggg.com')
# time.sleep(3)
# driver.find_element(By.NAME, 'name').send_keys('Bill')
# time.sleep(3)
# driver.find_element(By.NAME, 'country').send_keys('Romania')
# time.sleep(3)
# driver.find_element(By.NAME, 'company').send_keys('Facebook')
# time.sleep(3)

# driver.get('https://formy-project.herokuapp.com/form')
# driver.find_element(By.TAG_NAME, 'input').send_keys('George')
# time.sleep(2)
# input_list = driver.find_elements(By.TAG_NAME, 'input')
# input_list[1].send_keys('Carp')
# time.sleep(2)
# input_list[2].send_keys('CEO')
# time.sleep(2)
# driver.find_element(By.ID, 'radio-button-3').click()
# time.sleep(2)
# driver.find_element(By.ID, 'checkbox-3').click()
# time.sleep(2)
# driver.find_element(By.ID, 'select-menu').click()


# driver.get('https://www.techlistic.com/p/selenium-practice-form.html')
# driver.find_element(By.TAG_NAME, 'input').send_keys('George')
# input_list = driver.find_elements(By.TAG_NAME, 'input')
# input_list[1].send_keys('Carp')
# time.sleep(2)

# driver.get('https://formy-project.herokuapp.com/form')
# driver.find_element(By.CLASS_NAME, 'form-control').send_keys('George')
# time.sleep(2)
# driver.find_elements(By.CLASS_NAME, 'form-control')[1].send_keys('Carp')
# time.sleep(2)
# driver.find_elements(By.CLASS_NAME, 'form-control')[2].send_keys('CEO')
# time.sleep(2)


# driver.get('http://www.seleniumframework.com/Practiceform/')
# driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Name *"]').send_keys('George')
# driver.find_element(By.CSS_SELECTOR, 'input[placeholder="E-mail *"]').send_keys('carpgeorge11@yahoo.com')
# driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Telephone *"]').send_keys('0740966382')
# time.sleep(3)