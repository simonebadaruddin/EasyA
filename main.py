"""Practice for helping group with project 1 in cs 422"""


import json
    

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
    # natty_science_depts (set{str}): set of all the course codes for the departments in the natural science department
    natty_science_depts = set([ 'ANTH', 'ASTR', 'BI', 'CH', 'CIS', 'CIT', 'ERTH', 'ENVS', 
                                'HPHY', 'MATH', 'NEUR', 'PHYS', 'PSY' ])
    # both are sets to make comparision O(1)
    
    ################ CREATE DICT WITH ONLY THE CLASS DATA OF CLASSES IN THE NATURAL SCIENCE DEPARTMENTS ##################################    
    
    # check to make sure the garde data is correct at surface level
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

    ################# PARSE CLASS DATA INTO CATEGORIES BASED ON WHAT SHOULD BE GRAPHED ###################################################
            
    ######### Make dicts for each course; for graphs of instructor x grades for particular dept ##########################################
            
    # grades_for_courses_by_prof_(As/DsFs) (dict{str : dict{str: list[int, int]}): keys are course names; values are dicts.
    # value dicts have instructor names as keys and lists with the first element being the total %As or total %Ds and %Fs, 
    # and the second element being the number of times the instructor taught that course as values
    grades_for_courses_by_prof_As = {}
    grades_for_courses_by_prof_DsFs = {}
    for course in natty_science_courses: # iterate through the courses in natty_science_courses dict
        # initialize the course as a key to an empty dict value
        grades_for_courses_by_prof_As[course] = {}
        grades_for_courses_by_prof_DsFs[course] = {}
        for instance in natty_science_courses[course]: # iterate through the instances in which the class was taught
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


    ######### Make dicts for each department; for graphs of instructor x grades for particular department #######################################
                
    # grades_for_dept_by_prof_(As/DsFs) (dict{str: dict{str: list[int, int]}}): keys are natural science depts represented by 
    # dept code; values are dicts. Nested value dicts have instructor names as keys and lists with the first element being the 
    # total %As or %Ds and %Fs, and the second element being the number of times the instructor taught a course in that dept
    # as values
    grades_for_dept_by_prof_As = {}
    grades_for_dept_by_prof_DsFs = {}
    for dept in natty_science_depts: # initialize each department key to an empty dict value
        grades_for_dept_by_prof_As[dept] = {}
        grades_for_dept_by_prof_DsFs[dept] = {}
    for course in natty_science_courses: # iterate through the natural science courses
        # depts (list[str]): list of the natural science departments that a course is in
        depts = [dept for dept in natty_science_depts if dept in course] # finds all natural science depts a course is in
        if len(depts) == 1: # check if the course only falls under one department in the natural sciences
            # this_dept (str): the department in the natural sciences that the course falls under
            this_dept = depts[0] 
            # check if the department code is in the course code
            for instance in natty_science_courses[course]: # if it is, iterate through the class instances for the course
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
        
    ######### Make dicts for each level by department; for graphs instructor x grades for particular dept course level ################################
            
    # grades_for_dept_and_lvl_by_prof_(As/DsFs) (dict{str: dict{str: list[int, int]}}): keys are natural science depts and level
    # represented by dept code concatenated with a level 100-600; values are dicts. Nested value dicts have instructor names
    # as keys and lists with the first element being the total %As or %Ds and %Fs for the class instances the instructor has 
    # taught in that dept at that level and the second element being the number of instances that instructor taught as values
    grades_for_dept_and_lvl_by_prof_As = {}
    grades_for_dept_and_lvl_by_prof_DsFs = {}
    # levels (list[str]): a list of the course levels 100 through 600 as strings
    levels = ['100', '200', '300', '400', '500', '600']
    # dept_levels (list[str]): a list of the departments concatenated with each level in levels
    dept_levels = [dept+lvl for dept in natty_science_depts for lvl in levels]
    for dept_lvl in dept_levels:
        # initialize the dicts with strings from depts_levels as keys and empty dicts as values
        grades_for_dept_and_lvl_by_prof_As[dept_lvl] = {}
        grades_for_dept_and_lvl_by_prof_DsFs[dept_lvl] = {}
    for course in natty_science_courses: # iterate through the courses in the natural science dept
        for dept in natty_science_depts: # iterate through the depts in the natural sciences
            if dept in course: # check if the dept string is a substring of the course name
                for dept_lvl in dept_levels: # iterate through the dept-level strings in dept_levels
                    if dept_lvl[:len(dept)+1] in course: # check if the dept-level substring, dept concatenated with the
                        # first number of the level, is a substring in the course code
                        for instance in natty_science_courses[course]: # if it is, iterate through the class instances for that course
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


    ######## Make dicts for each level by department; for graphs of class x grades for particular dept course level ##############################
            
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
    for course in natty_science_courses: # iterate through the natural science courses
        for dept in natty_science_depts: # iterate through the natural science departments
            if dept in course: # check if the course is in the department
                for dept_lvl in dept_levels: # iterate through the dept-lvl strings in dept_level
                    if dept_lvl[:len(dept)+1] in course: # check if the dept-lvl substring, dept  concatenated with the 
                        # first number of the level, is a substring in the course code
                        for instance in natty_science_courses[course]: # if it is, iterate through the class insatnces for that course
                            if course in grades_for_dept_and_lvl_by_class_As[dept_lvl]:
                                # if the course is already in the dict corresponding to its dept and level, add the %As or
                                # %Ds and %Fs to the respective dicts and increment the class count
                                grades_for_dept_and_lvl_by_class_As[dept_lvl][course][0] += float(instance["aprec"])
                                grades_for_dept_and_lvl_by_class_As[dept_lvl][course][1] += 1
                                grades_for_dept_and_lvl_by_class_DsFs[dept_lvl][course][0] += (float(instance["dprec"]) + float(instance["fprec"]))
                                grades_for_dept_and_lvl_by_class_DsFs[dept_lvl][course][1] += 1
                            else:
                                # if the course is not in the dict corresponding to the dept and level, initialize them to 
                                # the %As or %Ds and %Fs, and the class count to 1 in their respective dicts
                                grades_for_dept_and_lvl_by_class_As[dept_lvl][course] = [float(instance["aprec"]), 1]
                                grades_for_dept_and_lvl_by_class_DsFs[dept_lvl][course] = [(float(instance["dprec"]) + float(instance["fprec"])), 1]
                        break
                break


if __name__ == '__main__':
    main()
