import datetime
import logging
from . import city_to_tzs

logger = logging.getLogger(__name__)

def get_time_zone_by_name(city):
    """
    Return list of tz for city
    """
    try:
        return city_to_tzs[city]
    except keyError as e:
        logger.error(e)
        raise

def get_curr_city_time_by_name(city, fmt=None):
    try:
        city_tzs = get_time_zone_by_name(city)
    except KeyError:
        logger.error("Could not fetch TZs for %s" % city)
        return {}

    if fmt is None:
        fmt = '%Y-%m-%d %H:%M:%S %Z%z'
    curr_times = {}

    for city_tz in city_tzs:
        _now = datetime.datetime.now(datetime.tzinfo(city_tz))
        curr_times[city_tz] = _now.strftime(fmt)
    return curr_times
