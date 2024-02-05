""" Administrator Module
This file contains methods to update and maintain grade data.

Origninal Author: Erin Cohen
"""
import json
import re
from difflib import SequenceMatcher as sm
from difflib import get_close_matches 

class Data_Maintainer:
    def __init__(self, data_file='gradedata.json'):
        # Initial set of natural sciences
        self.__natural_sciences = set([ 'ANTH', 'ASTR', 'BI', 'BIOE', 'CH', 'CIS', 'CIT', 'CPSY', 'DSCI', 'ERTH', 'ENVS', 
                                        'GEOG', 'HPHY', 'MATH', 'NEUR', 'PHYS', 'PSY', 'SPSY', 'STAT' ])
        # to store the grade data file name
        self.__data_file = data_file
        # to store grade data as a python dictionary
        self.__grade_data = None 


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

    def discrepancy_search(self, scraped_faculty_list):
        """ Compare the given list of names and the faculty in data set and search for any pairs of names that are 
            very similar but not identical. Return the resulting list of name close matches so an administrator
            can see any potential discrepencies that should be handled."""

        # Create a list of just the instructor names in the grade data
        instructors = self.get_grade_data_instructors()
     
        # Create a list of similar name pairs
        similar_name_pairs = []
        for name in scraped_faculty_list:
            # check for names with 80% or greater similarity
            close_matches = get_close_matches(name, instructors, cutoff=.8)
            # remove any exact matches in close matches
            close_matches = list(set(close_matches))  
            # !!! can replace with:
            # if name in close_matches:
                # close_matches.remove(name) 
            for n in close_matches:
                if n == name:
                    close_matches.remove(n)         
            # if there are any close matches to this name, (besides an exact match)
            # add them to the list
            if len(close_matches) > 1:
                    similar_name_pairs.append({name:close_matches})
        
        # Display the list of possible duplicates
        print("\n-------------------------------------------------")
        print("Faculty in scraped list : Potential duplicate names in grade data")
        print("-------------------------------------------------")
        for name in similar_name_pairs:
            print(name)
        print("-------------------------------------------------\n")

    def replace_faculty_name(self, name_to_replace, new_name):
        """ Alter __grade_data to replace a current name representation to
            a representation consistent with scraped data"""
        try: 
            for course in self.__grade_data:
                term = len(self.__grade_data[course])   
                # for each term of grade data for this course             
                for i in range(term-1): 
                    instructor = self.__grade_data[course][i]["instructor"]
                    if instructor == name_to_replace:
                        old_name = instructor
                        self.__grade_data[course][i]["instructor"] =  new_name
                        updated_name = self.__grade_data[course][i]["instructor"]
            # Todo:
            # update the grade_data file itself
            
            print("\nSuccess: Stored grade data has been changed.")
            print(f"'{old_name}' has been replaced with '{updated_name}' in stored grade data.\n")
        
        except:
            print("\nError: Entered names are not in the expected form, please correct and try again.")
            print("Recall: \n    arg1: name as it exists in grade data \n    arg2: name to replace it with")
            print("No changes have been made.\n")
        

    # ----------- Helper methods ---------------------

    def get_grade_data_instructors(self):
        """ Return a list of the instructors stored in grade data
         with names in the form : "First Middle Last" (if there is a middle)"""
        instructors = []
        for course in self.__grade_data:
            term = len(course[0]) # the number of terms stored in this course data set
            for i in range(term-1):
                # for each term of grade data for this course
                instructor = self.__grade_data[course][i]["instructor"]
                # The data has names stored as "Last, First middle" (if there is a middle)
                # so we need to change it to the form "First middle Last" (if there is a middle)
                if "," in instructor: # split the strings into first and last name
                    instructor = instructor.split(", ") 
                    instructor = f"{instructor[1]} {instructor[0]}" # I think this may rearrange names so theyre middle name or initial 
                    # first followed by first name and last name
                    instructors.append(instructor)
                    # add each name to the list 
                else: # otherwise append the single name
                    instructors.append(instructor)
        return instructors

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
