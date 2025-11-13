# src_w4/degree_dist_w4.py
from collections import Counter

def degree_distribution(sn):
    """
    Trả về dict {degree: số_sinh_viên}
    """
    degs = [len(sn.friends_of(u)) for u in sn.students]
    return dict(Counter(degs))
