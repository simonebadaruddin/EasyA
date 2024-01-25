"""
Module containing Graph_grades Python Object
"""


from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from typing import Dict, List
from abc import ABC, abstractmethod


# ==================================================================================================================================
# --------------------------------- Grapher Base class definition -----------------------------------------------------------------
# ==================================================================================================================================



class Grapher(ABC):
    def __init__(self, natty_science_courses: Dict[str, List[Dict[str, str]]], faculty: List[str]) -> None:
        """Constructor method for the Grapher abstract base class, not to be used.
        All Grapher subclasses inherit the instance attributes defined below"""
        # natty_science_courses (Dict[str, List[Dict[str, str]]]): A dict holding the grade data for only those classes
        # that are taught as part of the departments in the natural sciences
        self.natty_science_courses = natty_science_courses
        # faculty (List[str]): List of the names of the regular faculty as found on the web pages for the natural sciences
        self.faculty = faculty
        # natty_sciences (Set[str]): set containing the course codes for classes within the natural science departments
        self.natty_sciences = set([ 'ANTH', 'ASTR', 'BI', 'CH', 'CIS', 'CIT', 'CPSY', 'ERTH', 'ENVS', 
                                    'GEOG', 'HPHY', 'MATH', 'NEUR', 'PHYS', 'PSY' ])
        # natty_sciences (Set[str]): set containing the department codes for the natural science departments
        self.natty_science_depts = set([ 'ANTH', 'ASTR', 'BI', 'CH', 'CIS', 'CIT', 'ERTH', 'ENVS', 
                                         'GEOG', 'HPHY', 'MATH', 'NEUR', 'PHYS', 'PSY' ])
        
    # =============== Representational Methods ===========================================================================================

    @abstractmethod
    def __str__(self) -> str:
        """Returns: string representation of the instance attributes for output purposes
        Represents all the instance attributes of the graph subclasses as their length except for the faculty"""

        return f"As_data_all_instructors has {len(self.As_data_all_instructors) if self.As_data_all_instructors else 0} items,
                As_data_faculty_only has {len(self.As_data_faculty_only) if self.As_data_faculty_only else 0} items,  
                DsFs_data_all_instructors has {len(self.DsFs_data_all_instructors) if self.DsFs_data_all_instructors else 0} items, 
                DsFs_data_faculty_only has {len(self.DsFs_data_faculty_only) if self.DsFs_data_faculty_only else 0} items, 
                faculty = {str(self.__faculty) if self.__faculty else None}"
    
    @abstractmethod
    def __repr__(self) -> str:
        """Returns: string representation of the instance attributes for internal representation purposes
        Represents all the instance attributes of the graph subclasses as their length except for the faculty"""

        return f"As_data_all_instructors has {len(self.As_data_all_instructors) if self.As_data_all_instructors else 0} items,
                As_data_faculty_only has {len(self.As_data_faculty_only) if self.As_data_faculty_only else 0} items,  
                DsFs_data_all_instructors has {len(self.DsFs_data_all_instructors) if self.DsFs_data_all_instructors else 0} items, 
                DsFs_data_faculty_only has {len(self.DsFs_data_faculty_only) if self.DsFs_data_faculty_only else 0} items, 
                faculty = {str(self.__faculty) if self.__faculty else None}"
    
    # =============== Getter and Setter Methods ======================================================================================

    @abstractmethod
    def get_As_data_all_instructors(self):
        """Getter method for the As_data_all_instructors attribute
        
        Returns: the As_data_all_instructors attribute"""
        return self.As_data_all_instructors

    @abstractmethod
    def get_As_data_faculty_only(self) -> dict:
        """Getter method for the As_data_faculty_only attribute
        
        Returns: the As_data_faculty_only attribute"""
        return self.As_data_faculty_only
    
    @abstractmethod
    def get_DsFs_data_all_instructors(self):
        """Getter method for the DsFs_data_all_instructors sttribute
        
        Returns: the DsFs_data_all_instructors attribute"""
        return self.DsFs_data_all_instructors
    
    @abstractmethod
    def get_DsFs_data_faculty_only(self) -> dict:
        """Getter method for the DsFs_data_faculty_only attribute
        
        Returns: the DsFs_data_faculty_only attribute"""
        return self.DsFs_data_faculty_only
    
    @abstractmethod
    def set_faculty(self, faculty: List[str]):
        """Setter method for the faculty attribute
        
        args:
            faculty: list of regular faculty
            
        Raises:
            TypeError if faculty is not a list, or if the faculty list contains any non-strings."""
        if not isinstance(faculty, list): # check the input is a list
            raise TypeError("faculty must be a valid list type.")
        for name in faculty:
            if not isinstance(name, str): # check the input is a list of strings
                raise TypeError("faculty list contains none-string elements, names must be in valid string format")
        self.faculty = faculty

    @abstractmethod
    def get_faculty(self) -> List[str]:
        """Getter method for the faculty attribute
        
        Returns: the faculty attribute"""
        return self.faculty
    
    # ================== Data Parsing Methods =======================================================================================
    
    @abstractmethod
    def parse_for_all_instructors(self) -> Dict[str, Dict[str, str]]:
        """Takes all the grade data and parses it for all instructors listed for the purpose of graphing.
         Implemented in each subclass to make the parsing unique to the needs of its graphs 
         
         Raises:
            NotImplementedError if called from the Grapher base class"""
        raise NotImplementedError("Grapher base class should not be instantiated. All methods implemented in child classes.")
    
    @abstractmethod
    def parse_for_faculty_only(self) -> Dict[str, Dict[str, str]]:
        """Takes all the grade data and parses it for only the regular faculty listed for the purpose of graphing.
         Implemented in each subclass to make the parsing unique to the needs of its graphs 
         
         Raises:
            NotImplementedError if called from the Grapher base class"""
        raise NotImplementedError("Grapher base class should not be instantiated. All methods implemented in child classes.")
        
    # =================== Graphing Method ======================================================================================

    @abstractmethod
    def graph_data(self, category: str, level=None, faculty_only=False):
        """Graphs the data based on user input and the particular parcing that takes place in that object.
        Implemented in each subclass to make graphing unique to the type of graph. 
        
        Raises:
            NotImplementedError if called from the Grapher base class"""
        raise NotImplementedError("Grapher base class should not be instantiated. All methods implemented in child classes.")
    
    
