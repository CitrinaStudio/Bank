"""Gen objects"""

import string
import zlib


from numpy import random as nprand

def gen_crc32_hash(params):
    id = str(hex(zlib.crc32(str(params).encode("utf-8"))).split('x')[-1])

    return id

def gen_name(size):
    tumbler = nprand.randint(1, 3)
    if tumbler == 1:
        return string.capwords(''.join(nprand.choice(string.ascii_uppercase) for _ in range(size)))
    else:
        return string.capwords(''.join(nprand.choice(string.ascii_uppercase + string.digits) for _ in range(size)))

def gen_id(params):
    return zlib.adler32(str(params).encode('utf-8'))

def gen_card():
    ctype = ('Debit', 'Credit')
    card_type = nprand.choice(ctype)
    card_number = nprand.randint(0000000000000001, 9999999999999999)
    card_id = gen_crc32_hash(card_number)

    return (card_type, card_number, card_id)

def gen_user():
    bill_id = nprand.randint(1, 1000000)
    user_id = nprand.randint(1, 1000000)
    balance = nprand.randint(50, 100000000)
    name = gen_name(random.randint(1, 5))
