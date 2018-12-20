
#https://mailboxlayer.com/documentation

import requests
import json

key = '6e2c3442fb5ebbd6aa0f4126b4074910'

url = "http://apilayer.net/api/check?"

calendars = '/api/v0/en/calendars'

fullURL = url + 'access_key=' + key + '&email=support@timelinepi.com'

print( 'Testing: ' + fullURL )

str = '''
http://apilayer.net/api/check
    ? access_key = 6e2c3442fb5ebbd6aa0f4126b4074910
    & email = the.north.window@gmail.com
'''

ret = requests.get(fullURL)
print( ret )

jData = json.loads( ret.content )
print( jData )
for line in jData:
    print( line )
