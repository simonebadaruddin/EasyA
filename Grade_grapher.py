"""
Module containing Graph_grades Python Object
"""


import matplotlib as plt
from matplotlib.figure import Figure
from typing import Union, Dict, List
from abc import ABC, abstractmethod

class Grapher(ABC):
    def __init__(self, natty_science_courses: Dict[str, List[Dict[str, str]]], faculty: List[str]) -> None:
        self.natty_science_courses = natty_science_courses
        self.faculty = faculty
        self.natty_sciences = set([ 'ANTH', 'ASTR', 'BI', 'CH', 'CIS', 'CIT', 'CPSY', 'ERTH', 'ENVS', 
                          'GEOG', 'HPHY', 'MATH', 'NEUR', 'PHYS', 'PSY' ])
        self.natty_science_depts = set([ 'ANTH', 'ASTR', 'BI', 'CH', 'CIS', 'CIT', 'ERTH', 'ENVS', 
                                'HPHY', 'MATH', 'NEUR', 'PHYS', 'PSY' ])

    @abstractmethod
    def parse_for_all_instructors(self) -> Dict[str, Dict[str, str]]:
        pass

    @abstractmethod
    def parse_for_faculty_only(self) -> Dict[str, Dict[str, str]]:
        pass


class Courses_By_Prof_Grapher(Grapher):
    def __init__(self, natty_science_courses: Dict[str, List[Dict[str, str]]], faculty: List[str]) -> None:
        super().__init__(natty_science_courses, faculty)
        parsed_data_all_instructors = self.parse_for_all_instructors()
        parsed_data_faculty_only = self.parse_for_faculty_only()
        self.As_data_all_instructors = parsed_data_all_instructors[0]
        self.As_data_faculty_only = parsed_data_faculty_only[0]
        self.DsFs_data_all_instructors = parsed_data_all_instructors[1]
        self.DsFs_data_faculty_only = parsed_data_faculty_only[1]

    def parse_for_all_instructors(self) -> List[Dict[str, Dict[str, str]]]:
        # grades_for_courses_by_prof_(As/DsFs) (dict{str : dict{str: list[int, int]}): keys are course names; values are dicts.
        # value dicts have instructor names as keys and lists with the first element being the total %As or total %Ds and %Fs, 
        # and the second element being the number of times the instructor taught that course as values
        grades_for_courses_by_prof_As = {}
        grades_for_courses_by_prof_DsFs = {}
        for course in self.natty_science_courses: # iterate through the courses in natty_science_courses dict
            # initialize the course as a key to an empty dict value
            grades_for_courses_by_prof_As[course] = {}
            grades_for_courses_by_prof_DsFs[course] = {}
            for instance in self.natty_science_courses[course]: # iterate through the instances in which the class was taught
                instructor = instance["instructor"] # instructor (str): the instructor for each instance
                if instructor in grades_for_courses_by_prof_As[course]:
                    # if the instructor is already in the dict correponding to the course, add the %As or %Ds and %Fs
                    # to the respective dicts and increment their class count
                    grades_for_courses_by_prof_As[course][instructor][0] += float(instance["aprec"])
                    grades_for_courses_by_prof_As[course][instructor][1] += 1
                    grades_for_courses_by_prof_DsFs[course][instructor][0] += (float(instance["dprec"]) + float(instance["fprec"]))
                    grades_for_courses_by_prof_DsFs[course][instructor][1] += 1
                else:
                    # if the instructor is not in the dict corresponding to the course, initialize them to the %As or 
                    # %Ds and %Fs, and their class count to 1 in the respective dicts
                    grades_for_courses_by_prof_As[course][instructor] = [float(instance["aprec"]), 1]
                    grades_for_courses_by_prof_DsFs[course][instructor] = [(float(instance["dprec"]) + float(instance["fprec"])), 1]
                
        return [grades_for_courses_by_prof_As ,grades_for_courses_by_prof_DsFs]
    
    def parse_for_faculty_only(self) -> Dict[str, Dict[str, str]]:
        # grades_for_courses_by_prof_(As/DsFs) (dict{str : dict{str: list[int, int]}): keys are course names; values are dicts.
        # value dicts have instructor names as keys and lists with the first element being the total %As or total %Ds and %Fs, 
        # and the second element being the number of times the instructor taught that course as values
        grades_for_courses_by_prof_As_faculty_only = {}
        grades_for_courses_by_prof_DsFs_faculty_only = {}
        for course in self.natty_science_courses: # iterate through the courses in natty_science_courses dict
            # initialize the course as a key to an empty dict value
            grades_for_courses_by_prof_As_faculty_only[course] = {}
            grades_for_courses_by_prof_DsFs_faculty_only[course] = {}
            for instance in self.natty_science_courses[course]: # iterate through the instances in which the class was taught
                # instructor (str): the instructor for each instance
                if (instructor := instance["instructor"]) in self.faculty: # check if the instructor is part of the regular faculty
                    if instructor in grades_for_courses_by_prof_As_faculty_only[course]:
                        # if the instructor is already in the dict correponding to the course and is in the regular faculty,
                        # add the %As or %Ds and %Fs to the respective dicts and increment their class count
                        grades_for_courses_by_prof_As_faculty_only[course][instructor][0] += float(instance["aprec"])
                        grades_for_courses_by_prof_As_faculty_only[course][instructor][1] += 1
                        grades_for_courses_by_prof_DsFs_faculty_only[course][instructor][0] += (float(instance["dprec"]) + float(instance["fprec"]))
                        grades_for_courses_by_prof_DsFs_faculty_only[course][instructor][1] += 1
                    else:
                        # if the instructor is not in the dict corresponding to the course, but is in the regular faculty, 
                        # initialize them to the %As or %Ds and %Fs, and their class count to 1 in the respective dicts
                        grades_for_courses_by_prof_As_faculty_only[course][instructor] = [float(instance["aprec"]), 1]
                        grades_for_courses_by_prof_DsFs_faculty_only[course][instructor] = [(float(instance["dprec"]) + float(instance["fprec"])), 1]
                    
        return [grades_for_courses_by_prof_As_faculty_only, grades_for_courses_by_prof_DsFs_faculty_only]
    

