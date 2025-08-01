import streamlit as st
import gc
from memory_manager import create_objects, force_delete
from visualizer import get_gc_stats, draw_object_graph, explain_gc_details, count_tracked_objects, object_summary, get_backref_info

st.set_page_config(page_title="Python GC Visualizer", layout="centered")

st.title("🧹 Python Garbage Collection Visualizer")
st.markdown("This interactive tool demonstrates how Python's garbage collector works — especially in cases of **circular references**.")

# ---- SETTINGS ----
st.subheader("🔧 Setup")
create_cycle = st.checkbox("Create circular reference between objects?", value=True,
                           help="Circular references keep objects alive even when no other reference exists.")

if 'objects' not in st.session_state:
    st.session_state['objects'] = []

# ---- ACTIONS ----
st.subheader("⚙️ Actions")

col1, col2 = st.columns(2)

with col1:
    if st.button("➕ Create Objects"):
        a, b = create_objects(create_cycle)
        st.session_state['objects'].append((a, b))
        st.success("Created two objects (A & B)" + (" with circular references." if create_cycle else "."))

with col2:
    if st.button("🗑️ Delete All Objects"):
        for a, b in st.session_state['objects']:
            force_delete(a, b)
        # st.session_state['objects'] = []
        st.session_state['objects'].clear()
        st.warning("Deleted all objects and triggered garbage collection.")


st.divider()

# ---- GC CONTROL ----
st.subheader("♻️ Garbage Collector")

col3, col4 = st.columns(2)

with col3:
    if st.button("🔄 Force GC Now"):
        count = gc.collect()
        st.info(f"Garbage collector ran and collected **{count}** objects.")

with col4:
    if st.button("📊 Show GC Stats"):
        stats = get_gc_stats()
        st.write(f"**Memory usage**: {stats['memory_MB']:.2f} MB")
        st.write(f"**Unreachable objects**: {stats['unreachable']}")
        st.caption("Memory info pulled from `psutil.Process().memory_info()`.")

    
    if st.button("🔍 Force GC with Debug"):
        count = explain_gc_details()
        st.info(f"Garbage collector ran and collected **{count}** objects (debug stats shown in terminal).")

# ---- VISUALIZATION ----
if st.session_state['objects']:
    st.subheader("🔗 Visualize Object References")
    if st.button("🧠 Show Object Graph"):
        fig = draw_object_graph(st.session_state['objects'])
        st.pyplot(fig)
else:
    st.caption("No objects created yet. Click 'Create Objects' above first.")



st.divider()

st.header("📦 Live Object Insights")


col4, col5 = st.columns(2)

with col4:
    if st.button("🔢 Count Total Python Objects"):
        count = count_tracked_objects()
        st.info(f"Total objects currently tracked: {count}")

with col5:
    if st.button("📑 Object Type Summary"):
        summary = object_summary()
        st.subheader("Top Object Types in Memory")
        st.json(summary)

# ---- Backreference Info ----
st.markdown("---")
st.header("🔎 Backreference Information")
if st.session_state['objects']:
    if st.button("🕵️ Show Backref Info for Last Created Objects"):
        a, b = st.session_state['objects'][-1]
        a_info = get_backref_info(a)
        b_info = get_backref_info(b)
        st.subheader("A's Backreferences:")
        if a_info:
            st.json([str(i) for i in a_info])
        else:
            st.caption("No backreference info found for A.")
        st.subheader("B's Backreferences:")
        if b_info:
            st.json([str(i) for i in b_info])
        else:
            st.caption("No backreference info found for B.")
else:
    st.caption("No objects created yet. Click 'Create Objects' above first.")

st.markdown("---")
# st.caption("Powered by Python's gc and psutil modules.")

