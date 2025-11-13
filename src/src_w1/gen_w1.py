# src_w1/gen_w1.py
import random, json, os

names = ["An", "Binh", "Chi", "Dung", "Hanh", "Khanh", "Linh", "Minh", "Nam", "Trang"]
faculties = ["IT", "BA", "Design", "English"]
classes = ["INT101", "INT102", "DS101", "STA101", "ECO101", "MKT101"]
clubs = ["soccer", "music", "english", "robotic", "volunteer"]
hometowns = ["Hanoi", "Danang", "HCM", "Hue", "Cantho"]

def generate_students(n=2000):
    students = []
    for i in range(1, n+1):
        sid = f"w1_{i:04d}"
        student = {
            "id": sid,
            "name": random.choice(names) + str(i),
            "faculty": random.choice(faculties),
            "cohort": 2025,
            "classes": random.sample(classes, k=2),
            "clubs": random.sample(clubs, k=2),
            "hometown": random.choice(hometowns),
        }
        students.append(student)
    return students

def save_students(filename="data_w1/students_w1.json", n=2000):
    os.makedirs("data_w1", exist_ok=True)
    students = generate_students(n)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(students, f, ensure_ascii=False, indent=2)
    print(f"✅ Đã tạo {n} sinh viên → {filename}")
