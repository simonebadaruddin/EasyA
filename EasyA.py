"""Code module for CS 422 project 1"""

import data_maintainer


def new_main():
    """

    """
    grade_data_obj = data_maintainer.Data_Maintainer()
    grade_data = grade_data_obj.get_grade_data()
    # if there is no stored grade data, check for local 'gradedata.json' file
    if grade_data is None:
        # default, use local 'gradedata.json'
        grade_data_obj.update_grade_data('gradedata.json')
    else:
        # otherwise, grade data has already been stored/updated.

        """
        when initializing an object, each can be given a names list to restrict the names that will be shown 
        on the graph, if a names list is not given, one is made from all  the names in the grade data. 
        a faculty_only boolean keyword argument can be further used to restrict those shown from the names list
        to just regular faculty
        if input has specific class:
            initialize courses_by_prof_grapher object
        if input has specific class code:
            inititalize subjs_by_prof_grapher object
        if input has specific subject AND specific level AND user wants it categorized by instructor:
            initialize subjs_and_level_by_prof object
        if input has specific subject AND specific level AND user wants it categorized by grade:
            initialize subjs_and_level_by_class object
            
        call graphing method on object initialized, giving appropriate arguments for its graph type"""
        
        #######
        # Setup done.
        # Now do graphing stuff!
        ######
        
        return