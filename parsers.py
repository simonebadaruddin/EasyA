

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
    
   ####################### CREATE SETS OF CLASSES AND subjectS IN THE NATURAL SCIENCES ##########################################
        
    # natty_sciences (set{str}): set of the course codes for courses in the natural sciences subject
    natty_sciences = set([ 'ANTH', 'ASTR', 'BI', 'CH', 'CIS', 'CIT', 'CPSY', 'ERTH', 'ENVS', 
                          'GEOG', 'HPHY', 'MATH', 'NEUR', 'PHYS', 'PSY' ])
    # natty_science_subjs (set{str}): set of all the course codes for the subjects in the natural science subject
    natty_science_subjs = set([ 'ANTH', 'ASTR', 'BI', 'CH', 'CIS', 'CIT', 'ERTH', 'ENVS', 
                                'GEOG', 'HPHY', 'MATH', 'NEUR', 'PHYS', 'PSY' ])
    # both are sets to make comparision O(1)
    
    ################ CREATE DICT WITH ONLY THE CLASS DATA OF CLASSES IN THE NATURAL SCIENCE subjectS ##################################    
    
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
    for course in natty_science_course_names: 
            natty_science_courses[course] = grade_data[course]

    ################# PARSE CLASS DATA INTO CATEGORIES BASED ON WHAT SHOULD BE GRAPHED ###################################################
            
    ######### Make dicts for each course; for graphs of instructor x grades for particular subj ##########################################
            
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

    ######### Make dicts for each subject; for graphs of instructor x grades for particular subject #######################################
                
    # grades_for_subj_by_prof_(As/DsFs) (dict{str: dict{str: list[int, int]}}): keys are natural science subjs represented by 
    # subj code; values are dicts. Nested value dicts have instructor names as keys and lists with the first element being the 
    # total %As or %Ds and %Fs, and the second element being the number of times the instructor taught a course in that subj
    # as values
    grades_for_subj_by_prof_As = {}
    grades_for_subj_by_prof_DsFs = {}
    for subj in natty_science_subjs: # initialize each subject key to an empty dict value
        grades_for_subj_by_prof_As[subj] = {}
        grades_for_subj_by_prof_DsFs[subj] = {}
    for course in natty_science_courses: # iterate through the natural science courses
        # subjs (list[str]): list of the natural science subjects that a course is in
        subjs = [subj for subj in natty_science_subjs if subj in course] # finds all natural science subjs a course is in
        if len(subjs) == 1: # check if the course only falls under one subject in the natural sciences
            # this_subj (str): the subject in the natural sciences that the course falls under
            this_subj = subjs[0] 
            # check if the subject code is in the course code
            for instance in natty_science_courses[course]: # if it is, iterate through the class instances for the course
                instructor = instance["instructor"]
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
        elif len(subjs) > 1:
            raise AttributeError(f"A course {course} has been found to fit under more than one subject: {subjs}.")
        
    ######### Make dicts for each level by subject; for graphs instructor x grades for particular subj course level ################################
            
    # grades_for_subj_and_lvl_by_prof_(As/DsFs) (dict{str: dict{str: list[int, int]}}): keys are natural science subjs and level
    # represented by subj code concatenated with a level 100-600; values are dicts. Nested value dicts have instructor names
    # as keys and lists with the first element being the total %As or %Ds and %Fs for the class instances the instructor has 
    # taught in that subj at that level and the second element being the number of instances that instructor taught as values
    grades_for_subj_and_lvl_by_prof_As = {}
    grades_for_subj_and_lvl_by_prof_DsFs = {}
    # levels (list[str]): a list of the course levels 100 through 600 as strings
    levels = ['100', '200', '300', '400', '500', '600']
    # subj_levels (list[str]): a list of the subjects concatenated with each level in levels
    subj_levels = [subj+lvl for subj in natty_science_subjs for lvl in levels]
    for subj_lvl in subj_levels:
        # initialize the dicts with strings from subjs_levels as keys and empty dicts as values
        grades_for_subj_and_lvl_by_prof_As[subj_lvl] = {}
        grades_for_subj_and_lvl_by_prof_DsFs[subj_lvl] = {}
    for course in natty_science_courses: # iterate through the courses in the natural science subj
        subjs = [subj for subj in natty_science_subjs if subj in course] # iterate through the subjs in the natural sciences
        if len(subjs) == 1:
            this_subj = subjs[0]
            subj_lvls = [subj_lvl for subj_lvl in subj_levels if subj_lvl[:len(this_subj)+1] in course] # iterate through the subj-level strings in subj_levels
            if len(subj_lvls) == 1:
                this_subj_lvl = subj_lvls[0]
                # first number of the level, is a substring in the course code
                for instance in natty_science_courses[course]: # if it is, iterate through the class instances for that course
                    instructor = instance["instructor"] # instructor (str): instructor name for the class instance
                    if instructor in grades_for_subj_and_lvl_by_prof_As[this_subj_lvl]:
                        # if the instructor is already in the dict corresponding to the subj and level,add the %As 
                        # or %Ds and %Fs to the respective dicts and increment their class count 
                        grades_for_subj_and_lvl_by_prof_As[this_subj_lvl][instructor][0] += float(instance["aprec"])
                        grades_for_subj_and_lvl_by_prof_As[this_subj_lvl][instructor][1] += 1
                        grades_for_subj_and_lvl_by_prof_DsFs[this_subj_lvl][instructor][0] += (float(instance["dprec"]) + float(instance["fprec"]))
                        grades_for_subj_and_lvl_by_prof_DsFs[this_subj_lvl][instructor][1] += 1
                    else:
                        # if the instructor is not in the dict corresponding to the subj and level, initialize them to 
                        # the %As or %Ds and %Fs, and their class count to 1 in the respective dicts
                        grades_for_subj_and_lvl_by_prof_As[this_subj_lvl][instructor] = [float(instance["aprec"]), 1]
                        grades_for_subj_and_lvl_by_prof_DsFs[this_subj_lvl][instructor] = [(float(instance["dprec"]) + float(instance["fprec"])), 1]
                

    ######## Make dicts for each level by subject; for graphs of class x grades for particular subj course level ##############################
            
    # grades_for_subj_and_lvl_by_class_(As/DsFs) (dict{str: dict{str: list[int, int]}}): keys are natural science subjs and level
    # represented by subj code concatenated with a level 100-600; values are dicts. Nested value dicts have course code
    # as keys and lists with the first element being the total %As or %Ds and %Fs for the class instances for that course 
    # taught in that subj at that level and the second element being the number of instances that course was taught as values
    grades_for_subj_and_lvl_by_class_As = {}
    grades_for_subj_and_lvl_by_class_DsFs = {}
    for subj_lvl in subj_levels:
        # initialize the dicts with strings from subjs_levels as keys and empty dicts as values
        grades_for_subj_and_lvl_by_class_As[subj_lvl] = {}
        grades_for_subj_and_lvl_by_class_DsFs[subj_lvl] = {}
    for course in natty_science_courses: # iterate through the courses in the natural science subj
        subjs = [subj for subj in natty_science_subjs if subj in course] # iterate through the subjs in the natural sciences
        if len(subjs) == 1:
            this_subj = subjs[0]
            subj_lvls = [subj_lvl for subj_lvl in subj_levels if subj_lvl[:len(this_subj)+1] in course] # iterate through the subj-level strings in subj_levels
            if len(subj_lvls) == 1:
                this_subj_lvl = subj_lvls[0]
                # first number of the level, is a substring in the course code
                for instance in natty_science_courses[course]: # if it is, iterate through the class insatnces for that course
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


if __name__ == '__main__':
    main()
