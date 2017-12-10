import ssl
import csv
from suds.client import Client

#Add Phones to the UCM UCMAddPhone() accepts:
# UCMAddPhone(cucm_server,
#              phonename="SEPFFFFFFFF21FF",
#              description="Lastname, Firstname",
#              callingSearchSpaceName = "Devices-LND",
#              devicePoolName="London",
#              locationName="London",
#              lineIndexOneDisplay="Lastname, Firstname",
#              lineIndexOnePattern="8014",
#              lineIndexOneRoutePartitionName="S-ST-T",
#              lineIndexOnedisplayAscii="Lastname, Firstname",
#              lineIndexOnerecordingProfileName="Recording-LND",
#              phoneTemlateName="Standard 8865 OneLine",
#              enableExtensionMobility="true",
#              builtInBridgeStatus="On",
#              OwnerUserName="PACKEOUSER0001")
#
#Import CSV files via the UCMAddPhoneCSV()
#UCMAddPhoneCSV(csvfile)
#csv file should look like:
#SEP000000000001;AA, AA;Devices-LND;London;London;AA, AA;8100;S-ST-T;AA, AA;Recording-LND;Standard 8865 OneLine;TRUE;On;PACKEOUSER0001


# ignore ssl pain
ssl._create_default_https_context = ssl._create_unverified_context
# setup creds for auth
username = 'Administrator'
passwd = 'password'
wsdl_url = 'http://127.0.0.1/axlsqltoolkit/schema/11.5/AXLAPI.wsdl'
service_url = 'https://127.0.0.1/axl/'
cucm_server = Client(wsdl_url, location=service_url, username=username, password=passwd)


def UCMAddPhone(cucm_server, phonename,
                 description, callingSearchSpaceName, devicePoolName,
                 locationName, lineIndexOneDisplay,
                 lineIndexOnePattern, lineIndexOneRoutePartitionName, lineIndexOnedisplayAscii,
                 lineIndexOnerecordingProfileName, phoneTemlateName, enableExtensionMobility,
                 builtInBridgeStatus, OwnerUserName):
    result = cucm_server.service.addPhone({'name': phonename,
                                           'description': description,
                                           'product': 'Cisco 8865',
                                           'class': 'Phone',
                                           'protocol': 'SIP',
                                           'protocolSide': 'User',
                                           'callingSearchSpaceName': callingSearchSpaceName,
                                           'devicePoolName': devicePoolName,
                                           'networkLocation': 'Use System Default',
                                           'locationName': locationName,
                                           'securityProfileName': 'Cisco 8865 - Standard SIP Non-Secure Profile',
                                           'sipProfileName': 'Standard SIP Profile',
                                           'lines': {'line': [{'index': '1',
                                                               'display': lineIndexOneDisplay,
                                                               'dirn': {'pattern': lineIndexOnePattern,
                                                                        'routePartitionName': lineIndexOneRoutePartitionName},
                                                               'displayAscii': lineIndexOnedisplayAscii,
                                                               'maxNumCalls': '4',
                                                               'busyTrigger': '2',
                                                               'recordingProfileName': lineIndexOnerecordingProfileName,
                                                               'recordingFlag': 'Automatic Call Recording Enabled',
                                                               'recordingMediaSource': 'Gateway Preferred'}]},
                                           'phoneTemplateName': phoneTemlateName,
                                           'enableExtensionMobility': enableExtensionMobility,
                                           'builtInBridgeStatus': builtInBridgeStatus,
                                           'ownerUserName': OwnerUserName,
                                           'packetCaptureMode': 'None',
                                           'certificateOperation': 'No Pending Operation',
                                           'deviceMobilityMode': 'Default'})
    print(result['return'], end=' ')
    return;



def UCMAddPhoneCSV(csvlocation):
    with open(csvlocation) as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            for set in row:
                print(set, end=';')
            print(" ")
            UCMAddPhone(cucm_server, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
                         row[11], row[12], row[13])
            print(" ...Added")
    return;

UCMAddPhoneCSV(csvlocation='phones.csv')

