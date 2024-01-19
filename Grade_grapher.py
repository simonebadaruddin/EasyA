"""
Module containing Graph_grades Python Object
"""


import matplotlib as plt
from matplotlib.figure import Figure
from typing import Union


class Graph_grades(object):
    """
    Object representing the process of setting the data, and subsequently graphing a
    that data, for a certain subset of the University of Oregon 2013-2016 grade data.
     
    Attributes:
        As_data (dict): a dict containing dicts that are each within the category of groups 
        that a user has optioned to graph, each containing the name of the group as a key, and 
        the  proportion of the classes in that group which received an A in the class as a 
        percentage

        DsFs_data (dict): a dict containing dicts that are each within the category of groups 
        that a user has optioned to graph, each containing the name of the group as a key, and 
        the  proportion of the classes in that group which received a D or an F in the class as a 
        percentage

        Each dict consists of a an outer dict, having keys which are the names of the groups in a 
        category. The values for each of the groups is an inner, nested dict. The inner, nested 
        dict consists of a type of class that was taught in that category (e.g. instructors or
        class codes), the values for these keys are lists. The lists each contain either the 
        total percentage of the class that received the letter grade A, or the letter grades D and 
        F, as the first element; and the total number of classes that are within that subgroup (e.g.
        how many classes were taught by that instructor). The average across all the classes in that
        subgroup can then be calculated by dividing the total percentage across all classes, by the 
        number of classes.

        faculty (list[str]): a list of all the regular faculty at the university of Oregon in 2014 
        """

    def __init__(self, As_data=None, DsFs_data=None, faculty=None):
        if As_data and not isinstance(As_data, dict):
            raise TypeError("As_dict must be a valid dict type.")
        if DsFs_data and not isinstance(DsFs_data, dict):
            raise TypeError("DsFs_dict must be a valid dict type.")
        if faculty:
            if not isinstance(faculty, list):
                raise TypeError("faculty must be a valid list type.")
            for name in faculty:
                if not isinstance(name, str):
                    raise TypeError("faculty list contains none-string elements, names must be in valid string format")
        self.__As_data = As_data
        self.__DsFs_data = DsFs_data
        self.__faculty = faculty

    def __str__(self) -> str:
        return f"As_data = {str(self.__As_data) if self.__As_data else None}, 
                DsFs_data = {str(self.__DsFs_data) if self.__DsFs_data else None},
                faculty = {str(self.__faculty) if self.__faculty else None}"
    
    def __repr__(self) -> str:
        return f"As_data = {str(self.__As_data) if self.__As_data else None}, 
                DsFs_data = {str(self.__DsFs_data) if self.__DsFs_data else None},
                faculty = {str(self.__faculty) if self.__faculty else None}"
    
    def set_As_data(self, As_data: dict):
        if not isinstance(As_data, dict):
            raise TypeError("As_data must be a valid dict type.")
        self.__As_data = As_data

    def get_As_data(self):
        return self.__As_data
    
    def set_DsFs_data(self, DsFs_data: dict):
        if not isinstance(DsFs_data, dict):
            raise TypeError("DsFs_dict must be a valid dict type.")
        self.__DsFs_data = DsFs_data
    
    def get_DsFs_data(self):
        return self.__DsFs_data
    
    def set_faculty(self, faculty):
        if not isinstance(faculty, list):
            raise TypeError("faculty must be a valid list type.")
        for name in faculty:
            if not isinstance(name, str):
                raise TypeError("faculty list contains none-string elements, names must be in valid string format")
        self.__faculty = faculty

    def get_faculty(self):
        return self.__faculty
    
    def plot_As_data(self, categories: Union[str, list[str]], faculty_only=None, with_num_classes=None) -> Figure:
        for category in categories:
            try:
                data = self.__As_data[category]
            except:
                raise ValueError("no key {category} found in As_data attribute")
            if not isinstance(data, dict):
                raise TypeError("The category {category} does not correspond to a dictionary in the As_data attribute.")
            data_list = list(data.items())
            data_list.sort()
            categories = [item[0] for item in data_list]
            values = [round(item[1][0]/item[1][1], 2) for item in data_list]

            fig, ax = plt.subplots

        

    def plot_DsFs_data(self, faculty_only=None, with_num_classes=None) -> Figure:
        pass
