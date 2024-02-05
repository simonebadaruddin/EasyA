# Instructions for EasyA User System
## Project 1 for CS422, Winter 2024
### Written by Luke Marshall 2/4/2024

## Dependencies

The local dependencies include the `EasyA_application.py`, `data_maintainer.py`, and `Grade_grapher.py` files that should be in the `application` directory. If those files are not included in the downloaded package, please re-download the package and see that they are included.

The modules are only guaranteed to work if using Python versions 3.10-3.12.

NOTE: below you are instructed to use the `pip` command. If you are getting an error when this is attempted, you may need to use `pip3` in its place.

### The `EasyA_application.py` file includes its own dependencies that must be accounted for:

It is necessary to check for required libraries in the directory and install them if they are not found. Make sure you are in your terminal, in the `application` directory. 

1. The EasyA application file requires the use of a tk interface to create the user interface, the tkinter library is used to do this:
    - tkinter, which is used for this purpose, is part of the Python standard library and does not usually need to be installed
    - If you are using a Mac and the tkinter library is installed, but the application does not run, try using `brew install python-tk` in your terminal.

2. The EasyA application file requires the use of json file functionality to access the faculty list, the json library is used to do this:
    - Type `pip show json` into the command line of the terminal and hit enter.
    - If nothing appears, use `pip install json` to install the json library.

3. The EasyA application requires the use of image functionality to open graph images after they have been created, the pillow library is used for this purpose.
    - Type `pip show Pillow` into the command line of the terminal and hit enter.
    - If nothing appears, use `pip install Pillow` to install the json library.

### The `Grade_grapher.py` file includes its own dependencies that must be accounted for

It is necessary to check for required libraries in the directory and install them if they are not found. Make sure you are in your terminal, in the `application` directory.

1. The `Grade_grapher.py` file requires the use of graphing capabilies to create and produce the graphs, the matplotlib library is used for this purpose
    - Type `pip show matplotplib` into the command line of the terminal and hit enter.
    - If nothing appears, use `pip install matplotlib` to install the json library.

### The `data_maintainer.py` file includes its own dependencies that must be accounted for:

It is necessary to check for required libraries in the directory and install them if they are not found. Make sure you are in your terminal, in the `application` directory. 

1. The data maintainer file requires the use of regular expressions to filter the grade data for the data that is related to the natural science departments, the re library is used to do this:
    - Type `pip show re` into the command line of the terminal and hit enter.
    - If nothing appears, use `pip install re` to install the regex library.

2. The data maintainer file requires the use of json file functionality to access the grade data and the faculty list, the json library is used to do this:
    - Type `pip show json` into the command line of the terminal and hit enter.
    - If nothing appears, use `pip install json` to install the json library.

3. The data maintainer file requires the use of a similarity checker when comparing faculty names found via web scraping and the names in the filtered grade data:
    - difflib, which is used for this purpose, is part of the Python standard library and does not need to be installed.

## Usage 
After the dependencies have all been downloaded, the EasyA application may be initialized. In order to do so, make sure you are in your terminal in the `EasyA/application` directory.

1. First, type `Python EasyA_application.py` into the terminal. If an error comes up, you might try using `Python3` in your command instead. At this point the EasyA interface should appear on the screen as it is in the image below. 

![EasyA tkinter interface](./EasyA_interface.png)
If the interface opens and you do not see the `Plot Graph` and `Exit` buttons at the botton of the interface, use your mouse to click and drag one of the corners down to reveal what is hidden.


