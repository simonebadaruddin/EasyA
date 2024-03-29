"""
EasyA_application.py
Original Author: Luke Marshall
Module containing the tkinter EasyA interface and input/output processing
Contributers: Nithi, Simone
Later additions made by: ___________

This module contains the tkinter interface for the Group 3 CS422 EasyA group project.
The interface includes several dropdownn menus:
Course dropdown: allows a user to choose one of any of the courses in the grade data
that are in the natural science departments; a choice of class supercedes any other dichotomous
choices from other dropdowns
Subject dropdown: allows a user to choose one of any of the subjects in the natural science departments
levels dropdown: allows a user to choose one of any of the levels of courses [1-6]00
display dropdown: allows a user to determine if they would like their subject and level data to 
be displayed categorized by instructor or by class in that subject and level; can only be 
used when a subject and level are chosen.
grade dropdown: allows user to choose if they would like the grade data to be displayed in terms of 
%As, or %Ds and Fs; default is in %As
faculty dropdown: allows user to determine if they would like the grade data to be displayed for all
instructors or for only the faculty
class count dropdown: allows the user to choose if they would like the number of class instances that the
data for each x-axis variable (instructors or class) should be shown along with the class

After the user uses the dropdowns to make their choices, they press the 'Plot Graph' button.
This sends the interface input from the dropdowns to the backend where it can be processed.
All of the dropdowns have default text, and some allow for the option of 'None', which are both
checked for in order to find the dropdowns which have input that should be used to graph.
One of 4 grapher subclasses are instantiated based on the dropdons that were used, and the arguments
for this instantiation are garnered from the dropdown input. The graphing method is used on this object,
with data from the dropdowns used as arguments for displaying the graph how the user wants.

The object creates two jpg images in the users application directory, one for %As and the other for %Ds and Fs.
Depending if the user has used the grading dropdown and which choice they made if they did, one or the other of
these images will open.

At this point the user may choose to close the image and either return to the interface and make more choices and
graph more, or hit the 'Exit' button to close the program."""

# libraries
import tkinter as tk # interface library
from tkinter import ttk, messagebox # more modern interface designs
from data_maintainer import Data_Maintainer # Data_Maintainer object from local data_maintainer file
from Grade_grapher import ( Subjs_And_Level_by_Class_Grapher, Subjs_And_Level_By_Prof_Grapher, 
                        Subjs_By_Prof_Grapher, Courses_By_Prof_Grapher ) # Grade graphing objects from local grade_grapher module
import json # json file usage library
from PIL import Image # pillow library for interacting with images


# ==================================================================================================================================
# ----------------------------------------------- Data for Dropdowns -----------------------------------------------------------------
# ==================================================================================================================================


# Get the course data from the grade maintainer module
# DM (Data_Maintainer): intialized data maintainer object
DM = Data_Maintainer() # initialize the grade_maintainer object
DM.update_grade_data() # run the grade maintainer parsing and validation
COURSE_DATA = DM.get_grade_data() # retrieve the parsed and validated course data

with open("faculty_list.json", "r") as file:
    # FACULTY_LIST (list[str]): list of the names of faculty members in the natural science departments
    FACULTY_LIST = json.load(file) # Read the file contents into the variable

# retrieve a full course list from the course data keys
ALL_COURSES = list(COURSE_DATA.keys())
ALL_COURSES.insert(0, "None")

# SUBJECTS (list[str]): the subject codes for courses in the natural science department:
SUBJECTS = [ 'None', 'ANTH', 'ASTR', 'BI', 'BIOE', 'CH', 'CIS', 'CIT', 'CPSY', 'DSCI', 'ERTH', 'ENVS', 
            'GEOG', 'HPHY', 'MATH', 'NEUR', 'PHYS', 'PSY', 'SPSY', 'STAT' ]

# the levels for each course subject
LEVELS = ['None', '100', '200', '300', '400', '500', '600']

# values for grade categorization dropdowns:
CAT = ["%As", "%DsFs"]

# values for dropdowns with yes or no choices:
YN = ["Yes", "No"]


# values for dropdowns with class or instructor choises:
CLASS_INSTR = ["Class", "Instructors"]

