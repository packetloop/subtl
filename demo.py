#!/usr/bin/env python
'''
'''
from subtl import UdpTrackerClient

HASHES = [
    '089184ED52AA37F71801391C451C5D5ADD0D9501',
    'AFFF79E471EFF468C7F66DA6C91B90C6E89343CF',
]


def connect(utc):
    print('Connecting')
    utc.connect()
    if utc.poll_once():
        print('Success!')
    else:
        raise Exception('Could not connect')


def scrape(utc):
    utc.scrape(HASHES)
    data = utc.poll_once()
    if not data:
        raise Exception('Could not scrape')
    for info_hash, details in data['response'].iteritems():
        print(info_hash, details)


def announce(utc):
    utc.announce(info_hash=HASHES[0])
    data = utc.poll_once()
    if not data:
        raise Exception('Could not announce')
    for a in data['response']['peers']:
        print(a)


def main():
    utc = UdpTrackerClient('tracker.openbittorrent.com', 80)
    connect(utc)
    scrape(utc)
    announce(utc)


if __name__ == '__main__':
    main()