class Depts_By_Prof_Grapher(Grapher):
    def __init__(self, natty_science_courses: Dict[str, List[Dict[str, str]]], faculty: List[str]) -> None:
        super().__init__(natty_science_courses, faculty)
        parsed_data_all_instructors = self.parse_for_all_instructors()
        parsed_data_faculty_only = self.parse_for_faculty_only()
        self.As_data_all_instructors = parsed_data_all_instructors[0]
        self.As_data_faculty_only = parsed_data_faculty_only[0]
        self.DsFs_data_all_instructors = parsed_data_all_instructors[1]
        self.DsFs_data_faculty_only = parsed_data_faculty_only[1]

    def parse_for_all_instructors(self) -> Dict[str, Dict[str, str]]:
        # grades_for_dept_by_prof_(As/DsFs) (dict{str: dict{str: list[int, int]}}): keys are natural science depts represented by 
        # dept code; values are dicts. Nested value dicts have instructor names as keys and lists with the first element being the 
        # total %As or %Ds and %Fs, and the second element being the number of times the instructor taught a course in that dept
        # as values
        grades_for_dept_by_prof_As = {}
        grades_for_dept_by_prof_DsFs = {}
        for dept in self.natty_science_depts: # initialize each department key to an empty dict value
            grades_for_dept_by_prof_As[dept] = {}
            grades_for_dept_by_prof_DsFs[dept] = {}
        for course in self.natty_science_courses: # iterate through the natural science courses
            # depts (list[str]): list of the natural science departments that a course is in
            depts = [dept for dept in self.natty_science_depts if dept in course] # finds all natural science depts a course is in
            if len(depts) == 1: # check if the course only falls under one department in the natural sciences
                # this_dept (str): the department in the natural sciences that the course falls under
                this_dept = depts[0] 
                # check if the department code is in the course code
                for instance in self.natty_science_courses[course]: # if it is, iterate through the class instances for the course
                    instructor = instance["instructor"]
                    if instructor in grades_for_dept_by_prof_As[this_dept]:
                        # if the instructor is already in the dict correponding to the dept, add the %As or %Ds and %Fs
                        # to the respective dicts and increment their class count
                        grades_for_dept_by_prof_As[this_dept][instructor][0] += float(instance["aprec"])
                        grades_for_dept_by_prof_As[this_dept][instructor][1] += 1
                        grades_for_dept_by_prof_DsFs[this_dept][instructor][0] += (float(instance["dprec"]) + float(instance["fprec"]))
                        grades_for_dept_by_prof_DsFs[this_dept][instructor][1] += 1
                    else:
                        # if the instructor is not in the dict corresponding to the dept, initialize them to the %As or 
                        # %Ds and %Fs, and their class count to 1 in the respective dicts
                        grades_for_dept_by_prof_As[this_dept][instructor] = [float(instance["aprec"]), 1]
                        grades_for_dept_by_prof_DsFs[this_dept][instructor] = [(float(instance["dprec"]) + float(instance["fprec"])), 1]
            elif len(depts) > 1:
                raise AttributeError(f"A course {course} has been found to fit under more than one department: {depts}.")
        
        return [grades_for_dept_by_prof_As, grades_for_dept_by_prof_DsFs]
    
    def parse_for_faculty_only(self) -> Dict[str, Dict[str, str]]:
        # grades_for_dept_by_prof_(As/DsFs) (dict{str: dict{str: list[int, int]}}): keys are natural science depts represented by 
        # dept code; values are dicts. Nested value dicts have instructor names as keys and lists with the first element being the 
        # total %As or %Ds and %Fs, and the second element being the number of times the instructor taught a course in that dept
        # as values
        grades_for_dept_by_prof_As = {}
        grades_for_dept_by_prof_DsFs = {}
        for dept in self.natty_science_depts: # initialize each department key to an empty dict value
            grades_for_dept_by_prof_As[dept] = {}
            grades_for_dept_by_prof_DsFs[dept] = {}
        for course in self.natty_science_courses: # iterate through the natural science courses
            # depts (list[str]): list of the natural science departments that a course is in
            depts = [dept for dept in self.natty_science_depts if dept in course] # finds all natural science depts a course is in
            if len(this_dept) == 1: # check if the course only falls under one department in the natural sciences
                # this_dept (str): the department in the natural sciences that the course falls under
                this_dept = depts[0] 
                # check if the department code is in the course code
                for instance in self.natty_science_courses[course]: # if it is, iterate through the class instances for the course
                    if (instructor := instance["instructor"]) in self.faculty:
                        if instructor in grades_for_dept_by_prof_As[this_dept]:
                            # if the instructor is already in the dict correponding to the dept, add the %As or %Ds and %Fs
                            # to the respective dicts and increment their class count
                            grades_for_dept_by_prof_As[this_dept][instructor][0] += float(instance["aprec"])
                            grades_for_dept_by_prof_As[this_dept][instructor][1] += 1
                            grades_for_dept_by_prof_DsFs[this_dept][instructor][0] += (float(instance["dprec"]) + float(instance["fprec"]))
                            grades_for_dept_by_prof_DsFs[this_dept][instructor][1] += 1
                        else:
                            # if the instructor is not in the dict corresponding to the dept, initialize them to the %As or 
                            # %Ds and %Fs, and their class count to 1 in the respective dicts
                            grades_for_dept_by_prof_As[this_dept][instructor] = [float(instance["aprec"]), 1]
                            grades_for_dept_by_prof_DsFs[this_dept][instructor] = [(float(instance["dprec"]) + float(instance["fprec"])), 1]
            elif len(this_dept) > 1:
                raise AttributeError(f"A course {course} has been foud to fit under more than one department: {this_dept}.")
            
        return [grades_for_dept_by_prof_As, grades_for_dept_by_prof_DsFs]
    
