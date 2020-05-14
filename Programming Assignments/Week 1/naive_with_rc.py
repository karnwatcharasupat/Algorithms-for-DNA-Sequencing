from utils import *

def naive_with_rc(p, t):
    q = reverseComplement(p)

    if p == q:
        p_occ = naive(p, t)
        q_occ = []
    else:
        p_occ = naive(p, t)
        q_occ = naive(q, t)
    
    return p_occ, q_occ


