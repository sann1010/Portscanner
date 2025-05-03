import socket
import termcolor

def scan_targets(targets,ports):
    print ("Scanning started for:" + str(targets))
    for port in range(1,ports):
        scan_ports(targets,ports)

def scan_ports(ip_addresses, ports):
    try:
        sock = socket.socket()
        sock.connect((ip_addresses, ports))
        print ("-- Port Opened" + str(ports))
        sock.close()
    except:
        pass

targets = input(" Enter Ip Addresses to scan(split them by ,): ")
ports = int(input("Enter number of ports you want to scan: "))
if ',' in targets:
	print(termcolor.colored(("[*] Scanning Multiple Targets"), 'green'))
	for ip_addr in targets.split(','):
		scan_targets(ip_addr.strip(' '), ports)
else:
	scan_targets(targets,ports)
