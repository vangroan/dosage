from re import sub
from dosagelib.helpers import bounceStarter
from dosagelib.plugins.common import WordPressScraper
from dosagelib.scraper import ParserScraper


class Alfie(WordPressScraper):
    url = "https://buttsmithy.com/"
    stripUrl = url + "archives/comic/%s"
    firstStripUrl = stripUrl % "p1"
    adult = True
    starter = bounceStarter

    def namer(self, image_url, page_url):
        def repl(m):
            return "{0}".format(m.group(1).zfill(4))

        name = sub("^p-?(\d+)", repl, page_url.split("/")[-1])

        # Some of the first 1k pages were inconsistently named.
        renames = {
            "/comic/p145": "0145-1",
            "/comic/p-145": "0145-2",
            "/comic/268": "0268",
            "/comic/1132": "0313",
            "/comic/1169": "0319",
            "/comic/1186": "0324",
            "/comic/1404": "0378",
            "/comic/0338-2": "0339",
            "/comic/0369-2": "0469",
            "/comic/2080": "0517",
            "/comic/o-525": "0525",
            "/comic/p-361": "0553",
            "/comic/p-668-2": "0678",
            "/comic/p-670-2": "0670",
            "/comic/p-679-2": "0690",
            "/comic/3140": "0805",
        }
        for rename in renames:
            if rename in page_url:
                name = renames[rename]
        return name


class ExterminatusNow(WordPressScraper):
    url = "http://exterminatusnow.co.uk/"
    firstStripUrl = url + "/2003-09-29/comic/meet-the-crew/dirty-harry/"
    imageSearch = '//img[contains(@src, "comics/")]'
    prevSearch = '//a[d:class("navi-prev")]'


class CatsWay(WordPressScraper):
    url = "https://catswaycomic.com"
    stripUrl = url + "comic/%s/"
    firstStripUrl = stripUrl % "page-1"
    prevSearch = '//a[@class="comic-nav-base comic-nav-previous"]'
    nextSearch = '//a[@class="comic-nav-base comic-nav-next"]'
    latestSearch = '//a[@class="comic-nav-base comic-nav-last"]'


class Kochab(ParserScraper):
    url = "https://www.kochab-comic.com/"
    firstStripUrl = url + "comic/prologue-00"
    imageSearch = '//img[@id="cc-comic"]'
    prevSearch = '//a[d:class("cc-prev")]'
    nextSearch = '//a[d:class("cc-next")]'
    latestSearch = '//a[d:class("cc-last")]'
    endOfLife = True
