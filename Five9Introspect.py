from zeep import Client
from pprint import pprint

from zeep.wsse.username import UsernameToken
from zeep.transports import Transport

from requests.auth import HTTPBasicAuth  # or HTTPDigestAuth, or OAuth1, etc.
from requests import Session


session = Session()
session.auth = HTTPBasicAuth('TPI-API@sdp.tam', 'TimelinePI2018')


url = 'https://api.five9.com/wsadmin/v10_2/AdminWebService?wsdl&user=TPI-API@sdp.tam'

client = Client(wsdl=url, wsse=UsernameToken('TPI-API@sdp.tam', 'TimelinePI2018'), transport=Transport(session=session))


def parseElements(elements):
    all_elements = {}
    for name, element in elements:
        all_elements[name] = {}
        all_elements[name]['optional'] = element.is_optional
        if hasattr(element.type, 'elements'):
            all_elements[name]['type'] = parseElements(
                element.type.elements)
        else:
            all_elements[name]['type'] = str(element.type)

    return all_elements


interface = {}
for service in client.wsdl.services.values():
    interface[service.name] = {}
    for port in service.ports.values():
        interface[service.name][port.name] = {}
        operations = {}
        for operation in port.binding._operations.values():
            operations[operation.name] = {}
            operations[operation.name]['input'] = {}
            elements = operation.input.body.type.elements
            operations[operation.name]['input'] = parseElements(elements)
        interface[service.name][port.name]['operations'] = operations


pprint(interface)
