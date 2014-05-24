iDiscover
=========

A network discovery tool that fetches the manufacturer and IP information of
various connected devices in a network.


Installation
============

    pip install https://github.com/semk/iDiscover/tarball/master

Usage
=====

    Usage:		idiscover <ip-address/cidr>
    Examples:
                idiscover 10.73.19.0
                idiscover 10.74.215/24

Output
======

    sree@silverbullet ~ $ idiscover 192.168.2.0/24
    IP Address: 192.168.2.1 Manufacturer: Belkin International, Inc.
    IP Address: 192.168.2.3 Manufacturer: Murata Manufactuaring Co.,Ltd.
    IP Address: 192.168.2.5 Manufacturer: Liteon Technology Corporation
