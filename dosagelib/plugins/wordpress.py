# -*- coding: utf-8 -*-
from dosagelib.helpers import indirectStarter
from ..scraper import make_scraper, _ParserScraper


class _WordpressScraper(_ParserScraper):
    imageSearch = ('//div[@id="comic"]//img',
                   '//div[@class="webcomic-image"]//img')
    prevSearch = ("//a[contains(concat(' ', text(), ' '), ' Prev ')]",
                  "//a[contains(concat(' ', text(), ' '), ' Previous ')]",
                  "//a[contains(concat(' ', @class, ' '), ' navi-prev ')]",
                  "//a[contains(concat(' ', @class, ' '), ' navi-prev-in ')]",
                  "//a[contains(concat(' ', @class, ' '), ' navi-previous ')]",
                  "//a[contains(concat(' ', @class, ' '), ' previous-webcomic-link ')]")


def add(name, url, firstUrl=None, starter=None, textSearch=None, lang=None):
    attrs = dict(
        name=name,
        url=url
    )
    if lang:
        attrs['lang'] = lang
    if firstUrl:
        attrs['firstUrl'] = url + firstUrl
    if starter:
        attrs['starter'] = starter
    if textSearch:
        attrs['textSearch'] = textSearch
    globals()[name] = make_scraper(name, _WordpressScraper, **attrs)


# all comics on HijiNKS ENSUE
for (name, starterXPath) in [
    ('HijinksEnsue', '//h4[text()="Read The Latest HijiNKS ENSUE"]/..//a'),
    ('HijinksEnsueClassic', '//h4[text()="Read HijiNKS ENSUE Classic"]/..//a[3]'),
    ('Faneurysm', '//h4[text()="Read The Latest FANEURYSM"]/..//a'),
    ('HijinksEnsueConvention', '//h4[text()="Latest Fancy Convention Sketches"]/..//a'),
    ('HijinksEnsuePhoto', '//h4[text()="Latest Fancy Photo Comic"]/..//a')
]:
    add(name, 'http://hijinksensue.com/', starter=indirectStarter('http://hijinksensue.com/', starterXPath))