# ==================================================================================================================================
# --------------------------------- Courses_By_Prof_Grapher Subclass definition --------------------------------------------------------
# ==================================================================================================================================


class Courses_By_Prof_Grapher(Grapher):
    def __init__(self, natty_science_courses: Dict[str, List[Dict[str, str]]], faculty: List[str]) -> None:
        """Constructor method for instance of class."""
        super().__init__(natty_science_courses, faculty)
        # parse the data
        parsed_data_all_instructors = self.parse_for_all_instructors()
        parsed_data_faculty_only = self.parse_for_faculty_only()

        # %As data for the graphing grades x instructors/faculty who taught each course that 
        # is part of the natty_sciences attribute
        self.As_data_all_instructors = parsed_data_all_instructors[0]
        self.As_data_faculty_only = parsed_data_faculty_only[0]

        # %DsFs data for the graphing grades x instructors/faculty who taught each course that 
        # is part of the natty_sciences attribute
        self.DsFs_data_all_instructors = parsed_data_all_instructors[1]
        self.DsFs_data_faculty_only = parsed_data_faculty_only[1]

    # =============== Representational Methods (All implemented in Grapher Base Class) ======================================================

    def __str__(self) -> str:
        """Returns: string representation of the instance attributes for output purposes"""
        return super().__str__()
    
    def __rep__repr__(self) -> str:
        """Returns: string representation of the instance attributes for internal representation purposes"""
        return super().__repr__()
    
    # =============== Getter and Setter Methods (All implemented in Grapher Base Class) =======================================================
    
    def get_As_data_all_instructors(self):
        """Getter method for the As_data_all_instructors attribute
        
        Returns: the As_data_all_instructors attribute"""
        return super().get_As_data_all_instructors()
    
    def get_As_data_faculty_only(self) -> dict:
        """Getter method for the As_data_faculty_only attribute
        
        Returns: the As_data_faculty_only attribute"""
        return super().get_As_data_faculty_only()
    
    def get_DsFs_data_all_instructors(self):
        """Getter method for the DsFs_data_all_instructors sttribute
        
        Returns: the DsFs_data_all_instructors attribute"""
        return super().get_DsFs_data_all_instructors()
    
    def get_DsFs_data_faculty_only(self) -> dict:
        """Getter method for the DsFs_data_faculty_only attribute
        
        Returns: the DsFs_data_faculty_only attribute"""
        return super().get_DsFs_data_faculty_only()
    
    def set_faculty(self, faculty: List[str]):
        """Setter method for the faculty attribute
        
        args:
            faculty: list of regular faculty
            
        Raises:
            TypeError if faculty is not a list, or if the faculty list contains any non-strings."""
        super().set_faculty(faculty)
    
    def get_faculty(self) -> List[str]:
        """Getter method for the faculty attribute
        
        Returns: the faculty attribute"""
        return super().get_faculty()

    # ================== Data Parsing Methods =======================================================================================

    def parse_for_all_instructors(self) -> List[Dict[str, Dict[str, List[str]]]]:
        """Parses the natty_science_courses attribute into categories and data appropriate to the graph and its options 
        specified by the Grapher subclass and the methods used.
        
        The catgories for this parser are grade data in terms of %A or %Ds and %Fs for each of the courses in the natural
        science department for each of the instructors who taught it, along with the number of times they were taught it.
        This is iteratively parsed from the data and represented as a dict with keys that are names of the courses
        (e.g. MATH111, PSY201) and values that are dicts. The inner dict has the names of all the instructors who taught that 
        class as keys. The values for the inner dict are a lists, with the first element in each being the total %As or 
        %Ds and %Fs for all the instances of the class they taught, stored as a float; and the second element being the number 
        of instances they taught the class  (e.g. if an instructor has taught MATH 111 3 times and the %As were 
        45%, 65%, and 55% then thefirst element in the list will be 110.0, and the second element will be 3). The average 
        percentage of the grades can then be calculated from the two list items by dividing the first by the second when 
        graphing. 

        Returns:
            The dict of parsed natty_science_courses data described above
        """
        # grades_for_courses_by_prof_(As/DsFs) (dict{str : dict{str: list[float, int]}): keys are course names; values are dicts.
        # value dicts have instructor names as keys and lists with the first element being the total %As or total %Ds and %Fs, 
        # for all the instances of the class they have taught and the second element being the number of instances the instructor
        # taught the course
        grades_for_courses_by_prof_As = {}
        grades_for_courses_by_prof_DsFs = {}
        for course in self.natty_science_courses: # iterate through the courses in the natty_science_courses attribute
            # initialize the course as a keys to empty dicts to keep track of %As and %DsFs separately
            grades_for_courses_by_prof_As[course] = {}
            grades_for_courses_by_prof_DsFs[course] = {}
            for instance in self.natty_science_courses[course]: # iterate through the instances of the course
                instructor = instance["instructor"] # instructor (str): the instructor for each instance
                if instructor in grades_for_courses_by_prof_As[course]:
                    # if the instructor is already in the dict correponding to the course, add the %As, and %Ds and %Fs
                    # to their corresponding dicts according to the instructor and increment their class count
                    grades_for_courses_by_prof_As[course][instructor][0] += float(instance["aprec"])
                    grades_for_courses_by_prof_As[course][instructor][1] += 1
                    grades_for_courses_by_prof_DsFs[course][instructor][0] += (float(instance["dprec"]) + float(instance["fprec"]))
                    grades_for_courses_by_prof_DsFs[course][instructor][1] += 1
                else:
                    # if the instructor is not in the dict corresponding to the course, initialize them to the %As or 
                    # %Ds and %Fs for the first instance of that class taught by them; and their class count to 1, marking 
                    # the initial instance in the respective dicts
                    grades_for_courses_by_prof_As[course][instructor] = [float(instance["aprec"]), 1]
                    grades_for_courses_by_prof_DsFs[course][instructor] = [(float(instance["dprec"]) + float(instance["fprec"])), 1]
                
        return [grades_for_courses_by_prof_As ,grades_for_courses_by_prof_DsFs]
    
    def parse_for_faculty_only(self) -> Dict[str, Dict[str, List[str]]]:
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
    
    # =================== Graphing Method ======================================================================================
    
    def graph_data(self, category: str, level=None, faculty_only=False, class_count=False) -> None:
        if level:
            raise TypeError(f"graph_data() method given 1 extra keyword argument: level. Courses_By_Prof_Grapher object does not have a level option.")
        if not category:
            raise TypeError(f"graph_data() method missing 1 positional argument: category")
        try:
            if faculty_only:
                course_data_dict_As = self.As_data_faculty_only[category]
                course_data_dict_DsFs = self.DsFs_data_faculty_only[category]
            else:
                course_data_dict_As = self.As_data_all_instructors[category]
                course_data_dict_DsFs = self.DsFs_data_all_instructors[category]
        except KeyError as e:
            print(f"KeyError has occured: {e}")
        
        course_data_list_As = list(course_data_dict_As.items())
        course_data_list_DsFs = list(course_data_dict_DsFs.items())

        course_data_list_As.sort( key = lambda item: item[1][0]/item[1][1] )
        course_data_list_DsFs.sort( key = lambda item: item[1][0]/item[1][1], reverse=True )

        course_profs_list_As = [f"({item[1][1]}) {item[0]}" if class_count else item[0] for item in course_data_list_As]
        course_grades_list_As = [round(item[1][0]/item[1][1]) for item in course_data_list_As]

        fig, ax = plt.subplots()

        ax.bar(course_profs_list_As, course_grades_list_As, color='blue')
        ax.set_title(f"{category}", fontweight='bold')
        ax.set_xlable(f"{'Instructors' if not faculty_only else 'Faculty'}", fontweight='bold')
        ax.set_ylabel("%\nAs", rotaion=0, labbelpad=10, fontweight='bold')
        for side in ["top", "right"]:
            ax.spines[side].set_visible(False)
        
        plt.savefig('As_graph.jpg')

        course_profs_list_DsFs = [f"({item[1][1]}) {item[0]}" if class_count else item[0] for item in course_data_list_DsFs]
        course_grades_list_DsFs = [round(item[1][0]/item[1][1]) for item in course_data_list_DsFs]

        fig, ax = plt.subplots()

        ax.bar(course_profs_list_DsFs, course_grades_list_DsFs, color='red')

        ax.set_title(f"{category}", fontweight='bold')
        ax.set_xlable(f"{'Instructor' if not faculty_only else 'Faculty'}", fontweight='bold')
        ax.set_ylabel("%\nDsFs", rotaion=0, labbelpad=10, fontweight='bold')
        for side in ["top", "right"]:
            ax.spines[side].set_visible(False)
        
        plt.savefig('DsFs_graph.jpg')

        return


