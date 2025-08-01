import networkx as nx
import matplotlib.pyplot as plt
import gc
import psutil
import time
import inspect

def get_gc_stats():
    return {
        "collected": gc.collect(),
        "unreachable": len(gc.garbage),
        "memory_MB": psutil.Process().memory_info().rss / (1024 * 1024)
    }


def draw_object_graph(objects):
    G = nx.DiGraph()
    labels = {}

    for idx, (a, b) in enumerate(objects):
        a_name = f"A{idx}"
        b_name = f"B{idx}"
        G.add_node(a_name)
        G.add_node(b_name)
        labels[a_name] = a_name
        labels[b_name] = b_name

        G.add_edge(a_name, b_name)
        if hasattr(b, "ref") and b.ref == a:
            G.add_edge(b_name, a_name)

    fig, ax = plt.subplots()
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, arrows=True, node_size=2000, node_color='lightblue', font_weight='bold', ax=ax)
    return fig


def explain_gc_details():
    gc.set_debug(gc.DEBUG_STATS)
    collected = gc.collect()
    gc.set_debug(0)
    return collected


def count_tracked_objects():
    return len(gc.get_objects())


def object_summary():
    types = {}
    for obj in gc.get_objects():
        typename = type(obj).__name__
        types[typename] = types.get(typename, 0) + 1
    sorted_types = dict(sorted(types.items(), key=lambda x: x[1], reverse=True))
    return sorted_types


def get_backref_info(obj):
    refs = gc.get_referrers(obj)
    info = []
    for r in refs:
        try:
            if isinstance(r, dict):
                frame = r.get("__frame__")
                if frame:
                    info.append(inspect.getframeinfo(frame))
        except Exception:
            continue
    return info