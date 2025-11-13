# src_w3/components_w3.py
def connected_components(sn):
    """
    Dùng DFS/BFS để tìm tất cả các nhóm (component) trong mạng xã hội.
    Trả về list các set, mỗi set là 1 nhóm id sinh viên.
    """
    visited = set()
    components = []

    for u in sn.students:
        if u not in visited:
            comp = set()
            stack = [u]
            while stack:
                x = stack.pop()
                if x not in visited:
                    visited.add(x)
                    comp.add(x)
                    stack.extend(sn.friends_of(x))
            components.append(comp)
    return components
