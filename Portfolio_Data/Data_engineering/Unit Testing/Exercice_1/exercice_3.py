import numpy as np



def array(string):
    np.random.seed(10)
    random_nb = np.random.rand(1)
    return string + ' ' + str(random_nb)


