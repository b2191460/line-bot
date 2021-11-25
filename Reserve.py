import re

import datetime,schedule,time

def Reserve(word):
    if re.search('予約',word):
