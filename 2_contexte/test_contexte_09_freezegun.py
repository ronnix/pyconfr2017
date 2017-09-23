"""
Geler le temps avec freezegun
"""
from datetime import datetime

from freezegun import freeze_time


def c_est_le_week_end():
    return datetime.utcnow().isoweekday() in (6, 7)


def test_lundi():
    with freeze_time(datetime(2017, 9, 18)):
        assert not c_est_le_week_end()


def test_samedi():
    with freeze_time(datetime(2017, 9, 23)):
        assert c_est_le_week_end()
