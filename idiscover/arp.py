# -*- coding: utf-8 -*-
#
# Find out the MAC Address of the target host using arp
#
# @author: Sreejith Kesavan <sreejithemk@gmail.com>


import re
import sys
from subprocess import Popen, PIPE


class ARP(object):
    """ Finds the MAC Addresses using ARP

    NOTE: This finds mac addresses only within the subnet.
    It doesn't fetch mac addresses for routed network ips.
    """

    MAC_RE = re.compile(r'(([a-f\d]{1,2}[:-]){5}[a-f\d]{1,2})')

    def __init__(self):
        if sys.platform == 'win32':
            self.__arp_command_prefix = ['arp', '-a']
        else:
            self.__arp_command_prefix = ['arp', '-n']

    def find_mac(self, ip_address, ping=True):
        if ping:
            # do a ping for an ARP table update
            self.ping(ip_address)

        pid = None
        try:
            pid = Popen(self.__arp_command_prefix + [ip_address], stdout=PIPE)
            out = pid.communicate()[0]
            mac_found = self.MAC_RE.search(out)
            if mac_found:
                mac = mac_found.group(0).replace('-', ':')
                return mac
        finally:
            if pid:
                pid.stdout.close()

    @staticmethod
    def ping(ip_address):
        """ Ping ip_address
        """
        if sys.platform == 'win32':
            options = ['-n', '1', '-w', '1000']
        else:
            options = ['-c', '1', '-t', '1']

        # do a single ping
        pid = Popen(['ping'] + options + [ip_address], stdout=PIPE)
        pid.communicate()
        pid.stdout.close()
        if pid.returncode != 0:
            print '{ip} is unreachable'.format(ip=ip_address)


if __name__ == '__main__':
    arp = ARP()
    print arp.find_mac('10.61.187.127')
    print arp.find_mac('10.61.187.145')
    print arp.find_mac('10.73.19.112')

