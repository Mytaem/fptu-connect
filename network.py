# network.py - Quản lý mạng xã hội
import os
from pyvis.network import Network
import json

class Student:
    def __init__(self, sid, name, avatar="static/default.jpg"):
        self.sid = sid
        self.name = name
        self.avatar = avatar
        self.friends = set()

    def add_friend(self, friend_sid):
        self.friends.add(friend_sid)

class SocialNetwork:
    def __init__(self):
        self.students = {}
        self.data_file = "data/students.json"

    def add_student(self, sid, name, avatar):
        if sid not in self.students:
            self.students[sid] = Student(sid, name, avatar)
            self.save_data()

    def add_friendship(self, sid1, sid2):
        if sid1 in self.students and sid2 in self.students:
            self.students[sid1].add_friend(sid2)
            self.students[sid2].add_friend(sid1)
            self.save_data()

    def save_data(self):
        os.makedirs("data", exist_ok=True)
        data = {
            sid: {
                "name": s.name,
                "avatar": s.avatar,
                "friends": list(s.friends)
            } for sid, s in self.students.items()
        }
        with open(self.data_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                for sid, info in data.items():
                    student = Student(sid, info["name"], info.get("avatar", "static/default.jpg"))
                    student.friends = set(info.get("friends", []))
                    self.students[sid] = student

# Khởi tạo mạng
sn = SocialNetwork()
sn.load_data()

# Hàm tạo đồ thị
def generate_graph():
    net = Network(height="600px", width="100%", bgcolor="#222222", font_color="white")
    net.force_atlas_2based()
    
    for sid, student in sn.students.items():
        net.add_node(sid, label=student.name, title=student.name, shape="image", image=student.avatar)
    
    for sid, student in sn.students.items():
        for friend in student.friends:
            if friend in sn.students:
                net.add_edge(sid, friend)
    
    os.makedirs("static", exist_ok=True)
    net.save_graph("static/graph.html")

# Thêm dữ liệu mẫu nếu rỗng
if not sn.students:
    sn.add_student("w1_0001", "Nguyễn Văn A", "static/default.jpg")
    sn.add_student("w1_0002", "Trần Thị B", "static/default.jpg")
    sn.add_friendship("w1_0001", "w1_0002")
    generate_graph()