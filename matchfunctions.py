from datetime import datetime
from PIL import ImageTk
import tkinter as tk
from tkinter import *
from pybaseball import *
import tkinter as tk
from datetime import datetime
from tkinter import *

from PIL import ImageTk
from PIL import Image as IMG
from pybaseball import *
teamabbr = {
    "Orioles": "BAL",
    "Red Sox": "BOS",
    "Yankees": "NYY",
    "Rays": "TBR",
    "Blue Jays": "TOR",
    "White Sox": "CHW",
    "Guardians": "CLE",
    "Tigers": "DET",
    "Royals": "KCR",
    "Twins": "MIN",
    "Astros": "HOU",
    "Angels": "LAA",
    "Athletics": "OAK",
    "Mariners": "SEA",
    "Rangers": "TEX",
    "Braves": "ATL",
    "Marlins": "MIA",
    "Mets": "NYM",
    "Phillies": "PHI",
    "Nationals": "WSH",
    "Cubs": "CHC",
    "Reds": "CIN",
    "Brewers": "MIL",
    "Pirates": "PIT",
    "Cardinals": "STL",
    "Diamondbacks": "ARI",
    "Rockies": "COL",
    "Dodgers": "LAD",
    "Padres": "SDP",
    "Giants": "SFG",
    "Indians": "CLE",
}

abbrtoimg = {
    "BAL" : "mlbToday/images/BAL.png",
    "BOS" : "mlbToday/images/BOS.png",
    "NYY" : "mlbToday/images/NYY.png",
    "TBR" : "mlbToday/images/TBR.png",
    "TOR": "mlbToday/images/TOR.png",
    "CHW": "mlbToday/images/CHW.png",
    "CLE": "mlbToday/images/CLE.png",
    "DET": "mlbToday/images/DET.png",
    "KCR": "mlbToday/images/KCR.png",
    "MIN": "mlbToday/images/MIN.png",
    "HOU": "mlbToday/images/HOU.png",
    "LAA": "mlbToday/images/LAA.png",
    "OAK": "mlbToday/images/OAK.png",
    "SEA": "mlbToday/images/SEA.png",
    "TEX": "mlbToday/images/TEX.png",
    "ATL": "mlbToday/images/ATL.png",
    "MIA": "mlbToday/images/MIA.png",
    "NYM": "mlbToday/images/NYM.png",
    "PHI": "mlbToday/images/PHI.png",
    "WSH": "mlbToday/images/WSH.png",
    "CHC": "mlbToday/images/CHC.png",
    "CIN": "mlbToday/images/CIN.png",
    "MIL": "mlbToday/images/MIL.png",
    "PIT": "mlbToday/images/PIT.png",
    "STL": "mlbToday/images/STL.png",
    "ARI": "mlbToday/images/ARI.png",
    "COL": "mlbToday/images/COL.png",
    "LAD": "mlbToday/images/LAD.png",
    "SDP": "mlbToday/images/SDP.png",
    "SFG": "mlbToday/images/SFG.png"
}

def get_teamabbr(teamname):
    for key in teamabbr:
        if key in teamname:
            return teamabbr[key];