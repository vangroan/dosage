#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher
"""
Script to get a list of KeenSpot comics and save the info in a
JSON file for further processing.
"""
from __future__ import absolute_import, division, print_function

from six.moves.urllib.parse import urlsplit

from scriptutil import ComicListUpdater
from dosagelib.util import check_robotstxt


class KeenSpotUpdater(ComicListUpdater):
    dup_templates = ('Creators/%s', "GoComics/%s", "ComicGenesis/%s")

    # names of comics to exclude
    excluded_comics = (
        # non-standard navigation
        "BrawlInTheFamily",
        "Flipside",
        "LastBlood",
        "TheGodChild",
        "Twokinds",
    )

    extra = {
        'CrowScare': 'last="20111031"',
        'Dreamless': 'last="20100726"',
        'MysticRevolution': 'path="?cid=%s"',
        'PunchAnPie': 'path="daily/%s.html"',
        'ShockwaveDarkside': 'path="2d/%s.html"',
        'Yirmumah': 'path="%s/"',
    }

    def collect_results(self):
        """Parse the front page."""
        data = self.get_url('http://keenspot.com/')

        for comiclink in data.xpath('//td[@id]/a'):
            comicurl = comiclink.attrib['href']
            name = comiclink.xpath("string()")
            try:
                if "/d/" not in comicurl:
                    check_robotstxt(comicurl + "d/", self.session)
                else:
                    check_robotstxt(comicurl, self.session)
            except IOError as e:
                print("[%s] INFO: robots.txt denied: %s" % (name, e))
                continue

            self.add_comic(name, comicurl)

    def get_entry(self, name, url):
        sub = urlsplit(url).hostname.split('.', 1)[0]
        if name in self.extra:
            extra = ', ' + self.extra[name]
        else:
            extra = ''
        return u"cls('%s', '%s'%s)," % (name, sub, extra)


if __name__ == '__main__':
    KeenSpotUpdater(__file__).run()
