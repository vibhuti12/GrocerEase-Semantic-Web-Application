# This code extracts all the fruits & vegetables data from Safeway.com
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
fruits = []
fprice = []

# Printing all Fruits & Vegetables and their prices
driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Fruits-Vegetables/Fresh-Fruits/Apples")
apples = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for item in apples:
    fruits.append(item.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    fprice.append(pri.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Fruits-Vegetables/Fresh-Fruits/Bananas")
bananas = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for item in bananas:
    fruits.append(item.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    fprice.append(pri.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Fruits-Vegetables/Fresh-Fruits/Grapes")
grapes = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for item in grapes:
    fruits.append(item.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    fprice.append(pri.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Fruits-Vegetables/Fresh-Fruits/Citrus")
citrus = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for item in citrus:
    fruits.append(item.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    fprice.append(pri.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Fruits-Vegetables/Fresh-Fruits/Berries")
berries = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for item in berries:
    fruits.append(item.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    fprice.append(pri.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Fruits-Vegetables/Fresh-Fruits/Tropical-Fruit")
tropical = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for item in tropical:
    fruits.append(item.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    fprice.append(pri.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Fruits-Vegetables/Fresh-Vegetables-Herbs/Broccoli-Cauliflower")
broc = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for item in broc:
    fruits.append(item.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    fprice.append(pri.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Fruits-Vegetables/Fresh-Vegetables-Herbs/Cabbages")
cabb = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for item in cabb:
    fruits.append(item.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    fprice.append(pri.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Fruits-Vegetables/Fresh-Vegetables-Herbs/Carrots")
carrots = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for item in carrots:
    fruits.append(item.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    fprice.append(pri.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Fruits-Vegetables/Fresh-Vegetables-Herbs/Herbs")
herbs = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for item in herbs:
    fruits.append(item.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    fprice.append(pri.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Fruits-Vegetables/Fresh-Vegetables-Herbs/Lettuce-Greens")
lettuce = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for item in lettuce:
    fruits.append(item.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    fprice.append(pri.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Fruits-Vegetables/Fresh-Vegetables-Herbs/Mushrooms")
mush = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for item in mush:
    fruits.append(item.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    fprice.append(pri.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Fruits-Vegetables/Fresh-Vegetables-Herbs/Onions-Garlic")
onions = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for item in onions:
    fruits.append(item.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    fprice.append(pri.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Fruits-Vegetables/Fresh-Vegetables-Herbs/Peppers")
pepp = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for item in pepp:
    fruits.append(item.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    fprice.append(pri.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Fruits-Vegetables/Fresh-Vegetables-Herbs/Potatoes-Yams")
potatoes = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for item in potatoes:
    fruits.append(item.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    fprice.append(pri.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Fruits-Vegetables/Fresh-Vegetables-Herbs/Specialty-Vegetables")
spec = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for item in spec:
    fruits.append(item.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    fprice.append(pri.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Fruits-Vegetables/Fresh-Vegetables-Herbs/Tomatoes")
tom = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for item in tom:
    fruits.append(item.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    fprice.append(pri.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Fruits-Vegetables/Packaged-Produce-Tofu/Packaged-Fresh-Fruit")
packfru = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for item in packfru:
    fruits.append(item.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    fprice.append(pri.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Fruits-Vegetables/Packaged-Produce-Tofu/Packaged-Vegetables")
packveg = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for item in packveg:
    fruits.append(item.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    fprice.append(pri.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Fruits-Vegetables/Packaged-Produce-Tofu/Packaged-Salads")
packsal = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for item in packsal:
    fruits.append(item.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    fprice.append(pri.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Fruits-Vegetables/Packaged-Produce-Tofu/Tofu-Meat-Alternatives")
tofu = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for item in tofu:
    fruits.append(item.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    fprice.append(pri.get_attribute('value'))

# Writing stuff to csv
title = 'Safeway_Fruits.csv'
location = 'csv_Files/' + title
csv_file = open(location, 'wb')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Product', 'Price'])
for i in range(len(fruits)):
    csv_writer.writerow([fruits[i],fprice[i]])
csv_file.close()
