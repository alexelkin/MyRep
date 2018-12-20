#https://api.data.gov/

import requests
import json
from pprint import pprint

key = 'JoXvMQJaaImWIirNtNMzI1n81Aytyfafzu0rKrRe'

url = "https://api.data.gov/ed/collegescorecard/"
allSchools = '/v1/schools'

example = 'https://api.data.gov/ed/collegescorecard/v1/schools?api_key=JoXvMQJaaImWIirNtNMzI1n81Aytyfafzu0rKrRe&fields=school.name,id,latest.aid.median_debt.completers.overall,latest.repayment.1_yr_repayment.completers,latest.earnings.10_yrs_after_entry.working_not_enrolled.mean_earnings&page=100'

param = { 'api_key' : key,
          'fields' : 'school.name,id,latest.aid.median_debt.completers.overall,latest.repayment.1_yr_repayment.completers,latest.earnings.10_yrs_after_entry.working_not_enrolled.mean_earnings',
          'page' : '0'}


page = 0

with open('schools.json', 'w') as outfile:

    results=[]
    cnt = 0;

    while page < 400:

        param['page'] = str(page)

        ret = requests.get(url + allSchools, params=param)

        print('Page: ' + str(page) + '   Result: ' + str(ret))
#        print(ret.content)

        jsonobj = json.loads(ret.content)
#        print(str(jsonobj['metadata']))

        results.extend(jsonobj['results'])

        page += 1
        cnt += 20
        if cnt >= jsonobj['metadata']['total']:
            break


    jResult = {}
    jResult['Results'] = results

    json.dump( jResult , outfile)


#    json.dump(json.loads(str(results)), outfile)
#    outfile.write( '}')


# jData = json.loads( ret.content )
# pprint( jData )
# for line in jData['results']:
#     print( "The line: " + str(line) )

