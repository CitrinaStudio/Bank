from numpy import random as nprand
from cassandra.cluster import Cluster

from gen import *

import driver


CLUSTER = Cluster()
SESSION = CLUSTER.connect('bank_0')

def check_record_exist(obj_type, keyspace_name,):

    query = int(list(list(SESSION.execute("""SELECT count(*) FROM %s.%s WHERE id='%s';""" % (keyspace_name, obj_type, gen_crc32_hash(poz)) )) [0]) [0])

    if query == 1:

        print("/|\\")
        tumbler = 0

        while tumbler == 0:
            print("/|\\")

            
            poz = (x, y, z)



            query = int(list(list(SESSION.execute("""SELECT count(*) FROM %s.%s WHERE id='%s';""" % (keyspace_name, obj_type, gen_crc32_hash()) )) [0]) [0])

            if query == 0:
                tumbler = 1
    
    return poz