# default text displayed in the dropdown menus before choosing an option, dropdowns specified after the assignment:
COURSE_DD_TXT = "Select a Course" # courses
SUBJ_DD_TXT = "Select a Subject" # subjects
LVL_DD_TXT = "Select a Subject Level" # levels
DISPLAY_PROMPT = "For class or instructors?" # displays
GRADE_PROMPT = "Choose %As or %DsFs?" # grading category
FACULTY_PROMPT = "Show data for faculty only?" # faculty only or not
CLASS_COUNT_PROMPT = "Display class count?" # class count option


# ==================================================================================================================================
# ------------------------------------------------------ Graphing -----------------------------------------------------------------
# ==================================================================================================================================


def graph_choices():
    # retrieve the user inputs at the time that the button was pressed:
    # All are based on if the user used the respective dropdowns
    selected_course = chosen_course.get() # selected_course (str): the input from the course dropdown, a course code
    selected_subject = chosen_subject.get() # selected_subject (str): the input from the subject dropdown, a subject code
    selected_level = chosen_level.get() # selected_level (str): the input from the level dropdown, a number 100-600 as a string
    selected_display = chosen_display.get() # selected_display (str): "Instructors" or "class", from instructor/class dropdown
    selected_grading = chosen_grading.get() # selected_grading (str): "%As" or "%DsFs", from grading dropdown
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

    # change selected_grading to more usable bool type:
    selected_grading = False if selected_grading == "%DsFs" else True

    # Create the graphs according to the user input
    # category (str): the category the graph should be of (e.g. MATH111 or MATH)
    category = selected_subject # initialize category as subject chosen as 3/4 cases of graphs use this category
    if selected_course != COURSE_DD_TXT and selected_course != 'None': 
        # check if the selected_course is not the default or "None", otherwise a course has been chosen
        # graph (Grapher subclass): graher subclass object initialized dependent on which inputs chosen by user
        graph = Courses_By_Prof_Grapher(COURSE_DATA, FACULTY_LIST, names_list=names_list, faculty_only=selected_faculty)
        # ^initialize graph corresponding to graphing of courses, Courses_By_Prof_Grapher^
        category = selected_course # set category to selected course for graphing user input
    elif (selected_subject != SUBJ_DD_TXT and selected_subject != 'None' 
        and selected_level != LVL_DD_TXT and selected_level != None):
        # check to see if the subject and level both do not have their default input or "None" as inputs
        if selected_display == 'Class': # if they don't, check the display to determine the object to initialize
            graph = Subjs_And_Level_by_Class_Grapher(COURSE_DATA, FACULTY_LIST, names_list=names_list, 
                                                     faculty_only=selected_faculty)
            # ^ if class is the subject, use the Grapher subclass for graphing grades according to class ^
        else:
            graph = Subjs_And_Level_By_Prof_Grapher(COURSE_DATA, FACULTY_LIST, names_list=names_list, 
                                                     faculty_only=selected_faculty)
            # ^if selected display is not class, use the Grapher subclass for graphing grades according to instructor ^
    elif (selected_subject != SUBJ_DD_TXT and selected_subject != 'None'):
        # if only the selected subject is not its default or "None", use the object associated with graphing a single 
        # subject over all levels
        graph = Subjs_By_Prof_Grapher(COURSE_DATA, FACULTY_LIST, names_list=names_list, faculty_only=selected_faculty)
    else: # if none of these prior options, it is not a valid input, skip
        return
    
    # graph the data according to the user inputs and the Grapher subclass used
    graph.graph_data(category, level=selected_level, faculty_only=selected_faculty, class_count=selected_class_count)
    # Creates 2 jpg images in the directory to open depending on user input
    
    # if the grading option wasn't chosen or %As was chosen open the As jpg, if %DsFs was chosen open the DsFs jpg
    # img (Image): an opened Image object for use in displaying requested graph
    img = Image.open('As_graph.jpg') if selected_grading else Image.open('DsFs_graph.jpg')

    img.show() # display the image on the monitor

# ==================================================================================================================================
# ------------------------------------------------- Exiting ------------------------------------------------------------------------
# ==================================================================================================================================

def exit(): # called when the user presses the 'Exit' button
    if messagebox.askyesno("Exit", "Do you want to quit EasyA?"): # asks user in pop-up box if they'd like to exit
        # citation: https://docs.python.org/3/library/tkinter.messagebox.html
        root.destroy() # destroys the interface and exits the program

# ==================================================================================================================================
# ---------------------------------------------- Root Creation ------------------------------------------------------------------------
# ==================================================================================================================================

