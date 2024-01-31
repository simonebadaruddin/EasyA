# gui.py creates a Graphical User Interface (GUI) which takes choices
# from the user and presents 2 graphs back to the user.
# Created 01/12/24
# By Simone Badaruddin and Nithi Deivanayagam.
# gui.py takes graphs created by Grade_grapher.py
# Modifications made to add multiple dropdown menus on 01/26/24

# The graphing library
import matplotlib.pyplot as plt
# Used to integrate tkinter & matplotlib + create our canvas
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
# The Graphical User Interface (GUI) Library
import tkinter as tk
import numpy as np

# Initialize Tkinter
root = tk.Tk()
root.geometry("1000x1000")

# Create a white frame
frame = tk.Frame(root, bg="White")
frame.pack(side="top", fill="x")

# Create a larger white frame
white_frame = tk.Frame(root)
white_frame.pack(side="top", fill="both", expand=True)

# Create matplotlib figure with access to subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))

# Create canvas in global scope
canvas = None


def get_data():
    """
    Dummy function to generate example data.
    Replace this with actual logic to retrieve data from Grade_grapher.py.
    """
    # Example data
    x_data = np.linspace(1, 5, 100)
    y_data1 = np.sin(x_data)  # using a sine function as an example for graph 1
    y_data2 = np.cos(x_data)  # using a cosine function as an example for graph 2

    return x_data, y_data1, y_data2


def plot():
    """
    Our plotting function gets the selections inputted by the user plus
    the corresponding graphed data from Grade_grapher.py and plots the
    resulting graph whenever the "Plot Graph" button is pressed.
    """
    global canvas, ax1, ax2  # Declare ax1 and ax2 as global variables

    # Clear previous graphs
    ax1.clear()
    ax2.clear()

    # Get data (replace with actual data retrieval logic)
    x, y1, y2 = get_data()

    # Plot the graphs
    # ax1.bar(x, y1, label='Graph 1', color='slateblue')
    # ax1.set_title('Graph 1')
    # ax1.set_xlabel('X Axis Label for Graph 1')
    # ax1.set_ylabel('Y Axis Label for Graph 1')
    # ax1.tick_params(axis='both', labelsize=5)
    # ax1.legend()
    #
    # ax2.bar(x, y2, label='Graph 2', color='violet')
    # ax2.set_title('Graph 2')
    # ax2.set_xlabel('X Axis Label for Graph 2')
    # ax2.set_ylabel('Y Axis Label for Graph 2')
    # ax2.tick_params(axis='both', labelsize=5)
    # ax2.legend()

    # Create a new canvas if it doesn't exist
    if canvas is None:
        # Create a canvas which requires:
        # (a) matplotlib figure
        # (b) tkinter application
        canvas = FigureCanvasTkAgg(fig, master=white_frame)  # Use white_frame as the master
        # Integrate canvas into the white_frame
        canvas.get_tk_widget().pack()

        toolbar = NavigationToolbar2Tk(canvas, white_frame, pack_toolbar=False)
        toolbar.update()
        toolbar.pack(anchor="w", fill=tk.X)

    # Explicitly update the canvas
    canvas.draw_idle()


def create_dropdown_menu(frame, options, selected_option):
    selected_var = tk.StringVar()
    selected_var.set(selected_option)

    def on_select(callback=None, *args):
        callback(selected_var.get())

    selected_var.trace_add('write', on_select)

    dropdown_menu = tk.OptionMenu(frame, selected_var, *options)
    dropdown_menu.pack(pady=15, side=tk.TOP)

    return selected_var


def main():
    # Tkinter Application + Visuals
    label = tk.Label(white_frame, text="Group 3 Easy A", font="Helvetica", fg="Black", bg="White")
    label.config(font=("Courier", 50))
    label.pack()

    # Individual Class dropdown
    individual_class = ["CS 210", "CS 211"]
    selected_individual_class = create_dropdown_menu(white_frame, individual_class, "Select individual class")

    # Subject dropdown
    subject = ["Biology", "Chemistry", "Biochemistry", "Computer Science", "Earth Sciences",
                  "General Science", "Human Physiology", "Mathematics", "Neuroscience",
                  "Physics", "Psychology"]
    selected_subject = create_dropdown_menu(white_frame, subject, "Select department")

    # Class level dropdown
    class_level = ["100", "200", "300", "400", "500", "600"]
    selected_class_level = create_dropdown_menu(white_frame, class_level, "Select class level")

    # Faculty only decision dropdown
    faculty_only = ["yes", "no"]
    selected_faculty_only = create_dropdown_menu(white_frame, faculty_only, "Faculty only")

    # By class or professor dropdown
    class_or_professor = ["class", "professor"]
    class_or_professor = create_dropdown_menu(white_frame, class_or_professor, "Filter by")

    # Class count dropdown
    class_count = ["yes", "no"]
    class_count = create_dropdown_menu(white_frame, class_count, "Class count")

    # Input names query box
    teacher_entry_label = tk.Label(white_frame, text="Enter teacher names (comma-separated):", font=("Helvetica", 12))
    teacher_entry_label.pack(pady=5, side=tk.TOP)

    teacher_entry_var = tk.StringVar()
    teacher_entry = tk.Entry(white_frame, textvariable=teacher_entry_var)
    teacher_entry.pack(pady=5, side=tk.TOP)

    # Create button to plot with prev. plot func, link plotted data here
    tk.Button(white_frame, text="Plot Graph", command=plot).pack(pady=10, side=tk.BOTTOM)

    # Place label
    root.mainloop()


if __name__ == "__main__":
    main()