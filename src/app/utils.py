import string
import random



def random_str(size:int):
    # using random.choices()
    # generating random strings
    res = ''.join(random.choices(string.ascii_lowercase +
                                string.digits, k=size))
    # return result
    return res    