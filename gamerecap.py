import statsapi as mlb
from matchfunctions import get_teamabbr, teamabbr, abbrtoimg
import tkinter as tk
from datetime import datetime
from tkinter import *

from PIL import ImageTk
from PIL import Image as IMG
from pybaseball import *


def gamerecap(window, game_id):

    #Use game id to get more information than with team
    newwindow = Toplevel(window)
    width = newwindow.winfo_screenwidth()
    height = newwindow.winfo_screenheight()
    # setting tkinter window size
    newwindow.geometry("%dx%d" % (width, height))
    boxscore = mlb.boxscore(game_id)
    boxscoredata = mlb.boxscore_data(game_id)
    home = get_teamabbr(boxscoredata.get('teamInfo').get('home').get('teamName'));
    away = get_teamabbr(boxscoredata.get('teamInfo').get('away').get('teamName'));
    print(home)
    print(away)
    homeimg = IMG.open(abbrtoimg[home])
    newhomeimg = ImageTk.PhotoImage(homeimg)
    hpiclabel = tk.Label(newwindow, image=newhomeimg, borderwidth=1, relief='ridge', justify="left")
    hpiclabel.image = newhomeimg
    awayimg = IMG.open(abbrtoimg[away])
    newawayimg = ImageTk.PhotoImage(awayimg)
    apiclabel = tk.Label(newwindow, image=newawayimg, borderwidth=1, relief='ridge', justify="left")
    apiclabel.image = newawayimg
    # Flip this when reformatting
    hpiclabel.grid(row=0, column=1);
    apiclabel.grid(row=0, column=0);
    boxform = tk.Label(newwindow, text=boxscore);
    boxform.grid(row=1, column=1)

    # print(boxscore)
    newwindow.title(home + " vs " + away)

