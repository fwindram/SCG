# Skeletorfw's Challenge Generator v 0.0.3
# Skeletorfw 2017
# Python 3.4
#
# Created:  08/02/17
# Modified: 10/02/17
#
# A Challenge XML Generator for Binding of Isaac Afterbirth+.
# Due to the python backend, this application should be platform-agnostic
#
# ===== TO DO LIST =====
# TODO: Place cases into dicts
# DONE: Create nice class for run
# TODO: Output general class to XML file
# TODO: Create easy way to share runs: Seed system
# TODO: Create gui using tkinter
# TODO: Find achievement IDs

# SEEDS
# Could just cat all vars together as a CSF, separating list entries (e.g. items) with dots, then base64 encode?
# 1,name,6,404.412.300.12,15,5,0,3,1.3,2.4.8,16,50.51,-1,1,0,0,0,0,3,100,0,0,0,0,0,1

import csv
from tkinter import filedialog


class RunContainer:
    """Holds run data.
    Requires: runid, runname, endstage"""
    def __init__(self, runid, runname, endstage):
        # Required variables
        self.runid = runid
        self.runname = runname
        self.endstage = endstage    # between 6 - 12, 8+ requires "altpath = True"
        # Optional run variables
        self.items = []
        self.trinkets = []
        self.startpill = -1     # between -1 - 46   -1 = No Pill
        self.startcard = 0      # between -1 - 51   -1 = Random
        self.playertype = 0     # between 0 - 15
        self.bannedrooms = []   # between 1 - 22
        self.bannedcurses = []  # 1, 2, 4, 8 or 16
        self.forcedcurse = 0    # 1, 2, 4, 8 or 16
        self.achievements = []
        self.forcepath = 0      # -1 to +1, where 0 does not force a path. +1 sets altpath to be True
        self.canshoot = True
        self.redhp = 0   # 2 = 1 heart
        self.maxhp = 0
        self.soulhp = 0
        self.blackhp = 0
        self.coins = 0
        self.maxdmg = 100    # cannot be less than 100
        self.adddmg = 0
        self.minfirerate = -1
        self.minshotspeed = -1
        self.bigrange = False
        self.hardmode = False    # Sets difficulty to 1 if True
        self.megasatan = False


def loaddata():
    """Loads data from CSVs into dicts for quick use.
    Requires: N/A
    Returns: boi_items, boi_trinkets"""
    # Will need to generate an achievements list.
    boi_items = {}
    boi_trinkets = {}
    itempath = "./data/items.csv"
    trinketspath = "./data/trinkets.csv"
    with open(itempath, newline='') as itemfile:
        itemreader = csv.reader(itemfile)
        for row in itemreader:
            boi_items[int(row[0])] = row[1]
    with open(trinketspath, newline='') as trinketsfile:
        trinketreader = csv.reader(trinketsfile)
        for row in trinketreader:
            boi_trinkets[int(row[0])] = row[1]
    return boi_items, boi_trinkets


def validate_run(run):
    """Validates a run object to check that no illegal values have slipped through."""
    pass


def list2csstr(l):
    """Turns a list into a comma-separated string."""
    csstr = ""
    count = 0
    for x in l:
        count += 1
        if count == len(l):
            csstr += "{0}".format(x)
        else:
            csstr += "{0}, ".format(x)
    return csstr


def construct_runstr(run):
    """Constructs run string.
    Requires: run
    Returns: runstr"""
    # Remember to escape all quotes and leave no starting or trailing spaces!
    runstr = 'id="{0}" name="{1}" endstage="{2}"'.format(run.runid, run.runname, run.endstage)
    if run.items:
        runstr += ' startingitems="{0}"'.format(list2csstr(run.items))
    if run.trinkets:
        runstr += ' startingtrinkets="{0}"'.format(list2csstr(run.trinkets))
    if run.startpill != -1:
        runstr += ' startingpill="{0}"'.format(run.startpill)
    if run.startcard:
        runstr += ' startingcard="{0}"'.format(run.startcard)
    if run.playertype:
        runstr += ' playertype="{0}"'.format(run.playertype)
    if run.bannedrooms:
        runstr += ' roomfilter="{0}"'.format(list2csstr(run.bannedrooms))
    if run.bannedcurses:
        pass  # Add list parsing
    if run.forcedcurse:
        runstr += ' getcurse="{0}"'.format(run.forcedcurse)
    if run.achievements:
        pass  # Add list parsing
    if run.forcepath:
        if run.forcepath > 0:
            runstr += ' altpath="true"'     # value of 1 forces Cathedral
        else:
            runstr += ' altpath="false"'    # -1 forces Sheol
    if not run.canshoot:
        runstr += ' canshoot="false"'
    if run.redhp:
        runstr += ' redhp="{0}"'.format(run.redhp)
    if run.maxhp:
        runstr += ' maxhp="{0}"'.format(run.maxhp)
    if run.soulhp:
        runstr += ' soulhp="{0}"'.format(run.soulhp)
    if run.blackhp:
        runstr += ' blackhp="{0}"'.format(run.blackhp)
    if run.coins:
        runstr += ' coins="{0}"'.format(run.coins)
    if run.maxdmg > 100:
        runstr += ' maxdamage="{0}"'.format(run.maxdmg)
    if run.adddmg:
        runstr += ' adddamage="{0}"'.format(run.adddmg)
    if run.minfirerate != -1:
        runstr += ' minfirerate="{0}"'.format(run.minfirerate)
    if run.minshotspeed != -1:
        runstr += ' minshotspeed="{0}"'.format(run.minshotspeed)
    if run.bigrange:
        runstr += ' bigrange="true"'
    if run.hardmode:
        runstr += ' difficulty="1"'
    if run.megasatan:
        runstr += ' megasatan="true"'
    return runstr


def xml_export():
    """Exports final challenge XML file from Run class.
    Requires: run
    Returns: N/A"""
    # Need to force tkinter save dialog to front. Might be different on different OSs?
    # Construct initialfile from runname
    outfile = filedialog.asksaveasfile(mode='w', defaultextension=".xml", initialfile="")
    if outfile is None:     # Jump out if cancel is pressed
        return
    runstr = ""
    outfile.write('<challenges version="1">\n')             # Header
    outfile.write("<challenge {0} />\n".format(runstr))     # Challenge
    outfile.write("</challenges>\n")                        # Footer
    outfile.close()

# testrun = RunContainer(runid=1, runname="Test", endstage=6)
# testrun.bannedrooms = [1,2,3,5]
# teststr = construct_runstr(testrun)
# print("<challenge {0} />\n".format(teststr))
