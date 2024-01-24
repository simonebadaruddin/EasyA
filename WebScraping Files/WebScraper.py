# what to import
import requests
from bs4 import BeautifulSoup
import csv
import time

# urls defined by subjects
bio = "https://web.archive.org/web/20141107201402/http://catalog.uoregon.edu/arts_sciences/biology/#facultytext"
biochem = "https://web.archive.org/web/20141107201414/http://catalog.uoregon.edu/arts_sciences/chemistry/#facultytext"
cis = "https://web.archive.org/web/20141107201434/http://catalog.uoregon.edu/arts_sciences/computerandinfoscience/"
envs = "https://web.archive.org/web/20141107201454/http://catalog.uoregon.edu/arts_sciences/environmentalstudies/#facultytext"
huphys = "https://web.archive.org/web/20141101200118/http://catalog.uoregon.edu/arts_sciences/humanphysiology/"
math = "https://web.archive.org/web/20141028184934/http://catalog.uoregon.edu/arts_sciences/mathematics/"
physics = "https://web.archive.org/web/20141107202155/http://catalog.uoregon.edu/arts_sciences/physics/"
psy = "https://web.archive.org/web/20141107202211/http://catalog.uoregon.edu/arts_sciences/psychology/"
neuro = "https://web.archive.org/web/20141107202132/http://catalog.uoregon.edu/arts_sciences/neuroscience/"
earthsci = "https://web.archive.org/web/20141128094827/http://catalog.uoregon.edu/arts_sciences/geologicalsciences/#facultytext"
anth = "https://web.archive.org/web/20141107201352/http://catalog.uoregon.edu/arts_sciences/anthropology/#facultytext"
geo = "https://web.archive.org/web/20141128094244/http://catalog.uoregon.edu/arts_sciences/geography/#facultytext"

# url set to empty string
url = ""

# two lists, one with urls and one with subject names (as strings)
url_list = [bio, biochem, cis, envs, huphys, math, physics, psy, neuro, earthsci, anth, geo]
subject_list = ['bio', 'biochem', 'cis', 'envs', 'huphys', 'math', 'physics', 'psy', 'neuro', 'earthsci', 'anth', 'geo']

