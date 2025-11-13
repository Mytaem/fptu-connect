from collections import deque

def shortest_path(sn, start, goal):
    if start not in sn.students or goal not in sn.students:
        return None
    if start == goal:
        return [start]
    
    queue = deque([[start]])
    visited = {start}
    
    while queue:
        path = queue.popleft()
        current = path[-1]
        for friend in sn.students[current].friends:
            if friend not in visited:
                visited.add(friend)
                new_path = path + [friend]
                if friend == goal:
                    return new_path
                queue.append(new_path)
    return None