class Depts_And_Level_By_Prof_Grapher(Grapher):
    def __init__(self, natty_science_courses: Dict[str, List[Dict[str, str]]], faculty: List[str]) -> None:
        super().__init__(natty_science_courses, faculty)

    def parse_for_all_instructors(self) -> Dict[str, Dict[str, str]]:
        # grades_for_dept_and_lvl_by_prof_(As/DsFs) (dict{str: dict{str: list[int, int]}}): keys are natural science depts and level
        # represented by dept code concatenated with a level 100-600; values are dicts. Nested value dicts have instructor names
        # as keys and lists with the first element being the total %As or %Ds and %Fs for the class instances the instructor has 
        # taught in that dept at that level and the second element being the number of instances that instructor taught as values
        grades_for_dept_and_lvl_by_prof_As = {}
        grades_for_dept_and_lvl_by_prof_DsFs = {}
        # levels (list[str]): a list of the course levels 100 through 600 as strings
        levels = ['100', '200', '300', '400', '500', '600']
        # dept_levels (list[str]): a list of the departments concatenated with each level in levels
        dept_levels = [dept+lvl for dept in self.natty_science_depts for lvl in levels]
        for dept_lvl in dept_levels:
            # initialize the dicts with strings from depts_levels as keys and empty dicts as values
            grades_for_dept_and_lvl_by_prof_As[dept_lvl] = {}
            grades_for_dept_and_lvl_by_prof_DsFs[dept_lvl] = {}
        for course in self.natty_science_courses: # iterate through the courses in the natural science dept
            for dept in self.natty_science_depts: # iterate through the depts in the natural sciences
                if dept in course: # check if the dept string is a substring of the course name
                    for dept_lvl in dept_levels: # iterate through the dept-level strings in dept_levels
                        if dept_lvl[:len(dept)+1] in course: # check if the dept-level substring, dept concatenated with the
                            # first number of the level, is a substring in the course code
                            for instance in self.natty_science_courses[course]: # if it is, iterate through the class instances for that course
                                instructor = instance["instructor"] # instructor (str): instructor name for the class instance
                                if instructor in grades_for_dept_and_lvl_by_prof_As[dept_lvl]:
                                    # if the instructor is already in the dict corresponding to the dept and level,add the %As 
                                    # or %Ds and %Fs to the respective dicts and increment their class count 
                                    grades_for_dept_and_lvl_by_prof_As[dept_lvl][instructor][0] += float(instance["aprec"])
                                    grades_for_dept_and_lvl_by_prof_As[dept_lvl][instructor][1] += 1
                                    grades_for_dept_and_lvl_by_prof_DsFs[dept_lvl][instructor][0] += (float(instance["dprec"]) + float(instance["fprec"]))
                                    grades_for_dept_and_lvl_by_prof_DsFs[dept_lvl][instructor][1] += 1
                                else:
                                    # if the instructor is not in the dict corresponding to the dept and level, initialize them to 
                                    # the %As or %Ds and %Fs, and their class count to 1 in the respective dicts
                                    grades_for_dept_and_lvl_by_prof_As[dept_lvl][instructor] = [float(instance["aprec"]), 1]
                                    grades_for_dept_and_lvl_by_prof_DsFs[dept_lvl][instructor] = [(float(instance["dprec"]) + float(instance["fprec"])), 1]
                            break
                    break
        
        return [grades_for_dept_and_lvl_by_prof_As, grades_for_dept_and_lvl_by_prof_DsFs]
    
    def parse_for_faculty_only(self) -> Dict[str, Dict[str, str]]:
        # grades_for_dept_and_lvl_by_prof_(As/DsFs) (dict{str: dict{str: list[int, int]}}): keys are natural science depts and level
        # represented by dept code concatenated with a level 100-600; values are dicts. Nested value dicts have instructor names
        # as keys and lists with the first element being the total %As or %Ds and %Fs for the class instances the instructor has 
        # taught in that dept at that level and the second element being the number of instances that instructor taught as values
        grades_for_dept_and_lvl_by_prof_As = {}
        grades_for_dept_and_lvl_by_prof_DsFs = {}
        # levels (list[str]): a list of the course levels 100 through 600 as strings
        levels = ['100', '200', '300', '400', '500', '600']
        # dept_levels (list[str]): a list of the departments concatenated with each level in levels
        dept_levels = [dept+lvl for dept in self.natty_science_depts for lvl in levels]
        for dept_lvl in dept_levels:
            # initialize the dicts with strings from depts_levels as keys and empty dicts as values
            grades_for_dept_and_lvl_by_prof_As[dept_lvl] = {}
            grades_for_dept_and_lvl_by_prof_DsFs[dept_lvl] = {}
        for course in self.natty_science_courses: # iterate through the courses in the natural science dept
            for dept in self.natty_science_depts: # iterate through the depts in the natural sciences
                if dept in course: # check if the dept string is a substring of the course name
                    for dept_lvl in dept_levels: # iterate through the dept-level strings in dept_levels
                        if dept_lvl[:len(dept)+1] in course: # check if the dept-level substring, dept concatenated with the
                            # first number of the level, is a substring in the course code
                            for instance in self.natty_science_courses[course]: # if it is, iterate through the class instances for that course
                                if (instructor := instance["instructor"]) in self.faculty: # instructor (str): instructor name for the class instance
                                    if instructor in grades_for_dept_and_lvl_by_prof_As[dept_lvl]:
                                        # if the instructor is already in the dict corresponding to the dept and level,add the %As 
                                        # or %Ds and %Fs to the respective dicts and increment their class count 
                                        grades_for_dept_and_lvl_by_prof_As[dept_lvl][instructor][0] += float(instance["aprec"])
                                        grades_for_dept_and_lvl_by_prof_As[dept_lvl][instructor][1] += 1
                                        grades_for_dept_and_lvl_by_prof_DsFs[dept_lvl][instructor][0] += (float(instance["dprec"]) + float(instance["fprec"]))
                                        grades_for_dept_and_lvl_by_prof_DsFs[dept_lvl][instructor][1] += 1
                                    else:
                                        # if the instructor is not in the dict corresponding to the dept and level, initialize them to 
                                        # the %As or %Ds and %Fs, and their class count to 1 in the respective dicts
                                        grades_for_dept_and_lvl_by_prof_As[dept_lvl][instructor] = [float(instance["aprec"]), 1]
                                        grades_for_dept_and_lvl_by_prof_DsFs[dept_lvl][instructor] = [(float(instance["dprec"]) + float(instance["fprec"])), 1]
                                break
                        break
                





















