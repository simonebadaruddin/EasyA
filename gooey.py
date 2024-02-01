"""Maybe the GUI for group 3"""

import tkinter as tk
from tkinter import ttk
from data_maintainer import Data_Maintainer
from Grade_grapher import ( Grapher, Subjs_And_Level_by_Class_Grapher, Subjs_And_Level_By_Prof_Grapher, 
                           Subjs_By_Prof_Grapher, Courses_By_Prof_Grapher )
import json
from PIL import Image, ImageTk
import time




# Get the course data from the grade maintainer module
DM = Data_Maintainer() # initialize the grade_maintainer object
DM.update_grade_data() # run the grade maintainer parsing and validation
COURSE_DATA = DM.get_grade_data() # retrieve the parsed and validated course data

with open("faculty_list.json", "r") as file:
    FACULTY_LIST = json.load(file)

# retrieve a full course list from the course data keys
ALL_COURSES = list(COURSE_DATA.keys())
ALL_COURSES.insert(0, "None")

# the subject codes for courses in the natural science department:
SUBJECTS = [ 'None', 'ANTH', 'ASTR', 'BI', 'BIOE', 'CH', 'CIS', 'CIT', 'CPSY', 'DSCI', 'ERTH', 'ENVS', 
            'GEOG', 'HPHY', 'MATH', 'NEUR', 'PHYS', 'PSY', 'SPSY', 'STAT' ]

# the levels for each course subject
LEVELS = ['None', '100', '200', '300', '400', '500', '600']

# values for dropdowns with yes or no choices:
YN = ["Yes", "No"]

# values for dropdowns with class or instructor choises:
CLASS_INSTR = ["Class", "Instructors"]

COURSE_DD_TXT = "Select a Course"
SUBJ_DD_TXT = "Select a Subject"
LVL_DD_TXT = "Select a Subject Level"
DISPLAY_PROMPT = "for class or instructors?"
FACULTY_PROMPT = "Show data for faculty only?"
CLASS_COUNT_PROMPT = "Display class count?"


def graph_choices():
    # retrieve the user inputs at the time that the button was pressed:
    # All are based on if the user used the respective dropdowns
    selected_course = chosen_course.get() # selected_course (str): the input from the course dropdown, a course code
    selected_subject = chosen_subject.get() # selected_subject (str): the input from the subject dropdown, a subject code
    selected_level = chosen_level.get() # selected_level (str): the input from the level dropdown, a number 100-600 as a string
    selected_display = chosen_display.get() # selected_display (str): "Instructors" or "class", from instructor/class dropdown
    selected_faculty = faculty_choice.get() # selected_faculty (str): "yes" or "no", from faculty dropdown
    selected_class_count = class_count_choice.get() # selected_class_count (str): "yes" or "no", from class count dropdown
    selected_names = chosen_names.get() # selected_names (str): names that were typed into the names list test box as an unbroken string

    # parse names:
    if selected_names: # check to see if any names came through the text box
        # if it has names, split it between names
        names_list = selected_names.split(";") 
        for i, name in enumerate(names_list):
            # remove leading and trailing whitespace and semicolons from each name in the names list
            names_list[i] = name.strip("; ")
    else:
        names_list = [] # if it doesnt have any names in it, the names list is empty

    # change selected_faculty to more usable bool type:
    selected_faculty = True if selected_faculty == "Yes" else False

    # change selected_class_count to more usable bool type:
    selected_class_count = True if selected_class_count == "Yes" else False

    if selected_course != COURSE_DD_TXT and selected_course != 'None':
        print("got it")
        graph = Courses_By_Prof_Grapher(COURSE_DATA, FACULTY_LIST, names_list=names_list, 
                                        faculty_only=selected_faculty)
        graph.graph_data(selected_course, faculty_only=selected_faculty, 
                         class_count=selected_class_count)
    elif (selected_subject != SUBJ_DD_TXT and selected_subject != 'None' 
        and selected_level != LVL_DD_TXT and selected_level != None):
        if selected_display == 'Class':
            graph = Subjs_And_Level_by_Class_Grapher(COURSE_DATA, FACULTY_LIST, names_list=names_list, 
                                                     faculty_only=selected_faculty)
        else:
            graph = Subjs_And_Level_By_Prof_Grapher(COURSE_DATA, FACULTY_LIST, names_list=names_list, 
                                                     faculty_only=selected_faculty)
        graph.graph_data(selected_subject, level=selected_level, faculty_only=selected_faculty, 
                         class_count=selected_class_count)
    elif (selected_subject != SUBJ_DD_TXT and selected_subject != 'None'):
        graph = Subjs_By_Prof_Grapher(COURSE_DATA, FACULTY_LIST, names_list=names_list,
                                      faculty_only=selected_faculty)
        graph.graph_data(selected_subject, faculty_only=selected_faculty, class_count=selected_class_count)
    else:
        return
    
    time.sleep(1)

    As_img = Image.open('As_graph.jpg')
    DsFs_img = Image.open('DsFs_graph.jpg')

    width, height = 200, 200
    As_img = As_img.resize((width, height))
    DsFs_img = DsFs_img.resize((width, height))

    As_pic = ImageTk.PhotoImage(As_img)
    DsFs_pic = ImageTk.PhotoImage(DsFs_img)

    canvas.create_image(0, 0, anchor=tk.NW, image=As_pic)
    canvas.create_image(0, width, anchor=tk.NW, image=DsFs_pic)




