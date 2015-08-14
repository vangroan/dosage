# -*- coding: utf-8 -*-
from ..scraper import _ParserScraper


class _WordpressScraper(_ParserScraper):
    imageSearch = ('//div[@id="comic"]//img',
                   '//div[@class="webcomic-image"]//img')
    prevSearch = ("//a[contains(concat(' ', text(), ' '), ' Prev ')]",
                  "//a[contains(concat(' ', text(), ' '), ' Previous ')]",
                  "//a[contains(concat(' ', @class, ' '), ' navi-prev ')]",
                  "//a[contains(concat(' ', @class, ' '), ' navi-prev-in ')]",
                  "//a[contains(concat(' ', @class, ' '), ' navi-previous ')]",
                  "//a[contains(concat(' ', @class, ' '), ' previous-webcomic-link ')]")