# class Graph_grades(object):
#     """
#     Object representing the process of setting the data, and subsequently graphing a
#     that data, for a certain subset of the Univerity of Oregon 2013-2016 grade data.
     
#     Attributes:
#         As_data (dict): a dict containing dicts that are each within the category of groups 
#         that a user has optioned to graph, each containing the name of the group as a key, and 
#         the  proportion of the classes in that group which received an A in the class as a 
#         percentage

#         DsFs_data (dict): a dict containing dicts that are each within the category of groups 
#         that a user has optioned to graph, each containing the name of the group as a key, and 
#         the  proportion of the classes in that group which received a D or an F in the class as a 
#         percentage

#         Each dict consists of a an outer dict, having keys which are the names of the groups in a 
#         category. The values for each of the groups is an inner, nested dict. The inner, nested 
#         dict consists of a type of class that was taught in that category (e.g. instructors or
#         class codes), the values for these keys are lists. The lists each contain either the 
#         total percentage of the class that received the letter grade A, or the letter grades D and 
#         F, as the first element; and the total number of classes that are within that subgroup (e.g.
#         how many classes were taught by that instructor). The average across all the classes in that
#         subgroup can then be calculated by dividing the total percentage across all classes, by the 
#         number of classes.

#         faculty (list[str]): a list of all the regular faculty at the university of Oregon in 2014 
#         """

