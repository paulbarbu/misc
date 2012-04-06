#! /usr/bin/env python2.7
'''
The aim of this script is to get the latest headline from
http://www.archlinux.org/ and to display it to stdout in order to stay updated
with the news when updatinng the system for example without having to visit the
site in the browser thus saving some time

See pacman.sh for an example on how this script can be used
'''

from bs4 import BeautifulSoup
from contextlib import closing
import urllib

soup = ''
uri = 'http://archlinux.org'

with closing(urllib.urlopen(uri)) as source:
    soup = BeautifulSoup(source.read())

if soup:
    latest_headline = soup.find('div', id='news').h4.a

    print 'Latest headline {0}\n{1}\n'.format(
            uri + latest_headline['href'], latest_headline.text)
else:
    print 'An error fetching the page contents has occurred!'
