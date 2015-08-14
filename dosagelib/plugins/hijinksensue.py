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


for (name, starterXPath) in [
    ('HijinksEnsue', '//h4[text()="Read The Latest HijiNKS ENSUE"]/..//a'),
    ('HijinksEnsueClassic', '//h4[text()="Read HijiNKS ENSUE Classic"]/..//a[3]'),
    ('Faneurysm', '//h4[text()="Read The Latest FANEURYSM"]/..//a'),
    ('HijinksEnsueConvention', '//h4[text()="Latest Fancy Convention Sketches"]/..//a'),
    ('HijinksEnsuePhoto', '//h4[text()="Latest Fancy Photo Comic"]/..//a')
]:
    add(name, 'http://hijinksensue.com/', starter=indirectStarter('http://hijinksensue.com/', starterXPath))
