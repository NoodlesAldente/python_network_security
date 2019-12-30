#!/usr/bin/env python

import subprocess
import optparse

def get_arguments():
    parser= optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface its change MAC address")
    parser.add_option("-m", "--mac_adress", dest="mac_address", help="MAC adress to change")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error('[-] Please specify an interface, use --help for more informations.')
    elif not options.mac_address:
        parser.error('[-] Please specify an new MAC address , use --help for more informations.')
    return options


def change_mac(interface, mac_address):
    print("[+] Changing MAC address for " + interface + " to " + mac_address)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac_address])
    subprocess.call(["ifconfig", interface, "up"])

options = get_arguments()
change_mac(options.interface, options.mac_address)
