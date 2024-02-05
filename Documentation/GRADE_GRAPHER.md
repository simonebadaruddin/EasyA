# Programmers Documentation for the Grade Grapher Module
## Project 1 CS422 Winter 2024
## Written 2/4/2024 by Luke Marshall
##### Simone Badaruddin, Erin Cohen, Isabella Cortez, Nithi Deivanayagam, Luke Marshall

## The `Grade_grapher.py` file includes its own dependencies that must be accounted for

It is necessary to check for required libraries in the directory and install them if they are not found. Make sure you are in your terminal, in the `application` directory.

The `Grade_grapher.py` file requires the use of graphing capabilies to create and produce the graphs, the matplotlib library is used for this purpose
- Type `pip show matplotplib` into the command line of the terminal and hit enter.
- If nothing appears, use `pip install matplotlib` to install the json library.

NOTE: above you are instructed to use the `pip` command. If you are getting an error when this is attempted, you may need to use `pip3` in its place.

## Overview: 

The `Grade_grapher.py` includes:

- Grapher abstract base class
    - For creating a template for its subclasses, passing down mewthods and attributes
- Courses_By_Prof_Grapher subclass
    -for graphing individual course data according to instructors
- Subjs_By_Prof_Grapher
    - for graphing individual subject data according to instructors
- Subjs_And_Level_By_Prof_Grapher
    - for graphing individual subject and level according to instructors
- Subjs_And_Level_By_Class_Grapher
    - for graphing individual subject and level according to class

### Each class has two main methods along with the regular getter and setter methods:
- parse_data
    - parses the natty_science_courses attribute in each class into categories and data appropriate to the graph and its options specified by the particular Grapher subclass and the methods used. 
- graph_data
    - uses the parsed data from the attribute corresponding to user input to graph the grade data according to a category from user input.

## Class Details:

This base class provides a template for all  Grapher objects. It defines the attributes and methods necessary to define, parse, and process grading information into the type of graph that a user has requested. 
    
- Attributes:
    - natty_science_course_data (Dict[str, List[Dict[str, str]]]): the grade data for all the course instances for courses in the natural science subject.
    - faculty (List[str]): a list of all the regular faculty in the natural science subject.
    - natty_science_courses (Set[str]): a set of the course codes for all the courses in the natural science subject
    - natty_science_subjs (Set[str]): a set of the course codes for all the subjects in the natural science dapartment
    - As_data (Dict[str, Dict[str, List[float, int]]]): data from the natty_science_course_data, parsed into a dict of possible graphs, with the keys being the categories for the graph and the values being the data for each graph, data only references the values for %As
    - DsFs_data (Dict[str, Dict[str, List[float, int]]]): data from the natty_science_course_data, parsed into a dict of possible graphs, with the keys being the categories for the graph and the values being the data for each graph, data only references the values for %DsFs

- Implemented Methods:
    - str: for external string representation of the class
    - repr: for internal string representation of the class
    - get_As_data_all_instructors: Getter method for the As_data_all_instructors attribute
    - get_As_data_faculty_only: Getter method for the As_data_faculty_only attribute
    - get_DsFs_data_all_instructors: Getter method for the DsFs_data_all_instructors attribute
    - get_DsFs_data_faculty_only: Getter method for the DsFs_data_faculty_only attribute
    - set_faculty: Setter method for the faculty attribute
    - get_faculty: Getter method for the faculty attribute
    - filter_names: creates a names list if it isn't given as an argument, otherwise accepting the names list if it is, and filters it for faculty members if the keyword argument faculty_only is set to True
        
- Abstract methods:
    - parse_data: parses the natty_science_courses attribute into categories and data appropriate to the graph and its options specified by the Grapher subclass and the methods used. 
    - graph_data: uses the parsed data from the attribute corresponding to user input to graph the grade data according to a category from user input.
        
All attributes and regular methods are defined within the base class and are inherited as-is by the subclasses unless otherwise expressly implemented therin. All abstract methods have their signatures defined within the base class but their actual implementations are defined within each subclass to match the unique parsing and graphing needs. 

## Important methods:
parse_data and graph_graph data are by far the most important of the methods implemented in all the classes.

### parse_data
Takes all the grade data and parses it for all instructors listed for the purpose of graphing. It is mplemented in each subclass to make the parsing unique to the needs of its graphs.

#### Arguments:
- names_list (list[str]): a list of names that are in the grade data, and should be in the parsed grade data

### graph_data
Graphs the data based on user input and the particular parcing that takes place in that object. It is implemented in each subclass to make graphing unique to the type of graph.

#### Arguments:
- category (str): the name of a subject (e.g. MATH, PSY), or a specific course (e.g. MATH11, PSY201)
- level (str): a number [1-6]00, which determines the level that the subject should be limited to, or NoneType, depending on if the subclass requires a level for graphing
- faculty_only (bool): not used in this subclass
- class_count (bool): determines if the class count that the data for each x-axis category (instructors/faculty) has been garnered from should be included with the category label

    

