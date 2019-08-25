import subprocess
import optparse
import re

def change_mac(interface, new_mac):
    print("[+] Changing MAC address of interface " + interface + " to " + new_mac)
    subprocess.call(['ifconfig', interface, 'down'])
    subprocess.call(['ifconfig', interface, 'hw', 'ether', new_mac])
    subprocess.call(['ifconfig', interface, 'up'])

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option('-i', '--interface', dest='interface', help='Name of interface')
    parser.add_option('-m', '--mac', dest='new_mac', help='New MAC address of interface')
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("\n[-] Please specify interface. Use -h or --help for more information.")
    elif not options.new_mac:
        parser.error("\n[-] Please specify new MAC address. Use -h or --help for more information.")
    interface = options.interface
    new_mac = options.new_mac
    return interface,new_mac


interface, new_mac = get_arguments()
change_mac(interface, new_mac)


#print(output)

ifconfig_output = subprocess.check_output(['ifconfig', interface])

#print(ifconfig_output)

mac_capture = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_output)

#print(mac_capture.group())

if mac_capture.group():

    if new_mac == mac_capture.group():
        print("[+] MAC address has been successfully changed.")
    else:
        print("[-] Error while changing MAC address.")

else:
    print("[-] Could not read MAC address.")