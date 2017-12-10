import ssl
from suds.client import Client

fromPhone = "SEPFFFFFFFF22FF"
toPhone = "SEPFFFFFFFF21FF"

ssl._create_default_https_context = ssl._create_unverified_context
username = 'Administrator'
passwd = 'password'
wsdl_url = 'http://127.0.0.1/axlsqltoolkit/schema/11.5/AXLAPI.wsdl'
service_url = 'https://127.0.0.1/axl/'
cucm_server = Client(wsdl_url, location=service_url, username=username, password=passwd)

def getspeeddials(PName):
    speedidals = []
    users = cucm_server.service.getPhone(PName)
    for speeddial in users['return']['phone']['speeddials']['speeddial']:
        speedidals.append(speeddial)
    return speedidals;

def putspeeddials(PName, speeddial):
    cucm_server.service.updatePhone(name = PName, speeddials={'speeddial': speeddial}                                              )
    return;

putspeeddials(PName=toPhone, speeddial=getspeeddials(PName=fromPhone))

#def testputspeeddials(PName, speeddials):
#    users = cucm_server.service.updatePhone(name = PName,
#                                            speeddials={'speeddial':[{'dirn' : '8129', 'label':'Test', 'index':'1'},
#                                                                     {'dirn' : '8126', 'label': 'Test2', 'index': '2'},
#                                                                     {'dirn': '8127', 'label': 'Test3', 'index': '3'}]})
#    print(users)
#    return;
