"""Gen objects"""

import string
import zlib

from numpy import random as nprand

import driver

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

def gen_user(count):
    queris_pool = ""
    queris_in_pool = 0

    for i in range(0, count, 1):
    
        bill_id = nprand.randint(1, 1000000)
        user_id = nprand.randint(1, 1000000)
        balance = nprand.randint(50, 100000000)
        name = gen_name(random.randint(1, 5))

    queris_pool += "INSERT INTO . (user_id, name, balance, bill_id) VALUES ('%s', '%s', '%s', '%s'); " % (
            user_id, name, balance, bill_id)

    queris_in_pool += 1
    
    if queris_in_pool >= 500:
            queris_in_pool = 0
            driver.execute_cqlsh(queris_pool)
            queris_pool = ""

    driver.execute_cqlsh(queris_pool)

def gen_bank_adress(): #bl9 ne beite
    cityname = ('A', 'B', 'C', 'D', 'E') 
    streetname = ('a', 'b', 'c', 'd', 'e') 
    city_name = nprand.choice(cityname) 
    street_name = nprand.choice(streetname)
    house_number = nprand.randint(001, 999) 

def gen_bank():
    queris_pool = ""
    queris_in_pool = 0

    for i in range(0, count, 1):
        bank_name = gen_name(random.randint(6,9))
        banktype = ('Commercial', 'Central', 'Investment') 
        bank_type = nprand.choice(banktype)
        bank_number = nprand.randint(00000000001, 99999999999) 
        bank_id = gen_crc32_hash(bank_name)
        bank_capital = nprand.randint(50000000, 100000000)

    queris_in_pool += 1
    
    if queris_in_pool >= 500:
            queris_in_pool = 0
            driver.execute_cqlsh(queris_pool)
            queris_pool = ""

    driver.execute_cqlsh(queris_pool)

def gen_situations():
    name_bank = gen_name(random.randint(4, 6))
    s1 = ('Works stably and without delays')
    s2 = ('This year the banks capital increased')
    s3 = ('The dollar rate rose by 32 kopecks and the bank went bankrupt, all employees were fired and the coins of the bank climbed into huge debts. ')
    sits_list = (s1, s2, s3)
    nprand.choice(sits_list)
