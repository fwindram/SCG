# Skeletorfw's Challenge Generator v 0.0.2
# Skeletorfw 2017
# Python 3.4
#
# Created:  08/02/17
# Modified: 09/02/17
#
# A Challenge XML Generator for Binding of Isaac Afterbirth+.
#
# ===== TO DO LIST =====
# TODO: Place cases into dicts
# DONE: Create nice class for run
# TODO: Output general class to XML file
# TODO: Create easy way to share runs: Seed system
# TODO: Create gui using tkinter

# SEEDS
# Could just cat all vars together as a CSF, separating list entries e.g. items with dots, then base64 encode?
# 1,name,6,404.412.300.12,15,5,0,3,1.3,2.4.8,16,50.51,-1,1,0,0,0,0,3,100,0,0,0,0,0,1

# import tkinter


class Run:
    """Holds run data"""
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
        self.minfirerate = 0
        self.minshotspeed = 0
        self.bigrange = False
        self.hardmode = False    # Sets difficulty to 1 if True
        self.megasatan = False
