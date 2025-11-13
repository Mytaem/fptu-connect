# src_w4/topk_w4.py
import heapq

def topk_by_degree(sn, k: int = 10):
    """
    Tìm k sinh viên có nhiều bạn nhất.
    Trả về list (id, degree).
    """
    degrees = [(len(sn.friends_of(u)), u) for u in sn.students]
    topk = heapq.nlargest(k, degrees)
    # đảo tuple để in đẹp (id, degree)
    return [(u, d) for d, u in topk]
