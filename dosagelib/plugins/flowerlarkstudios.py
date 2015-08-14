from dosagelib.helpers import indirectStarter
from dosagelib.plugins.cmsscraper import _WordpressScraper
from dosagelib.scraper import make_scraper


def add(name, url, starter=None):
    attrs = dict(
        name=name,
        url=url,
        starter=starter
    )
    globals()[name] = make_scraper(name, _WordpressScraper, **attrs)


for (name, linkNumber) in [
    ('Ashes', 1),
    ('Eryl', 3),
    ('Laiyu', 5),
    ('NoMoreSavePoints', 7),
    ('EasilyAmused', 9)
]:
    add(name, 'http://www.flowerlarkstudios.com/',
        starter=indirectStarter('http://www.flowerlarkstudios.com/',
                                '(//div[@id="sidebar-left"]//a)[' + str(linkNumber) + ']'))
