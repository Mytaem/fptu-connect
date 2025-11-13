# src_w2/io_w2.py
import json
from typing import List

def save_edges(filename: str, sn) -> None:
    """
    Lưu cạnh dưới dạng list các cặp [u, v] với u < v.
    """
    edges = []
    for u, nbrs in sn.adj.items():
        for v in nbrs:
            if u < v:
                edges.append([u, v])
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(edges, f, ensure_ascii=False, indent=2)

def load_edges(filename: str) -> List[list]:
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

def apply_edges(sn, edges: list) -> None:
    for u, v in edges:
        sn.add_friend(u, v)
