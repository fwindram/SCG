# Skeletorfw's Challenge Generator v 0.0.1
# Skeletorfw 2016
# Python 3.4
#
# Created:  08/02/17
# Modified: 08/02/17
#
# A Python3/SQL project for building and maintaining a book database.
#
# ===== TO DO LIST =====
# TODO: Place cases into dicts
# TODO: Create nice class for run
# TODO: Output general class to XML file
# TODO: Create easy way to share runs: Seed system

# VARS
# Ranges are inclusive for now
# id = 0
# name = ""
# endstage = 0    # between 6 - 12
# items = []
# trinkets = []
# pill = 0        # between -1 - 46
# card = 0        # between -1 - 51
# playertype = 0  # between 0 - 15
# bannedrooms = []    # between 1 - 22
# bannedcurses = []   # 1, 2, 4, 8 or 16
# forcedcurse = 0     # 1, 2, 4, 8 or 16
# achievements = []
# forcepath = 0   # -1 to +1, where 0 does not force a path.
# canshoot = True
# redhp = 0   # 2 = 1 heart
# maxhp = 0
# soulhp = 0
# blackhp = 0
# coins = 0
# maxdmg = 100    # cannot be less than 100
# adddmg = 0
# minfirerate = 0
# minshotspeed = 0
# bigrange = False
# hardmode = False    # Sets difficulty to 1 if True
# megasatan = False




# SEEDS
#

# import tkinter

class Run:
    """Holds run data"""
    def __init__(self, runid, runname, endstage, items, trinkets, title, language):
        self.runid = runid
        self.runname = runname
        self.endstage = endstage
        self.items = items
        self.trinkets = trinkets
        self.title = title
        self.language = language