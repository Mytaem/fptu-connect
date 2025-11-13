# generate_graph.py
from pyvis.network import Network
import network

net = Network(height="700px", width="100%", directed=False, bgcolor="#222222", font_color="white")

nodes = list(network.sn.students.keys())[:300]
for sid in nodes:
    info = network.sn.students[sid]
    color = {"IT": "#ff4444", "BA": "#3366cc", "Design": "#00C851", "English": "#ffbb33"}.get(info["faculty"], "#777777")
    net.add_node(sid, label=info["name"], title=f"{info['faculty']} • {info['hometown']}", color=color)

for u in nodes:
    for v in network.sn.friends_of(u):
        if v in nodes:
            net.add_edge(u, v)

net.show("static/graph.html")
print("Đã tạo đồ thị: static/graph.html")