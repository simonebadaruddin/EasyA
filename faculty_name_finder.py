"""
WebScraper: CS 422 Project 1
Author: Isabella Cortez
Credit: YouTube, GeeksforGeeks
This file scrapes faculty names off of the Wayback Machine for 11 different departments
Date Modified: 02/03/2024
"""

# import statements (importing BeautifulSoup Libraries, requests, json and time)
import requests
from bs4 import BeautifulSoup
import json
from time import sleep
import timeit

# subject names set equal to department url from WayBack Machine
bio = "https://web.archive.org/web/20141107201402/http://catalog.uoregon.edu/arts_sciences/biology/#facultytext"
biochem = "https://web.archive.org/web/20141107201414/http://catalog.uoregon.edu/arts_sciences/chemistry/#facultytext"
cis = "https://web.archive.org/web/20141107201434/http://catalog.uoregon.edu/arts_sciences/computerandinfoscience/"
envs = "https://web.archive.org/web/20141107201454/http://catalog.uoregon.edu/arts_sciences/environmentalstudies/#facultytext"
huphys = "https://web.archive.org/web/20141101200118/http://catalog.uoregon.edu/arts_sciences/humanphysiology/"
math = "https://web.archive.org/web/20141028184934/http://catalog.uoregon.edu/arts_sciences/mathematics/"
physics = "https://web.archive.org/web/20141107202155/http://catalog.uoregon.edu/arts_sciences/physics/"
psy = "https://web.archive.org/web/20141107202211/http://catalog.uoregon.edu/arts_sciences/psychology/"
earthsci = "https://web.archive.org/web/20141128094827/http://catalog.uoregon.edu/arts_sciences/geologicalsciences/#facultytext"
anth = "https://web.archive.org/web/20141107201352/http://catalog.uoregon.edu/arts_sciences/anthropology/#facultytext"
geo = "https://web.archive.org/web/20141128094244/http://catalog.uoregon.edu/arts_sciences/geography/#facultytext"

# url set to empty string
url = ""

# url_list is the list of the urls
url_list = [bio, biochem, cis, envs, huphys, math, physics, psy, earthsci, anth, geo]

# subject_list is the list of subjects (I will try to get these to the json file)
subject_list = ['bio', 'biochem', 'cis', 'envs', 'huphys', 'math', 'physics', 'psy', 'earthsci', 'anth', 'geo']

