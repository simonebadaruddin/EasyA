""" Administrator Module
This file contains methods to update and maintain grade data.

Origninal Author: Erin Cohen
Updated By: --- (enter here if you update)
"""
import json
import re


# ----------- Globals ---------------------
# Initail set of natural sciences
NATURAL_SCIENCES = set([ 'ANTH', 'ASTR', 'BI', 'CH', 'CIS', 'CIT', 'CPSY', 'ERTH', 'ENVS', 
                          'GEOG', 'HPHY', 'MATH', 'NEUR', 'PHYS', 'PSY' ])

# to store grade data as a python dictionary, initially None
GRADE_DATA = None


# ----------- Administrator Functions ---------------------

def update_grade_data(new_data):
    # this function takes a new json data file and stores this data set to be used by the system
    validated_data = validate_data(new_data)

    # if data is found to be invalid, exit
    if validated_data is None:
        return
    #^^^ may not be necesary if the exception exits program and not just the function

    data_dict = nat_sci_filter(validated_data)
    print("Grade Data has been successfully updated.")
    return


# possibly change this to 3 separate functions; add, remove and replace.
# this would be good for ease of administrator use, they do not need to know anything about
# the format of the set or every natural science course code to update/add/remove one code
def set_nat_sci():
    # this function updates the set of natural science course codes
    # ie. updating CIS to CS
    pass




# ----------- Helper Functions ---------------------

def nat_sci_filter(data):
    # this function takes a course data set and removes all course
    # data that does not have a natural science course key
    
    nat_sci_list = get_nat_sci()
    nums = r'[0-9]'

    all_courses_keys = list(data.keys())

    # start with the full list of course keys...
    nat_sci_course_keys = all_courses_keys

    # filter out non-natural science courses.
    for course in all_courses_keys: 
        # remove numbers from the course code
        code = re.sub(nums, '', course)

        # if the course does not contain a course code in the set of natural science course codes...
        a_nat_sci = lambda code, nat_sci_list: any(map(lambda w: w in code, nat_sci_list))
        if not a_nat_sci(code, nat_sci_list):
            # remove the course from the set of natural science courses.
            nat_sci_course_keys.remove(course)

    nat_sci_course_keys = set(nat_sci_course_keys)

    # dictionary to contain all course data of natural science courses
    nat_sci_course_data = {}
    # now copy only courses with a natural science course key to the new dictionary 
    for key in all_courses_keys:
        if key in nat_sci_course_keys:
            nat_sci_course_data[key] = data[key]

    return nat_sci_course_data




def get_nat_sci():
    # this function retrieves the set of natural science course codes
    return NATURAL_SCIENCES

def validate_data(data):
    # this function takes a json file and verifies that it is in the appropriate 
    # format to be used as a data set for the grade data system.
    # If the data is valid, it is return as a string, otherwise an exception is raised.
    try:
        with open(data, 'r') as grade_file:
            # data (str): holds the entire contents of gradedata.json
            data = grade_file.read() # read the file into a python string
            data_dict = json.loads(data) # load the data into a python dictionary
            return data_dict
        
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {data} was not found, upload the file using the admin module to continue.")
    except ValueError:
        raise ValueError(f"The file {data} contains data in an unexpected format.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
