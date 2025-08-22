# Student Marks Histogram

Visualizing student marks helps educators and students understand performance distribution. This project uses Python and matplotlib to create a histogram that displays how student marks are distributed across specific ranges, offering a clear graphical representation of achievement patterns and identifying common performance bands.

---

## About the Author

This project was developed by Khushi Kumari, a 3rd-year student of Computer Science and Data Analytics at IIT Patna.

---

## Features

* **Data Visualization:** Creates a histogram to visualize the distribution of student marks.
* **Custom Bins:** Groups marks into defined ranges (e.g., 0-10, 11-20, etc.) for clear analysis.
* **Axis Labels & Title:** Includes descriptive labels for the X and Y axes, and a clear chart title.
* **Data Export:** Saves the generated histogram as a .png image and the count data as a .csv file.

---

## Requirements

The following Python libraries are required to run this project:

* **matplotlib:** For creating the histogram plot.
* **numpy:** For numerical operations, specifically for calculating histogram counts.
* **pandas:** For creating a data frame to save the counts to a CSV file.

You can install these dependencies using pip:

```bash
pip install matplotlib numpy pandas

---

## How to Run

1.  **Save the code:** Save the provided Python code as a file, for example, `create_histogram.py`.
2.  **Ensure requirements are met:** Make sure you have installed all the necessary libraries.
3.  **Run the script:** Execute the script from your terminal:

```bash
python create_histogram.py

After running the script, a histogram plot will be displayed in a window, and two files will be saved in the same directory: `student_marks_histogram.png` (the image of the plot) and `marks_bin_counts.csv` (a table of the student counts per mark range).

---

## Code Overview

### `marks`

This is a Python list containing the raw student marks. You can easily modify this list to analyze a different dataset.

```python
marks = [45, 56, 78, 88, 34, 60, 71, 49, 53, 67, 95, 100, 37, 43, 80]

### Histogram Plotting

The `plt.hist()` function from matplotlib is the core of the visualization. It takes the `marks` data and the `bin_edges` list to create the histogram, showing the frequency of marks within each specified range.

```python
plt.hist(marks, bins=bin_edges, edgecolor="black")

## Output

### Visual Output

A histogram will be displayed with the title "Student Marks Distribution (Histogram)". The X-axis will be labeled "Marks Range," and the Y-axis will be labeled "Number of Students."

### File Output

The project generates two files:

* `student_marks_histogram.png`: A high-resolution image of the histogram.
* `marks_bin_counts.csv`: A CSV file containing a table with two columns: Marks Range and Number of Students.