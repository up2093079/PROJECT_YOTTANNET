import pyeapi
from pprint import pprint
from getpass import getpass

eapi_new = pyeapi.client.connect(
	transport='https',
	host = '2.1.1.10',
	username= 'YOTTANET',
	password= getpass(),
	port=443,
)

#enable = getpass("Enable:")
eapi_yot = pyeapi.client.Node(eapi_new)

output = eapi_yot.enable(['show interfaces ethernet 3','show version'])
#pprint(output)
