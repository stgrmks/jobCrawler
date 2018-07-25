# coding: utf-8
__author__ = 'MSteger'

import datetime

umlaute_dict = {
    '\xc3\xa4': 'ae',  # U+00E4	   \xc3\xa4
    '\xc3\xb6': 'oe',  # U+00F6	   \xc3\xb6
    '\xc3\xbc': 'ue',  # U+00FC	   \xc3\xbc
    '\xc3\x84': 'Ae',  # U+00C4	   \xc3\x84
    '\xc3\x96': 'Oe',  # U+00D6	   \xc3\x96
    '\xc3\x9c': 'Ue',  # U+00DC	   \xc3\x9c
    '\xc3\x9f': 'ss',  # U+00DF	   \xc3\x9f
}

def replace_umlaute(unicode_string, return_unicode = False):
    utf8_string = unicode_string.encode('utf-8')

    for k in umlaute_dict.keys():
        utf8_string = utf8_string.replace(k, umlaute_dict[k])

    if return_unicode: utf8_string = utf8_string.decode()
    return utf8_string


def timeDiffDays(dt):
    diff_hr = float((datetime.datetime.now() - dt).total_seconds())/60**2
    return round(diff_hr / 24,2)