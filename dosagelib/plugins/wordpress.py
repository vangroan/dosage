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
    ('AsTheMayoTurns', 'as-the-mayo-turns/'),
    ('ComicBookMafia', 'comic-book-mafia/'),
    ('Dealers', 'dealers-1-1998-was-the-year/'),
    ('DigitalHobo', 'digital-hobo-1-its-a-living-kinda/'),
    ('EastCoastVsWestCoast', 'east-coast-vs-west-coast-greetings-from-the-coasts/'),
    ('GunCulture', 'gun-culture/'),
    ('IHateMyKids', 'i-hate-my-kids/'),
    ('InARelationship', 'in-a-relationship-3/'),
    ('JapaneseSchoolgirlsInLove', 'japanese-schoolgirls-in-love-1/'),
    ('KingdomOfTheDwarves', 'kingdom-of-the-dwarves/'),
    ('LesterCrenshawIsDead', 'lester-crenshaw-is-dead/'),
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
    ('TheKingsOfViralVideo', 'the-kings-of-viral-video-premiere/'),
    ('TheSharonAndTonyExperiment', 'the-sharon-and-tony-experiment/'),
    ('TonyDestructo', 'tony-destructo/'),
    ('WeirdBikerTales', 'weird-biker-tales-the-last-outlaw/'),
    ('WillysSpaceDive', 'willys-space-dive/')
]:
    add(name, 'http://www.thewebcomicfactory.com',
        starter=indirectStarter('http://www.thewebcomicfactory.com/comic/' + url,
                                "//a[contains(concat(' ', text(), ' '), ' Last ')]"))
