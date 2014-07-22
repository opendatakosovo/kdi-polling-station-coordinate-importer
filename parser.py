import csv

from pymongo import MongoClient
from bson import ObjectId

# Connect to default local instance of mongo
client = MongoClient()

# Get database and collection
db = client.kdi
collection = db.localelectionsfirstround2013

def result():

	with open('qendrat_votimit.csv', 'rb') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		for row in reader:
			lat = row[4]
			lon = row[5]
			
			stationNumber=row[6].lower()
			
			print(stationNumber + ': ' + lat + ' - ' + lon)
			cursor = collection.find({'pollingStation.number':stationNumber})
	
			
			if cursor.count() == 0:
				print("not matched " + stationNumber)
			else:
				
				
				collection.update({'pollingStation.number':stationNumber},{'$set':{'pollingStation.coordinates':{'lat':lat,'lon':lon}}},multi=True)
				
			

result()



