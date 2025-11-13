# src_w2/demo_w2_seed.py
from src_w1.core_w1 import StudentNetworkW1
from src_w1.io_w1 import load_students
from src_w2.w2_seeder import seed_by_indexes
from src_w2.io_w2 import save_edges
from src_w2.net_stats_w2 import compute_stats

def run_demo():
    # 1) Load dữ liệu SV từ tuần 1
    students = load_students("data_w1/students_w1.json")
    sn = StudentNetworkW1()
    for s in students:
        sn.add_user(s)

    # 2) Seeding kết nối
    added, touched = seed_by_indexes(
        sn,
        p_class=0.25, p_club=0.35, p_home=0.15,
        max_new_per_student=15,
        rng_seed=42
    )
    print(f"Đã thêm {added} kết nối mới, liên quan {touched} sinh viên.")

    # 3) Thống kê mạng
    stats = compute_stats(sn)
    print("Thống kê mạng sau seeding:", stats)

    # 4) Lưu cạnh để tái sử dụng
    save_edges("data_w2/edges_w2.json", sn)
    print("Đã lưu cạnh vào data_w2/edges_w2.json")

    # 5) In thử bạn của một SV
    sample_id = "w1_0001"
    print(f"Bạn của {sample_id} (tối đa 15 hiển thị):", list(sn.friends_of(sample_id))[:15])

if __name__ == "__main__":
    run_demo()
