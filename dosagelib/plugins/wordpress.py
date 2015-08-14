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


class Amya(_WordpressScraper):
    url = 'http://www.amyachronicles.com/'


class Number1997(_WordpressScraper):
    url = 'http://1977thecomic.com/'


class Alice(_WordpressScraper):
    url = 'http://www.alicecomics.com/'
    starter = indirectStarter('http://www.alicecomics.com/', '//a[text()="Latest Alice!"]')


class AxeCop(_WordpressScraper):
    url = 'http://axecop.com/comic/season-two/'


class Bardsworth(_WordpressScraper):
    url = 'http://www.bardsworth.com/'


class BloodBound(_WordpressScraper):
    url = 'http://bloodboundcomic.com/'


class BratHalla(_WordpressScraper):
    url = 'http://brat-halla.com/'


class BroodHollow(_WordpressScraper):
    url = 'http://broodhollow.chainsawsuit.com/'


class Buni(_WordpressScraper):
    url = 'http://www.bunicomic.com/'


class BusinessCat(_WordpressScraper):
    url = 'http://www.businesscat.happyjar.com/'


class Catena(_WordpressScraper):
    url = 'http://catenamanor.com/'


class CatsAndCameras(_WordpressScraper):
    url = 'http://catsncameras.com/'


class CraftedFables(_WordpressScraper):
    url = 'http://www.caf-fiends.net/comicpress/'


class CourtingDisaster(_WordpressScraper):
    url = 'http://www.courting-disaster.com/'


class CowboyJedi(_WordpressScraper):
    url = 'http://www.cowboyjedi.com/'


class FowlLanguage(_WordpressScraper):
    url = 'http://www.fowllanguagecomics.com/'


class HappyJar(_WordpressScraper):
    url = 'http://www.happyjar.com/'


class Hipsters(_WordpressScraper):
    url = 'http://www.hipsters-comic.com/'


class IDreamOfAJeanieBottle(_WordpressScraper):
    url = 'http://jeaniebottle.com/'


class ItsWalky(_WordpressScraper):
    url = 'http://www.itswalky.com/'


class KatzenfutterGeleespritzer(_WordpressScraper):
    url = 'http://www.katzenfuttergeleespritzer.de/'
    lang = 'de'


class Meek(_WordpressScraper):
    url = 'http://www.meekcomic.com/'


class Meiosis(_WordpressScraper):
    url = 'http://meiosiswebcomic.com/'


class Melonpool(_WordpressScraper):
    url = 'http://www.melonpool.com/'


class MistyTheMouse(_WordpressScraper):
    url = 'http://www.mistythemouse.com/'


class Nedroid(_WordpressScraper):
    url = 'http://nedroid.com/'


class NerfNow(_WordpressScraper):
    url = 'https://www.nerfnow.com/'


class Nicky510(_WordpressScraper):
    url = 'http://www.nickyitis.com/'


class OnTheEdge(_WordpressScraper):
    url = 'http://ontheedgecomics.com/'


class PandyLand(_WordpressScraper):
    url = 'http://pandyland.net/'


class SailorsunOrg(_WordpressScraper):
    url = 'http://sailorsun.org/'


class Sharksplode(_WordpressScraper):
    url = 'http://sharksplode.com/'
    textSearch = '//div[@id="comic"]//img/@alt'


class Sithrah(_WordpressScraper):
    url = 'http://sithrah.com/'


class SlightlyDamned(_WordpressScraper):
    url = 'http://www.sdamned.com/'


class SPQRBlues(_WordpressScraper):
    url = 'http://spqrblues.com/IV/'


class TheDreamlandChronicles(_WordpressScraper):
    url = 'http://www.thedreamlandchronicles.com/'


class TheGentlemansArmchair(_WordpressScraper):
    url = 'http://thegentlemansarmchair.com/'


class TheMelvinChronicles(_WordpressScraper):
    url = 'http://melvin.jeaniebottle.com/'


