from getpass import getpass
from pprint import pprint
from napalm import get_network_driver
import warnings
warnings.filterwarnings(action='ignore',module='paramiko.*')

others = {
	   "secret": "AHMED007",
	   "delay_factor": 5
}

CSRPE1 = dict(
	hostname = "2.1.1.4",
	device_type = "ios",
	username="YOTTANET",
	password= getpass(),
	optional_args = others,
)

vEOSPE6 = dict(
        hostname = "2.1.1.9",
        device_type = "eos",
        username="YOTTANET",
        password= getpass(),
        #optional_args = others,
)

device_name = CSRPE1

device_type = device_name.pop("device_type")

driver = get_network_driver(device_type)
device = driver(**device_name)

print()
device.open()

output = device.get_facts()
output = device.get_interfaces()
pprint(output)
print()
