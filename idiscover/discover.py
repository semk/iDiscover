# -*- coding: utf-8 -*-
#
# Discover the target host types in the subnet
#
# @author: Sreejith Kesavan <sreejithemk@gmail.com>


import arp
import oui
import ipcalc
import sys


class Discovery(object):
    """ Find out the host types in the Ip range (CIDR)

    NOTE: This finds mac addresses only within the subnet.
    It doesn't fetch mac addresses for routed network ip's.
    """

    def __init__(self):
        self.__arp = arp.ARP()
        self.__oui = oui.OUI()

    def discover(self, network):
        for ip in ipcalc.Network(network):
            ip = str(ip)
            mac = self.__arp.find_mac(ip)
            if mac:
                if len(mac.split(':')[0]) == 1:
                    mac = '0' + mac
                manuf_str = mac.replace(':', '')[:6].upper()
                manuf = self.__oui.find_manuf(manuf_str)
                if manuf:
                    yield (ip, manuf)


def run():
    if len(sys.argv) < 2:
        print
        print 'Usage:\t\tidiscover <ip-address/cidr>'
        print 'Examples:'
        print '\t\tidiscover 10.73.19.0'
        print '\t\tidiscover 10.74.215/24'
        print
    else:
        addrs = sys.argv[1:]
        d = Discovery()

        try:
            for addr in addrs:
                for ip, manuf in d.discover(addr):
                    print 'IP Address: {ip} Manufacturer: {manuf}'.format(ip=ip, manuf=manuf)
        except KeyboardInterrupt:
            print 'Exiting...'


if __name__ == '__main__':
    run()