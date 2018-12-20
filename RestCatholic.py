
# Useful: https://techietweak.wordpress.com/2015/03/30/http-restful-api-with-python-requests-library/
# Useful: https://stackoverflow.com/questions/17301938/making-a-request-to-a-restful-api-using-python

# Public services https://github.com/toddmotto/public-apis/blob/master/README.md
# https://www.quora.com/Where-can-I-find-Free-Public-REST-APIs-preferably-JSON

import requests
import json

url = 'http://calapi.inadiutorium.cz'

calendars = '/api/v0/en/calendars'

query1 = '/api/v0/en//calendars/default/2018/12'


query = '''
{
  "system": {
    "promulgated": 1969,
    "effective_since": 1970,
    "desc": "promulgated by motu proprio Mysterii Paschalis of Paul VI. (AAS 61 (1969), pp. 222-226)."
  },
  "sanctorale": {
    "title": "Calendarium Romanum Generale",
    "language": "la"
  }
}
'''

ret = requests.get(url + query1)
print( ret )

jData = json.loads( ret.content )
print( jData )
for line in jData:
    print( line )

