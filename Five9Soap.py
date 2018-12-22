
# https://python-zeep.readthedocs.io/en/master/
# https://webapps.five9.com/assets/files/for_customers/documentation/apis/config-webservices-api-reference-guide.pdf

#  https://api.five9.com/wsadmin/v10_2/AdminWebService?wsdl&user=<Five9username>
import sys
import zeep

from zeep import Client
from zeep.wsse.username import UsernameToken
from zeep.transports import Transport

from requests.auth import HTTPBasicAuth  # or HTTPDigestAuth, or OAuth1, etc.
from requests import Session

import xml.etree.ElementTree as ET

from pprint import pprint

session = Session()
session.auth = HTTPBasicAuth('TPI-API@sdp.tam', 'TimelinePI2018')


url = 'https://api.five9.com/wsadmin/v10_2/AdminWebService?wsdl&user=TPI-API@sdp.tam'

client = Client(wsdl=url, wsse=UsernameToken('TPI-API@sdp.tam', 'TimelinePI2018'), transport=Transport(session=session))
# pprint(client.wsdl.messages)

repoty_folder = 'Call Log Reports'
report = 'Call Log'

# repoty_folder = 'Agent Reports'
# report = 'Agent State Details'



with client.settings(raw_response=True):

    time_criteria = client.get_type('ns0:reportTimeCriteria')
    report_criteria = client.get_type('ns0:customReportCriteria')
    my_time = time_criteria(start='2018-09-20T21:00:00.000-07:00', end='2018-12-20T21:00:00.000-07:00')
    my_criteria = report_criteria(time=my_time)

    response = client.service.runReport(folderName=repoty_folder, reportName = report, criteria = my_criteria)

    # response is now a regular requests.Response object
    print( "Type of response: " + str(type(response)))

    print(response.status_code)
    print(response.text)

#    jret = response.json()
#    pprint(jret)

#    a = str(zeep.helpers.serialize_object(response.content))
#     a = str(response.content)
#     print('Before parsing: ' + a)
#
    tree = ET.fromstring(response.text)
#
#     print(type(tree))
#
    return_value = ''

    for child in tree[1][0]:
        print(child)
        return_value = child.text

    print('Report started', return_value, sep = ':: ' )
    reportID = return_value

    return_value = 'true'

    while return_value == 'true':

        response = client.service.isReportRunning( identifier = reportID, timeout = 4 )
        print('Waiting for report', response.text, sep = ':: \n' )


        tree = ET.fromstring(response.text)
        for child in tree[1][0]:
            print(child)
            return_value = child.text

        print( 'Is waiting? ', return_value )

    response = client.service.getReportResultCsv(identifier=reportID)
    print('Got the report!', response.text, sep=':: \n')
