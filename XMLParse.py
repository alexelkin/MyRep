import xml.etree.cElementTree as et

import xml.etree.ElementTree as ET
from pprint import pprint as pp


sxml = '''<env:Envelope xmlns:env="http://schemas.xmlsoap.org/soap/envelope/">
    <env:Header/>
    <env:Body>
        <ns2:runReportResponse xmlns:ns2="http://service.admin.ws.five9.com/">
            <return>47CC8E1068F0CCC80rt1.c.ie.o8254B@Ep70012sAlFf4v89BcCm</return>
        </ns2:runReportResponse>
    </env:Body>
</env:Envelope>
'''

# https://docs.python.org/2/library/xml.etree.elementtree.html

test_string = '''<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>
'''


# for el in tree.findall('return'):
#     print(el)
#     for ch in el.getchildren():
#         print('{:>15}: {:<30}'.format(ch.tag, ch.text))


# pp([dict((attr.tag, attr.text) for attr in el) for el in et.fromstring(sxml)])

#tree = et.fromstring(sxml)
tree = ET.fromstring(sxml)

print(type(tree))

for child in tree[1][0]:
    print(child)
    print(child.text)

# con = ET.fromstring(test_string)
# for child in con[0]:
#     print(type(child))
#     print(child.tag, child.attrib, child.text)



