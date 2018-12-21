# https://webapps.five9.com/assets/files/for_customers/documentation/apis/vcc-agent+supervisor-rest-api-reference-guide.pdf
# https://webapps.five9.com/product-documentation/?ref=community

# {
# "passwordCredentials":{
# "username":"syoung@infodev.com",
# "password":"XXXXXXXX"
#  },
# "policy":"None"
# }

import requests
import json
from pprint import pprint

name = 'TPI-API@sdp.tam'
password = 'TimelinePI2018'

login_param = {
'passwordCredentials':{
    'username':'TPI-API@sdp.tam',
    'password':'TimelinePI2018'
},
"policy":'AttachExisting'
}

jdump = json.dumps(login_param)
print(jdump)

# POST /auth/login
# https://api.five9.com/
# https://app-scl.five9.com/

head = {'Content-type':'application/json',
             'Accept':'application/json'}

url = 'https://app.five9.com:443/appsvcs/rs/svc/auth/login'
ret = requests.post(url, headers=head, data=jdump)

print(ret)
print(ret.content)

# {"tokenId":"a6165191-0576-11e9-a508-000c29420338","orgId":"123478","userId":"3042901","context":{"farmId":"81"},"metadata":{"freedomUrl":"https://app.five9.com","dataCenters":[{"name":"Santa Clara Data Center","uiUrls":[{"host":"app-scl.five9.com","port":"443","routeKey":"SCLUI4KbBC","version":"10.2.16"}],"apiUrls":[{"host":"app-scl.five9.com","port":"443","routeKey":"SCLAPIfCEZ","version":"10.2.16"}],"loginUrls":[{"host":"app-scl.five9.com","port":"443","routeKey":"SCLLGNYoI4","version":"10.2.16"}],"active":true}]}}

