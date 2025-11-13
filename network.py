# network.py
from src.src_w1.core_w1 import StudentNetworkW1
from src.src_w1.io_w1 import load_students
from src.src_w2.io_w2 import load_edges, apply_edges

print("Đang tải 2000 sinh viên...")
sn = StudentNetworkW1()
students = load_students("data_w1/students_w1.json")
for s in students:
    sn.add_user(s)

print("Đang tải kết nối bạn bè...")
edges = load_edges("data_w2/edges_w2.json")
apply_edges(sn, edges)

print(f"HOÀN TẤT: {len(sn.students)} SV, {len(edges)} kết nối")