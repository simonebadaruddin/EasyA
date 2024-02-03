# Web Scraper Documentation

## File Name: faculty_name_finder.py 

### Description
The WebScraper.py scrapes faculty names from 11 different departments. The scraped information is from the WayBack Machine links that contain the department faculty lists. There are three different fuctions doing different parts to make the WebScraper work in full. 

The first fuction is called scrape_faculty_names. This function goes through each url and adds the faculty names to the list. Once all names are added to the list, the list is then returned.

The second function is called save_to_json. This function opens and dumps information into a json file

The third function is called return_faculty_list. This function calls the first function to scrape the faculty names. It uses the returned faculty list and puts that to a json file. Then the faculty list in this function, which is the same one from the first function, is returned.

#### Usage Within the System
The scraper is used for the graph and grade objects can use the faculty names. The administrator handles descrepancies between the provided "gradedata.js" and the web scraped faculty names. In the system, the student is able to choose one of the faculty names based on the subject and class. 


#### Installation Requirements
In the python terminal there are three external libraries to install. Here are the commands that must be ran:

        > - pip install requests (possibly may need to do: py -m pip install reuqests)
        > - pip install html5lib (possibly may need to do: py -m pip install html5lib)
        > - pip install bs4 (possibly may need to do: py -m pip install bs4)
        >
        > (if you are just running this file, once these are installed, it will run without errors)
        >   (these three lines must be uncommented for it to run):
        >        - get_faculty_list = return_faculty_list()
        >        - get_faculty_py_list = get_faculty_as_py_list()
        >        - print(get_faculty_py_list) -- (this line is optional; it prints out the names of the faculty in the terminal)
        >        - print("done") -- (this line is optional it just tells you when it is done running)


#### Running the WebScraper File in another Python File
To run the WebScraper file in another File, here are the lines of code needed:

        > - from faculty_name_finder import return_faculty_list
        > - from faculty_name_finder import get_faculty_as_py_list()
        > - get_faculty_list = return_faculty_list()
        > - get_faculty_py_list = get_faculty_as_py_list()
        > - print(get_faculty_py_list) -- (this line is optional; it prints out the names of the faculty in the terminal)
        > - print('done') -- (this line is optional it just tells you when it is done running)


#### Runtime
The web scraper file takes about two and a half minutes total to run and scrape all 11 departments.

#### When the File is done running (or when the word done is in the terminal) 
Once the file is done running, there should be a json file shown within the files
The optional faculty names and the optional word done should be there too (if those lines of code are in the Python file)

#### Conclusion
Once everything wanted is shown in the output, that means the web scrape was successful.

##### What Exactly is a Web Scraper
A web scraper is a file that fetches information from the web and extracts that information.