# root (tk): the main tkinter object on which all other specifications are built
root = tk.Tk() # initialize the tkinter base platform
root.title("Group 3 Easy A") # title the interface window

# set the size of the tkinter window at start
root.geometry("800x800")

# Create a white frame
frame = tk.Frame(root, bg="White")
frame.pack(side="top", fill="x")

# Create a larger white frame
white_frame = tk.Frame(root)
white_frame.pack(side="top", fill="both", expand=True)

# create the title on the page itself
label = tk.Label(white_frame, text="Group 3 Easy A")
label.config(font=("Times New Roman", 50))
label.pack()

# ==================================================================================================================================
# ------------------------------------------------- Dropdown Creation -----------------------------------------------------------------
# ==================================================================================================================================
"""
All dropdowns have the same format for creation:
create the label for the dropdown: this creates the text that will be displayed above each dropdown and formats it
    format: text, Times New Roman size 15 font, centered on the interface, with a 1 pixel raised border to separate 
    the text from the rest of the interface, and a 2 pixel pad between the text and the border
configure the dropdown: this configures the dropdown with the name it will attach to its store value when the 'Plot Graph' 
button is pressed, what options are to be displayed by in the dropdown, the state of the dropdown 
(read-only so no user shenanigans), and the default text to be displayed in the dropdown before any choices are made. 
"""

# create label for course choice:
courses_label = ttk.Label(root, text="If a course is chosen it will display over any other choices made, set to 'None' to reset.", relief="raised", borderwidth=1)
courses_label.config(padding=(2, 2), anchor="center", font=("Times New Roman", 15)) # set the label style
courses_label.pack() # set the label in the interface
# configure dropdown for Courses
chosen_course = tk.StringVar() # create object to store the chosen option
course_dropdown = ttk.Combobox(root, textvariable=chosen_course, values=ALL_COURSES, state="readonly") # make dropdown, set options, 
course_dropdown.set(COURSE_DD_TXT) # set default text                                                           set read-only
course_dropdown.pack() # set the box in the interface

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

# create label for graph grading category:
grade_label = ttk.Label(root, text="Choose the grading category (default %As)", relief="raised", borderwidth=1, wraplength=500)
grade_label.config(padding=(2,2), anchor="center", font=("Times New Roman", 15))
grade_label.pack()
# create secondary label explaining color usage:
grade_label2 = ttk.Label(root, text="Color variants help discriminate between the graph types. %As are shown in blue, %DsFs are shown in red", relief="raised", borderwidth=1, wraplength=500)
grade_label2.config(padding=(2,2), anchor="center", font=("Times New Roman", 15))
grade_label2.pack()
# Configure dropdown for grading category:
chosen_grading = tk.StringVar()
grading_dropdown = ttk.Combobox(root, textvariable=chosen_grading, values=CAT, state="readonly")
grading_dropdown.set(GRADE_PROMPT)
grading_dropdown.pack()

# create label for faculty only dropdown:
faculty_label = ttk.Label(root, text="Option to display graphs made with faculy data only. This option can be used with any other allowed combination of options.", relief="raised", borderwidth=1, wraplength=500)
faculty_label.config(padding=(2,2), anchor="center", font=("Times New Roman", 15))
faculty_label.pack()
# Configure dropdown for faculty_only:
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
names_label = ttk.Label(root, text="Enter names if you would like to limit the data to a subset of instructors (separate names by semicolon; write names in the format they are found in the grade_data.json file if they ar not in the faculty_list.json, otherwise write them in the format they are found in the faculty_list.json. )", 
                        relief="raised", borderwidth=1, wraplength=500)
names_label.pack()
#configure a text box for names:
chosen_names = tk.StringVar()
names_box = ttk.Entry(root, textvariable=chosen_names)
names_box.pack()

# ==================================================================================================================================
# --------------------------------------------------- Button Creation -----------------------------------------------------------------
# ==================================================================================================================================

# create plot graph button
# when pressed the button will call the graph_choices() function which will create graphs depending on user input
plot_button = ttk.Button(root, text="Plot Graph", command=graph_choices)
plot_button.pack(pady=10) # pad the button for visual clarity

# create exit button
# when pressed the button will call the exit() function which will exit the program if the user checks yes oon the message box
exit_button = ttk.Button(root, text="Exit Program", command=exit)
exit_button.pack(pady=10) # pad the button for visual clarity

# causes the interface to be created according to the specifications
root.mainloop()
