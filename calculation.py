import numpy as np

def L2_dist(emb1,emb2):
    """
    It calculate the L2 distance between embedding 1 and embedding 2,
    and return True if the L2 distance is below the threhold.
    """

    dist = np.sqrt(np.sum((emb1-emb2)**2))
    return dist
