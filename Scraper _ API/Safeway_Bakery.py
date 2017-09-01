# This code extracts all the Bakery products data from Safeway.com
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
bakery = []
bprice = []
# Scraping all bakery items and their prices
driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Bread-Bakery/Bakery-Bread/Sandwich-Bread")
sandwich = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for item in sandwich:
    bakery.append(item.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    bprice.append(pri.get_attribute('value'))
    
driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Bread-Bakery/Bakery-Bread/Baguettes-Loaves")
baguettes = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for s in baguettes:
    bakery.append(s.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    bprice.append(pri.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Bread-Bakery/Bakery-Bread/Sandwich-Rolls")
rolls = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for s in rolls:
    bakery.append(s.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    bprice.append(pri.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Bread-Bakery/Bakery-Bread/Flatbread-Pita-Bread")
flatbread = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for s in flatbread:
    bakery.append(s.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    bprice.append(pri.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Bread-Bakery/Bakery-Desserts-Snacks/Brownies-Cookies")
browny = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for s in browny:
    bakery.append(s.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    bprice.append(pri.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Bread-Bakery/Bakery-Desserts-Snacks/Cakes")
cake = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for s in cake:
    bakery.append(s.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    bprice.append(pri.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Bread-Bakery/Bakery-Desserts-Snacks/Pies-Tarts-Cobblers")
pies = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for s in pies:
    bakery.append(s.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    bprice.append(pri.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Bread-Bakery/Breakfast-Bakery/Bagels")
bagels = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for s in bagels:
    bakery.append(s.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    bprice.append(pri.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Bread-Bakery/Breakfast-Bakery/Breakfast-Loaves")
loaves = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for s in loaves:
    bakery.append(s.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    bprice.append(pri.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Bread-Bakery/Breakfast-Bakery/Donuts")
donuts = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for s in donuts:
    bakery.append(s.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    bprice.append(pri.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Bread-Bakery/Breakfast-Bakery/Pastries-Croissants")
pastries = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for s in pastries:
    bakery.append(s.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    bprice.append(pri.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Bread-Bakery/Breakfast-Bakery/Muffins-Scones")
muffins = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for s in muffins:
    bakery.append(s.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    bprice.append(pri.get_attribute('value'))

# Writing stuff to csv
title = 'Safeway_Bakery.csv'
location = 'csv_Files/' + title
csv_file = open(location, 'wb')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Product', 'Price'])
for i in range(len(bakery)):
    csv_writer.writerow([bakery[i],bprice[i]])
csv_file.close()


