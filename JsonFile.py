
import json
from pprint import pprint

def nonempty_val(v):
    if type(v['latest.aid.median_debt.completers.overall']) == type(None):
        return 0;
    if type(v['latest.earnings.10_yrs_after_entry.working_not_enrolled.mean_earnings']) == type(None):
        return 0;
    return v['latest.aid.median_debt.completers.overall']
#    return v['latest.earnings.10_yrs_after_entry.working_not_enrolled.mean_earnings']




with open('schools.json', 'r') as infile:
    data = json.loads(infile.read())

#pprint( data )

schools = data['Results']
print( 'Keys: ' )
for key in schools[0].keys():
    print(key)

#Keys: dict_keys(['school.name', 'id', 'latest.aid.median_debt.completers.overall', 'latest.repayment.1_yr_repayment.completers', 'latest.earnings.10_yrs_after_entry.working_not_enrolled.mean_earnings'])

newlist = sorted(schools, key=nonempty_val, reverse=True)

for school in newlist:
    print(school['school.name'] + '\t ' + str(school['latest.aid.median_debt.completers.overall']) + ' \t '
          + str(school['latest.earnings.10_yrs_after_entry.working_not_enrolled.mean_earnings']))

