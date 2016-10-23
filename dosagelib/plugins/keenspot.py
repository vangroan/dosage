# -*- coding: utf-8 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from ..scraper import _ParserScraper


class KeenSpot(_ParserScraper):
    multipleImagesPerStrip = True
    imageSearch = (
        '//img[contains(@src, "/comics/")]',
        # Shockwave Darkside
        '//img[contains(@src, "/comics2D/")]',
        '//img[contains(@src, "com/shockwave")]',
        # Sore Thumbs
        '//img[contains(@src, "com/st2")]',
        # Wayward Sons
        '//img[contains(@src, "com/2")]',
    )
    prevSearch = (
        '//link[@rel="prev"]',
        '//a[@rel="prev"]',
        # Exposure
        '//a[img[@id="exp29"]]',
        # Hero By Night
        '//area[contains(@coords, ",-7,")]',
        # Katrina
        '//a[img[@id="katc7"]]',
        # No Room For Magic, Everyone Loves Adis, Wisdom Of Moo
        '//a[text()="Previous comic"]',
        # Supernovas
        '//a[img[@id="p_top_nav"]]',
    )
    help = 'Index format: yyyymmdd'

    def __init__(self, name, sub, last=None, path='d/%s.html'):
        super(KeenSpot, self).__init__('KeenSpot/' + name)
        self.url = 'http://%s.keenspot.com/' % sub
        self.stripUrl = self.url + path

        if last:
            self.url = self.stripUrl % last
            self.endOfLife = True

    @classmethod
    def getmodules(cls):
        return (
            # Not on frontpage...
            cls('Buzzboy', 'buzzboy'),
            cls('EveryoneLovesAdis', 'adis'),

            # do not edit anything below since these entries are generated from
            # scripts/update_plugins.sh
            # START AUTOUPDATE
            cls('27TwentySeven', 'twenty-seven'),
            cls('Avengelyne', 'avengelyne'),
            cls('BanzaiGirl', 'banzaigirl'),
            cls('Barker', 'barkercomic'),
            cls('ChoppingBlock', 'choppingblock'),
            cls('ClichFlamb', 'clicheflambe'),
            cls('CountYourSheep', 'countyoursheep'),
            cls('CrowScare', 'crowscare', last="20111031"),
            cls('Dreamless', 'dreamless', last="20100726"),
            cls('EverythingJake', 'everythingjake'),
            cls('Exposure', 'exposure'),
            cls('FallOutToyWorks', 'fallouttoyworks'),
            cls('FriarAndBrimstone', 'friarandbrimstone'),
            cls('GeneCatlow', 'genecatlow'),
            cls('GodMode', 'godmode'),
            cls('GreenWake', 'greenwake'),
            cls('HeadTrip', 'headtrip'),
            cls('HeroByNight', 'herobynight'),
            cls('HoaxHunters', 'hoaxhunters'),
            cls('InfinityRefugees', 'newshounds'),
            cls('InHere', 'inhere'),
            cls('JadeWarriors', 'jadewarriors'),
            cls('Katrina', 'katrina'),
            cls('Landis', 'landis'),
            cls('LutherStrode', 'lutherstrode'),
            cls('MakeshiftMiracle', 'makeshiftmiracle'),
            cls('Marksmen', 'marksmen'),
            cls('MarryMe', 'marryme'),
            cls('MedusasDaughter', 'medusasdaughter'),
            cls('MonsterMassacre', 'monstermassacre'),
            cls('MysticRevolution', 'mysticrevolution', path="?cid=%s"),
            cls('NoPinkPonies', 'nopinkponies'),
            cls('NoRoomForMagic', 'noroomformagic'),
            cls('OutThere', 'outthere'),
            cls('Porcelain', 'porcelain'),
            cls('PunchAnPie', 'punchanpie', path="daily/%s.html"),
            cls('QUILTBAG', 'quiltbag'),
            cls('RedSpike', 'redspike'),
            cls('RumbleFall', 'rumblefall'),
            cls('SamuraisBlood', 'samuraisblood'),
            cls('Sharky', 'sharky'),
            cls('ShockwaveDarkside', 'shockwave', path="2d/%s.html"),
            cls('SomethingHappens', 'somethinghappens'),
            cls('SoreThumbs', 'sorethumbs'),
            cls('Striptease', 'striptease'),
            cls('Supernovas', 'supernovas'),
            cls('Superosity', 'superosity'),
            cls('TheFirstDaughter', 'thefirstdaughter'),
            cls('TheHopeVirus', 'hopevirus'),
            cls('TheHuntersOfSalamanstra', 'salamanstra'),
            cls('TheLounge', 'thelounge'),
            cls('TheVault', 'thevault'),
            cls('WaywardSons', 'waywardsons'),
            cls('WeirdingWillows', 'weirdingwillows'),
            cls('WICKEDPOWERED', 'wickedpowered'),
            cls('WisdomOfMoo', 'wisdomofmoo'),
            cls('Yirmumah', 'yirmumah', path="%s/"),
            # END AUTOUPDATE
        )

    def shouldSkipUrl(self, url, data):
        return url in (
            'http://sorethumbs.keenspot.com/d/20160117.html'
        )