# ==================================================================================================================================
# --------------------------------- Depts_By_Prof_Grapher Subclass definition --------------------------------------------------------
# ==================================================================================================================================


class Depts_By_Prof_Grapher(Grapher):
    def __init__(self, natty_science_courses: Dict[str, List[Dict[str, str]]], faculty: List[str]) -> None:
        """Constructor method for instance of class."""
        super().__init__(natty_science_courses, faculty)
        # parse the data
        parsed_data_all_instructors = self.parse_for_all_instructors()
        parsed_data_faculty_only = self.parse_for_faculty_only()

        # %As data for the graphing grades x instructors/faculty who taught in each department in 
        # the natty_science_depts attribute
        self.As_data_all_instructors = parsed_data_all_instructors[0]
        self.As_data_faculty_only = parsed_data_faculty_only[0]

        # %DsFs data for the graphing grades x instructors/faculty who taught in each department in 
        # the natty_science_depts attribute
        self.DsFs_data_all_instructors = parsed_data_all_instructors[1]
        self.DsFs_data_faculty_only = parsed_data_faculty_only[1]

    # =============== Representational Methods (All implemented in Grapher Base Class) ===========================================================================================

    def __str__(self) -> str:
        """Returns: string representation of the instance attributes for output purposes
        Represents all the instance attributes of the graph subclasses as their length except for the faculty"""
        return super().__str__()
    
    def __rep__repr__(self) -> str:
        """Returns: string representation of the instance attributes for internal representation purposes
        Represents all the instance attributes of the graph subclasses as their length except for the faculty"""
        return super().__repr__()
    
    # =============== Getter and Setter Methods (All implemented in Grapher Base Class) ======================================================================================
    
    def get_As_data_all_instructors(self):
        """Getter method for the As_data_all_instructors attribute
        
        Returns: the As_data_all_instructors attribute"""
        return super().get_As_data_all_instructors()
    
    def get_As_data_faculty_only(self) -> dict:
        """Getter method for the As_data_faculty_only attribute
        
        Returns: the As_data_faculty_only attribute"""
        return super().get_As_data_faculty_only()
    
    def get_DsFs_data_all_instructors(self):
        """Getter method for the DsFs_data_all_instructors sttribute
        
        Returns: the DsFs_data_all_instructors attribute"""
        return super().get_DsFs_data_all_instructors()
    
    def get_DsFs_data_faculty_only(self) -> dict:
        """Getter method for the DsFs_data_faculty_only attribute
        
        Returns: the DsFs_data_faculty_only attribute"""
        return super().get_DsFs_data_faculty_only()
    
    def set_faculty(self, faculty: List[str]):
        """Setter method for the faculty attribute
        
        args:
            faculty: list of regular faculty
            
        Raises:
            TypeError if faculty is not a list, or if the faculty list contains any non-strings."""
        super().set_faculty(faculty)
    
    def get_faculty(self) -> List[str]:
        """Getter method for the faculty attribute
        
        Returns: the faculty attribute"""
        return super().get_faculty()
    
    # ================== Data Parsing Methods =======================================================================================

    def parse_for_all_instructors(self) -> Dict[str, Dict[str, List[str]]]:
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
    
    def parse_for_faculty_only(self) -> Dict[str, Dict[str, List[str]]]:
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
    
    # =================== Graphing Method ======================================================================================
    
    def graph_data(self, category: str, level=None, faculty_only=False, class_count=False) -> None:
        if level:
            raise TypeError(f"graph_data() method given 1 extra keyword argument: level. Depts_By_Prof_Grapher object does not have a level option.")
        if not category:
            raise TypeError(f"graph_data() method missing 1 positional argument: category")
        try:
            if faculty_only:
                course_data_dict_As = self.As_data_faculty_only[category]
                course_data_dict_DsFs = self.DsFs_data_faculty_only[category]
            else:
                course_data_dict_As = self.As_data_all_instructors[category]
                course_data_dict_DsFs = self.DsFs_data_all_instructors[category]
        except KeyError as e:
            print(f"KeyError has occured: {e}")
        
        course_data_list_As = list(course_data_dict_As.items())
        course_data_list_DsFs = list(course_data_dict_DsFs.items())

        course_data_list_As.sort( key = lambda item: item[1][0]/item[1][1] )
        course_data_list_DsFs.sort( key = lambda item: item[1][0]/item[1][1], reverse=True )

        course_profs_list_As = [f"({item[1][1]}) {item[0]}" if class_count else item[0] for item in course_data_list_As]
        course_grades_list_As = [round(item[1][0]/item[1][1]) for item in course_data_list_As]

        fig, ax = plt.subplots()

        ax.bar(course_profs_list_As, course_grades_list_As, color='blue')
        ax.set_title(f"All {category} Classes", fontweight='bold')
        ax.set_xlable(f"{'Instructor' if not faculty_only else 'Faculty'}", fontweight='bold')
        ax.set_ylabel("%\nAs", rotaion=0, labbelpad=10, fontweight='bold')
        for side in ["top", "right"]:
            ax.spines[side].set_visible(False)
        
        plt.savefig('As_graph.jpg')

        course_profs_list_DsFs = [f"({item[1][1]}) {item[0]}" if class_count else item[0] for item in course_data_list_DsFs]
        course_grades_list_DsFs = [round(item[1][0]/item[1][1]) for item in course_data_list_DsFs]

        fig, ax = plt.subplots()

        ax.bar(course_profs_list_DsFs, course_grades_list_DsFs, color='red')

        ax.set_xlable(f"{'Instructor' if not faculty_only else 'Faculty'}", fontweight='bold')
        ax.set_title(f"All {category} Classes", fontweight='bold')
        ax.set_ylabel("%\nDsFs", rotaion=0, labbelpad=10, fontweight='bold')
        for side in ["top", "right"]:
            ax.spines[side].set_visible(False)
        
        plt.savefig('DsFs_graph.jpg')

        return
    

