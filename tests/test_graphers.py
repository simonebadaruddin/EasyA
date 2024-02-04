import pytest
# from Grade_grapher import (Grapher, Subjs_And_Level_by_Class_Grapher, Subjs_And_Level_By_Prof_Grapher,
#                              Courses_By_Prof_Grapher, Subjs_By_Prof_Grapher)
# from data_maintainer import Data_Maintainer
# import json
from WebScraper import return_faculty_list


def test_instances():
    # change class count to get the class count or not during testing
    # class_count = True
    # faculty_only = True
    
    faculty_list = return_faculty_list()
    print(faculty_list)
    
    assert False
    
    
    # faculty = ["Arbo, Matthew David"]


    # # faculty = return_faculty_list()

    # DM = Data_Maintainer()
    # DM.update_grade_data()
    # course_data = DM.get_grade_data()

    # obj1 = Courses_By_Prof_Grapher(course_data, faculty, faculty_only=faculty_only)
    # assert isinstance(obj1, Courses_By_Prof_Grapher)
    # As_data = obj1.get_As_data()
    # # print(As_data)
    # DsFs_data = obj1.get_DsFs_data()
    # # print(DsFs_data)
    # obj1.graph_data('MATH111', class_count=class_count, faculty_only=faculty_only)

    # assert False

    # obj2 = Subjs_By_Prof_Grapher(course_data, faculty)
    # assert isinstance(obj2, Subjs_By_Prof_Grapher)
    # As_data = obj2.get_As_data()
    # # print(As_data)
    # DsFs_data = obj2.get_DsFs_data()
    # # print(DsFs_data)
    # # obj2.graph_data('PSY', class_count=class_count)

    # obj3 = Subjs_And_Level_By_Prof_Grapher(course_data, faculty)
    # assert isinstance(obj3, Subjs_And_Level_By_Prof_Grapher)
    # As_data = obj3.get_As_data()
    # # print(As_data)
    # DsFs_data = obj3.get_DsFs_data()
    # # print(DsFs_data)
    # # obj3.graph_data('CPSY', level='100', class_count=class_count)

    # obj4 = Subjs_And_Level_by_Class_Grapher(course_data, faculty)
    # assert isinstance(obj4, Subjs_And_Level_by_Class_Grapher)
    # As_data = obj4.get_As_data()
    # # print(As_data)
    # DsFs_data = obj4.get_DsFs_data()
    # # print(DsFs_data)
    # # obj4.graph_data('CPSY', level='100', class_count=class_count)
    
    # # for visual inspection of the parced data, uncomment the print statement corresponding to 
    # # it and the assertion below:
    # # assert False
