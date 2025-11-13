# src_w1/io_w1.py
import json

def load_students(filename="data_w1/students_w1.json"):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

def save_students(filename, students):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(students, f, ensure_ascii=False, indent=2)
