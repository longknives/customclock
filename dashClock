from tkinter import *
from tkinter.ttk import*
from time import strftime
import requests
from datetime import date
from threading import Timer
import time
from tkinter.constants import COMMAND, END, FALSE
import urllib.request as urllib2
import tkinter as tk
from tkinter import ttk
import time as t
from tkinter import messagebox
import googlesearch
import webbrowser
from bs4 import BeautifulSoup
import re
from urllib.request import url2pathname
from urllib.request import url2pathname
import urllib
import urllib3
import pyautogui
import requests
import datetime
from tkinter import messagebox





text_file_title = open('title.txt', "r")

title = text_file_title.readline()

text_file_title.close()

text_file_background = open('background.txt', "r")

backgroundcolor = text_file_background.readline()

text_file_background.close()

text_file_textcolor = open('textcolor.txt', "r")

textcolor = text_file_textcolor.readline()

text_file_textcolor.close()

text_file_font = open('font.txt', "r")

font1 = text_file_font.readline()

text_file_font.close()

text_file_time = open('time.txt', "r")

time1 = text_file_time.readline()

text_file_time.close()


text_file_default = open('timedefault.txt', "r")

time2 = text_file_default.readline()

text_file_default.close()








root = Tk()
root.title(title)




buttonClicked = 0


def time(buttonClicked):
   if(buttonClicked == 1): 
    
    string = strftime(time1)
    label.config(text= string)
    label.after(1000)
label = Label(root, font=("ds-digital", 80), background= backgroundcolor, foreground= textcolor)
label.pack(anchor='center')



button3 = ttk.Button(root, text = "Custom Clock", command=lambda buttonClicked = 1:time(buttonClicked))

button3.pack(anchor='center')


             

time(buttonClicked)

mainloop()
