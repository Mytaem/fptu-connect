# src_w3/path_w3.py
from collections import deque

def shortest_path(sn, start: str, goal: str):
    """
    BFS tìm đường đi ngắn nhất giữa start và goal.
    Trả về list các id hoặc None nếu không có đường đi.
    """
    if start not in sn.students or goal not in sn.students:
        return None
    if start == goal:
        return [start]

    visited = {start}
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        node = path[-1]
        for neighbor in sn.friends_of(node):
            if neighbor == goal:
                return path + [neighbor]
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])
    return None
