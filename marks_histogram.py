# Student Marks Histogram Project
# Requirements: matplotlib, numpy, pandas
# Install if needed: pip install matplotlib numpy pandas

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# ------- Input: marks list -------
marks = [45, 56, 78, 88, 34, 60, 71, 49, 53, 67, 95, 100, 37, 43, 80]

# ------- Bins: 0–10, 11–20, ..., 91–100 -------
bin_edges = [0, 11, 21, 31, 41, 51, 61, 71, 81, 91, 101]
bin_labels = [f"{start}-{end}" for start, end in zip(bin_edges[:-1], [e-1 for e in bin_edges[1:]])]

# ------- Count students per bin -------
counts, _ = np.histogram(marks, bins=bin_edges)

print("Marks distribution by range:\n")
for rng, c in zip(bin_labels, counts):
    print(f"{rng}: {c} students")

# ------- Plot Histogram -------
plt.figure(figsize=(8, 5))
plt.hist(marks, bins=bin_edges, edgecolor="black")
plt.title("Student Marks Distribution (Histogram)")
plt.xlabel("Marks Range")
plt.ylabel("Number of Students")
plt.grid(True, linestyle="--", alpha=0.5)

# Readable x-ticks
bin_centers = (np.array(bin_edges[:-1]) + np.array(bin_edges[1:]) - 1) / 2.0
plt.xticks(bin_centers, bin_labels, rotation=45, ha="right")

plt.tight_layout()
plt.savefig("student_marks_histogram.png", dpi=150)
plt.show()

# ------- Save counts table as CSV -------
df = pd.DataFrame({"Marks Range": bin_labels, "Number of Students": counts})
df.to_csv("marks_bin_counts.csv", index=False)