# ==================================================================================================================================
# --------------------------------- Depts_And_Level_By_Prof_Grapher Subclass definition --------------------------------------------------------
# ==================================================================================================================================


class Depts_And_Level_By_Prof_Grapher(Grapher):
    def __init__(self, natty_science_courses: Dict[str, List[Dict[str, str]]], faculty: List[str]) -> None:
        """Constructor method for instance of class."""
        super().__init__(natty_science_courses, faculty)
        # parse the data
        parsed_data_all_instructors = self.parse_for_all_instructors()
        parsed_data_faculty_only = self.parse_for_faculty_only()

        # %As data for the graphing grades x instructors/faculty who taught in a department in the natty_science_depts 
        # attribute at a given level
        self.As_data_all_instructors = parsed_data_all_instructors[0]
        self.As_data_faculty_only = parsed_data_faculty_only[0]

        # %DsFs data for the graphing grades x instructors/faculty who taught in a department in the natty_science_depts 
        # attribute at a given level
        self.DsFs_data_all_instructors = parsed_data_all_instructors[1]
        self.DsFs_data_faculty_only = parsed_data_faculty_only[1]

    # =============== Representational Methods (All implemented in Grapher Base Class) ===========================================================================================

    def __str__(self) -> str:
        """Returns: string representation of the instance attributes for output purposes
        Represents all the instance attributes of the graph subclasses as their length except for the faculty"""
        return super().__str__()
    
    def __rep__repr__(self) -> str:
        """Returns: string representation of the instance attributes for internal representation purposes
        Represents all the instance attributes of the graph subclasses as their length except for the faculty"""
        return super().__repr__()
    
    # =============== Getter and Setter Methods (All implemented in Grapher Base Class)==========================================================
    
    def get_As_data_all_instructors(self):
        """Getter method for the As_data_all_instructors attribute
        
        Returns: the As_data_all_instructors attribute"""
        return super().get_As_data_all_instructors()
    
    def get_As_data_faculty_only(self) -> dict:
        """Getter method for the As_data_faculty_only attribute
        
        Returns: the As_data_faculty_only attribute"""
        return super().get_As_data_faculty_only()
    
    def get_DsFs_data_all_instructors(self):
        """Getter method for the DsFs_data_all_instructors sttribute
        
        Returns: the DsFs_data_all_instructors attribute"""
        return super().get_DsFs_data_all_instructors()
    
    def get_DsFs_data_faculty_only(self) -> dict:
        """Getter method for the DsFs_data_faculty_only attribute
        
        Returns: the DsFs_data_faculty_only attribute"""
        return super().get_DsFs_data_faculty_only()
    
    def set_faculty(self, faculty: List[str]):
        """Setter method for the faculty attribute
        
        args:
            faculty: list of regular faculty
            
        Raises:
            TypeError if faculty is not a list, or if the faculty list contains any non-strings."""
        super().set_faculty(faculty)
    
    def get_faculty(self) -> List[str]:
        """Getter method for the faculty attribute
        
        Returns: the faculty attribute"""
        return super().get_faculty()
    
    # ================== Data Parsing Methods =======================================================================================

    def parse_for_all_instructors(self) -> Dict[str, Dict[str, List[str]]]:
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
            depts = [dept for dept in self.natty_science_depts if dept in course] # iterate through the depts in the natural sciences
            if len(depts) == 1:
                this_dept = depts[0]
                dept_lvls = [dept_lvl for dept_lvl in dept_levels if dept_lvl[:len(this_dept)+1] in course] # iterate through the dept-level strings in dept_levels
                if len(dept_lvls) == 1:
                    this_dept_lvl = dept_lvls[0]
                    # first number of the level, is a substring in the course code
                    for instance in self.natty_science_courses[course]: # if it is, iterate through the class instances for that course
                        instructor = instance["instructor"] # instructor (str): instructor name for the class instance
                        if instructor in grades_for_dept_and_lvl_by_prof_As[this_dept_lvl]:
                            # if the instructor is already in the dict corresponding to the dept and level,add the %As 
                            # or %Ds and %Fs to the respective dicts and increment their class count 
                            grades_for_dept_and_lvl_by_prof_As[this_dept_lvl][instructor][0] += float(instance["aprec"])
                            grades_for_dept_and_lvl_by_prof_As[this_dept_lvl][instructor][1] += 1
                            grades_for_dept_and_lvl_by_prof_DsFs[this_dept_lvl][instructor][0] += (float(instance["dprec"]) + float(instance["fprec"]))
                            grades_for_dept_and_lvl_by_prof_DsFs[this_dept_lvl][instructor][1] += 1
                        else:
                            # if the instructor is not in the dict corresponding to the dept and level, initialize them to 
                            # the %As or %Ds and %Fs, and their class count to 1 in the respective dicts
                            grades_for_dept_and_lvl_by_prof_As[this_dept_lvl][instructor] = [float(instance["aprec"]), 1]
                            grades_for_dept_and_lvl_by_prof_DsFs[this_dept_lvl][instructor] = [(float(instance["dprec"]) + float(instance["fprec"])), 1]
                    
        
        return [grades_for_dept_and_lvl_by_prof_As, grades_for_dept_and_lvl_by_prof_DsFs]
    
    def parse_for_faculty_only(self) -> Dict[str, Dict[str, List[str]]]:
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
            depts = [dept for dept in self.natty_science_depts if dept in course] # iterate through the depts in the natural sciences
            if len(depts) == 1:
                this_dept = depts[0]
                dept_lvls = [dept_lvl for dept_lvl in dept_levels if dept_lvl[:len(this_dept)+1] in course] # iterate through the dept-level strings in dept_levels
                if len(dept_lvls) == 1:
                    this_dept_lvl = dept_lvls[0]
                    # first number of the level, is a substring in the course code
                    for instance in self.natty_science_courses[course]: # if it is, iterate through the class instances for that course
                        if (instructor := instance["instructor"]) in self.faculty: # instructor (str): instructor name for the class instance
                            if instructor in grades_for_dept_and_lvl_by_prof_As[this_dept_lvl]:
                                # if the instructor is already in the dict corresponding to the dept and level,add the %As 
                                # or %Ds and %Fs to the respective dicts and increment their class count 
                                grades_for_dept_and_lvl_by_prof_As[this_dept_lvl][instructor][0] += float(instance["aprec"])
                                grades_for_dept_and_lvl_by_prof_As[this_dept_lvl][instructor][1] += 1
                                grades_for_dept_and_lvl_by_prof_DsFs[this_dept_lvl][instructor][0] += (float(instance["dprec"]) + float(instance["fprec"]))
                                grades_for_dept_and_lvl_by_prof_DsFs[this_dept_lvl][instructor][1] += 1
                            else:
                                # if the instructor is not in the dict corresponding to the dept and level, initialize them to 
                                # the %As or %Ds and %Fs, and their class count to 1 in the respective dicts
                                grades_for_dept_and_lvl_by_prof_As[this_dept_lvl][instructor] = [float(instance["aprec"]), 1]
                                grades_for_dept_and_lvl_by_prof_DsFs[this_dept_lvl][instructor] = [(float(instance["dprec"]) + float(instance["fprec"])), 1]
        
        return [grades_for_dept_and_lvl_by_prof_As, grades_for_dept_and_lvl_by_prof_DsFs]
    
    def graph_data(self, category: str, level=None, faculty_only=False, class_count=False) -> None:
        if not level:
            raise TypeError(f"graph_data() method missing 1 keyword argument: level.")
        if not category:
            raise TypeError(f"graph_data() method missing 1 positional argument: category")
        
        category += str(level)
        try:
            if faculty_only:
                course_data_dict_As = self.As_data_faculty_only[category]
                course_data_dict_DsFs = self.DsFs_data_faculty_only[category]
            else:
                course_data_dict_As = self.As_data_all_instructors[category]
                course_data_dict_DsFs = self.DsFs_data_all_instructors[category]
        except KeyError as e:
            print(f"KeyError has occured: {e}")
        
        course_data_list_As = list(course_data_dict_As.items())
        course_data_list_DsFs = list(course_data_dict_DsFs.items())

        course_data_list_As.sort( key = lambda item: item[1][0]/item[1][1] )
        course_data_list_DsFs.sort( key = lambda item: item[1][0]/item[1][1], reverse=True )

        course_profs_list_As = [f"({item[1][1]}) {item[0]}" if class_count else item[0] for item in course_data_list_As]
        course_grades_list_As = [round(item[1][0]/item[1][1]) for item in course_data_list_As]

        fig, ax = plt.subplots()

        ax.bar(course_profs_list_As, course_grades_list_As, color='blue')
        ax.set_title(f"{category - str(level)} {level}-level", fontweight='bold')
        ax.set_xlable(f"{'Instructor' if not faculty_only else 'Faculty'}", fontweight='bold')
        ax.set_ylabel("%\nAs", rotaion=0, labbelpad=10, fontweight='bold')
        for side in ["top", "right"]:
            ax.spines[side].set_visible(False)
        
        plt.savefig('As_graph.jpg')

        course_profs_list_DsFs = [f"({item[1][1]}) {item[0]}" if class_count else item[0] for item in course_data_list_DsFs]
        course_grades_list_DsFs = [round(item[1][0]/item[1][1]) for item in course_data_list_DsFs]

        fig, ax = plt.subplots()

        ax.bar(course_profs_list_DsFs, course_grades_list_DsFs, color='red')

        ax.set_title(f"All {category - str(level)} {level}-level", fontweight='bold')
        ax.set_xlable(f"{'Instructor' if not faculty_only else 'Faculty'}", fontweight='bold')
        ax.set_ylabel("%\nDsFs", rotaion=0, labbelpad=10, fontweight='bold')
        for side in ["top", "right"]:
            ax.spines[side].set_visible(False)
        
        plt.savefig('DsFs_graph.jpg')

        return


