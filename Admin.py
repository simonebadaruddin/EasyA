"""
Administrator tool for updating data and checking for validity of the data and 
discrepencies between the names in the data and names in the web-scraped faculty list"""

from data_maintainer import Data_Maintainer
def main():
    DM = Data_Maintainer()
    DM.update_grade_data()
    DM.discrepancy_search()
    # DM.get_faculty_list() : retreive the new faculty list

if __name__ == '__main__':
    main()


