"""Gen objects"""

import string
import zlib
import random

from numpy import random as nprand

import driver

def gen_crc32_hash(params):
    id = str(hex(zlib.crc32(str(params).encode("utf-8"))).split('x')[-1])

    return id

def gen_name(size):
    tumbler = nprand.randint(1, 3)
    if tumbler == 1:
        return string.capwords(''.join(random.choice(string.ascii_uppercase) for _ in range(size)))
    else:
        return string.capwords(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(size)))

def gen_id(params):
    return zlib.adler32(str(params).encode('utf-8'))

def gen_card():
    ctype = ('Debit', 'Credit')
    card_type = nprand.choice(ctype)
    card_number = nprand.randint(1000000000000000, 9999999999999999)
    card_id = gen_crc32_hash(card_number)

    return (card_type, card_number, card_id)

def gen_user(count):
    queris_pool = ""
    queris_in_pool = 0

    sits_list = ('Works stably and without delays', 'This year the banks capital increased', 'The dollar rate rose by 32 kopecks and the bank went bankrupt, all employees were fired and the coins of the bank climbed into huge debts. ')
    situation = nprand.choice(sits_list)

    for i in range(0, count, 1):
        
        if 

        bill_id = nprand.randint(1, 1000000)
        user_id = nprand.randint(1, 1000000)
        name = gen_name(nprand.randint(1, 5))

    queris_pool += "INSERT INTO bank_0.user (user_id, name, balance, bill_id) VALUES ('%s', '%s', '%s', '%s'); " % (
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
    house_number = nprand.randint(100, 999) 

def gen_bank():

    for i in range(1):
        bank_name = gen_name(random.randint(6,9))
        banktype = ('Commercial', 'Central', 'Investment') 
        bank_type = nprand.choice(banktype)
        bank_number = nprand.randint(10000000000, 99999999999) 
        bank_id = gen_crc32_hash(bank_name)
        bank_capital = nprand.randint(50000000, 100000000)

    queris_pool += "INSERT INTO bank_0.bank (bank_id, bank_name, bank_type, bank_number, bank_capital) VALUES ('%s', '%s', '%s', '%s', '%s'); " % (
            bank_id, bank_name, bank_type, bank_number,bank_capital)

    driver.execute_cqlsh(queris_pool)


        
