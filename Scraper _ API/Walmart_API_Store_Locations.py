#This code extracts the Walmart Stores Location details below using the Walmart API.

import urllib2
import json
import csv
import sys;
reload(sys);
sys.setdefaultencoding("utf8")

apiKey = '86g35ew2ufsxjk33evj9vevk'
city = 'tempe'
url = 'http://api.walmartlabs.com/v1/stores?format=json&city=' + city + '&apiKey=' + apiKey
json_obj = urllib2.urlopen(url)
data_dict = json.load(json_obj)

csv_title = 'Walmart_Stores.csv'
csv_location = 'CSV Files/' + csv_title
csv_File = open(csv_location, 'w')
csvwriter = csv.writer(csv_File)
csvwriter.writerow(['Store', 'Store_Num', 'Store_name', 'Latitude', 'Longitude', 'Store_Address', 'Zip', 'Store_Phone_Num'])

for store in data_dict:
	Store_Num 	= store['no']
	Store_name  = store['name']
	Latitude    = store['coordinates'][1]
	Longitude   = store['coordinates'][0]
	Store_Address = store['streetAddress'] + ', ' +store['city'] + ', ' + store['stateProvCode']
	#Store_City  = store['city']
	Zip         = store['zip']
	#State_Prov_Code = store['stateProvCode']
	Store_Phone_Num = store['phoneNumber']
	csvwriter.writerow(['Walmart',Store_Num, Store_name, Latitude, Longitude, Store_Address, Zip, Store_Phone_Num])	
csv_File.close()
print 'Done successfully'
