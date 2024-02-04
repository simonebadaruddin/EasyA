"""
Administrator tool for updating data and checking for validity of the data and 
discrepencies between the names in the data and names in the web-scraped faculty list"""

from data_maintainer import Data_Maintainer
import json
def main():
    DM = Data_Maintainer()
    DM.update_grade_data()
    DM.discrepancy_search()

    with open("faculty_list.json", "r") as file:
        faculty = json.load(file)
        
    flipped_faculty = []
    for instructor in faculty:
        

if __name__ == '__main__':
    main()


