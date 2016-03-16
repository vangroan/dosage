# -*- coding: utf-8 -*-
# Copyright (C) 2013-2014 Bastian Kleineidam
# Copyright (C) 2016 Tobias Gruetzmacher

import pytest
import sys
from . import dosage_cmd, run_checked, tmpdir  # noqa


def run_with_options(options, cmd=dosage_cmd):
    """Run dosage with given options."""
    run_checked([sys.executable, cmd, '--allow-multiple'] + options)


class TestDosage(object):
    """Test the dosage commandline client."""

    def test_list_comics(self):
        for option in ("-l", "--list", "--singlelist"):
            run_with_options([option])

    def test_display_version(self):
        run_with_options(["--version"])

    def test_display_help(self):
        for option in ("-h", "--help"):
            run_with_options([option])

    def test_module_help(self):
        run_with_options(["-m", "xkcd"])

    def test_no_comics_specified(self):
        with pytest.raises(OSError):
            run_with_options([])

    def test_unknown_option(self):
        with pytest.raises(OSError):
            run_with_options(['--imadoofus'])

    def test_multiple_comics_match(self):
        with pytest.raises(OSError):
            run_with_options(['Garfield'])

    def test_fetch_html_and_rss(self, tmpdir):  # noqa
        run_with_options(["-n", "2", "-v", "-b", tmpdir, "-o", "html", "-o",
                          "rss", "xkcd"])

    def test_fetch_html_and_rss_2(self, tmpdir):  # noqa
        run_with_options(["--numstrips", "2", "--baseurl", "bla",
                          "--basepath", tmpdir, "--output", "rss", "--output",
                          "html", "--adult", "oglaf"])

    def test_fetch_indexed(self, tmpdir):  # noqa
        run_with_options(["-n", "2", "-v", "-b", tmpdir, "xkcd:303"])
