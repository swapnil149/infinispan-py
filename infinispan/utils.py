# -*- coding: utf-8 -*-

import re

from infinispan.hotrod import TimeUnits


UNIT_CONVERSION_DICT = {
    's': TimeUnits.SECONDS,
    'ms': TimeUnits.MILISECONDS,
    'ns': TimeUnits.NANOSECONDS,
    'us': TimeUnits.MICROSECONDS,
    'm': TimeUnits.MINUTES,
    'h': TimeUnits.HOURS,
    'd': TimeUnits.DAYS
}


def from_pretty_time(time):
    if time == 'inf':
        return (None, TimeUnits.INFINITE)
    elif time == 'def':
        return (None, TimeUnits.DEFAULT)

    time_match = re.match(r'^(\d+)([a-z]+)$', time)
    if not time_match:
        raise ValueError("Invalid time format")
    groups = time_match.groups()
    if groups[1] not in UNIT_CONVERSION_DICT:
        raise ValueError("Invalid time format unit '%s'", groups[1])

    duration, unit = int(groups[0]), UNIT_CONVERSION_DICT[groups[1]]
    return duration, unit


def get_all_subclasses(cls):
    all_subclasses = []

    for subclass in cls.__subclasses__():
        all_subclasses.append(subclass)
        all_subclasses.extend(get_all_subclasses(subclass))

    return all_subclasses