root = tk.Tk()
root.title("Group 3 Easy A")

# Create a canvas to display images
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

root.geometry("800x1000")

# Create a white frame
frame = tk.Frame(root, bg="White")
frame.pack(side="top", fill="x")

# Create a larger white frame
white_frame = tk.Frame(root)
white_frame.pack(side="top", fill="both", expand=True)

label = tk.Label(white_frame, text="Group 3 Easy A")
label.config(font=("Times New Roman", 50))
label.pack()

# create label for course choice:
courses_label = ttk.Label(root, text="If a course is chosen it will display over any other choices made, set to 'None' to reset.", relief="raised", borderwidth=1)
courses_label.config(padding=(2, 2), anchor="center", font=("Times New Roman", 15))
courses_label.pack()
# configure dropdown for Courses
chosen_course = tk.StringVar()
course_dropdown = ttk.Combobox(root, textvariable=chosen_course, values=ALL_COURSES, state="readonly")
course_dropdown.set(COURSE_DD_TXT)
course_dropdown.pack()

# create label for subject and level choices:
subject_and_level_label = ttk.Label(root, text="A subject can be chosen on its own or with a level. the level option cannot be used on its own. The instructor vs classes option may only be used if both a subject and a level are chosen", relief="raised", borderwidth=1, wraplength=500)
subject_and_level_label.config(padding=(2, 2), anchor="center", font=("Times New Roman", 15))
subject_and_level_label.pack()
# Configure dropdown for subjects
chosen_subject = tk.StringVar()
subj_dropdown = ttk.Combobox(root, textvariable=chosen_subject, values=SUBJECTS, state="readonly")
subj_dropdown.set(SUBJ_DD_TXT)
subj_dropdown.pack()

# Configure dropdown for levels
chosen_level = tk.StringVar()
level_dropdown = ttk.Combobox(root, textvariable=chosen_level, values=LEVELS, state="readonly")
level_dropdown.set(LVL_DD_TXT)
level_dropdown.pack()

# Configure dropdown for displaying for class or prof
chosen_display = tk.StringVar()
display_options_dropdown = ttk.Combobox(root, textvariable=chosen_display, values=CLASS_INSTR, state="readonly")
display_options_dropdown.set(DISPLAY_PROMPT)
display_options_dropdown.pack()

# create label for faculty only dropdown:
faculty_label = ttk.Label(root, text="Option to display graphs made with faculy data only. This option can be used with any other allowed combination of options.", relief="raised", borderwidth=1, wraplength=500)
faculty_label.config(padding=(2,2), anchor="center", font=("Times New Roman", 15))
faculty_label.pack()
# Configure dropdown for faculty_only configuration
faculty_choice = tk.StringVar()
faculty_dropdown = ttk.Combobox(root, textvariable=faculty_choice, values=YN, state="readonly")
faculty_dropdown.set(FACULTY_PROMPT)
faculty_dropdown.pack()

# create label for faculty only dropdown:
class_count_label = ttk.Label(root, text="Option to display graphs with class counts by the x-axis categories. This option an be used with any other allowed combination of options.", relief="raised", borderwidth=1, wraplength=500)
class_count_label.config(padding=(2,2), anchor="center", font=("Times New Roman", 15))
class_count_label.pack()
# configure dropdown for class count options:
class_count_choice = tk.StringVar()
class_count_dropdown = ttk.Combobox(root, textvariable=class_count_choice, values=YN, state="readonly")
class_count_dropdown.set(CLASS_COUNT_PROMPT)
class_count_dropdown.pack()

# create label for names text box:
names_label = ttk.Label(root, text="Enter names if you would like to limit the data to a subset of instructors (separate names by semicolon; write names in Last, First Middle format)", relief="raised", borderwidth=1, wraplength=500)
names_label.pack()
#configure a text box for names:
chosen_names = tk.StringVar()
names_box = ttk.Entry(root, textvariable=chosen_names)
names_box.pack()


plot_button = ttk.Button(root, text="Plot Graphs", command=graph_choices)
plot_button.pack(pady=10)

root.mainloop()

