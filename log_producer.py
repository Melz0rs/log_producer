import pandas as pd
from datetime import datetime
from random import randint
from time import sleep

referrers = list(pd.read_csv("data/referrers.csv"))
products = list(pd.read_csv("data/products.csv"))
actions = list(pd.read_csv("data/actions.csv"))

records_threshold = 1000

f = open("log.txt", "w").close()

while records_threshold > 0:
    f = open("log.txt", "a+")

    records_threshold -= 1

    timestamp = datetime.now()

    referrer_int = randint(0, len(referrers) - 1)
    referrer = referrers[referrer_int]

    product_int = randint(0, len(products) - 1)
    product = products[product_int]

    action_int = randint(0, len(actions) - 1)
    action = actions[action_int]

    log_line = f'{timestamp}\t{referrer}\t{action}\t{product}\n'

    f.write(f'{log_line}')

    sleep(randint(5, 150) / 100)

    f.close()




