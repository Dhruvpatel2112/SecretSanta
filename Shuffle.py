import random
import numpy

def shuffle_fun(dict1):
    keys=list(dict1.keys())
    random.shuffle(keys)
    #creates a new shuffled dictionary...........
    dict2 = {k: dict1[k] for k in keys}
    #shifts keys.............
    keys=numpy.roll(keys,random.randrange(1,len(keys)))
    return  dict(zip(keys, dict2.values()))