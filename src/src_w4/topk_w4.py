def topk_by_degree(sn, k=10):
    return sorted(
        sn.students.items(),
        key=lambda x: len(x[1].friends),
        reverse=True
    )[:k]
