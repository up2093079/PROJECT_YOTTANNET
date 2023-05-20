from __future__ import print_function, unicode_literals
import jinja2
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
import csv
from project_devices import csr_pe_rtr1,csr_pe_rtr2,csr_pe_rtr3,csr_pe_rtr4
from netmiko import ConnectHandler
import warnings
warnings.filterwarnings(action='ignore',module='paramiko.*')

yottannet_csv = 'mpls_internet_ios.csv'
#the csv file to be refernced by JInja2 template

with open(yottannet_csv) as f:
	yottannet_read = csv.DictReader(f)
	#the csv file is read using the python dictionary reader

	for mpls_int_var in yottannet_read:
		if mpls_int_var['device_name'] == 'csr-pe1':
			csr_pe_rtr1['pertr_var'] = mpls_int_var
		if mpls_int_var['device_name'] == 'csr-pe2':
                        csr_pe_rtr2['pertr_var'] = mpls_int_var
		if mpls_int_var['device_name'] == 'csr-pe3':
                        csr_pe_rtr3['pertr_var'] = mpls_int_var
		if mpls_int_var['device_name'] == 'csr-pe4':
                        csr_pe_rtr4['pertr_var'] = mpls_int_var
		#commands used to seperate the configurations according to their device names

	devices = [csr_pe_rtr1,csr_pe_rtr2,csr_pe_rtr3,csr_pe_rtr4]
	# list is created to reference all the needed network devices

	for yottannet_dev in devices:
		yottannet_dev_copy = yottannet_dev.copy()
		yottannet_pop = yottannet_dev_copy.pop('pertr_var')
	
		#a very intelligent way to seperate the device login credentials and the
		#configuration elements
		template_file = 'mpls_internet_ios.j2'
		with open(template_file) as f:
			template_new = f.read()
			#template file is read
		new_output = jinja2.Template(template_new)
		print('-'*50)
		new_output1 = (new_output.render(yottannet_pop))
		#the configuration elements from the .csv file is rendered onto the jinja2 file
		for yottannet_output in [new_output1.strip()]:
			yottannet_output2 = yottannet_output.splitlines()
			#the final configuration prepared for the configuration line
		net_connect = ConnectHandler(**yottannet_dev_copy)
		net_connect.enable()
		#print(net_connect.base_prompt)
		new_output2 = net_connect.send_config_set(yottannet_output2)
		#final configuration pushed to network devices
		print(new_output2)
