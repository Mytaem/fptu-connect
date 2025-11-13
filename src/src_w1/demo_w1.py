# src_w1/demo_w1_basic.py
from src_w1.core_w1 import StudentNetworkW1

def run_demo():
    sn = StudentNetworkW1()
    sn.add_user({"id": "w1_0001", "name": "An", "faculty": "IT", "classes": ["INT101"], "clubs": ["soccer"], "hometown": "Danang"})
    sn.add_user({"id": "w1_0002", "name": "Binh", "faculty": "IT", "classes": ["INT101"], "clubs": ["music"], "hometown": "Hanoi"})

    sn.add_friend("w1_0001", "w1_0002")

    print("Bạn của w1_0001:", sn.friends_of("w1_0001"))
    print("Bạn của w1_0002:", sn.friends_of("w1_0002"))

if __name__ == "__main__":
    run_demo()
