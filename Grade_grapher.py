"""
Module containing Grapher Python class and its subclasses
"""


from matplotlib import pyplot as plt
from typing import Dict, List
from abc import ABC, abstractmethod


# ==================================================================================================================================
# --------------------------------- Grapher Base class definition -----------------------------------------------------------------
# ==================================================================================================================================



class Grapher(ABC):
    """Abstract base class representing a Graph
    
    This base class provides a template for all  Grapher objects.
    It defines the attributes and methods necessary to define, parse, and process
    grading information into the type of graph that a user has requested. 
    
    Attributes:
        natty_science_course_data (Dict[str, List[Dict[str, str]]]): the grade data for all the course instances for
        courses in the natural science subject.
        faculty (List[str]): a list of all the regular faculty in the natural science subject.
        natty_science_courses (Set[str]): a set of the course codes for all the courses in the natural science subject
        natty_science_subjs (Set[str]): a set of the course codes for all the subjects in the natural science dapartment
        As_data (Dict[str, Dict[str, List[float, int]]]): data from the natty_science_course_data, parsed into a dict of 
        possible graphs, with the keys being the categories for the graph and the values being the data for each graph, data 
        only references the values for %As
        DsFs_data (Dict[str, Dict[str, List[float, int]]]): data from the natty_science_course_data, parsed into a dict of 
        possible graphs, with the keys being the categories for the graph and the values being the data for each graph, data 
        only references the values for %DsFs

    Methods:
        str: for external string representation of the class
        repr: for internal string representation of the class
        get_As_data_all_instructors: Getter method for the As_data_all_instructors attribute
        get_As_data_faculty_only: Getter method for the As_data_faculty_only attribute
        get_DsFs_data_all_instructors: Getter method for the DsFs_data_all_instructors attribute
        get_DsFs_data_faculty_only: Getter method for the DsFs_data_faculty_only attribute
        set_faculty: Setter method for the faculty attribute
        get_faculty: Getter method for the faculty attribute
        filter_names: creates a names list if it isn't given as an argument, otherwise accepting the names list if it is,
        and filters it for faculty members if the keyword argument faculty_only is set to True
        
    Abstract methods:
        parse_for_all_instructors: parses the natty_science_course_data attribute into the As_data_all_instructors and 
        DsFs_data_all_instructors attributes. Parsing is implemented and executed according to the Grapher subclass
        that it is called on.
        parse_for_faculty_only: parses the natty_science_course_data attribute into the As_data_faculty_only and
        DsFs_data_faculty_only attreibutes. Parsing is implemented and executed according to the Grapher subclass 
        that it is called on.
        graph_data: uses the parsed data from the attribute corresponding to user input to graph the grade data 
        according to a category from user input.
        
    All attributes and regular methods are defined within the base class and are inherited as-is by the subclasses unless
    otherwise expressly implemented therin. All abstract methods have their signatures defined within the base class
    but their actual implementations are defined within each subclass to match the unique parsing and graphing needs. 
    
    """

    def __init__(self, natty_science_course_data: Dict[str, List[Dict[str, str]]], 
                 faculty: List[str], names_list=[], faculty_only=False) -> None:
        """Constructor method for the Grapher abstract base class, not to be used.
        All Grapher subclasses inherit the attributes defined below"""
        # natty_science_course_data (Dict[str, List[Dict[str, str]]]): A dict holding the grade data for only those classes
        # that are taught as part of the subjects in the natural sciences
        self.natty_science_course_data = natty_science_course_data
        # faculty (List[str]): List of the names of the regular faculty as found on the web pages for the natural sciences
        self.__faculty = set(faculty)
        # natty_science_courses (Set[str]): set containing the course codes for classes within the natural science subjects
        self.natty_science_courses = set([ 'ANTH', 'ASTR', 'BI', 'BIOE', 'CH', 'CIS', 'CIT', 'CPSY', 'DSCI', 'ERTH', 'ENVS', 
                                            'GEOG', 'HPHY', 'MATH', 'NEUR', 'PHYS', 'PSY', 'SPSY', 'STAT' ])
        # natty_science_subjs (Set[str]): set containing the subject codes for the natural science subjects
        
        if faculty_only and not faculty: # check if being asked to parse by faculty without a faculty list
            raise AttributeError("one positional argument missing: parsing by faculty requires a faculty list")
        
        # filter names_list:
        names_list = set(self.filter_names(names_list, faculty_only))
        
        # parse the data
        parsed_data = self.parse_data(names_list)

        # %As data from the parsed natty_science_course_data for all the possible graphs with all the data necessary being 
        # oriented to be as accessible as possible for graphing
        self.__As_data = parsed_data[0]

        # %DsFs data from the parsed natty_science_course_data for all the possible graphs with all the data necessary being 
        # oriented to be as accessible as possible for graphing
        self.__DsFs_data= parsed_data[1]
        
    # =============== Representational Methods ===========================================================================================

    def __str__(self) -> str:
        """Returns: string representation of the instance attributes for output purposes
        Represents all the instance attributes of the graph subclasses as their length except for the faculty"""

        return f"""As_data_all_instructors has {len(self.__As_data) if self.__As_data else 0} items,
                DsFs_data has {len(self.__DsFs_data) if self.__DsFs_data else 0} items, 
                faculty = {str(self.__faculty) if self.__faculty else None}"""
    
    def __repr__(self) -> str:
        """Returns: string representation of the instance attributes for internal representation purposes
        Represents all the instance attributes of the graph subclasses as their length except for the faculty
        which is represented by the list itself"""

        return f"""As_data has {len(self.__As_data) if self.__As_data else 0} items,
                DsFs_data has {len(self.__DsFs_data) if self.__DsFs_data else 0} items, 
                faculty = {str(self.__faculty) if self.__faculty else None}"""
    
    # =============== Getter and Setter Methods ======================================================================================

    def get_As_data(self):
        """Getter method for the As_data_all_instructors attribute
        
        Returns: the As_data_all_instructors attribute"""
        return self.__As_data
    
    def get_DsFs_data(self):
        """Getter method for the DsFs_data_all_instructors sttribute
        
        Returns: the DsFs_data_all_instructors attribute"""
        return self.__DsFs_data
    
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
        self.__faculty = faculty

    def get_faculty(self) -> List[str]:
        """Getter method for the faculty attribute
        
        Returns: the faculty attribute"""
        return self.__faculty
    
    # ================== Data Parsing Method =======================================================================================

    def filter_names(self, names_list=[], faculty_only=False) -> List[str]:
        """If names list is empty a list of all the names from the data is created.
        Takes names list and filters out non-faculty members if the faculty_only paremeter is set to True
        
        args: 
            names_list (List[str]): A list of names the user wants to use in limited graphing; or an empty list by default so 
            the graphing is not limited to a subset of names
            faculty_only (bool): A bool value, defaults to False, which determines if the names_list (either given or created) should 
            be filtered to only hold faculty names"""
        if not names_list:
            names_list = [instance["instructor"] for course in self.natty_science_course_data for instance in self.natty_science_course_data[course]]
        if faculty_only:
            names_list = filter(lambda name: name in self.__faculty, names_list)

        return names_list
        
    @abstractmethod
    def parse_data(self, names_list=[], faculty_only=False) -> Dict[str, Dict[str, str]]:
        """Takes all the grade data and parses it for all instructors listed for the purpose of graphing.
         Implemented in each subclass to make the parsing unique to the needs of its graphs 
         
         Raises:
            NotImplementedError if called from the Grapher base class"""
        raise NotImplementedError("Grapher base class should not be instantiated. All methods implemented are only executable in child classes.")
    
    # =================== Graphing Method ======================================================================================

    @abstractmethod
    def graph_data(self, category: str, level=None, faculty_only=False):
        """Graphs the data based on user input and the particular parcing that takes place in that object.
        Implemented in each subclass to make graphing unique to the type of graph. 
        
        Raises:
            NotImplementedError if called from the Grapher base class"""
        raise NotImplementedError("Grapher base class should not be instantiated. All methods implemented are only executable in child classes.")
    
    
