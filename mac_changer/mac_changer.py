#!/usr/bin/env python

import subprocess
import optparse

parser= optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="Interface its change MAC address")
parser.add_option("-m", "--mac_adress", dest="mac_address", help="MAC adress to change")
(options, arguments) = parser.parse_args()

interface= options.interface
mac_address= options.mac_address

print("[+] Changing MAC address for " + interface + " to " + mac_address)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", mac_address])
subprocess.call(["ifconfig", interface, "up"])
