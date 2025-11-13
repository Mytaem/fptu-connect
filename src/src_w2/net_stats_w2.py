# src_w2/net_stats_w2.py
def compute_stats(sn):
    """
    Tính nhanh các thống kê cơ bản về mạng:
    - nodes, edges, avg_degree, min/max degree
    """
    n = len(sn.students)
    # số cạnh = 1/2 * tổng bậc
    degrees = [len(sn.adj[u]) for u in sn.students]
    m = sum(degrees) // 2
    avg_deg = (sum(degrees) / n) if n else 0
    min_deg = min(degrees) if degrees else 0
    max_deg = max(degrees) if degrees else 0
    return {
        "nodes": n,
        "edges": m,
        "avg_degree": round(avg_deg, 2),
        "min_degree": min_deg,
        "max_degree": max_deg,
    }
