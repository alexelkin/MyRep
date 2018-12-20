
#http://charityapi.orghunter.com/content/charity-search-summary-api

import requests
import json

key = '7c60a4592b8cd66f0eaebba83a9e93db'

url = "http://data.orghunter.com/v1/charitysearch"
fullURL = url + '?user_key=' + key + '&zipCode=01740'

print( 'Testing: ' + fullURL )

param = { 'zipCode' : '01720', 'user_key' : key }
head = {'Content-type':'application/json',
             'Accept':'application/json'}

jObj = json.dumps(param)

#ret = requests.post(url,header=head,data=jObj)

ret = requests.post(url,params=param)

#ret = requests.get(fullURL)

print( ret )

jData = json.loads( ret.content )
print( jData )
for line in jData['data']:
    print( line['charityName'] )

for key in jData:
        print(key + " : " + jData[key])

