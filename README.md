# EasyA
a system called EasyA that students can use to figure out which professors in which classes are giving the most As, and which professors are giving the fewest Ds or Fs.

https://classes.cs.uoregon.edu/24W/cs422/index_files/activities.png![image](https://github.com/simonebadaruddin/EasyA/assets/115610746/5e6d9719-1e29-46c7-b260-291a6b7f1852)


# Project Plan:
## Management plan:
- Our team is organized with distinct roles for each member:
  - Nithi is responsible for creating the Project 1 Plan document and parsing data into categories by class, professor, level, and class category.
  - Luke will build object graphs.
  - Erin is assigned to Jupyter translation, documentation, and notation.
  - Simone's tasks include accepting .js files with JSON data, checking data correctness, managing modifications to default graphs, and incorporating graph options from the command line.
  - Isabella is in charge of web scraping using BeautifulSoup, and she will monitor and report individual and project progress
- Decisions within the team are made through collaborative discussions, with communication primarily occurring through text and Discord. 
- Our work breakdown schedule outlines more than 10 milestones, with specific tasks assigned to each team member. 
  - #1: Create initial plan/group chat/Github during the first meeting
  - #2: Finalize initial plan (second meeting)
  - #3: Finalize outline of code (third meeting)
  - #4: Start code production individually
  - #5: Code checkpoint (fourth meeting)
    - Everyone knows what they are doing and has started implementing their part of the project
  - #6: Finish rough draft of code and documentation
  - #7: Second code checkpoint (fifth meeting)
    - Peer review
  - #8: Make revisions
  - #9: Final code changes and documentation
      - Walk through and practice presentation
  - #10: Turn in project 02/05/24
  - #11: Present project to the class 02/06/24
 
## Meeting schedule:
- Our team has organized a series of meetings as follows:
  - Friday, 01/12/24: In-person
  - Monday, 01/15/24: Zoom/Discord
  - Thursday, 01/18/24: In-person
  - Thursday, 01/25/24: In-person
  - Thursday, 02/01/24: In-person
  - Saturday, 02/03/24: In-person
- These meetings are essential for discussing project updates, addressing any challenges, and ensuring effective communication among team members.
- Our team communicates through text. 

## Rationale for Build Plan:
We divided the system into these specific parts to use each team member's expertise effectively. The chosen steps align with the project requirements and contribute to a comprehensive and well-organized system. Risks, such as potential delays or issues with data correctness, are incorporated through regular monitoring and reporting, providing prompt identification and resolution of any challenges that may arise during the project. The collaborative decision-making process within the team also contributes to risk reduction. 

# SDS:
## Description of the product:
The product, EasyA (or JustPass), is a system designed for students to evaluate and compare professors' grading histories. It aims to help students make informed decisions when selecting classes or instructors. The system will provide side-by-side visualizations of grading patterns, allowing users to see the distribution of As and Ds/Fs for different instructors teaching the same class or across different class levels. Users, students, and administrators will be able to interact with the system to view data in various ways, such as by class, department, or instructor. The system will utilize grade data from the years 2013-2016 at the University of Oregon, provided by the Daily Emerald. 

## Overall Design Description:
- The major parts of the system include:
  -  Data Ingestion and Storage: 
    - Handles the acquisition of grade data from the provided source and stores it in a structured format.
  - Data Processing and Analysis: 
    - Analyzes the grade data to generate meaningful visualizations and insights.
  - User Interface (UI): 
    - Provides an interactive interface for users to explore and compare grading histories. 
    - Allows users to choose different views and options.
  - System Administration Tools: 
    - Facilitates the process of updating the system with new data, including a program for administrators to replace all data quickly and easily