# define function called scrape faculty names
def scrape_faculty_names(u):
    # create empty list to contain department faculty names
    faculty_names = []

    # index: counter variable for how long url_list is
    # go through url_list and scrape depending on what page it is
    for index in range(len(url_list)):
        # wait every 10 seconds to scrape
        sleep(10)

        '''
        time.time()
        timeit.timeit()
        '''

        # url[index]: the url depending on what number index is
        # url is set equal to the url[index] (each time it runs through)
        url = url_list[index]

        # request: get request to specific url link
        request = requests.get(url)

        # BeautSoup: set it to html5
        BeautSoup = BeautifulSoup(request.content, 'html5lib')

        # data: look for faculty text container in
        data = BeautSoup.find(id='facultytextcontainer')

        # create empty professor data lists
        faculty_list = []
        courtesy_list = []
        emeriti_list = []
        ss_list = []
        pf_list = []

        # strings within the websites to look for
        # start: string to find is Faculty
        start = BeautSoup.find('h3', string="Faculty")
        # middle_part1: string to find is Courtesy
        middle_part1 = BeautSoup.find('h3', string="Courtesy")
        # middle_part2: string to find is Special Staff
        middle_part2 = BeautSoup.find('h3', string="Special Staff")
        # end: string to find is Emeriti
        end = BeautSoup.find('h3', string="Emeriti")
        # last_sentence: string to find is the date in... sentence
        last_sentence = BeautSoup.find('p', string="The date in parentheses at the end of each entry is the first year on the University of Oregon faculty.")

        # find urls in list 
        # looking for url in position 2 (cis), 7 (psy), 9 (anth)
        # list is zero indexed
        if url == url_list[2] or url == url_list[7] or url == url_list[9]:
            # facultyNames: look for the word Faculty and anything strings underneath it
            for facultyNames in data.find(string='Faculty').parent.find_next_siblings():
                # if the string is equal to end (Emeriti)
                if facultyNames == end:
                    # stop looking for strings if equal to end
                    break
                else:
                    # set faculty equal to text of faculty names
                    # split the faculty information up with a comma (,)
                    # [0]: keep the first, last names of Faculty
                    faculty = facultyNames.get_text().split(',')[0]

                    # add the faculty names to faculty_list
                    faculty_list.append(faculty)

        # find urls in list 
        # looking for url in position 3 (envs)
        # list is zero indexed
        if url == url_list[3]:
            # facultyNames: look for the word Faculty and anything strings underneath it
            for facultyNames in data.find(string='Faculty').parent.find_next_siblings():
                # if the string is equal to last_sentence (The data in...)
                if facultyNames == last_sentence:
                    # stop looking for strings if equal to last_sentence
                    break
                else:
                    # set faculty equal to text of faculty names
                    # split the faculty information up with a comma (,)
                    # [0]: keep the first, last names of Faculty
                    faculty = facultyNames.get_text().split(',')[0]

                    # add the faculty names to faculty_list
                    faculty_list.append(faculty)

        # find urls in list 
        # looking for url in position 0 (bio), 4 (huphys), 5 (math), 8 (earthsci)
        # list is zero indexed
        if url == url_list[0] or url == url_list[4] or url == url_list[5] or url == url_list[8]:
            # facultyNames: look for the word Faculty and anything strings underneath it
            for facultyNames in data.find(string='Faculty').parent.find_next_siblings():
                # if the string is equal to middle_part1 (Courtesy)
                if facultyNames == middle_part1:
                    # stop looking for strings if equal to middle_part1
                    break
                else:
                    # set faculty equal to text of faculty names
                    # split the faculty information up with a comma (,)
                    # [0]: keep the first, last names of Faculty
                    faculty = facultyNames.get_text().split(',')[0]

                    # add the faculty names to faculty_list
                    faculty_list.append(faculty)

        # find urls in list 
        # looking for url in position 1 (biochem), 6 (physics), 10 (geo)
        # list is zero indexed
        if url == url_list[1] or url == url_list[6] or url == url_list[10]:
            # facultyNames: look for the word Faculty and anything strings underneath it
            for facultyNames in data.find(string='Faculty').parent.find_next_siblings():
                # if the string is equal to middle_part2 (Special Staff)
                if facultyNames == middle_part2:
                    # stop looking for strings if equal to middle_part2
                    break
                else:
                    # set faculty equal to text of faculty names
                    # split the faculty information up with a comma (,)
                    # [0]: keep the first, last names of Faculty
                    faculty = facultyNames.get_text().split(',')[0]

                    # add the faculty names to faculty_list
                    faculty_list.append(faculty)

        # Add faculty names to the overall list
        faculty_names.extend(faculty_list)

    # return faculty names
    return faculty_names

# define function save_to_json
def save_to_json(data, filename='faculty_list.json'):
    # create and open json file up
    with open(filename, 'w', encoding='utf-8') as json_file:
        # dump faculty information to json file
        json.dump(data, json_file, ensure_ascii=False, indent=4)

# define function return_faculty_list
def return_faculty_list():
    # use the same url_list as defined above (to loop through)
    url_list = [bio, biochem, cis, envs, huphys, math, physics, psy, earthsci, anth, geo]
    # faculty_list: calls the scrape_faculty_names function (uses url_list and goes through tht list in the scrape_faculty_names)
    faculty_list = scrape_faculty_names(url_list)
    # call save_to_json function -> use faculty_list
    save_to_json(faculty_list)
    # returns faculty_list
    return faculty_list

# define function get_faculty_as_py_list
def get_faculty_as_py_list():
    # opens the json file (faculty_list.json)
    with open('faculty_list.json', 'r') as f:
        # sets the faculty list to json.loads
        scraped_faculty_list = json.loads(f.read())
    # returns list as python list
    return scraped_faculty_list

# print(get_faculty_as_py_list())
# print(type(get_faculty_as_py_list()))
# get_faculty_list = return_faculty_list()
# print(get_faculty_list)
# print("done")