class YAFGC(_WordpressScraper):
    url = 'http://yafgc.net/'

# all comics on HijiNKS ENSUE
for (name, starterXPath) in [
    ('HijinksEnsue', '//h4[text()="Read The Latest HijiNKS ENSUE"]/..//a'),
    ('HijinksEnsueClassic', '//h4[text()="Read HijiNKS ENSUE Classic"]/..//a[3]'),
    ('Faneurysm', '//h4[text()="Read The Latest FANEURYSM"]/..//a'),
    ('HijinksEnsueConvention', '//h4[text()="Latest Fancy Convention Sketches"]/..//a'),
    ('HijinksEnsuePhoto', '//h4[text()="Latest Fancy Photo Comic"]/..//a')
]:
    add(name, 'http://hijinksensue.com/', starter=indirectStarter('http://hijinksensue.com/', starterXPath))

# all comics on flowerlarkstudios
for (name, linkNumber) in [
    ('Ashes', 1),
    ('Eryl', 3),
    # this is a duplicate as it was under this name in previous versions of dosage
    ('DarkWings', 3),
    ('Laiyu', 5),
    ('NoMoreSavePoints', 7),
    ('EasilyAmused', 9)
]:
    add(name, 'http://www.flowerlarkstudios.com/',
        starter=indirectStarter('http://www.flowerlarkstudios.com/',
                                '(//div[@id="sidebar-left"]//a)[' + str(linkNumber) + ']'))

# all comics on the webcomic factory

for (name, url) in [
    ('AntiwarComic', 'the-antiwar-comic-the-party/'),
    ('AstheMayoTurns', 'as-the-mayo-turns/'),
    ('ComicBookMafia', 'comic-book-mafia/'),
    ('Dealers', 'dealers-1-1998-was-the-year/'),
    ('DigitalHobo', 'digital-hobo-1-its-a-living-kinda/'),
    ('EastCoastVsWestCoast', 'east-coast-vs-west-coast-greetings-from-the-coasts/'),
    ('GunCulture', 'gun-culture/'),
    ('IHateMyKids', 'i-hate-my-kids/'),
    ('InARelationship', 'in-a-relationship-3/'),
    ('JapaneseSchoolgirlsinLove', 'japanese-schoolgirls-in-love-1/'),
    ('KingdomoftheDwarves', 'kingdom-of-the-dwarves/'),
    ('LesterCrenshawisDead', 'lester-crenshaw-is-dead/'),
    ('Millennials', 'millennials/'),
    ('MiserableComedians', 'miserable-comedians-1-funny-because-its-sad/'),
    ('OldeTymeGamer', 'olde-tyme-gamer-playing-injured/'),
    ('PinJunkies', 'pin-junkies/'),
    ('PostApocalypticNick', 'post-apocalyptic-nick/'),
    ('RealTalk', 'real-talk-people-who-cut-in-line/'),
    ('SoManyNightmares', 'so-many-nightmares-freedom-nightmare/'),
    ('SportsGuys', 'sports-guys/'),
    ('TalesOfPizza', 'tales-of-pizza-bad-tipper/'),
    ('TheGentlemensClub', 'the-gentlemens-club/'),
    ('TheHorrorOfColony6', 'the-horror-of-colony-6-page-1/'),
    ('TheKingsofViralVideo', 'the-kings-of-viral-video-premiere/'),
    ('TheSharonandTonyExperiment', 'the-sharon-and-tony-experiment/'),
    ('TonyDestructo', 'tony-destructo/'),
    ('WeirdBikerTales', 'weird-biker-tales-the-last-outlaw/'),
    ('WillysSpaceDive', 'willys-space-dive/')
]:
    add(name, 'http://www.thewebcomicfactory.com',
        starter=indirectStarter('http://www.thewebcomicfactory.com/comic/' + url,
                                "//a[contains(concat(' ', text(), ' '), ' Last ')]"))
