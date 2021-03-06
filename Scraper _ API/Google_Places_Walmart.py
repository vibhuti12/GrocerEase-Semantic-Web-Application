#The code below extracts the Points of Interest located around Walmart Stores using Google Places API.

import urllib2
import json
import csv
import sys;
reload(sys);
sys.setdefaultencoding("utf8")

mapKey='AIzaSyBeVAABXr_LFeEeW7s5XJ_kZOCcN5_dqfg'

#The Store_Type variable defines the type of places which we are looking for through the Google Places API.
#We limited the category to 5 different types which further are combination of several other types.
Store_Type = {1:['restaurant', 'cafe', 'bakery'], 2: ['hospital', 'pharmacy'], 3: ['bank', 'atm'], 4: ['gas_station'], 5: ['night_club', 'bar']}

#This is the CSV file which acts as a source of input by providing the latitudes and longitudes of the Walmart Stores around which Points of #Interest have to be found.
csv_File = open('Walmart Data/CSV Files/Walmart_Stores.csv', 'r')
csv_read = csv.reader(csv_File)

url_base = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='

csv_Output = open('POI_near_Walmart.csv', 'w')
csvWriter = csv.writer(csv_Output)
csvWriter.writerow(['Origin_Store', 'Lati', 'Long', 'POI_Name', 'POI_Type', 'POI_Lat', 'POI_Long', 'Place_Icon', 'POI_ID', 'Vicinity'])


#The code below reads the structured data from JSON and writes that into a CSV file.
count = 1
for row in csv_read:
	if count == 1:
		count +=1
		pass
	else:
		lati = row[3]
		loni = row[4]
		radius = 500
		#typo = 'restaurant'
		for k in Store_Type.keys():
			for typ in Store_Type[k]:
				url = url_base+ str(lati) + ',' +str(loni)+'&radius='+ str(radius) + '&type=' + typ +'&key=' + mapKey
				json_obj = urllib2.urlopen(url)
				data_dict = json.load(json_obj)
				data = data_dict['results']

				for place in data:
					plc_lat = place['geometry']['location']['lat']
					plc_lon = place['geometry']['location']['lng']
					plc_nm  = place['name']
					plc_icon= place['icon']
					plc_id  = place['place_id']
			
					plc_string = ' '.join([pl for pl in Store_Type[k]])
					plc_vicnity= place['vicinity']
			
					csvWriter.writerow(['Walmart', lati, loni, plc_nm, plc_string, plc_lat, plc_lon, plc_icon, plc_id, plc_vicnity])
csv_Output.close()
csv_File.close()
print 'Done successfully'


