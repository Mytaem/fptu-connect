# src_w3/mutual_w3.py
def mutual_friends(sn, u: str, v: str):
    """
    Trả về tập bạn chung giữa u và v
    """
    if u not in sn.students or v not in sn.students:
        return set()
    return sn.friends_of(u) & sn.friends_of(v)
