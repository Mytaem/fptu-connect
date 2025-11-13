# src_w4/suggest_w4.py
def suggest_friends(sn, u: str, top_n: int = 5):
    """
    Gợi ý bạn bè cho sinh viên u dựa trên số bạn chung nhiều nhất.
    Trả về list (id, số_bạn_chung).
    """
    if u not in sn.students:
        return []

    current_friends = sn.friends_of(u)
    scores = {}

    # duyệt bạn bè của bạn bè
    for f in current_friends:
        for cand in sn.friends_of(f):
            if cand == u or cand in current_friends:
                continue
            # tăng điểm nếu có nhiều bạn chung
            scores[cand] = scores.get(cand, 0) + 1

    # sắp xếp theo số bạn chung giảm dần
    sorted_cands = sorted(scores.items(), key=lambda x: (-x[1], x[0]))
    return sorted_cands[:top_n]
