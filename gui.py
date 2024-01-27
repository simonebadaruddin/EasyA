###
# i get objects from grade_grapher.py
#
#
#     B  P
#     Y  R    - a single class (e.g. Math 111) <--- drop down every single class
#        O    - a single dept (ie math)
#        F    - single dept + level combo (ie math 400 levels)
#        
#      
#     B  C    - a single dept-level combo (ie math 400 levels) 
#     Y  L
#        A
#        S
#        S
# 
# Dropdowns: All individual classes, all departments, all levels, all instructors or faculty only, by class or by prof 
#
# if they leave 
# so i will get the user's choice of what graphs to display?
#
####
import tkinter as tk
from tkinter import *
from tkinter import filedialog # To get the dialog box to open when required 
from PIL import ImageTk, Image # loading Python Imaging Library
import json 
