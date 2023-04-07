import os
from datetime import datetime

from polygon import RESTClient

client = RESTClient(os.environ.get("POLYGON_API_KEY") or 'slfhowwfy')

def get_upl_and_apiKey(url):
    return url+'?apiKey='+os.environ.get('POLYGON_API_KEY')

def get_month_list():
    ps = []
    count = 0
    for r in range(1, 13):
        qw = datetime(year=2020, month=r, day=1)
        ps.append(qw.strftime("%B"))
        count = count + 1
    return ps


rus_months = ['январь','февраль','март','апрель','май',
        'июнь','июль','август','сентябрь','октябрь',
        'ноябрь','декабрь',
    ]


def get_rus_month(m):
    return rus_months[m-1]