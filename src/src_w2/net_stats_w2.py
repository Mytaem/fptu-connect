def compute_stats(sn):
    nodes = len(sn.students)
    edges = sum(len(s.friends) for s in sn.students.values()) // 2
    avg_degree = sum(len(s.friends) for s in sn.students.values()) / nodes if nodes else 0
    return {"nodes": nodes, "edges": edges, "avg_degree": avg_degree}