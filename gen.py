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
    name = gen_name(random.randint(3, 7))

def gen_situations():
    name_bank = gen_name(random.randint(4, 6))
    s1 = ('Works stably and without delays')
    s2 = ('This year the banks capital increased')
    s3 = ('The dollar rate rose by 32 kopecks and the bank went bankrupt, all employees were fired and the coins of the bank climbed into huge debts. ')
    sits_list = (s1, s2, s3)
    nprand.choice(sits_list)
