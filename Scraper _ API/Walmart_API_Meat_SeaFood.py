#This code below extracts the Products data for Meat and Seafood category using Walmart API.
#It is similar to the code for extracting all other Products but it was written alone first to test the code.

import urllib2
import json
import csv
import sys;
reload(sys);
sys.setdefaultencoding("utf8")

apiKey = '86g35ew2ufsxjk33evj9vevk'
key = '976759_1071964_976796'

csv_title = 'Walmart_Meat_Seafood.csv'
csv_location = 'CSV Files/' + csv_title	
csv_File = open(csv_location, 'w')
csvwriter = csv.writer(csv_File)

csvwriter.writerow(['Prod_id', 'Prod_name', 'Prod_price', 'Prod_size', 'Prod_stock', 'Prod_brand',\
'Prod_Model', 'Prod_Desc', 'Prod_Img', 'Prod_Rating', 'Prod_review', 'Prod_Shipping'])

url = 'http://api.walmartlabs.com/v1/paginated/items?format=json&category='
url_final = url + key +'&apiKey=' + apiKey
json_obj = urllib2.urlopen(url_final)
data_dict = json.load(json_obj)

for item in data_dict['items']:
	#print 'Category: ', i
	prod_id       = item['itemId']
	prod_name     = item['name']
	prod_price    = ''
	prod_size     = ''
	prod_brand    = ''
	prod_stock    = ''
	prod_model    = ''
	prod_rating   = ''
	prod_reviews  = ''
	prod_shipping = ''
	prod_desc     = ''
	prod_img      = ''
	if 'salePrice' in item.keys(): 
		prod_price= item['salePrice']
	
	if 'size' in item.keys():
		prod_size = item['size']
	
	if 'stock' in item.keys():
		prod_stock = item['stock']
	
	if 'brandName' in item.keys() and 'modelNumber' in item.keys():
		prod_brand = item['brandName']
		prod_model = item['modelNumber']
		
	if 'shortDescription' in item.keys():
		prod_desc = item['shortDescription']
		
	if 'mediumImage' in item.keys():
		prod_img = item['mediumImage']
	
	if 'customerRating' in item.keys() and 'numReviews' in item.keys():
		prod_rating = item['customerRating']
		prod_reviews = item['numReviews']
		
	if 'freeShippingOver50Dollars' in item.keys():	
		prod_shipping = item['freeShippingOver50Dollars']   
	
	csvwriter.writerow([prod_id, prod_name, prod_price, prod_size, prod_stock, prod_brand,\
	prod_model, prod_desc, prod_img, prod_rating, prod_reviews, prod_shipping])
	#csvwriter.writerow()
csv_File.close()
  
print 'Done successfully'
  
