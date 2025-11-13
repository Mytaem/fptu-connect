# src_w2/w2_seeder.py
import random
from typing import Tuple

def seed_by_indexes(
    sn,
    p_class: float = 0.25,     # xác suất kết nối nếu cùng lớp
    p_club: float  = 0.35,     # xác suất kết nối nếu cùng CLB
    p_home: float  = 0.15,     # xác suất kết nối nếu cùng quê
    max_new_per_student: int = 15,  # tối đa số bạn mới/1 SV
    rng_seed: int = 123
) -> Tuple[int, int]:
    """
    Tạo kết nối bạn bè dựa trên chỉ mục của tuần 1.
    Trả về (so_ket_noi_moi_thuc_te, so_sinh_vien_co_ket_noi_moi).
    """
    random.seed(rng_seed)
    added_edges = 0
    touched_students = 0

    # helper: sinh ứng viên theo lớp/CLB/quê, không trùng & chưa là bạn
    def iter_candidates(sid, info):
        seen = set()
        # cùng lớp
        for c in info.get("classes", []):
            for x in sn.idx_class.get(c, ()):
                if x != sid and x not in sn.adj[sid] and x not in seen:
                    seen.add(x); yield x, "class"
        # cùng CLB
        for clb in info.get("clubs", []):
            for x in sn.idx_club.get(clb, ()):
                if x != sid and x not in sn.adj[sid] and x not in seen:
                    seen.add(x); yield x, "club"
        # cùng quê
        for x in sn.idx_home.get(info.get("hometown", ""), ()):
            if x != sid and x not in sn.adj[sid] and x not in seen:
                seen.add(x); yield x, "home"

    for sid, info in sn.students.items():
        created = 0
        for cand, src in iter_candidates(sid, info):
            # áp xác suất theo nguồn
            r = random.random()
            if   src == "class" and r >= p_class:  continue
            elif src == "club"  and r >= p_club:   continue
            elif src == "home"  and r >= p_home:   continue

            # tránh thêm cạnh 2 lần: chỉ thêm khi sid < cand
            if sid < cand:
                sn.add_friend(sid, cand)
                added_edges += 1
                created += 1
                if created >= max_new_per_student:
                    break
        if created > 0:
            touched_students += 1

    return added_edges, touched_students