# ==================================================================================================================================
# --------------------------------- Courses_By_Prof_Grapher Subclass definition --------------------------------------------------------
# ==================================================================================================================================


class Courses_By_Prof_Grapher(Grapher):
    """Subclass of Grapher, representing a graph of a single course in the natural science subject
    
    The graph is a bar graph with the X-axis categories being the names of professors who taught the 
    course and the Y-axis measurement being the %As or %Ds and %Fs.

    Attributes inherited from Grapher base class:
        natty_science_course_data (Dict[str, List[Dict[str, str]]]): the grade data for all the course instances for
        courses in the natural science subject.
        faculty (List[str]): a list of all the regular faculty in the natural science subject.
        natty_science_courses (Set[str]): a set of the course codes for all the courses in the natural science subject
        natty_science_subjs (Set[str]): a set of the course codes for all the subjects in the natural science dapartment
        As_data (Dict[str, Dict[str, List[float, int]]]): data from the natty_science_course_data, parsed into a dict of 
        possible graphs, with the keys being the categories for the graph and the values being the data for each graph, data 
        only references the values for %As
        DsFs_data (Dict[str, Dict[str, List[float, int]]]): data from the natty_science_course_data, parsed into a dict of 
        possible graphs, with the keys being the categories for the graph and the values being the data for each graph, data 
        only references the values for %DsFs

    Methods inherited from Grapher base class:
        str: for external string representation of the class
        repr: for internal string representation of the class
        get_As_data_all_instructors: Getter method for the As_data_all_instructors attribute
        get_As_data_faculty_only: Getter method for the As_data_faculty_only attribute
        get_DsFs_data_all_instructors: Getter method for the DsFs_data_all_instructors attribute
        get_DsFs_data_faculty_only: Getter method for the DsFs_data_faculty_only attribute
        set_faculty: Setter method for the faculty attribute
        get_faculty: Getter method for the faculty attribute
        filter_names: creates a names list if it isn't given as an argument, otherwise accepting the names list if it is,
        and filters it for faculty only if the user chooses that option

    Implemented methods:
        parse_data: Parses the natty_science_course_data dict into a dict with categories corresponding to a single graph each
        as keys and all it graphable data and options within the values
        graph_data: Graphs the data according to the way it is parsed and the options that the user has chosen (specific names,
        faculty only, class counts included)
    """
    def __init__(self, natty_science_course_data: Dict[str, List[Dict[str, str]]], faculty: List[str], names_list=[], faculty_only=False) -> None:
        super().__init__(natty_science_course_data, faculty, names_list, faculty_only)

    # ================== Data Parsing Method =======================================================================================

    def parse_data(self, names_list=[]) -> List[Dict[str, Dict[str, List[str]]]]:
        """Parses the natty_science_courses attribute into categories and data appropriate to the graph and its options 
        specified by the Grapher subclass and the methods used.
        
        The categories for this parser are grade data in terms of %A or %Ds and %Fs for each of the courses in the natural
        science subjects for each of the instructors who taught it, along with the number of times they taught it.
        This is iteratively parsed from the data and represented as a dict with keys that are names of the courses
        (e.g. MATH111, PSY201) and values that are dicts. The inner dict has the names of all the instructors who taught that 
        class as keys. The values for the inner dict are a lists, with the first element in each being the total %As or 
        %Ds and %Fs for all the instances of the class they taught, stored as a float; and the second element being the number 
        of instances they taught the class  (e.g. if an instructor has taught MATH 111 3 times and the %As were 
        45%, 65%, and 55% then the first element in the list will be 110.0, and the second element will be 3). The average 
        percentage of the grades can then be calculated from the two list items by dividing the first element by the second 
        when graphing. 

        Returns:
            The dicts of parsed natty_science_courses data described above
        """
        # grades_for_courses_by_prof_(As/DsFs) (dict{str : dict{str: list[float, int]}): keys are course names; values are dicts.
        # value dicts have instructor names as keys and lists with the first element being the total %As or total %Ds and %Fs, 
        # for all the instances of the class they have taught and the second element being the number of instances the instructor
        # taught the course
        grades_for_courses_by_prof_As = {}
        grades_for_courses_by_prof_DsFs = {}
        for course in self.natty_science_course_data: # iterate through the courses in natty_science_course_data dict
            # initialize the course code as a key to an empty dict value
            grades_for_courses_by_prof_As[course] = {}
            grades_for_courses_by_prof_DsFs[course] = {}
            for instance in self.natty_science_course_data[course]: # iterate through the instances in which the class was taught
                # instructor (str): the name of the instructor for each instance
                if (instructor := instance["instructor"]) in names_list: # check if the instructor name is in names_list
                    # if it is, apply the correct dict operations to merge their data
                    if instructor in grades_for_courses_by_prof_As[course]:
                        # if the instructor is already in the dict correponding to the course and is in the names_list,
                        # add the %As or %Ds and %Fs to the respective dicts and increment their class instance count
                        grades_for_courses_by_prof_As[course][instructor][0] += float(instance["aprec"])
                        grades_for_courses_by_prof_As[course][instructor][1] += 1
                        grades_for_courses_by_prof_DsFs[course][instructor][0] += (float(instance["dprec"]) + float(instance["fprec"]))
                        grades_for_courses_by_prof_DsFs[course][instructor][1] += 1
                    else:
                        # if the instructor is not in the dict corresponding to the course, but is in the names_list, 
                        # initialize them to the %As or %Ds and %Fs, and their class instance count to 1 in the respective dicts
                        grades_for_courses_by_prof_As[course][instructor] = [float(instance["aprec"]), 1]
                        grades_for_courses_by_prof_DsFs[course][instructor] = [(float(instance["dprec"]) + float(instance["fprec"])), 1]

        # return the two dicts as elements of a list            
        return [grades_for_courses_by_prof_As, grades_for_courses_by_prof_DsFs]
    
    # =================== Graphing Method ======================================================================================
    
    def graph_data(self, category: str, level=None, faculty_only=False, class_count=False) -> None:
        if level: # level isn't an available argument for this particular subgraph 
            raise TypeError(f"graph_data() method given 1 extra keyword argument: level. Courses_By_Prof_Grapher object does not have a level option.")
        if not category: # category is a necessary argument for this subgraph
            raise TypeError(f"graph_data() method missing 1 positional argument: category")
        try:
            # course_data_dict_(As/DsFs) (Dict[str, List[float, int]]): the inner dict of the As_data and DsFs_data 
            # corresponding to category
            course_data_dict_As = self._Grapher__As_data[category]
            course_data_dict_DsFs = self._Grapher__DsFs_data[category]
        except KeyError as e: # the category is not in the data
            print(f"Attempt to graph a category that doesn't exist: {e}")

        # course_data_list_(As/DsFs) (Tuple[str, List[float, int]]): a list of tuples of the key-value pairs in course_data_dict_(As/DsFs)
        course_data_list_As = list(course_data_dict_As.items())
        course_data_list_DsFs = list(course_data_dict_DsFs.items())

        # The second element in the tuple is a list with 2 values, this sorts the tuples in terms of the quotient of its
        # first and second elements
        course_data_list_As.sort( key = lambda item: item[1][0]/item[1][1], reverse=True ) # sorts in descending order
        course_data_list_DsFs.sort( key = lambda item: item[1][0]/item[1][1] ) # sorts in ascending order

        if len(course_data_list_As) > 20: # checks that the course data is less than 21 items long
            # if they are above 20 items long, this cuts out the middle, only keeping the highest and lowest 10 items
            del course_data_list_As[10:-10]
            del course_data_list_DsFs[10:-10]
            
        # course_profs_list_As (list[str]): list of instructor names; concatenated with their class counts if the class_count argument is set
        course_profs_list_As = [f"({item[1][1]}) {item[0]}" if class_count else item[0] for item in course_data_list_As]
        # course_grades_list_As (list[float]): list of the average %As for each instructor for the classes they taught in category
        course_grades_list_As = [round(item[1][0]/item[1][1]) for item in course_data_list_As]

        # create a matplotlib Figure and Axes:
        fig, ax = plt.subplots()

        # 
        ax.bar(course_profs_list_As, course_grades_list_As, color='blue')
        ax.set_title(f"{category}", fontweight='bold')
        ax.set_xlabel(f"{'Instructors' if not faculty_only else 'Faculty'}", fontweight='bold')
        ax.set_ylabel("%\nAs", rotation=0, labelpad=10, fontweight='bold')
        for side in ["top", "right"]:
            ax.spines[side].set_visible(False)
        
        plt.savefig('As_graph.jpg')

        course_profs_list_DsFs = [f"({item[1][1]}) {item[0]}" if class_count else item[0] for item in course_data_list_DsFs]
        course_grades_list_DsFs = [round(item[1][0]/item[1][1]) for item in course_data_list_DsFs]

        fig, ax = plt.subplots()

        ax.bar(course_profs_list_DsFs, course_grades_list_DsFs, color='red', width=0.1)

        x_tick_positions = [x for x in range(len(course_profs_list_DsFs))]


        ax.set_title(f"{category}", fontweight='bold')
        ax.set_xlabel(f"{'Instructor' if not faculty_only else 'Faculty'}", fontsize=8, fontweight='bold')
        ax.set_xticks(x_tick_positions)
        ax.set_xticklabels(course_profs_list_DsFs, ha='right', fontsize=10, rotation=55)
        ax.set_ylabel("%\nDsFs", rotation=0, labelpad=10, fontweight='bold')
        for side in ["top", "right"]:
            ax.spines[side].set_visible(False)
        plt.tight_layout()
        
        plt.savefig('DsFs_graph.jpg', dpi=300)

        return