# open csv file
with open('professorData.csv', mode='w', newline='', encoding='utf-8') as file:
    # write in csv file
    writer = csv.writer(file)

    # csv headers for the rows
    writer.writerow(['Faculty', '', '', 'Emeriti', '', '', 'Courtesy', '', '', 'Special Staff', '', '', 'Participating Faculty'])  # Header row

    # go through the url list
    for index in range(len(url_list)):
        # time it
        time.time()

        # url is set equal to the index (each time it runs through)
        url = url_list[index]
        request = requests.get(url)
        BeautSoup = BeautifulSoup(request.content, 'html5lib')

        # look for faculty text
        data = BeautSoup.find(id='facultytextcontainer')

        # create professor data lists
        faculty_list = []
        courtesy_list = []
        emeriti_list = []
        ss_list = []
        pf_list = []

        # strings to look for
        start = BeautSoup.find('h3', string="Faculty")
        middle_part1 = BeautSoup.find('h3', string = "Courtesy")
        middle_part2 = BeautSoup.find('h3', string = "Special Staff")
        end = BeautSoup.find('h3', string="Emeriti")

        last_sentence = BeautSoup.find('p', string="The date in parentheses at the end of each entry is the first year on the University of Oregon faculty.")

        # urls in list to look for
        if url == url_list[2] or url == url_list[7] or url == url_list[10]:
            # generate faculty list
            for facultyNames in data.find(string='Faculty').parent.find_next_siblings():
                if facultyNames == end:
                    break
                else:
                    faculty = facultyNames.get_text().split(',')[0] + " = " + subject_list[index]
                    faculty_list.append(faculty)

            # generate emeriti list
            for emeritiNames in data.find(string='Emeriti').parent.find_next_siblings():
                if emeritiNames == last_sentence:
                    break
                else:
                    emeriti = emeritiNames.get_text().split(',')[0] + " = " + subject_list[index]
                    emeriti_list.append(emeriti)

        # url in list to look for
        if url == url_list[3]:
            # generate faculty list
            for facultyNames in data.find(string='Faculty').parent.find_next_siblings():
                if facultyNames == last_sentence:
                    break
                else:
                    faculty = facultyNames.get_text().split(',')[0] + " = " + subject_list[index]
                    faculty_list.append(faculty)

        # urls in list to look for
        if url == url_list[0] or url == url_list[4] or url == url_list[5]:
            # get list of faculty
            for facultyNames in data.find(string='Faculty').parent.find_next_siblings():
                if facultyNames == middle_part1:
                    break
                else:
                    faculty = facultyNames.get_text().split(',')[0] + " = " + subject_list[index]
                    faculty_list.append(faculty)

            # get list of courtesy
            for courtesyNames in data.find(string='Courtesy').parent.find_next_siblings():
                if courtesyNames == end:
                    break
                else:
                    courtesy = courtesyNames.get_text().split(',')[0] + " = " + subject_list[index]
                    courtesy_list.append(courtesy)

            # get list of emeriti
            for emeritiNames in data.find(string='Emeriti').parent.find_next_siblings():
                if emeritiNames == last_sentence:
                    break
                else:
                    emeriti = emeritiNames.get_text().split(',')[0] + " = " + subject_list[index]
                    emeriti_list.append(emeriti)

        # look for urls in list
        if url == url_list[1] or url == url_list[6] or url == url_list[11]:
            # get list of faculty
            for facultyNames in data.find(string='Faculty').parent.find_next_siblings():
                if facultyNames == middle_part2:
                    break
                else:
                    faculty = facultyNames.get_text().split(',')[0] + " = " + subject_list[index]
                    faculty_list.append(faculty)

            # get list of special staff
            for specialNames in data.find(string='Special Staff').parent.find_next_siblings():
                if specialNames == end:
                    break
                else:
                    special = specialNames.get_text().split(',')[0] + " = " + subject_list[index]
                    ss_list.append(special)

            # get list of emeriti
            for emeritiNames in data.find(string='Emeriti').parent.find_next_siblings():
                if emeritiNames == last_sentence:
                    break
                else:
                    emeriti = emeritiNames.get_text().split(',')[0] + " = " + subject_list[index]
                    emeriti_list.append(emeriti)

        # look for url in list
        if url == url_list[8]:
            # get list of participating faculty
            for parFacNames in data.find(string='Participating Faculty').parent.find_next_siblings():
                    participating = parFacNames.get_text().split(',')[0] + " = " + subject_list[index]
                    pf_list.append(participating)

        # look for url in list
        if url == url_list[9]:
            # get list of faculty
            for facultyNames in data.find(string='Faculty').parent.find_next_siblings():
                if facultyNames == middle_part1:
                    break
                else:
                    faculty = facultyNames.get_text().split(',')[0] + " = " + subject_list[index]
                    faculty_list.append(faculty)

            # get list of courtesy
            for courtesyNames in data.find(string='Courtesy').parent.find_next_siblings():
                if courtesyNames == middle_part2:
                    break
                else:
                    courtesy = courtesyNames.get_text().split(',')[0]
                    courtesy_list.append(courtesy)

            # get list of special staff
            for specialNames in data.find(string='Special Staff').parent.find_next_siblings():
                if specialNames == end:
                    break
                else:
                    special = specialNames.get_text().split(',')[0] + " = " + subject_list[index]
                    ss_list.append(special)

            # get list of emeriiti
            for emeritiNames in data.find(string='Emeriti').parent.find_next_siblings():
                if emeritiNames == last_sentence:
                    break
                else:
                    emeriti = emeritiNames.get_text().split(',')[0] + " = " + subject_list[index]
                    emeriti_list.append(emeriti)

        # use the lists
        max_len = max(len(faculty_list), len(emeriti_list), len(courtesy_list), len(ss_list), len(pf_list))

        # go through the range of the length and list professor names
        for i in range(max_len):
            faculty_name = faculty_list[i] if i < len(faculty_list) else ''
            emeriti_name = emeriti_list[i] if i < len(emeriti_list) else ''  
            courtesy_name = courtesy_list[i] if i < len(courtesy_list) else ''
            ss_name = ss_list[i] if i < len(ss_list) else ''
            pf_name = pf_list[i] if i < len(pf_list) else ''
            empty_name = ''
            writer.writerow([faculty_name, empty_name, empty_name, emeriti_name, empty_name, empty_name, courtesy_name, empty_name, empty_name, ss_name, empty_name, empty_name, pf_name])

print("CSV file generated successfully.")