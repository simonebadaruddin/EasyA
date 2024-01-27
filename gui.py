"""
GUI
"""

# The graphing library
import matplotlib.pyplot as plt
# Used to integrate tkinter & matplotlib + create our canvas
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
# The Graphical User Interface (GUI) Library
import tkinter as tk
import numpy as np


def plot():
    """
    Our plotting function gets the selections inputted by the user plus the
    corresponding data from Grade_grapher.py and plots the resulting graph.

    graph1_title:
        A single class name, A single department name, a single
        department name and class level combination, or a single
        department name plus class level combination

    graph1_x_axis_data:


    graph1_y_axis_data:
        % A's

    graph1_title:
        A single class name, A single department name, a single
        department name and class level combination, or a single
        department name plus class level combination

    ########

    graph2_x_axis_data:


    graph2_y_axis_data:
        % D's / F's

    graph2_title:
        A single class name, A single department name, a single
        department name and class level combination, or a single
        department name plus class level combination
    """
    ax.clear()
    x = np.random.randint(0, 10, 10)  # PLACEHOLDER UNTIL OUR DATA FIXME
    y = np.random.randint(0, 10, 10)  # PLACEHOLDER UNTIL OUR DATA FIXME
    ax.plot(x, y)
    # This call updates the graph:
    canvas.draw()


# Initialize Tkinter
root = tk.Tk()
# (a) Create matplotlib figure with access to subplots
fig, ax = plt.subplots()

# Tkinter Application + Visuals
frame = tk.Frame(root)
label = tk.Label(text="Math 111")
label.config(font=("Courier", 32))
label.pack()

# Create a canvas which requires:
# (a) matplotlib figure
# (b) tkinter application
canvas = FigureCanvasTkAgg(fig, master=frame)
# Integrate canvas into the application
canvas.get_tk_widget().pack()

toolbar = NavigationToolbar2Tk(canvas, frame, pack_toolbar=False)
toolbar.update()
toolbar.pack()

# Place label
frame.pack()

# Create button to plot with prev. plot func, link plotted data here #FIXME
tk.Button(frame, text="Plot Graph", command=plot).pack(pady=10, side=tk.BOTTOM)

root.mainloop()
