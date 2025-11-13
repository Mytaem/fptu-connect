# src_w3/demo_w3.py
from src_w1.core_w1 import StudentNetworkW1
from src_w1.io_w1 import load_students
from src_w2.io_w2 import load_edges, apply_edges
from src_w3.mutual_w3 import mutual_friends
from src_w3.path_w3 import shortest_path
from src_w3.components_w3 import connected_components
from src_w2.net_stats_w2 import compute_stats

def run_demo():
    # 1) Nạp dữ liệu sinh viên + edges từ tuần 2
    students = load_students("data_w1/students_w1.json")
    sn = StudentNetworkW1()
    for s in students:
        sn.add_user(s)

    edges = load_edges("data_w2/edges_w2.json")
    apply_edges(sn, edges)

    print("Thống kê mạng:", compute_stats(sn))

    # 2) Tìm bạn chung
    u, v = "w1_0001", "w1_0002"
    mutuals = mutual_friends(sn, u, v)
    print(f"Bạn chung giữa {u} và {v}:", list(mutuals)[:10])

    # 3) Tìm đường đi ngắn nhất
    start, goal = "w1_0001", "w1_0100"
    path = shortest_path(sn, start, goal)
    if path:
        print(f"Đường đi ngắn nhất {start} -> {goal}: {' -> '.join(path)} (độ dài {len(path)-1})")
    else:
        print(f"Không tìm thấy đường đi giữa {start} và {goal}")

    # 4) Tìm các nhóm
    comps = connected_components(sn)
    print(f"Tổng số nhóm (connected components): {len(comps)}")
    print("Kích thước 5 nhóm đầu:", [len(c) for c in comps[:5]])

if __name__ == "__main__":
    run_demo()
