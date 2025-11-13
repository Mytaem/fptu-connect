# generate_graph.py - Tạo đồ thị mạng
import network
import os

if __name__ == "__main__":
    print("Đang tạo đồ thị mạng...")
    network.generate_graph()
    print("Hoàn thành! Đã tạo static/graph.html")
    
    # Tạo thư mục nếu chưa có
    os.makedirs("static", exist_ok=True)