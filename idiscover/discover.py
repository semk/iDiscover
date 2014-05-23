# -*- coding: utf-8 -*-
#
# Discover the target host types in the subnet
#
# @author: Sreejith Kesavan <sreejithemk@gmail.com>


import arp
import oui
import ipcalc


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
    pass


if __name__ == '__main__':
    d = Discovery()
    for ip, manuf in d.discover('10.73.19.0/24'):
        print ip, manuf

    for ip, manuf in d.discover('10.74.215.0/24'):
        print ip, manuf