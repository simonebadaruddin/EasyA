import pytest
from Grade_grapher import (Grapher, Subjs_And_Level_by_Class_Grapher, Subjs_And_Level_By_Prof_Grapher,
                             Courses_By_Prof_Grapher, Subjs_By_Prof_Grapher)
from data_maintainer import Data_Maintainer
from WebScraper import return_faculty_list


def test_instances():
    # faculty = return_faculty_list()
    faculty = ["micheal"]

    DM = Data_Maintainer()
    DM.update_grade_data()
    course_data = DM.get_grade_data()

    obj1 = Courses_By_Prof_Grapher(course_data, faculty)
    assert isinstance(obj1, Courses_By_Prof_Grapher)
    As_data = obj1.get_As_data()
    assert isinstance(As_data, dict)

    obj2 = Subjs_By_Prof_Grapher(course_data, faculty)
    assert isinstance(obj2, Subjs_By_Prof_Grapher)