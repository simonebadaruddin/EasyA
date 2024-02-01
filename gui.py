# a gui.py creates a Graphical User Interface (GUI) which takes choices
# from the user and presents 2 graphs back to the user.
# Created 01/12/24
# By Simone Badaruddin and Nithi Deivanayagam.
# gui.py takes graphs created by Grade_grapher.py
# Modifications made to add multiple dropdown menus on 01/26/24

# The Graphical User Interface (GUI) Library
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import numpy as np
import json

from Grade_grapher import (Grapher, Subjs_And_Level_by_Class_Grapher, Subjs_And_Level_By_Prof_Grapher,
                           Courses_By_Prof_Grapher, Subjs_By_Prof_Grapher)
from data_maintainer import Data_Maintainer

#
DM = Data_Maintainer()
DM.update_grade_data()
COURSE_DATA = DM.get_grade_data()
CLASSES = list(COURSE_DATA.keys())

#
with open("faculty_list.json", "r") as file:
    FACULTY = json.load(file)

# Initialize Tkinter
root = tk.Tk()
root.geometry("1000x1000")

# Create a white frame
frame = tk.Frame(root, bg="White")
frame.pack(side="top", fill="x")

# Create a larger white frame
white_frame = tk.Frame(root)
white_frame.pack(side="top", fill="both", expand=True)

# Create fig
fig = figsize=(8, 4)

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
    global canvas

    # Create a new canvas if it doesn't exist
    if canvas is None:
        # Create a canvas which requires:
        # (a) matplotlib jpegs
        # (b) tkinter application
        # Integrate canvas into the white_frame
        canvas = tk.Canvas(white_frame)  # Create a new canvas using tkinter
        canvas.pack(fill=tk.BOTH, expand=True)

    # Clear previous content on the canvas
    canvas.delete("all")

    # Get data (replace with actual data retrieval logic)
    x, y1, y2 = get_data()

    # Example: Load a sample image (replace this with your actual image loading logic)
    image_path = "As_graph.jpg"
    img = Image.open(image_path)
    img = img.resize((300, 300))  # Adjust the size as needed
    photo = ImageTk.PhotoImage(img)

    # Display the image on the canvas
    canvas.create_image(10, 10, anchor=tk.NW, image=photo)

    # Update the canvas
    canvas.update()


def create_dropdown_menu(frame, options, selected_option):
    selected_var = tk.StringVar()
    selected_var.set(selected_option)

    # Instead of above code, use ttk.Combobox for dropdown menu in order to handle str's
    dropdown_menu = ttk.Combobox(frame, textvariable=selected_var, values=options)
    dropdown_menu.pack(pady=15, side=tk.TOP)

    return selected_var


def main():
    # Tkinter Application + Visuals
    label = tk.Label(white_frame, text="Group 3 Easy A", font="Helvetica", fg="Black", bg="White")
    label.config(font=("Courier", 50))
    label.pack()

    def on_plot_button_click(natty_science_course_data=None):
        # Call the appropriate function based on user choices

        if (selected_subject.get() and selected_class_level.get() and
                class_or_professor.get() == "professor"):
            # Set faculty_only if the user selected "yes" in the dropdown
            received_faculty = selected_faculty_only.get()
            faculty_only = True if received_faculty == "yes" else False
            # Create an instance of Subjs_And_Level_By_Prof_Grapher
            grapher = Subjs_And_Level_By_Prof_Grapher(COURSE_DATA, FACULTY, faculty_only=faculty_only)

            # Get the selected subject, class level, and teacher names
            subject = selected_subject.get()
            class_level = selected_class_level.get()
            teacher_names = teacher_entry_var.get() if teacher_entry_var.get() else []

            # Graph the data
            grapher.graph_data(subject, level=class_level, names_list=teacher_names, faculty_only=faculty_only)

            # Add resultant graphs to canvas
            canvas.update()

    # Individual Class dropdown
    selected_individual_class = create_dropdown_menu(white_frame, CLASSES, "Select individual class")

    # Subject dropdown
    subject = [ 'ANTH', 'ASTR', 'BI', 'BIOE', 'CH', 'CIS', 'CIT', 'CPSY', 'DSCI', 'ERTH', 'ENVS',
                'GEOG', 'HPHY', 'MATH', 'NEUR', 'PHYS', 'PSY', 'SPSY', 'STAT' ]
    selected_subject = create_dropdown_menu(white_frame, subject, "Select department")

    # Class level dropdown
    class_level = ["100", "200", "300", "400", "500", "600"]
    selected_class_level = create_dropdown_menu(white_frame, class_level, "Select class level")

    # Faculty only decision dropdown
    faculty_only = ["Yes", "No"]
    selected_faculty_only = create_dropdown_menu(white_frame, faculty_only, "Faculty only")

    # By class or professor dropdown
    class_or_professor = ["Class", "Professor"]
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
