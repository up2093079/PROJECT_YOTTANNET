
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
#print(output)
output_int = output[0]
#print(output_int)
output_int1 = output_int['result']
output_int2 = output_int1['interfaces']
output_int3 = output_int2['Ethernet3']
output_int4 = output_int3['interfaceCounters']
#pprint(output_int4)

for keys, values in output_int4.items():
	print(f"keys for ethernet3: {keys}, values is: {values}")

