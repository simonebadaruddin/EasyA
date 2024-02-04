# EasyA
A system called EasyA that students can use to figure out which professors in which classes are giving the most As, and which professors are giving the fewest Ds or Fs. Created by Group BCCDM

# Project Plan:

## Management Plan:

### Team organization
Our team is organized with distinct roles for each member:
- Nithi will create the Project 1 Plan document
- Luke will build graph objects that include parsing
- Erin will translate, document, and annotate the project in Jupyter Notebook.
- Simone will accept and read the JavaScript file into the Python module, isolate and validate the data, accept and validate input from the command line to collect user option choices on how to display the data in the graphs.
- Isabella will web scrape faculty names using BeautifulSoup; monitor and report individual and project progress.

### Decision making
- Decisions within the team are made through collaborative discussions.
- Communication will primarily occur through text and Discord.
- The team is an equal-status delegation.

### Work breakdown schedule
Our work breakdown schedule outlines 11 milestones, with specific tasks assigned to each team member. 
1. Create initial plan, group chat, Github during the first meeting.
2. Finalize initial plan during the second meeting.
3. Finalize outline of code during the third meeting.
4. Start code production individually in between third and fourth meetings.
5. Code checkpoint during fourth meeting.
    - Everyone knows what they are doing and has started implementing their part of the project
    - Initial code review
6. Finish rough draft of code and documentation in between fourth and fifth meetings 
7. Second code checkpoint during the fifth meeting.
    - Group peer review
8. Make revisions individually based on review in between fifth and sixth meetings.
9. Finalize code and documentation in sixth meeting
    - Code walk through 
    - Practice presentation
10. Turn in project 02/05/24
11. Present project to the class 02/06/24

Each individual team meamber's project schedule consists of meeting these targets within their own task as laid out in team organization.
 
### Monitoring and reporting
Throughout the project individual team members will be in charge of keeping track of what they have done, and reporting will be to the group during code review meetings. 

## Meeting schedule:
Our team has organized a series of meetings as follows:
- Friday, 01/12/24: In-person
- Monday, 01/15/24: Zoom/Discord
- Thursday, 01/18/24: In-person
- Thursday, 01/25/24: In-person
- Thursday, 02/01/24: In-person
- Saturday, 02/03/24: In-person

These meetings are essential for discussing project updates, addressing any challenges, and ensuring effective communication among team members.
Our team communicates through a group text and Discord.

## Build Plan
Each part of the build will occur at once, with each team member assigned to that part of the build working to finish at the same time as all the others. When project parts rely on others (e.g. when input to one portion relies on output from another), the team members tasked with those parts will communicate to resolve the dependencies. The sequence of steps that we will use to build the system depend upon the task. Each team member will have the responsibility of managing their portion of the project so that it is completed up to what is expected at each of the milestones and the output of their portion matches the expected input of any other.

### Rationale for Build Plan:
The system is divided and assigned in order to use each team member's expertise effectively. The chosen steps align with the project requirements and contribute to a comprehensive and well-organized system. Risks, such as potential delays or issues with data correctness, are incorporated through regular monitoring and reporting, providing prompt identification and resolution of any challenges that may arise during the project. The collaborative decision-making process within the team also contributes to risk reduction. 

# SDS:
## Description of the product:
The product, EasyA (or JustPass), is a system designed for students to evaluate and compare instructors' grading histories. It aims to help students make informed decisions when selecting classes or instructors. The system will provide side-by-side visualizations of grading patterns, allowing users to see the distribution of As and Ds/Fs as average percentages of the grades given for different instructors teaching the same class, across different class levels, across one subject and level and different classes, or across one subject and level across instructors (see assignment outline for full description). Users, students, and administrators will be able to interact with the system to view data in various ways, such as by class, subject, or instructor. The system will utilize grade data from the years 2013-2016 at the University of Oregon, provided by the Daily Emerald. 

## Overall Design Description:
The major parts of the system include:
-  Data input, parsing, and storage: 
  - Handles the acquisition of grade data from the provided source and stores it in a structured format.
- Data processing and analysis: 
  - Analyzes the grade data to generate meaningful visualizations and insights through side-by-side graphs.
- User interface (UI): 
  - Provides an interactive interface for users to explore and compare grading histories. 
  - Allows users to choose different views and options.
- System administration tools: 
  - Facilitates the process of updating the system with new data, including a program for administrators to replace all data quickly and easily

## System Structure:
The system has a number of individual components that the the group has tasked its members with individually implementing:
1. Data input, parsing, and storage: 
    - The system accepts gradedata.js as input to retrieve the data.
      - To change the data used, the admin will need to replace this file with another which holds the new data but in the same format. 
    - Upon validation, the data in the file will be parsed into particular Python dictionaries depending on command line input from the user specifying what type of graphs need to be displayed and with which options.
2. User input
    - The user will be shown a series of messages through their terminal.
    - The messages will prompt them for input as to which graphs they would like displayed, and which options they would like to format the graphs with.
    - Upon validation of the user input, the correct graphs will be displayed side-by-side through the use of functions and a graphing object.
3. Data processing: 
    - The user input will define the processing and parsing that the data from the input file will undergo.
    - The appropriate data will end up in a Python dictionary.
4. Graph creation:
    - The graphs will be created through the use of a graph object which accepts the appropriate Python dicts as input, creates the figure objects as processing, and outputs the figure object as an output.

The system is a series of steps that begins with file and user input processing, data processing based on that data and user input, and finally output of the requested graphs in a side-by-side view based on the data, user input, and processing.
 
## Static Model and Dynamic Model:
- Static Model: 
  - Utilizes class diagrams to represent the structure of major components (Data Ingestion, Data Processing, UI, Admin Tools) and their relationships.
- Dynamic Model: 
  - Uses sequence diagrams to illustrate the interactions and flow of information between the major subsystems during tasks such as data analysis and user interactions.

## Design Rationale:
The design choice prioritizes simplicity, modularity, and ease of use. Breaking the system into distinct components allows for independent development and maintenance of each part. The choice of data storage option (local) provides centralization. The use of standard libraries and limited external imports (matplotlib) aligns with the programming constraints and provides a straightforward implementation. The design aims to fulfill the project requirements efficiently while maintaining clarity and user-friendly interactions.



