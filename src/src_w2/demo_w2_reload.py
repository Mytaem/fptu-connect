# src_w2/demo_w2_reload.py
from src_w1.core_w1 import StudentNetworkW1
from src_w1.io_w1 import load_students
from src_w2.io_w2 import load_edges, apply_edges
from src_w2.net_stats_w2 import compute_stats

def run_demo():
    students = load_students("data_w1/students_w1.json")
    sn = StudentNetworkW1()
    for s in students:
        sn.add_user(s)

    edges = load_edges("data_w2/edges_w2.json")
    apply_edges(sn, edges)

    stats = compute_stats(sn)
    print("Thống kê mạng sau khi load edges từ file:", stats)

    # kiểm tra 1 node
    sample_id = "w1_0001"
    print(f"{sample_id} có {len(sn.friends_of(sample_id))} bạn.")

if __name__ == "__main__":
    run_demo()
