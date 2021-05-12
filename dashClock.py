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
from time import strftime
from tkinter import *
from tkinter.ttk import*
import sys
import os
from tkinter import Tk, Label, Button











window = tk.Tk()




buttonClicked = False
buttonClickedText = False
buttonClickedTitle = False
start = False


date = datetime.datetime.today()

start = False

window.minsize(600,400) 
   

root = Tk()



  

def restart_program():
  
    python = sys.executable
    os.execl(python, python, * sys.argv)



label = ttk.Label(window, text = "To make a new clock, enter your settings, press reset, and click start") 
label.grid(column=10, row=10)
button = ttk.Button(window, text="Reset", command=restart_program)
button.grid(column=10, row=12)


















def gui(buttonClicked, buttonClickedText, buttonClickedTitle, start):

 
 result = name.get()
 resultext = name1.get()
 resulttitle = name2.get()
 
 if(buttonClicked == True):
    
  f = open('background.txt', 'r+')
  f.truncate(0)     
  f.write(result)

 if(buttonClickedText == True):
      f = open('textcolor.txt', 'r+')
      f.truncate(0)     
      f.write(resultext)


 if(buttonClickedTitle == True):
      f = open('title.txt', 'r+')
      f.truncate(0)     
      f.write(resulttitle)
      text12 = f.readlines()







 
 
 




    



   

    
    
button = ttk.Button(window, text = "Enter", command=lambda buttonClicked = True:gui(buttonClicked,buttonClickedText, buttonClickedTitle, start))
             
button.grid(column= 15, row = 1) 


name = tk.StringVar()
nameEntered = ttk.Entry(window, width = 15, textvariable = name)
nameEntered.grid(column = 10, row = 1) 




label = ttk.Label(window, text = "Background Color") 
label.grid(column = 0, row = 1) 

    
button = ttk.Button(window, text = "Enter", command=lambda buttonClickedText = True:gui(buttonClicked,buttonClickedText, buttonClickedTitle, start ))
             
button.grid(column= 15, row = 2) 


name1 = tk.StringVar()
nameEntered1 = ttk.Entry(window, width = 15, textvariable = name1)
nameEntered1.grid(column = 10, row = 2) 




label = ttk.Label(window, text = "Title") 
label.grid(column = 0, row = 3) 

button = ttk.Button(window, text = "Enter", command=lambda buttonClickedTitle = True:gui(buttonClicked,buttonClickedText , buttonClickedTitle, start))
             
button.grid(column= 15, row = 3) 


name2 = tk.StringVar()
nameEntered2 = ttk.Entry(window, width = 15, textvariable = name2)
nameEntered2.grid(column = 10, row = 3) 




label = ttk.Label(window, text = "Font Color") 
label.grid(column = 0, row = 2) 





             





start = False


def clock(start):


  string = strftime("%H:%M:%S :pm")

  label1.config(text = string)
  label1.after(1000)

button = ttk.Button(window, text = "Start", command=lambda start = True:clock(start))
button.grid(column= 10, row = 4) 

f = open('textcolor.txt', 'rt')


text12 = f.readline() 

a = open('background.txt','rt')

background1 = a.readline()

w = open('title.txt','rt')

title12 = w.readline()

root.title(title12)
label1 = Label(root, font=("ds-digital", 80), background= background1, foreground= text12)
label1.pack(anchor='center')

if(start == True):
    clock(start)









window.mainloop()



















            