# ==================================================================================================================================
# --------------------------------- subjs_By_Prof_Grapher Subclass definition --------------------------------------------------------
# ==================================================================================================================================


class Subjs_By_Prof_Grapher(Grapher):
    """Subclass of Grapher, representing a graph of a single subject in the natural science subject
    
    The graph is a bar graph with the X-axis categories being the names of professors who taught classes that were 
    in the subject and the Y-axis measurement being the %As or %Ds and %Fs.

    Attributes inherited from Grapher base class:
        natty_science_course_data (Dict[str, List[Dict[str, str]]]): the grade data for all the course instances for
        courses in the natural science subject.
        faculty (List[str]): a list of all the regular faculty in the natural science subject.
        natty_science_courses (Set[str]): a set of the course codes for all the courses in the natural science subject
        natty_science_subjs (Set[str]): a set of the course codes for all the subjects in the natural science dapartment
        As_data (Dict[str, Dict[str, List[float, int]]]): data from the natty_science_course_data, parsed into a dict of 
        possible graphs, with the keys being the categories for the graph and the values being the data for each graph, data 
        only references the values for %As
        DsFs_data (Dict[str, Dict[str, List[float, int]]]): data from the natty_science_course_data, parsed into a dict of 
        possible graphs, with the keys being the categories for the graph and the values being the data for each graph, data 
        only references the values for %DsFs

    Methods inherited from Grapher base class:
        str: for external string representation of the class
        repr: for internal string representation of the class
        get_As_data_all_instructors: Getter method for the As_data_all_instructors attribute
        get_As_data_faculty_only: Getter method for the As_data_faculty_only attribute
        get_DsFs_data_all_instructors: Getter method for the DsFs_data_all_instructors attribute
        get_DsFs_data_faculty_only: Getter method for the DsFs_data_faculty_only attribute
        set_faculty: Setter method for the faculty attribute
        get_faculty: Getter method for the faculty attribute
        filter_names: creates a names list if it isn't given as an argument, otherwise accepting the names list if it is,
        and filters it for faculty only if the user chooses that option

    Implemented methods:
        parse_data: Parses the natty_science_course_data dict into a dict with categories corresponding to a single graph each
        as keys and all it graphable data and options within the values
        graph_data: Graphs the data according to the way it is parsed and the options that the user has chosen (specific names,
        faculty only, class counts included)
    """
    def __init__(self, natty_science_course_data: Dict[str, List[Dict[str, str]]], faculty: List[str], names_list=[], faculty_only=False) -> None:
        super().__init__(natty_science_course_data, faculty, names_list, faculty_only)
    
    # ================== Data Parsing Method =======================================================================================

    def parse_data(self, names_list=[]) -> Dict[str, Dict[str, List[str]]]:
        """Parses the natty_science_courses attribute into categories and data appropriate to the graph and its options 
        specified by the Grapher subclass and the methods used.
        
        The categories for this parser are grade data in terms of %A or %Ds and %Fs for each of the course subjects in the 
        natural science subjects for each of the instructors who taught it, along with the number of times they taught it.
        This is iteratively parsed from the data and represented as a dict with keys that are names of the subjects
        (e.g. MATH, PSY, SPSY) and values that are dicts. The inner dict has the names of all the instructors who taught that 
        subject as keys. The values for the inner dict are a lists, with the first element in each being the total %As or 
        %Ds and %Fs for all the instances of the subject they taught, stored as a float; and the second element being the number 
        of instances they taught the siubject (e.g. if an instructor has taught MATH 3 times and the %As were 
        45%, 65%, and 55% then the first element in the list will be 110.0, and the second element will be 3). The average 
        percentage of the grades can then be calculated from the two list items by dividing the first element by the second 
        when graphing. 

        Returns:
            The dicts of parsed natty_science_courses_data described above
        """
        # grades_for_subj_by_prof_(As/DsFs) (dict{str: dict{str: list[int, int]}}): keys are natural science subjs represented by 
        # subj code; values are dicts. Nested value dicts have instructor names as keys and lists with the first element being the 
        # total %As or %Ds and %Fs, and the second element being the number of times the instructor taught a course in that subj
        # as values
        grades_for_subj_by_prof_As = {}
        grades_for_subj_by_prof_DsFs = {}
        for subj in self.natty_science_courses: # initialize each subject key to an empty dict value
            grades_for_subj_by_prof_As[subj] = {}
            grades_for_subj_by_prof_DsFs[subj] = {}
        for course in self.natty_science_course_data: # iterate through the natural science courses
            # subjs (list[str]): list of the natural science subjects that a course is in
            subjs = [subj for subj in self.natty_science_courses if course.startswith(subj)] 
            if len(subjs) == 1: # check if the course has only one subject
                # this_subj (str): the subject of the course
                this_subj = subjs[0] # retreive the subject of the course from the list
                for instance in self.natty_science_course_data[course]: # iterate through the class instances for the course
                    if (instructor := instance["instructor"]) in names_list: # check if the instructor name is in names_list
                        # if it is, apply the correct dict operations to merge their data
                        if instructor in grades_for_subj_by_prof_As[this_subj]:
                            # if the instructor is already in the dict correponding to the subj, add the %As or %Ds and %Fs
                            # to the respective dicts and increment their class count
                            grades_for_subj_by_prof_As[this_subj][instructor][0] += float(instance["aprec"])
                            grades_for_subj_by_prof_As[this_subj][instructor][1] += 1
                            grades_for_subj_by_prof_DsFs[this_subj][instructor][0] += (float(instance["dprec"]) + float(instance["fprec"]))
                            grades_for_subj_by_prof_DsFs[this_subj][instructor][1] += 1
                        else:
                            # if the instructor is not in the dict corresponding to the subj, initialize them to the %As or 
                            # %Ds and %Fs, and their class count to 1 in the respective dicts
                            grades_for_subj_by_prof_As[this_subj][instructor] = [float(instance["aprec"]), 1]
                            grades_for_subj_by_prof_DsFs[this_subj][instructor] = [(float(instance["dprec"]) + float(instance["fprec"])), 1]
            elif len(this_subj) > 1: # validate that course is only in one subject
                raise AttributeError(f"A course {course} has been foud to fit under more than one subject: {this_subj}.")
        
        # return the dicts as elements of a list
        return [grades_for_subj_by_prof_As, grades_for_subj_by_prof_DsFs]
    
    # =================== Graphing Method ======================================================================================
    
    def graph_data(self, category: str, level=None, faculty_only=False, class_count=False) -> None:
        if level:
            raise TypeError(f"graph_data() method given 1 extra keyword argument: level. subjs_By_Prof_Grapher object does not have a level option.")
        if not category:
            raise TypeError(f"graph_data() method missing 1 positional argument: category")
        try:
            course_data_dict_As = self._Grapher__As_data[category]
            course_data_dict_DsFs = self._Grapher__DsFs_data[category]
            
        except KeyError as e:
            print(f"KeyError has occured: {e}")
        
        course_data_list_As = list(course_data_dict_As.items())
        course_data_list_DsFs = list(course_data_dict_DsFs.items())

        course_data_list_As.sort( key = lambda item: item[1][0]/item[1][1], reverse=True )
        course_data_list_DsFs.sort( key = lambda item: item[1][0]/item[1][1] )

        course_profs_list_As = [f"({item[1][1]}) {item[0]}" if class_count else item[0] for item in course_data_list_As]
        course_grades_list_As = [round(item[1][0]/item[1][1]) for item in course_data_list_As]

        fig, ax = plt.subplots()

        ax.bar(course_profs_list_As, course_grades_list_As, color='blue')
        ax.set_title(f"All {category} Classes", fontweight='bold')
        ax.set_xlabel(f"{'Instructor' if not faculty_only else 'Faculty'}", fontweight='bold')
        ax.set_ylabel("%\nAs", rotation=0, labelpad=10, fontweight='bold')
        for side in ["top", "right"]:
            ax.spines[side].set_visible(False)
        
        plt.savefig('As_graph.jpg')

        course_profs_list_DsFs = [f"({item[1][1]}) {item[0]}" if class_count else item[0] for item in course_data_list_DsFs]
        course_grades_list_DsFs = [round(item[1][0]/item[1][1]) for item in course_data_list_DsFs]

        fig, ax = plt.subplots()

        ax.bar(course_profs_list_DsFs, course_grades_list_DsFs, color='red')

        ax.set_title(f"All {category} Classes", fontweight='bold')
        ax.set_xlabel(f"{'Instructor' if not faculty_only else 'Faculty'}", fontweight='bold')
        ax.set_ylabel("%\nDsFs", rotation=0, labelpad=15, fontweight='bold')
        for side in ["top", "right"]:
            ax.spines[side].set_visible(False)
        
        plt.savefig('DsFs_graph.jpg')

        return
    

