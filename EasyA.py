"""Code module for CS 422 project 1"""

import json
import data_maintainer


def new_main():
    """ Erin:
    with the new data_maintainer file, there is a lot of code repetition here 
    and I think this "new_main" could replace main if it sounds good, or we
    can integrate the two some other way. Let me know your thoughts!

    thoughts: if it ends up working, sounds good. while the functional programming with lambdas,
    filter, and mapping along with regex is cool, I dont know if theres a way to implement it 
    without another check in there for the two letter course codes, and at that point it most 
    likely becomes larger and less efficient than brute force. If you can get it to work in a
    a couple more tries then great, otherwise i'd just stick with the one written in old main.

    the admin functionality needs a way to fix any discrepencies between the faculty list
    and the instructor names in the grade data e.g. a prompt that says 'these names in the 
    faculty list are not in the grade data:'

    The admin functionality needs a way for the admin to quickly and easily replace the data, either
    by inputting a json object and the program writing it into the gradedata file or inputting
    a json file and the program writing its data into the gradedata file. either way validation 
    needs to occur before the overwriting happens.

    """
    grade_data_obj = data_maintainer.Data_Maintainer()
    grade_data = grade_data_obj.get_grade_data()
    # if there is no stored grade data, check for local 'gradedata.json' file
    if grade_data is None:
        # default, use local 'gradedata.json'
        data_maintainer.update_grade_data('gradedata.json')
    else:
        # otherwise, grade data has already been stored/updated.
        return

    pass

def main():

    ####################### READ 'gradedata.json' FILE ###########################################################################

    # open the gradedata.js file
    try:
        with open('gradedata.json', 'r') as grade_file:
            # data (str): holds the entire contents of gradedata.json
            data = grade_file.read() # read the file into a python string
            grade_data = json.loads(data) # load the data from gradedata.json into a python dict
    except FileNotFoundError:
        raise FileNotFoundError("The file gradedata.json was not found, upload the file using the admin module to continue.")
    except ValueError:
        raise ValueError("The file gradedata.json contains data in an unexpected format.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
   ####################### CREATE SETS OF CLASSES AND DEPARTMENTS IN THE NATURAL SCIENCES ##########################################
        
    # natty_sciences (set{str}): set of the course codes for courses in the natural sciences department
    natty_sciences = set([ 'ANTH', 'ASTR', 'BI', 'CH', 'CIS', 'CIT', 'CPSY', 'ERTH', 'ENVS', 
                          'GEOG', 'HPHY', 'MATH', 'NEUR', 'PHYS', 'PSY' ])
    
    ################ CREATE DICT WITH ONLY THE CLASS DATA OF CLASSES IN THE NATURAL SCIENCE DEPARTMENTS ##################################    
    ###### passed as argument to Grapher objects during construction ##############

    # check to make sure the grade data is correct at surface level
    if not isinstance(grade_data, dict):
        raise ValueError("The data from gradedata.json was incorrectly loaded.")
    
    # all courses (list): list of all the courses within the data set
    all_courses = list(grade_data.keys())
    # natty_science_courses (list[str]): list of only the courses in the data set which are also in the natural science courses
    natty_science_course_names = all_courses.copy() # copy all courses list
    for clas in all_courses: # iterate through all_courses list
        if (clas[:2] not in natty_sciences) and (clas[:3] not in natty_sciences) and (clas[:4] not in natty_sciences):
            # check if the class code for the class is one in the natural sciences; if it isn't,
            # remove it from natty_science_courses
            natty_science_course_names.remove(clas)
        if (clas[:2] in natty_sciences) and (not clas[2].isdigit()):
            # double check the ones which match by their first 2 characters only have 2 characters in their class codes
            natty_science_course_names.remove(clas)

    # Make natty_science_course_names a set so that comparing to them is O(1)
    natty_science_course_names = set(natty_science_course_names)

    # natty_science_courses (dict{str: list[dict{str, str}]}): a subdict of the original grade_data dict that only contains
    # the data for the courses in the natural sciences
    natty_science_courses = {}
    for course in all_courses: # iterate through the keys in the all_courses dict
        if course in natty_science_course_names: # check if the key (course) is in the course names for all the courses in
            # the natural science dept; if it is, add it to the natty_science_courses dict
            natty_science_courses[course] = grade_data[course]