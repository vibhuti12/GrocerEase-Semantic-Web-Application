# This code extracts all the Dairy products data data from Safeway.com
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

# Scraping all dairy items and their prices and putting them in lists
dairy = []
dprice = []
driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Dairy-Eggs-Cheese/Butter-Sour-Cream/Butter")
da = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for item in da:
    dairy.append(item.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    dprice.append(pri.get_attribute('value'))
    
driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Dairy-Eggs-Cheese/Butter-Sour-Cream/Margarine-Spreads")
spreads = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for s in spreads:
    dairy.append(s.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    dprice.append(pri.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Dairy-Eggs-Cheese/Butter-Sour-Cream/Sour-Cream")
cream = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for s in cream:
    dairy.append(s.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    dprice.append(pri.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Dairy-Eggs-Cheese/Eggs/Eggs")
eggs = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for s in eggs:
    dairy.append(s.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    dprice.append(pri.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Dairy-Eggs-Cheese/Eggs/Eggs")
cotcheese = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for s in cotcheese:
    dairy.append(s.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    dprice.append(pri.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Dairy-Eggs-Cheese/Cheese/Sandwich-Cheese")
sandcheese = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for s in sandcheese:
    dairy.append(s.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    dprice.append(pri.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Dairy-Eggs-Cheese/Cheese/SpreadProcessed-Cheese")
spreadcheese = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for s in spreadcheese:
    dairy.append(s.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    dprice.append(pri.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Dairy-Eggs-Cheese/Milk-Cream/Milk")
milk = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for s in milk:
    dairy.append(s.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    dprice.append(pri.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Dairy-Eggs-Cheese/Milk-Cream/Creamer")
creamer = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for s in creamer:
    dairy.append(s.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    dprice.append(pri.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Dairy-Eggs-Cheese/Milk-Cream/Milk-Alternatives")
milkalt = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for s in milkalt:
    dairy.append(s.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    dprice.append(pri.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Dairy-Eggs-Cheese/Milk-Cream/Milk--Flavored")
flavmilk = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for s in flavmilk:
    dairy.append(s.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    dprice.append(pri.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Dairy-Eggs-Cheese/Milk-Cream/Milk--Lactose-Free")
lactmilk = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for s in lactmilk:
    dairy.append(s.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    dprice.append(pri.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Dairy-Eggs-Cheese/Yogurt/Yogurt")
yogurt = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for s in yogurt:
    dairy.append(s.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    dprice.append(pri.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Dairy-Eggs-Cheese/Yogurt/Kids-Yogurt")
kidsyog = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for s in kidsyog:
    dairy.append(s.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    dprice.append(pri.get_attribute('value'))

driver.get("https://shop.safeway.com/ecom/shop-by-aisle/Dairy-Eggs-Cheese/Yogurt/Greek-Yogurt")
greekyog = driver.find_elements_by_class_name("state-uiFocus-richInfo")
for s in greekyog:
    dairy.append(s.text)
price = driver.find_elements_by_class_name("id-price-qty")
for p in price:
    pr = p.find_element_by_css_selector('.field.id-PricePerSellingUnit')
    pri = pr.find_element_by_tag_name('input')
    dprice.append(pri.get_attribute('value'))

# Writing data to csv

title = 'Safeway_Dairy.csv'
location = 'csv_Files/' + title
csv_file = open(location, 'wb')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Product', 'Price'])
for i in range(len(dairy)):
    csv_writer.writerow([dairy[i],dprice[i]])
csv_file.close()
    

