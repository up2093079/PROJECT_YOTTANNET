from netmiko import ConnectHandler
from getpass import getpass
import warnings
warnings.filterwarnings(action='ignore',module='paramiko.*')
csr_pe_rtr1 = {
  'host': '2.1.1.4',
  'username': 'YOTTANET',
  'password': getpass(),
  'secret': getpass(),
  'device_type':'cisco_ios'
}

vEOS_pe_rtr6 = {
  'host': '2.1.1.9',
  'username': 'YOTTANET',
  'password': getpass(),
  #'secret': getpass(),
  'device_type':'arista_eos',
}

with open('csr-pe-rtr1.txt') as f:
	new_output = f.read().splitlines()

new_connect = ConnectHandler(**csr_pe_rtr1)
new_connect.enable()
output1 = new_connect.send_config_set(new_output)
print(output1)

with open('veos-pe-rtr6.txt') as f:
	new_output2 = f.read().splitlines()
	print(new_output2)
new_connect1 = ConnectHandler(**vEOS_pe_rtr6)
print(new_connect1.find_prompt())
new_connect1.enable()
print(new_connect1.find_prompt())

output2 = new_connect1.send_config_set(new_output2)
print(output2)
