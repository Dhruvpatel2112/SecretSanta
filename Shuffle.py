import random
def shuffle_fun(dic1):
    keys=list(dic1.keys())
    random.shuffle(keys)
    return  dict(zip(keys, dic1.values()))