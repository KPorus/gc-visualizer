# 🧹 Python GC Visualizer

An interactive tool to understand and experiment with Python's built-in garbage collection (GC) system — especially how it handles **circular references** and unreachable objects.

Built using **Streamlit**, this educational tool helps visualize and debug memory management behavior in real time.

---

## 🚀 Features

* ✅ Create Python objects with or without circular references
* 🧼 Force garbage collection manually
* 📊 View memory usage and unreachable object count
* 🔁 Toggle circular references to simulate GC edge cases
* 🧠 Show internal GC debug statistics
* 📦 Live summary of object types in memory

---

## 🧪 Usage

1. **Launch app locally**:

   ```bash
   streamlit run app.py
   ```

2. **Explore buttons**:

   * Create and delete objects
   * Toggle circular references
   * Force GC and monitor behavior

3. **Understand output**:

   * See how memory usage changes
   * Discover how many objects GC can reclaim
   * Use object type summary to detect object leaks

---

## 📸 Screenshots

> (You can add screenshots here after running it!)
![alt text](image.png)

---

## 🧠 What You'll Learn

* How Python tracks and reclaims memory
* Why circular references need a GC (not just reference counting)
* How to analyze memory behavior using `gc`, `psutil`, and `inspect`

---

## 🛠️ Tech Stack

* **Python 3.9+**
* **Streamlit** — for the interactive frontend
* **gc**, **psutil**, **inspect** — for memory analysis

---

## 📄 License

MIT — use freely and learn boldly!