# ==================================================================================================================================
# --------------------------------- Subjs_And_Level_By_Prof_Grapher Subclass definition --------------------------------------------------------
# ==================================================================================================================================


class Subjs_And_Level_By_Prof_Grapher(Grapher):
    """Subclass of Grapher, representing a graph of a single subject level in the natural science subject
    
    The graph is a bar graph with the X-axis categories being the names of professors who taught classes that were
    in the subject in the given level and the Y-axis measurement being the %As or %Ds and %Fs.

    Attributes inherited from Grapher base class:
        natty_science_course_data (Dict[str, List[Dict[str, str]]]): the grade data for all the course instances for
        courses in the natural science subject.
        faculty (List[str]): a list of all the regular faculty in the natural science subject.
        natty_science_courses (Set[str]): a set of the course codes for all the courses in the natural science subject
        natty_science_subjs (Set[str]): a set of the course codes for all the subjects in the natural science dapartment
        As_data (Dict[str, Dict[str, List[float, int]]]): data from the natty_science_course_data, parsed into a dict of 
        possible graphs, with the keys being the categories for the graph and the values being the data for each graph, data 
        only references the values for %As
        DsFs_data (Dict[str, Dict[str, List[float, int]]]): data from the natty_science_course_data, parsed into a dict of 
        possible graphs, with the keys being the categories for the graph and the values being the data for each graph, data 
        only references the values for %DsFs

    Methods inherited from Grapher base class:
        str: for external string representation of the class
        repr: for internal string representation of the class
        get_As_data: Getter method for the As_data attribute
        get_DsFs_data: Getter method for the DsFs_data attribute
        set_faculty: Setter method for the faculty attribute
        get_faculty: Getter method for the faculty attribute
        filter_names: creates a names list if it isn't given as an argument, otherwise accepting the names list if it is,
        and filters it for faculty only if the user chooses that option

    Implemented methods:
        parse_data: Parses the natty_science_course_data dict into a dict with categories corresponding to a single graph each
        as keys and all it graphable data and options within the values
        graph_data: Graphs the data according to the way it is parsed and the options that the user has chosen (specific names,
        faculty only, class counts included)
    """
    def __init__(self, natty_science_course_data: Dict[str, List[Dict[str, str]]], faculty: List[str], names_list=[], faculty_only=False) -> None:
        super().__init__(natty_science_course_data, faculty, names_list, faculty_only)
    
    # ================== Data Parsing Method =======================================================================================

    def parse_data(self, names_list=[]) -> Dict[str, Dict[str, List[str]]]:
        # grades_for_subj_and_lvl_by_prof_(As/DsFs) (dict{str: dict{str: list[int, int]}}): keys are natural science subjects and 
        # level represented by subject code concatenated with a level 100-600; values are dicts. Nested value dicts have 
        # instructor names as keys and lists with the first element being the total %As or %Ds and %Fs for the class instances 
        # the instructor has taught in that subj at that level and the second element being the number of instances that 
        # instructor taught as values
        grades_for_subj_and_lvl_by_prof_As = {}
        grades_for_subj_and_lvl_by_prof_DsFs = {}
        # levels (list[str]): a list of the course levels 100 through 600 as strings
        levels = ['100', '200', '300', '400', '500', '600']
        # subj_levels (list[str]): a list of the subject concatenated with each level in levels
        subj_levels = [subj+lvl for subj in self.natty_science_courses for lvl in levels]
        for subj_lvl in subj_levels:
            # initialize the dicts with strings from subj_levels as keys and empty dicts as values
            grades_for_subj_and_lvl_by_prof_As[subj_lvl] = {}
            grades_for_subj_and_lvl_by_prof_DsFs[subj_lvl] = {}
        for course in self.natty_science_course_data: # iterate through the courses in the natural sciences
            # subjs (List[str]): list of all the subjects that a course is in (e.g. CPSY is in CPSY)
            subjs = [subj for subj in self.natty_science_courses if course.startswith(subj)]
            if len(subjs) == 1: # check to make sure there is only one subject per course
                # this_subj (List[str]): the single subject of course
                this_subj = subjs[0] # retrieve the subject of the course from the list
                # subj_level (str): list of the subjects according to level that a course is in (e.g. CPSY199 is in CSPY100)
                subj_lvls = [subj_lvl for subj_lvl in subj_levels if course.startswith(subj_lvl[:len(this_subj)+1])]
                if len(subj_lvls) == 1: # check to make sure there is only one subject and level per course
                    # subj_subj_lvl (str): the subject and level of a course
                    subj_subj_lvl = subj_lvls[0] # retrieve the subject and level of the course from the list
                    for instance in self.natty_science_course_data[course]: # iterate through the class instances for course
                        # instructor (str): instructor name for the class instance
                        if (instructor := instance["instructor"]) in names_list: # check to make sure the instructor name is in names_list
                            # if it is, apply the correct dict operations to merge their data
                            if instructor in grades_for_subj_and_lvl_by_prof_As[subj_subj_lvl]:
                                # if the instructor is already in the dict corresponding to the subj and level,add the %As 
                                # or %Ds and %Fs to the respective dicts and increment their class count 
                                grades_for_subj_and_lvl_by_prof_As[subj_subj_lvl][instructor][0] += float(instance["aprec"])
                                grades_for_subj_and_lvl_by_prof_As[subj_subj_lvl][instructor][1] += 1
                                grades_for_subj_and_lvl_by_prof_DsFs[subj_subj_lvl][instructor][0] += (float(instance["dprec"]) + float(instance["fprec"]))
                                grades_for_subj_and_lvl_by_prof_DsFs[subj_subj_lvl][instructor][1] += 1
                            else:
                                # if the instructor is not in the dict corresponding to the subj and level, initialize them to 
                                # the %As or %Ds and %Fs, and their class count to 1 in the respective dicts
                                grades_for_subj_and_lvl_by_prof_As[subj_subj_lvl][instructor] = [float(instance["aprec"]), 1]
                                grades_for_subj_and_lvl_by_prof_DsFs[subj_subj_lvl][instructor] = [(float(instance["dprec"]) + float(instance["fprec"])), 1]
                elif len(subj_lvls) > 1: # validate that there is at most one subject and level per course
                    raise AttributeError(f"A course {course} has been foud to fit under more than one subject and level: {subj_lvls}.")
            elif len(subjs) > 1: # validate that there is at most one subject per course
                raise AttributeError(f"A course {course} has been foud to fit under more than one subject: {subjs}.")
        
        # return the dicts as elements of a list
        return [grades_for_subj_and_lvl_by_prof_As, grades_for_subj_and_lvl_by_prof_DsFs]
    
    def graph_data(self, category: str, level=None, faculty_only=False, class_count=False) -> None:
        if not level:
            raise TypeError(f"graph_data() method missing 1 keyword argument: level.")
        if not category:
            raise TypeError(f"graph_data() method missing 1 positional argument: category")
        if not isinstance(category, str):
            raise TypeError("category positional argument should be a string.")
        if not isinstance(level, str):
            raise TypeError("level positional argument should be a string.")
        if not level in set(['100', '200', '300', '400', '500', '600']):
            raise AttributeError(f"level {level} is not an appropriate level")

        category += str(level)
        try:
            course_data_dict_As = self._Grapher__As_data[category]
            course_data_dict_DsFs = self._Grapher__DsFs_data[category]

        except KeyError as e:
            print(f"KeyError has occured: {e}")
        
        course_data_list_As = list(course_data_dict_As.items())
        course_data_list_DsFs = list(course_data_dict_DsFs.items())

        course_data_list_As.sort( key = lambda item: item[1][0]/item[1][1], reverse=True )
        course_data_list_DsFs.sort( key = lambda item: item[1][0]/item[1][1] )

        course_profs_list_As = [f"({item[1][1]}) {item[0]}" if class_count else item[0] for item in course_data_list_As]
        course_grades_list_As = [round(item[1][0]/item[1][1]) for item in course_data_list_As]

        fig, ax = plt.subplots()

        ax.bar(course_profs_list_As, course_grades_list_As, width=0.25, color='blue')
        ax.set_title(f"{category.rstrip(level)} {level}-level", fontweight='bold')
        ax.set_xlabel(f"{'Instructor' if not faculty_only else 'Faculty'}", fontweight='bold')
        ax.set_ylabel("%\nAs", rotation=0, labelpad=10, fontweight='bold')
        for side in ["top", "right"]:
            ax.spines[side].set_visible(False)
        
        plt.savefig('As_graph.jpg')

        course_profs_list_DsFs = [f"({item[1][1]}) {item[0]}" if class_count else item[0] for item in course_data_list_DsFs]
        course_grades_list_DsFs = [round(item[1][0]/item[1][1]) for item in course_data_list_DsFs]

        fig, ax = plt.subplots()

        ax.bar(course_profs_list_DsFs, course_grades_list_DsFs, color='red', width=0.8)

        ax.set_title(f"All {category.rstrip(level)} {level}-level", fontweight='bold')
        ax.set_xlabel(f"{'Instructor' if not faculty_only else 'Faculty'}", fontweight='bold')
        ax.set_ylabel("%\nDsFs", rotation=0, labelpad=10, fontweight='bold')
        for side in ["top", "right"]:
            ax.spines[side].set_visible(False)
        
        plt.savefig('DsFs_graph.jpg')

        return


