""" Administrator Module
This file contains methods to update and maintain grade data.

Origninal Author: Erin Cohen
Updated By: --- (enter here if you update)
"""
import json
import re

class Data_Maintainer:
<<<<<<< HEAD
    def __init__(self, data_file='gradedata.json'):
        # Initail set of natural sciences
        self.__natural_sciences = set([ 'ANTH', 'ASTR', 'BI', 'CH', 'CIS', 'CIT', 'CPSY', 'ERTH', 'ENVS', 
                                  'GEOG', 'HPHY', 'MATH', 'NEUR', 'PHYS', 'PSY' ])
        # to store the grade data file name
        self.__data_file = data_file
        # to store grade data as a python dictionary
        self.__grade_data = None 
=======
    def init(self): # !!!! added self so I could test
        # ----------- Globals ---------------------
        # Initail set of natural sciences
        self.__NATURAL_SCIENCES = set([ 'ANTH', 'ASTR', 'BI', 'CH', 'CIS', 'CIT', 'CPSY', 'ERTH', 'ENVS', 
                                  'GEOG', 'HPHY', 'MATH', 'NEUR', 'PHYS', 'PSY' ])
        # !!!! for some reason the accessing of this attribute isn't working

        # to store grade data as a python dictionary, initially None
        self.__GRADE_DATA = None
>>>>>>> 21595ade60bb6b381c03c75080173734ef498ba7


    # ----------- Administrator Functions ---------------------

    def update_grade_data(self, new_data_file):
        # this function takes a new json data file and stores this data set to be used by the system
        extracted_data = self.validate_data(new_data_file)
        self.__data_file = new_data_file

        # if data is found to be invalid, exit
        if extracted_data is None:
            return
        #^^^ may not be necesary if the exception exits program and not just the function

        data_dict = self.nat_sci_filter(extracted_data)
        self.__grade_data = data_dict
        print("Grade Data has been successfully updated.")
        return


    # possibly change this to 3 separate functions; add, remove and replace.
    # this would be good for ease of administrator use, they do not need to know anything about
    # the format of the set or every natural science course code to update/add/remove one code
    def set_nat_sci(self, new_set):
        # this function updates the set of natural science course codes
        # ie. updating CIS to CS
        self.__natural_sciences = new_set

    # ----------- Helper methods ---------------------

    def nat_sci_filter(self, data):
        # this function takes a course data set and removes all course
        # data that does not have a natural science course key

        nat_sci_list = self.get_nat_sci() ### !!!! it doesn't like this, i replaced it with the set itself for testing
        nums = r'[0-9]'

        all_courses_keys = list(data.keys())

        # start with the full list of course keys...
        nat_sci_course_keys = all_courses_keys

        # filter out non-natural science courses.
        for course in all_courses_keys: 
            # remove numbers from the course code
            code = re.sub(nums, '', course)

            # if the course does not contain a course code in the set of natural science course codes...
            a_nat_sci = lambda code, nat_sci_list: any(map(lambda w: w == code, nat_sci_list))
            if not a_nat_sci(code, nat_sci_list):
                # remove the course from the set of natural science courses.
                nat_sci_course_keys.remove(course)
<<<<<<< HEAD
            #else:
            #    print(code)
=======
            # !!!! this produces a somewhat filtered list, the 2 letter dept codes mess with it
            # because of the in operator and its testing for substrings 
            # e.g. CH is in CH for chemistry but its also in CHIN for Chinese language and literature
            # I solved this by checking if a 2 letter course code matches, to check that the next
            # character after is a digit e.g. CH101 vs CHIN101, you could check length since you got 
            # rid of the numbers but that may require brute force and at that point youve jumped the shark

>>>>>>> 21595ade60bb6b381c03c75080173734ef498ba7

        nat_sci_course_keys = set(nat_sci_course_keys)

        # dictionary to contain all course data of natural science courses
        nat_sci_course_data = {}
        # now copy only courses with a natural science course key to the new dictionary 
        for key in all_courses_keys:
            if key in nat_sci_course_keys:
                nat_sci_course_data[key] = data[key]

        print(list(nat_sci_course_data.keys()))
        return nat_sci_course_data

    def get_nat_sci(self):
        # this function retrieves the set of natural science course codes
        return self.__natural_sciences

    def get_grade_data(self):
        return self.__grade_data
    
    def get_data_file(self):
        return self.__data_file
    
    def set_data_file(self, new_data_file):
        self.__data_file = new_data_file
    

    def validate_data(self, data):
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
