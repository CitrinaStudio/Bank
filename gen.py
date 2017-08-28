"""Gen objects"""

import random
import string
import zlib


from numpy import random as nprand

def gen_name(size):
    tumbler = nprand.randint(1, 3)
    if tumbler == 1:
        return string.capwords(''.join(random.choice(string.ascii_uppercase) for _ in range(size)))
    else:
        return string.capwords(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(size)))

