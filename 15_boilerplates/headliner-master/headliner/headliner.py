#!/usr/bin/env python

import os
import sys
import argparse
import random

import requests_html
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

__version__ = '1.0.1'

USER_AGENTS = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
               'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100 101 Firefox/22.0',
               'Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46 Safari/536.5',
               'Mozilla/5.0 (Windows; Windows NT 6.1) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46 Safari/536.5',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8'
               )


def cli():
    parser = argparse.ArgumentParser(description='Headlines from URLs')
    parser.add_argument('-u', '--url', type=str, help='URL of resource to parse', default='https://www.lanacion.com.ar/')
    parser.add_argument('-t', '--tag', type=str, help='HTML element to look for', default='h2')
    parser.add_argument('--ssl', help='Verify SSL', action='store_true')
    parser.add_argument('-v', '--version', help='displays the current version', action='store_true')
    args = parser.parse_args()

    headlines(args.url, args.tag, args.ssl)


def headlines(url='https://www.bloomberg.com/', tag='h2', verify_ssl=False):
    with requests_html.HTMLSession() as session:
        r = session.get(url, verify=verify_ssl)
        print(''.join(['\n-> {}'.format(header.text) for header in r.html.find(tag)]))


if __name__ == '__main__':
    test()
