from getpass import getpass
password = getpass()

csr_pe_rtr1 = {
"host": "2.1.1.4",
"device_type": "cisco_ios",
"username": "YOTTANET",
"password": password,
"secret": password,
}

csr_pe_rtr2 = {
"host": "2.1.1.5",
"device_type": "cisco_ios",
"username": "YOTTANET",
"password": password,
"secret": password,
}

csr_pe_rtr3 = {
"host": "2.1.1.6",
"device_type": "cisco_ios",
"username": "YOTTANET",
"password": password,
"secret": password,
}

csr_pe_rtr4 = {
"host": "2.1.1.7",
"device_type": "cisco_ios",
"username": "YOTTANET",
"password": password,
"secret": password,
}

veos_pe_rtr6 = {
"host": "2.1.1.9",
"device_type": "arista_eos",
"username": "YOTTANET",
"password": password,
}

veos_pe_rtr7 = {
"host": "2.1.1.10",
"device_type": "arista_eos",
"username": "YOTTANET",
"password": password,
#"secret": password,
}

