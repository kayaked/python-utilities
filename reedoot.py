from tkinter import *
import requests
import json
from tkinter.messagebox import showinfo
from tkinter.ttk import *
import os
import traceback
import webbrowser
from os.path import join

master = Tk()

data_root=None

def GCP(link):
    global data_root
    req=requests.get("https://www.reddit.com/{}.json".format(link), headers={'User-Agent':'reedoot'}).json()


    try:
        data_root=req['data']
        changeSubreddit()
    except KeyError:
        try:
            data_root=req[0]['data']
        except Exception:
            showinfo("reedoot", "The requested subreddit was not found!")

def changeSubreddit():
    if data_root==None:
        showinfo("Error: JSON data root could not be found. Please report to the maintainer")
    try:
        entr1.set(data_root['children'][0]['data']['title'])
        entr2.set(data_root['children'][1]['data']['title'])
        entr3.set(data_root['children'][2]['data']['title'])
        entr4.set(data_root['children'][3]['data']['title'])
        entr5.set(data_root['children'][4]['data']['title'])
        entr6.set(data_root['children'][5]['data']['title'])
        entr7.set(data_root['children'][6]['data']['title'])
        entr8.set(data_root['children'][7]['data']['title'])
        entr9.set(data_root['children'][8]['data']['title'])
        entr10.set(data_root['children'][9]['data']['title'])
    except TclError:
        showinfo("reedoot", "Error: This page contains an emoji or another character reedoot/tkinter/python does not recognize. There will be handling for this in time, but as of now it breaks reedoot! Sorry")



    upv1.set("^ ({})".format(str(data_root['children'][0]['data']['ups'])))
    upv2.set("^ ({})".format(str(data_root['children'][1]['data']['ups'])))
    upv3.set("^ ({})".format(str(data_root['children'][2]['data']['ups'])))
    upv4.set("^ ({})".format(str(data_root['children'][3]['data']['ups'])))
    upv5.set("^ ({})".format(str(data_root['children'][4]['data']['ups'])))
    upv6.set("^ ({})".format(str(data_root['children'][5]['data']['ups'])))
    upv7.set("^ ({})".format(str(data_root['children'][6]['data']['ups'])))
    upv8.set("^ ({})".format(str(data_root['children'][7]['data']['ups'])))
    upv9.set("^ ({})".format(str(data_root['children'][8]['data']['ups'])))
    upv10.set("^ ({})".format(str(data_root['children'][9]['data']['ups'])))

def popInfo(offset:int):
    global data_root
    if data_root==None:
        showinfo("Error: JSON data root could not be found. Please report to the maintainer")
    offset=offset-1
    webbrowser.open("reddit.com{}".format(data_root['children'][offset]['data']['permalink']))


entr1=StringVar()
entr2=StringVar()
entr3=StringVar()
entr4=StringVar()
entr5=StringVar()
entr6=StringVar()
entr7=StringVar()
entr8=StringVar()
entr9=StringVar()
entr10=StringVar()

upv1=StringVar()
upv2=StringVar()
upv3=StringVar()
upv4=StringVar()
upv5=StringVar()
upv6=StringVar()
upv7=StringVar()
upv8=StringVar()
upv9=StringVar()
upv10=StringVar()

chsub=StringVar()

chsub.set("all")

sort_by=StringVar(master)

sort_by.set("hot")

GCP("r/all/")

def uty(*args):
    GCP("r/{}/{}/".format(chsub.get().replace("/r/", "").replace("r/", ""), sort_by.get()))

master.title("reedoot - the back page of the internet")

ff = Entry(master, textvariable=chsub)
ff.grid(padx=5, pady=5, row=0, column=0, sticky=W)

Button(master, text="pick sub", command= lambda: GCP("r/{}/{}/".format(chsub.get().replace("/r/", "").replace("r/", ""), sort_by.get()))).grid(padx=5, pady=5, row=0, column=1, sticky=W)

gg = OptionMenu(master, sort_by, "hot", "hot", "top", "controversial", "rising", "new")
gg.grid(padx=5, pady=5, row=0, column=2, sticky=W)

sort_by.trace('w', uty)

Button(master, textvariable=entr1, width=100, command= lambda: popInfo(1)).grid(padx=5, pady=5, row=1, column=0, sticky=W, columnspan=6)
Button(master, textvariable=entr2, width=100, command= lambda: popInfo(2)).grid(padx=5, pady=5, row=2, column=0, sticky=W, columnspan=6)
Button(master, textvariable=entr3, width=100, command= lambda: popInfo(3)).grid(padx=5, pady=5, row=3, column=0, sticky=W, columnspan=6)
Button(master, textvariable=entr4, width=100, command= lambda: popInfo(4)).grid(padx=5, pady=5, row=4, column=0, sticky=W, columnspan=6)
Button(master, textvariable=entr5, width=100, command= lambda: popInfo(5)).grid(padx=5, pady=5, row=5, column=0, sticky=W, columnspan=6)
Button(master, textvariable=entr6, width=100, command= lambda: popInfo(6)).grid(padx=5, pady=5, row=6, column=0, sticky=W, columnspan=6)
Button(master, textvariable=entr7, width=100, command= lambda: popInfo(7)).grid(padx=5, pady=5, row=7, column=0, sticky=W, columnspan=6)
Button(master, textvariable=entr8, width=100, command= lambda: popInfo(8)).grid(padx=5, pady=5, row=8, column=0, sticky=W, columnspan=6)
Button(master, textvariable=entr9, width=100, command= lambda: popInfo(9)).grid(padx=5, pady=5, row=9, column=0, sticky=W, columnspan=6)
Button(master, textvariable=entr10, width=100, command= lambda: popInfo(10)).grid(padx=5, pady=5, row=10, column=0, sticky=W, columnspan=6)

Button(master, textvariable=upv1, width=10, command= lambda: popInfo(1)).grid(padx=5, pady=5, row=1, column=6, sticky=W)
Button(master, textvariable=upv2, width=10, command= lambda: popInfo(2)).grid(padx=5, pady=5, row=2, column=6, sticky=W)
Button(master, textvariable=upv3, width=10, command= lambda: popInfo(3)).grid(padx=5, pady=5, row=3, column=6, sticky=W)
Button(master, textvariable=upv4, width=10, command= lambda: popInfo(4)).grid(padx=5, pady=5, row=4, column=6, sticky=W)
Button(master, textvariable=upv5, width=10, command= lambda: popInfo(5)).grid(padx=5, pady=5, row=5, column=6, sticky=W)
Button(master, textvariable=upv6, width=10, command= lambda: popInfo(6)).grid(padx=5, pady=5, row=6, column=6, sticky=W)
Button(master, textvariable=upv7, width=10, command= lambda: popInfo(7)).grid(padx=5, pady=5, row=7, column=6, sticky=W)
Button(master, textvariable=upv8, width=10, command= lambda: popInfo(8)).grid(padx=5, pady=5, row=8, column=6, sticky=W)
Button(master, textvariable=upv9, width=10, command= lambda: popInfo(9)).grid(padx=5, pady=5, row=9, column=6, sticky=W)
Button(master, textvariable=upv10, width=10, command= lambda: popInfo(10)).grid(padx=5, pady=5, row=10, column=6, sticky=W)

if data_root==None:
    print("Error: JSON data root could not be found. Please report to the maintainer")

changeSubreddit()

s = Style()
s.theme_use('clam')

master.resizable(False, False)

master.mainloop()