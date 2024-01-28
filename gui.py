"""
GUI.py takes choices from the user and graphs them. Created 01/12/24
by Simone Badaruddin and Nithi Deivanayagam.
It takes data to graph from Grade_grapher.py
Modifications made by: FIXME to FIXME
"""

# The graphing library
import matplotlib.pyplot as plt
# Used to integrate tkinter & matplotlib + create our canvas
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
# The Graphical User Interface (GUI) Library
import tkinter as tk
from tkinter import ttk
import numpy as np


def get_data(selected_department, selected_visual, selected_by_level, selected_class, selected_faculty):
    """
    Dummy function to generate example data.
    Replace this with actual logic to retrieve data from Grade_grapher.py.
    """
    # Example data
    x_data = np.linspace(1, 5, 100)
    y_data = np.sin(x_data)  # using a sine function as an example

    return x_data, y_data


def plot(selected_department, selected_visual, selected_by_level, selected_class, selected_faculty):
    """
    Our plotting function gets the selections inputted by the user plus
    the corresponding data from Grade_grapher.py and plots the
    resulting graph whenever the "Plot Graph" button is pressed.

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
    # Old graph clears before new one
    ax.clear()

    # Get data (replace with actual data retrieval logic)
    x, y = get_data(selected_department, selected_visual, selected_by_level, selected_class, selected_faculty)

    ax.plot(x, y)

    # Explicitly update the canvas
    canvas.draw_idle()


def main():
    # Initialize Tkinter
    root = tk.Tk()
    root.geometry("1000x1000")
    # (a) Create matplotlib figure with access to subplots
    fig, ax = plt.subplots()

    # Tkinter Application + Visuals
    frame = tk.Frame(root)
    label = tk.Label(text="Viewing Options")
    label.config(font=("Courier", 20))
    label.pack(pady=20)

    # Dropdown menu to select department
    department_options = [
        "Biology", "Chemistry", "Biochemistry", "Computer Science", "Earth Sciences",
        "General Science Program", "Human Physiology", "Mathematics", "Neuroscience",
        "Physics", "Psychology"
    ]
    selected_department = tk.StringVar()
    selected_department.set("Select a department")
    department_dropdown = ttk.Combobox(frame, textvariable=selected_department, values=department_options)
    department_dropdown.pack()

    # Visual options dropdown menu
    visual_options = ["Whole department", "Particular level", "Particular class"]
    selected_visual = tk.StringVar()
    selected_visual.set("What data would you like to see?")
    visual_dropdown = ttk.Combobox(frame, textvariable=selected_visual, values=visual_options)
    visual_dropdown.pack()

    # Other dropdown menus (similar to the first two) can be added here

    # Create button to plot with prev. plot func, link plotted data here
    tk.Button(frame, text="Plot Graph", command=lambda: plot(
        selected_department.get(),
        selected_visual.get(),
        # Add other selected values here
    )).pack(pady=10, side=tk.BOTTOM)

    # Create a canvas which requires:
    # (a) matplotlib figure
    # (b) tkinter application
    canvas = FigureCanvasTkAgg(fig, master=frame)
    # Integrate canvas into the application
    canvas.get_tk_widget().pack()

    toolbar = NavigationToolbar2Tk(canvas, frame, pack_toolbar=False)
    toolbar.update()
    toolbar.pack(anchor="w", fill=tk.X)

    # Place label
    frame.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
