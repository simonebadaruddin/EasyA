""" Administrator Module
This file contains methods to update and maintain grade data.

Origninal Author: Erin Cohen
Updated By: --- (enter here if you update)
"""
import json
import re

class Data_Maintainer:
    def __init__(self, data_file='gradedata.json'):
        # Initial set of natural sciences
        self.__natural_sciences = set([ 'ANTH', 'ASTR', 'BI', 'BIOE', 'CH', 'CIS', 'CIT', 'CPSY', 'DSCI', 'ERTH', 'ENVS', 
                                        'GEOG', 'HPHY', 'MATH', 'NEUR', 'PHYS', 'PSY', 'SPSY', 'STATS' ])
        # to store the grade data file name
        self.__data_file = data_file
        # to store grade data as a python dictionary
        self.__grade_data = None 


    #TODO:
    #  the admin functionality needs a way to fix any discrepencies between the faculty list
    # and the instructor names in the grade data e.g. a prompt that says 'these names in the 
    # faculty list are not in the grade data:'
        """
        When replacing the system data, ideally, discrepancies between names found in
        “gradedata.js” and the names found in the scraped instructor data would be easy to resolve
        using the administrator tools, to ensure that the data in your tables is clean, consistent and
        accurate. (Optionally, as the two sources of data are brought into alignment, the tools could
        generate statistics such as lists of names from both data sources that have yet to find a match,
        so you can see how your data resolving process needs to be further improved.)"""

    # ----------- Administrator Functions ---------------------

    def update_grade_data(self, new_data_file='gradedata.json'):
        # this function takes a new json data file and stores this data to be used by the system
        extracted_data = self.validate_data(new_data_file)
        self.__data_file = new_data_file
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

    def nat_sci_filter(self, all_courses):
        # this function takes a course data python dictionary and 
        # creates a new dictionary of only natural science course data

        # creating a local variable to point to private variable so the lambda can access it later
        nat_sci_set = self.__natural_sciences
        
        # regex for any number
        nums = r'[0-9]'

        # dictionary will store course data for all natural science courses in the given dict
        nat_sci_course_data = {}


        # check every course in the dictionary to see if it is a natural science course
        for course in all_courses: 
            # remove numbers from the course code to compare codes with natural science set
            code = re.sub(nums, '', course)

            # function to check if a course code is a natural science course code
            a_nat_sci = lambda code, nat_sci_set: any(map(lambda w: w == code, nat_sci_set))
            
            # if the course contains a course code in the set of natural science course codes...
            if a_nat_sci(code, nat_sci_set):
                # ... add the course to the dict
                nat_sci_course_data[course] = all_courses[course]
                
            
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
