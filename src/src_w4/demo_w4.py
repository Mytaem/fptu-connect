# src_w4/demo_w4.py
from src_w1.core_w1 import StudentNetworkW1
from src_w1.io_w1 import load_students
from src_w2.io_w2 import load_edges, apply_edges
from src_w4.suggest_w4 import suggest_friends
from src_w4.topk_w4 import topk_by_degree
from src_w4.degree_dist_w4 import degree_distribution

def run_demo():
    # 1) Nạp dữ liệu tuần 1 + edges tuần 2
    students = load_students("data_w1/students_w1.json")
    sn = StudentNetworkW1()
    for s in students:
        sn.add_user(s)

    edges = load_edges("data_w2/edges_w2.json")
    apply_edges(sn, edges)

    # 2) Gợi ý bạn bè
    u = "w1_0001"
    suggestions = suggest_friends(sn, u, top_n=5)
    print(f"Gợi ý bạn bè cho {u}:")
    for cand, score in suggestions:
        print(f"  {cand} (bạn chung: {score})")

    # 3) Top-k sinh viên có nhiều bạn nhất
    print("\nTop 5 sinh viên nổi bật nhất (nhiều kết nối):")
    for sid, deg in topk_by_degree(sn, 5):
        print(f"  {sid} ({deg} bạn)")

    # 4) Phân phối bậc
    dist = degree_distribution(sn)
    print("\nMột phần phân phối bậc (degree distribution):")
    for d in sorted(dist.keys())[:10]:
        print(f"  {d} bạn: {dist[d]} sinh viên")

if __name__ == "__main__":
    run_demo()