# ==================================================================================================================================
# --------------------------------- Subjs_And_Level_by_Class_Grapher Subclass definition --------------------------------------------------------
# ==================================================================================================================================

    
class Subjs_And_Level_by_Class_Grapher(Grapher):
    """Subclass of Grapher, representing a graph of a single subject level in the natural science subject
    
    The graph is a bar graph with the X-axis categories being the names of professors who taught classes that were
    in the subject in the given level and the Y-axis measurement being the %As or %Ds and %Fs.

    Attributes inherited from Grapher base class:
        natty_science_course_data (Dict[str, List[Dict[str, str]]]): the grade data for all the course instances for
        courses in the natural science subject.
        faculty (List[str]): a list of all the regular faculty in the natural science subject.
        natty_science_courses (Set[str]): a set of the course codes for all the courses in the natural science subject
        natty_science_subjs (Set[str]): a set of the course codes for all the subjects in the natural science dapartment
        As_data (Dict[str, Dict[str, List[float, int]]]): data from the natty_science_course_data, parsed into a dict of 
        possible graphs, with the keys being the categories for the graph and the values being the data for each graph, data 
        only references the values for %As
        DsFs_data (Dict[str, Dict[str, List[float, int]]]): data from the natty_science_course_data, parsed into a dict of 
        possible graphs, with the keys being the categories for the graph and the values being the data for each graph, data 
        only references the values for %DsFs

    Methods inherited from Grapher base class:
        str: for external string representation of the class
        repr: for internal string representation of the class
        get_As_data: Getter method for the As_data attribute
        get_DsFs_data: Getter method for the DsFs_data attribute
        set_faculty: Setter method for the faculty attribute
        get_faculty: Getter method for the faculty attribute
        filter_names: creates a names list if it isn't given as an argument, otherwise accepting the names list if it is,
        and filters it for faculty only if the user chooses that option

    Implemented methods:
        parse_data: Parses the natty_science_course_data dict into a dict with categories corresponding to a single graph each
        as keys and all it graphable data and options within the values
        graph_data: Graphs the data according to the way it is parsed and the options that the user has chosen (specific names,
        faculty only, class counts included)
    """
    def __init__(self, natty_science_course_data: Dict[str, List[Dict[str, str]]], faculty: List[str], names_list=[], faculty_only=False) -> None:
        super().__init__(natty_science_course_data, faculty, names_list, faculty_only)
    
    # ================== Data Parsing Method =======================================================================================

    def parse_data(self, names_list=[]) -> Dict[str, Dict[str, List[str]]]:
        # levels (list[str]): a list of the course levels 100 through 600 as strings
        levels = ['100', '200', '300', '400', '500', '600']
        # subj_levels (list[str]): a list of the subjects concatenated with each level in levels
        subj_levels = [subj+lvl for subj in self.natty_science_courses for lvl in levels]
        # grades_for_subj_and_lvl_by_class_(As/DsFs) (dict{str: dict{str: list[int, int]}}): keys are natural science subjects 
        # and level represented by subj code concatenated with a level 100-600; values are dicts. Nested value dicts have course
        # number as keys and lists with the first element being the total %As or %Ds and %Fs for the class instances for that 
        # course taught in that subject at that level and the second element being the number of instances that course was 
        # taught as values
        grades_for_subj_and_lvl_by_class_As = {}
        grades_for_subj_and_lvl_by_class_DsFs = {}
        for subj_lvl in subj_levels:
            # initialize the dicts with strings from subj_levels as keys and empty dicts as values
            grades_for_subj_and_lvl_by_class_As[subj_lvl] = {}
            grades_for_subj_and_lvl_by_class_DsFs[subj_lvl] = {}
        for course in self.natty_science_course_data: # iterate through the courses in the natural science subj
            # subjs (List[str]): list of all the subjects that a course is in (e.g. CPSY is in CPSY)
            subjs = [subj for subj in self.natty_science_courses if course.startswith(subj)]
            if len(subjs) == 1: # check that the course is only in one subject
                # this_subj (str): the subject of the 
                this_subj = subjs[0] # retrieve the subject for the course from the list
                # subj_lvls (List[str]): list of all the subjects with level that course is in
                subj_lvls = [subj_lvl for subj_lvl in subj_levels if course.startswith(subj_lvl[:len(this_subj)+1])]
                if len(subj_lvls) == 1: # check that the course is only in one subject with level
                    # this_subj_lvl (str): the course suubject with level
                    this_subj_lvl = subj_lvls[0] # retrieve the subject with level that the course is in
                    for instance in self.natty_science_course_data[course]: # iterate through the class instances for that course
                        if instance["instructor"] in names_list: # check if the instructor name is in the names_list
                            # if it is, apply the correct dict operations to merge their data
                            if course in grades_for_subj_and_lvl_by_class_As[this_subj_lvl]:
                                # if the course is already in the dict corresponding to its subj and level, add the %As or
                                # %Ds and %Fs to the respective dicts and increment the class count
                                grades_for_subj_and_lvl_by_class_As[this_subj_lvl][course][0] += float(instance["aprec"])
                                grades_for_subj_and_lvl_by_class_As[this_subj_lvl][course][1] += 1
                                grades_for_subj_and_lvl_by_class_DsFs[this_subj_lvl][course][0] += (float(instance["dprec"]) + float(instance["fprec"]))
                                grades_for_subj_and_lvl_by_class_DsFs[this_subj_lvl][course][1] += 1
                            else:
                                # if the course is not in the dict corresponding to the subj and level, initialize them to 
                                # the %As or %Ds and %Fs, and the class count to 1 in their respective dicts
                                grades_for_subj_and_lvl_by_class_As[this_subj_lvl][course] = [float(instance["aprec"]), 1]
                                grades_for_subj_and_lvl_by_class_DsFs[this_subj_lvl][course] = [(float(instance["dprec"]) + float(instance["fprec"])), 1]

        # return the dicts as elements of a list
        return [grades_for_subj_and_lvl_by_class_As, grades_for_subj_and_lvl_by_class_DsFs]
    
    # =================== Graphing Method ======================================================================================
    
    def graph_data(self, category: str, level=None, faculty_only=False, class_count=False) -> None:
        if not level:
            raise TypeError(f"graph_data() method missing 1 keyword argument: level.")
        if not category:
            raise TypeError(f"graph_data() method missing 1 positional argument: category")
        if not isinstance(category, str):
            raise TypeError("category positional argument should be a string.")
        if not isinstance(level, str):
            raise TypeError("level positional argument should be a string.")
        if not level in set(['100', '200', '300', '400', '500', '600']):
            raise AttributeError(f"level {level} is not an appropriate level")
        
        category += str(level)
        try:
            course_data_dict_As = self._Grapher__As_data[category]
            course_data_dict_DsFs = self._Grapher__DsFs_data[category]
            
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
        ax.set_title(f"{category.rstrip(level)} {level}-level", fontweight='bold')
        ax.set_xlabel(f"{'Class' if not faculty_only else 'Class (faculty only)'}", fontweight='bold')
        ax.set_ylabel("%\nAs", rotation=0, labelpad=10, fontweight='bold')
        for side in ["top", "right"]:
            ax.spines[side].set_visible(False)
        
        plt.savefig('As_graph.jpg')

        course_profs_list_DsFs = [f"({item[1][1]}) {item[0]}" if class_count else item[0] for item in course_data_list_DsFs]
        course_grades_list_DsFs = [round(item[1][0]/item[1][1]) for item in course_data_list_DsFs]

        fig, ax = plt.subplots(figsize=(15,10))

        ax.bar(course_profs_list_DsFs, course_grades_list_DsFs, color='red')

        ax.set_title(f"All {category.rstrip(level)} {level}-level", fontweight='bold')
        ax.set_xlabel(f"{'Class' if not faculty_only else 'Class (faculty only)'}", fontweight='bold')
        ax.set_xticklabels(course_profs_list_DsFs, fontsize=5, rotation=45)
        ax.set_ylabel("%\nDsFs", rotation=0, labelpad=10, fontweight='bold')
        for side in ["top", "right"]:
            ax.spines[side].set_visible(False)
        
        plt.savefig('DsFs_graph.jpg')

        return   