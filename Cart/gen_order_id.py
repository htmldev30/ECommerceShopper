import random
import string
from datetime import date
import datetime
from time import time

from Cart.models import OrderItem

def generate_order_id():
    date_str = time.strftime('%Y%m')[2:] + str(datetime.datetime).now().second
    rand_str = "".join([random.choice(string.digits) for counter in range(3)])
    return date_str + rand_str