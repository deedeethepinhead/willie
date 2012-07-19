#!/usr/bin/env python
"""
xkcd.py - XKCD Module
Copyright 2010, Michael Yanovich (yanovich.net), and Morgan Goose
Copyright 2012, Lior Ramati
Licensed under the Eiffel Forum License 2.

More info:
* Jenni: https://github.com/myano/jenni/
* Phenny: http://inamidst.com/phenny/
"""

import random
from search import google_search

""".xkcd - Finds an xkcd comic strip. Takes one of 3 inputs:
    If no input is provided it gives a random comic.
    If a numeric input is provided it will return that comic
    If non-numeric input is provided it will return the first google result for those keywords on the xkcd.com site"""
    
def xkcd(jenni, input):
    import urllib2
    from lxml import etree
    if not input.group(2):
        body = urllib2.urlopen("http://xkcd.com/rss.xml").readlines()[1]
        parsed = etree.fromstring(body)
        newest = etree.tostring(parsed.findall("channel/item/link")[0])
        max_int = int(newest.split("/")[-3])
        website = "http://xkcd.com/%d/" % random.randint(0,max_int+1)
        jenni.say(website)
    else:
        query = input.group(2)
        if (query.strip().isdigit()): 
            random.seed()
            website = "http://xkcd.com/" + query.strip()
            jenni.say(website)
        else:
           try:
                query = query.encode('utf-8')
           except:
               pass
           uri = google_search("site:xkcd.com "+ query)
           if uri:
               jenni.reply(uri)
           elif uri is False: jenni.say("Problem getting data from Google.")
           else: jenni.say("No results found for '%s'." % query) 
xkcd.commands = ['xkcd']
xkcd.priority = 'low'

if __name__ == '__main__':
    print __doc__.strip()
