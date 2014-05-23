# -*- coding: utf-8 -*-
#
# Helper file to identify manufacturer from OUI
#   http://standards.ieee.org/develop/regauth/oui/oui.txt
#   http://en.wikipedia.org/wiki/Organizationally_unique_identifier
#
# @author: Sreejith Kesavan <sreejithemk@gmail.com>


import os
import re


class OUI(object):
    """ The OUI database
    """

    __shared_state = {}

    oui_file = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        'data/oui.txt')

    hex_manuf_pattern = re.compile('\s+(?P<hex>\S+)\s+(\(hex\)|\(base 16\))\s+(?P<manuf>.*)')

    def __init__(self):
        # This is borg. Shares the same state across all instances
        self.__dict__ = self.__shared_state
        self.__parse_oui_file()

    def __parse_oui_file(self):
        # parse the file only once
        if not hasattr(self, '__oui_db'):
            self.__oui_db = {}
            with open(self.oui_file) as f:
                lines = f.readlines()
                for line in lines:
                    match = self.hex_manuf_pattern.match(line)
                    if match:
                        self.__oui_db[match.group('hex')] = match.group('manuf')

    def find_manuf(self, oui):
        return self.__oui_db.get(oui, None)


if __name__ == '__main__':
    oui = OUI()
    print oui.find_manuf('0080E5')
    print oui.find_manuf('00B04A')
    print oui.find_manuf('281878')