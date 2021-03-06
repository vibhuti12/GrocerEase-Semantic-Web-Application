#The code below extracts the CategoryID of the product groups from Walmart using its API.
#The IDs so extracted are further used in extracting the Products from Walmart.

import urllib2
import json
import csv

apiKey = '86g35ew2ufsxjk33evj9vevk'
#query = 'tv'
#filtr = 'facet=on&facet.filter=brand:Samsung'
url = 'http://api.walmartlabs.com/v1/taxonomy?format=json&apiKey=' + apiKey
json_obj = urllib2.urlopen(url)
data_dict = json.load(json_obj)
#We can't print json_obj
#print json_obj

walmart_prod = open('Walmart_product.csv', 'w')
csvwriter = csv.writer(walmart_prod)
i = 1
for item in data_dict['categories']:
    #print 'Category: ', i
    prod_id  = item['id']
    prod_name= item['name']
    prod_path= item['path']
    csvwriter.writerow([prod_id, prod_name, prod_path])
    if 'children' in item.keys():
        for item_2 in item['children']:
            prod_id  = item_2['id']
            prod_name= item_2['name']
            prod_path= item_2['path']
            csvwriter.writerow([prod_id, prod_name, prod_path])
            if 'children' in item_2.keys():
                for item_3 in item_2['children']:
                    prod_id  = item_3['id']
                    prod_name= item_3['name']
                    prod_path= item_3['path']
                    csvwriter.writerow([prod_id, prod_name, prod_path])

print 'Done successfully'
walmart_prod.close()    