# ==================================================================================================================================
# --------------------------------- Depts_And_Level_by_Class_Grapher Subclass definition --------------------------------------------------------
# ==================================================================================================================================

    
class Depts_And_Level_by_Class_Grapher(Grapher):
    def __init__(self, natty_science_courses: Dict[str, List[Dict[str, str]]], faculty: List[str]) -> None:
        """Constructor method for instance of class."""
        super().__init__(natty_science_courses, faculty)
        # parse the grade data
        parsed_data_all_instructors = self.parse_for_all_instructors()
        parsed_data_faculty_only = self.parse_for_faculty_only()

        # %As data for the graphing grades x class taught by instructors/faculty for classes in the natty_science_depts
        # attribute at a given level
        self.As_data_all_instructors = parsed_data_all_instructors[0]
        self.As_data_faculty_only = parsed_data_faculty_only[0]

        # %DsFs data for the graphing grades x class taught by instructors/faculty for classes in the natty_science_depts
        # attribute at a given level
        self.DsFs_data_all_instructors = parsed_data_all_instructors[1]
        self.DsFs_data_faculty_only = parsed_data_faculty_only[1]

    # =============== Representational Methods (All implemented in Grapher Base Class) ===========================================================================================

    def __str__(self) -> str:
        """Returns: string representation of the instance attributes for output purposes
        Represents all the instance attributes of the graph subclasses as their length except for the faculty"""
        return super().__str__()
    
    def __rep__repr__(self) -> str:
        """Returns: string representation of the instance attributes for internal representation purposes
        Represents all the instance attributes of the graph subclasses as their length except for the faculty"""
        return super().__repr__()
    
    # =============== Getter and Setter Methods (All implemented in Grapher Base Class) ======================================================================================

    def get_As_data_all_instructors(self):
        """Getter method for the As_data_all_instructors attribute
        
        Returns: the As_data_all_instructors attribute"""
        return super().get_As_data_all_instructors()
    
    def get_As_data_faculty_only(self) -> dict:
        """Getter method for the As_data_faculty_only attribute
        
        Returns: the As_data_faculty_only attribute"""
        return super().get_As_data_faculty_only()
    
    def get_DsFs_data_all_instructors(self):
        """Getter method for the DsFs_data_all_instructors sttribute
        
        Returns: the DsFs_data_all_instructors attribute"""
        return super().get_DsFs_data_all_instructors()
    
    def get_DsFs_data_faculty_only(self) -> dict:
        return super().get_DsFs_data_faculty_only()
    """Getter method for the DsFs_data_faculty_only attribute
        
        Returns: the DsFs_data_faculty_only attribute"""
    
    def set_faculty(self, faculty: List[str]):
        """Setter method for the faculty attribute
        
        args:
            faculty: list of regular faculty
            
        Raises:
            TypeError if faculty is not a list, or if the faculty list contains any non-strings."""
        super().set_faculty(faculty)
    
    def get_faculty(self) -> List[str]:
        """Getter method for the faculty attribute
        
        Returns: the faculty attribute"""
        return super().get_faculty()
    
    # ================== Data Parsing Methods =======================================================================================

    def parse_for_all_instructors(self) -> Dict[str, Dict[str, List[str]]]:
        # levels (list[str]): a list of the course levels 100 through 600 as strings
        levels = ['100', '200', '300', '400', '500', '600']
        # dept_levels (list[str]): a list of the departments concatenated with each level in levels
        dept_levels = [dept+lvl for dept in self.natty_science_depts for lvl in levels]
        # grades_for_dept_and_lvl_by_class_(As/DsFs) (dict{str: dict{str: list[int, int]}}): keys are natural science depts and level
        # represented by dept code concatenated with a level 100-600; values are dicts. Nested value dicts have course code
        # as keys and lists with the first element being the total %As or %Ds and %Fs for the class instances for that course 
        # taught in that dept at that level and the second element being the number of instances that course was taught as values
        grades_for_dept_and_lvl_by_class_As = {}
        grades_for_dept_and_lvl_by_class_DsFs = {}
        for dept_lvl in dept_levels:
            # initialize the dicts with strings from depts_levels as keys and empty dicts as values
            grades_for_dept_and_lvl_by_class_As[dept_lvl] = {}
            grades_for_dept_and_lvl_by_class_DsFs[dept_lvl] = {}
        for course in self.natty_science_courses: # iterate through the courses in the natural science dept
            depts = [dept for dept in self.natty_science_depts if dept in course] # iterate through the depts in the natural sciences
            if len(depts) == 1:
                this_dept = depts[0]
                dept_lvls = [dept_lvl for dept_lvl in dept_levels if dept_lvl[:len(this_dept)+1] in course] # iterate through the dept-level strings in dept_levels
                if len(dept_lvls) == 1:
                    this_dept_lvl = dept_lvls[0]
                    # first number of the level, is a substring in the course code
                    for instance in self.natty_science_courses[course]: # if it is, iterate through the class insatnces for that course
                        if course in grades_for_dept_and_lvl_by_class_As[this_dept_lvl]:
                            # if the course is already in the dict corresponding to its dept and level, add the %As or
                            # %Ds and %Fs to the respective dicts and increment the class count
                            grades_for_dept_and_lvl_by_class_As[this_dept_lvl][course][0] += float(instance["aprec"])
                            grades_for_dept_and_lvl_by_class_As[this_dept_lvl][course][1] += 1
                            grades_for_dept_and_lvl_by_class_DsFs[this_dept_lvl][course][0] += (float(instance["dprec"]) + float(instance["fprec"]))
                            grades_for_dept_and_lvl_by_class_DsFs[this_dept_lvl][course][1] += 1
                        else:
                            # if the course is not in the dict corresponding to the dept and level, initialize them to 
                            # the %As or %Ds and %Fs, and the class count to 1 in their respective dicts
                            grades_for_dept_and_lvl_by_class_As[this_dept_lvl][course] = [float(instance["aprec"]), 1]
                            grades_for_dept_and_lvl_by_class_DsFs[this_dept_lvl][course] = [(float(instance["dprec"]) + float(instance["fprec"])), 1]
        
        return [grades_for_dept_and_lvl_by_class_As, grades_for_dept_and_lvl_by_class_DsFs]

    def parse_for_faculty_only(self) -> Dict[str, Dict[str, List[str]]]:
        # levels (list[str]): a list of the course levels 100 through 600 as strings
        levels = ['100', '200', '300', '400', '500', '600']
        # dept_levels (list[str]): a list of the departments concatenated with each level in levels
        dept_levels = [dept+lvl for dept in self.natty_science_depts for lvl in levels]
        # grades_for_dept_and_lvl_by_class_(As/DsFs) (dict{str: dict{str: list[int, int]}}): keys are natural science depts and level
        # represented by dept code concatenated with a level 100-600; values are dicts. Nested value dicts have course code
        # as keys and lists with the first element being the total %As or %Ds and %Fs for the class instances for that course 
        # taught in that dept at that level and the second element being the number of instances that course was taught as values
        grades_for_dept_and_lvl_by_class_As = {}
        grades_for_dept_and_lvl_by_class_DsFs = {}
        for dept_lvl in dept_levels:
            # initialize the dicts with strings from depts_levels as keys and empty dicts as values
            grades_for_dept_and_lvl_by_class_As[dept_lvl] = {}
            grades_for_dept_and_lvl_by_class_DsFs[dept_lvl] = {}
        for course in self.natty_science_courses: # iterate through the courses in the natural science dept
            depts = [dept for dept in self.natty_science_depts if dept in course] # iterate through the depts in the natural sciences
            if len(depts) == 1:
                this_dept = depts[0]
                dept_lvls = [dept_lvl for dept_lvl in dept_levels if dept_lvl[:len(this_dept)+1] in course] # iterate through the dept-level strings in dept_levels
                if len(dept_lvls) == 1:
                    this_dept_lvl = dept_lvls[0]
                    # first number of the level, is a substring in the course code
                    for instance in self.natty_science_courses[course]: # if it is, iterate through the class insatnces for that course
                        if instance["instructor"] in self.faculty:
                            if course in grades_for_dept_and_lvl_by_class_As[this_dept_lvl]:
                                # if the course is already in the dict corresponding to its dept and level, add the %As or
                                # %Ds and %Fs to the respective dicts and increment the class count
                                grades_for_dept_and_lvl_by_class_As[this_dept_lvl][course][0] += float(instance["aprec"])
                                grades_for_dept_and_lvl_by_class_As[this_dept_lvl][course][1] += 1
                                grades_for_dept_and_lvl_by_class_DsFs[this_dept_lvl][course][0] += (float(instance["dprec"]) + float(instance["fprec"]))
                                grades_for_dept_and_lvl_by_class_DsFs[this_dept_lvl][course][1] += 1
                            else:
                                # if the course is not in the dict corresponding to the dept and level, initialize them to 
                                # the %As or %Ds and %Fs, and the class count to 1 in their respective dicts
                                grades_for_dept_and_lvl_by_class_As[this_dept_lvl][course] = [float(instance["aprec"]), 1]
                                grades_for_dept_and_lvl_by_class_DsFs[this_dept_lvl][course] = [(float(instance["dprec"]) + float(instance["fprec"])), 1]

        return [grades_for_dept_and_lvl_by_class_As, grades_for_dept_and_lvl_by_class_DsFs]
    
    # =================== Graphing Method ======================================================================================
    
    def graph_data(self, category: str, level=None, faculty_only=False, class_count=False) -> None:
        if not level:
            raise TypeError(f"graph_data() method missing 1 keyword argument: level.")
        if not category:
            raise TypeError(f"graph_data() method missing 1 positional argument: category")
        
        category += str(level)
        try:
            if faculty_only:
                course_data_dict_As = self.As_data_faculty_only[category]
                course_data_dict_DsFs = self.DsFs_data_faculty_only[category]
            else:
                course_data_dict_As = self.As_data_all_instructors[category]
                course_data_dict_DsFs = self.DsFs_data_all_instructors[category]
        except KeyError as e:
            print(f"KeyError has occured: {e}")
        
        course_data_list_As = list(course_data_dict_As.items())
        course_data_list_DsFs = list(course_data_dict_DsFs.items())

        course_data_list_As.sort( key = lambda item: item[1][0]/item[1][1] )
        course_data_list_DsFs.sort( key = lambda item: item[1][0]/item[1][1], reverse=True )

        course_profs_list_As = [f"({item[1][1]}) {item[0]}" if class_count else item[0] for item in course_data_list_As]
        course_grades_list_As = [round(item[1][0]/item[1][1]) for item in course_data_list_As]

        fig, ax = plt.subplots()

        ax.bar(course_profs_list_As, course_grades_list_As, color='blue')
        ax.set_title(f"{category - str(level)} {level}-level", fontweight='bold')
        ax.set_xlable(f"{'Class' if not faculty_only else 'Class (faculty only)'}", fontweight='bold')
        ax.set_ylabel("%\nAs", rotaion=0, labbelpad=10, fontweight='bold')
        for side in ["top", "right"]:
            ax.spines[side].set_visible(False)
        
        plt.savefig('As_graph.jpg')

        course_profs_list_DsFs = [f"({item[1][1]}) {item[0]}" if class_count else item[0] for item in course_data_list_DsFs]
        course_grades_list_DsFs = [round(item[1][0]/item[1][1]) for item in course_data_list_DsFs]

        fig, ax = plt.subplots()

        ax.bar(course_profs_list_DsFs, course_grades_list_DsFs, color='red')

        ax.set_title(f"All {category - str(level)} {level}-level", fontweight='bold')
        ax.set_xlable(f"{'Class' if not faculty_only else 'Class (faculty only)'}", fontweight='bold')
        ax.set_ylabel("%\nDsFs", rotaion=0, labbelpad=10, fontweight='bold')
        for side in ["top", "right"]:
            ax.spines[side].set_visible(False)
        
        plt.savefig('DsFs_graph.jpg')

        return   