#     def __init__(self, As_data=None, DsFs_data=None, faculty=None):
#         """Constructor function
        
#         args:
#             As_data: dict of group data relating to the proportion of As in a group
#             DsFs_data: dict group data relating to the proportion of Ds and Fs in a group
#             faculty: list of regular faculty"""
        
#         if As_data and not isinstance(As_data, dict):
#             raise TypeError("As_dict must be a valid dict type.")
#         if DsFs_data and not isinstance(DsFs_data, dict):
#             raise TypeError("DsFs_dict must be a valid dict type.")
#         if faculty:
#             if not isinstance(faculty, list):
#                 raise TypeError("faculty must be a valid list type.")
#             for name in faculty:
#                 if not isinstance(name, str):
#                     raise TypeError("faculty list contains none-string elements, names must be in valid string format")
#         self.__As_data = As_data
#         self.__DsFs_data = DsFs_data
#         self.__faculty = faculty

#     def __str__(self) -> str:
#         """Returns: string representation of the instance attributes"""
#         return f"As_data = {str(self.__As_data) if self.__As_data else None}, 
#                 DsFs_data = {str(self.__DsFs_data) if self.__DsFs_data else None},
#                 faculty = {str(self.__faculty) if self.__faculty else None}"
    
#     def __repr__(self) -> str:
#         """Returns: string representation of the instance attributes"""
#         return f"As_data = {str(self.__As_data) if self.__As_data else None}, 
#                 DsFs_data = {str(self.__DsFs_data) if self.__DsFs_data else None},
#                 faculty = {str(self.__faculty) if self.__faculty else None}"
    
