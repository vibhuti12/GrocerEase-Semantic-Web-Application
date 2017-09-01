# This code extracts all the breakfast & cereals data from Safeway.com
# and makes csv file of the same

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv
chrome_path="C:\Python27\Lib\chromedriver_win32\chromedriver.exe"
driver=webdriver.Chrome(chrome_path)
wait = WebDriverWait(driver, 10)
driver.get("https://shop.safeway.com/ecom/account/sign-in")
inputZip=driver.find_element_by_id("Register_ZipCode")
inputZip.send_keys('85281')
driver.find_element_by_name("Browse").click()
driver.find_element_by_xpath('''//*[@id="toPushFooter"]/div[1]/div/div[9]/ul/li[2]/a''').click()
driver.get("https://shop.safeway.com/ecom/shop-by-aisle")
menu = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "area-navigateMenu")))
unordered_list = menu.find_elements_by_tag_name('ul')
cereal = []
cprice = []

# Printing all cereals and their prices
driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Breakfast-Cereal/Cereal/Cereal--All-Family")
normal = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for item in normal:
    cereal.append(item.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    cprice.append(pri.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Breakfast-Cereal/Cereal/Cereal--NaturalOrganic")
organic = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for item in organic:
    cereal.append(item.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    cprice.append(pri.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Breakfast-Cereal/Cereal/Cereal--Sweet")
sweet = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for item in sweet:
    cereal.append(item.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    cprice.append(pri.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Breakfast-Cereal/Cereal/Granola-Muesli")
muesli = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for item in muesli:
    cereal.append(item.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    cprice.append(pri.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Breakfast-Cereal/Cereal/Oatmeal-Hot-Cereal")
oatmeal = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for item in oatmeal:
    cereal.append(item.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    cprice.append(pri.get_attribute('value'))

# Writing stuff to csv
title = 'Safeway_Cereals.csv'
location = 'csv_Files/' + title
csv_file = open(location, 'wb')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Product', 'Price'])
for i in range(len(cereal)):
    csv_writer.writerow([cereal[i],cprice[i]])
csv_file.close()
