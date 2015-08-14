from dosagelib.helpers import indirectStarter
from dosagelib.plugins.wordpress import _WordpressScraper
from dosagelib.scraper import make_scraper


def add(name, url, starter=None):
    attrs = dict(
        name=name,
        url=url,
        starter=starter
    )
    globals()[name] = make_scraper(name, _WordpressScraper, **attrs)


__author__ = 'null'
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