#     def set_As_data(self, As_data: dict):
#         """Setter method for the As_data attribute
        
#         args:
#             As_data: dict of group data relating to the proportion of As in a group"""
#         if not isinstance(As_data, dict):
#             raise TypeError("As_data must be a valid dict type.")
#         self.__As_data = As_data

#     def get_As_data(self) -> dict:
#         """Getter method for the As_data attribute
        
#         Returns: the As_data attribute"""
#         return self.__As_data
    
#     def set_DsFs_data(self, DsFs_data: dict):
#         """Setter method for the DsFs_data attribute
        
#         args:
#             DsFs_data: dict group data relating to the proportion of Ds and Fs in a group"""
#         if not isinstance(DsFs_data, dict):
#             raise TypeError("DsFs_dict must be a valid dict type.")
#         self.__DsFs_data = DsFs_data
    
#     def get_DsFs_data(self) -> dict:
#         """getter method for the Dsfs_data sttribute
        
#         Returns: the DsFs_data attribute"""
#         return self.__DsFs_data
    
#     def set_faculty(self, faculty):
#         """Setter method for the faculty attribute
        
#         args:
#             faculty: list of regular faculty"""
#         if not isinstance(faculty, list):
#             raise TypeError("faculty must be a valid list type.")
#         for name in faculty:
#             if not isinstance(name, str):
#                 raise TypeError("faculty list contains none-string elements, names must be in valid string format")
#         self.__faculty = faculty

#     def get_faculty(self):
#         """Getter method for the faculty attribute
        
#         Returns: the faculty attribute"""
#         return self.__faculty
    
#     def plot_As_data(self, categories: Union[str, list[str]], faculty_only=None, with_num_classes=None) -> Figure:
#         for category in categories:
#             try:
#                 data = self.__As_data[category]
#             except:
#                 raise ValueError("no key {category} found in As_data attribute")
#             if not isinstance(data, dict):
#                 raise TypeError("The category {category} does not correspond to a dictionary in the As_data attribute.")
#             data_list = list(data.items())
#             data_list.sort()
#             categories = [item[0] for item in data_list]
#             values = [round(item[1][0]/item[1][1], 2) for item in data_list]

#             fig, ax = plt.subplots

        

#     def plot_DsFs_data(self, faculty_only=None, with_num_classes=None) -> Figure:
#         pass