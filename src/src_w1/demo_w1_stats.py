# src_w1/demo_w1_stats.py
from src_w1.core_w1 import StudentNetworkW1
from src_w1.io_w1 import load_students
from src_w1.gen_w1 import save_students

def run_demo():
    # Nếu chưa có dữ liệu thì sinh
    save_students("data_w1/students_w1.json", n=2000)

    students = load_students("data_w1/students_w1.json")
    sn = StudentNetworkW1()
    for s in students:
        sn.add_user(s)

    print("Tổng số sinh viên:", len(sn.students))
    print("Một vài lớp:", list(sn.idx_class.keys())[:5])
    print("Một vài CLB:", list(sn.idx_club.keys())[:5])
    print("Một vài khoa:", list(sn.idx_faculty.keys()))
    print("Một vài quê:", list(sn.idx_home.keys()))
    print("Số SV học INT101:", len(sn.idx_class['INT101']))

if __name__ == "__main__":
    run_demo()
