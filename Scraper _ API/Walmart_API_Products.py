#This code below extracts the Products data using Walmart API.

import urllib2
import json
import csv
import sys;
reload(sys);
sys.setdefaultencoding("utf8")

apiKey = '86g35ew2ufsxjk33evj9vevk'

#The keyList below provides the set of input Category_IDs of walmart Product Groups whose data is to be extracted.
#The keys below have been further extracted through Walmart API using another source code.
keyList = ['976759_976783_1231208', '976759_976783_1231210', '976759_1071964_976779', '976759_1071964_976788', '976759_976783_1001417\
']


#The code below extracts the Products data and writes them into respective CSV files based on the index assigned to the categories.
i=0
while i < 5:
	if i == 0:
		csv_title = 'Walmart_Cold_Cereal.csv'
		url = 'http://api.walmartlabs.com/v1/paginated/items?format=json&category='
		key = keyList[0]
	elif i == 1:
		csv_title = 'Walmart_Oatmal_&_Hot.csv'
		url = 'http://api.walmartlabs.com/v1/paginated/items?format=json&category='
		key = keyList[1]
	elif i == 2:
		csv_title = 'Walmart_Bakery.csv'
		url = 'http://api.walmartlabs.com/v1/paginated/items?format=json&category=' 
		key = keyList[2]
	elif i == 3:
		csv_title = 'Walmart_Dairy.csv'
		url = 'http://api.walmartlabs.com/v1/paginated/items?format=json&category='
		key = keyList[3]
	elif i == 4: 
		csv_title = 'Walmart_Frozen_Breakfast.csv'
		url = 'http://api.walmartlabs.com/v1/paginated/items?format=json&category='
		key = keyList[4]
	
	csv_location = 'Updated_CSV/' + csv_title	
	csv_File = open(csv_location, 'w')
	csvwriter = csv.writer(csv_File)
	
	csvwriter.writerow(['Prod_id', 'Prod_name', 'Prod_price', 'Prod_size', 'Prod_stock', 'Prod_brand',\
	'Prod_Model', 'Prod_Desc', 'Prod_Img', 'Prod_Rating', 'Prod_review', 'Prod_Shipping'])
	
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
	i +=1   
	print 'Done successfully'
  
