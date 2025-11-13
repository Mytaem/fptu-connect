1# src_w1/core_w1.py
from collections import defaultdict

class StudentNetworkW1:
    def __init__(self):
        self.students = {}       # id -> thông tin sinh viên
        self.adj = {}            # id -> set(id bạn bè)

        # Chỉ mục
        self.idx_class = defaultdict(set)
        self.idx_club = defaultdict(set)
        self.idx_faculty = defaultdict(set)
        self.idx_home = defaultdict(set)

    def add_user(self, student: dict):
        sid = student["id"]
        self.students[sid] = student
        self.adj.setdefault(sid, set())

        # cập nhật chỉ mục
        for c in student.get("classes", []):
            self.idx_class[c].add(sid)
        for clb in student.get("clubs", []):
            self.idx_club[clb].add(sid)
        fac = student.get("faculty")
        if fac: self.idx_faculty[fac].add(sid)
        home = student.get("hometown")
        if home: self.idx_home[home].add(sid)

    def add_friend(self, u, v):
        if u in self.students and v in self.students and u != v:
            self.adj[u].add(v)
            self.adj[v].add(u)

    def friends_of(self, u):
        return self.adj.get(u, set())
