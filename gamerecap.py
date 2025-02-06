import statsapi as mlb
from matchfunctions import get_teamabbr, teamabbr, abbrtoimg
import tkinter as tk
from datetime import datetime
from tkinter import *

from PIL import ImageTk
from PIL import Image as IMG
from pybaseball import *


def gamerecap(window, game):
    game_id = game['game_id']
    #Use game id to get more information than with team
    newwindow = Toplevel(window)
    width = newwindow.winfo_screenwidth()
    height = newwindow.winfo_screenheight()
    # setting tkinter window size
    newwindow.geometry("%dx%d" % (width, height))
    boxscore = mlb.boxscore(game_id, battingBox=True, battingInfo=True, fieldingInfo=True, pitchingBox=False, gameInfo=False)
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
    hscorelabel = tk.Label(newwindow, text=game['home_score'], font=('Arial', 16, 'bold'))
    ascorelabel = tk.Label(newwindow, text=game['away_score'], font=('Arial', 16, 'bold'))
    apiclabel.grid(row=0, column=0,rowspan=1)
    ascorelabel.grid(row=0, column=1,rowspan=1)
    hpiclabel.grid(row=0, column=3,rowspan=1);
    hscorelabel.grid(row=0, column=4,rowspan=1)

    indices = ['1','2','3','4','5','6','7','8','9']
    awaybatters = []
    homebatters = []
    for i in range(len(boxscoredata['homeBatters'])):
        if boxscoredata['homeBatters'][i]['namefield'][0] in indices:
            homebatters.append(boxscoredata['homeBatters'][i]['namefield'])
    for i in range(len(boxscoredata['awayBatters'])):
        if boxscoredata['awayBatters'][i]['namefield'][0] in indices:
            awaybatters.append(boxscoredata['awayBatters'][i]['namefield'])
    for i in range(len(awaybatters)):
        alineupnum = tk.Label(newwindow, text=str(i+1), font=('Arial', 16, 'bold'))
        alineupnum.grid(row=i+1, column=0)
        alineupname = tk.Label(newwindow, text=awaybatters[i][2:], font=('Arial', 16, 'bold'))
        alineupname.grid(row=i+1, column=1)
        hlineupnum = tk.Label(newwindow, text=str(i + 1), font=('Arial', 16, 'bold'))
        hlineupnum.grid(row=i+1, column=3)
        hlineupname = tk.Label(newwindow, text=homebatters[i][2:], font=('Arial', 16, 'bold'))
        hlineupname.grid(row=i+1, column=4)

    boxform = tk.Label(newwindow, text=boxscore);


    boxform.grid(row=0, column=2,rowspan=22)

    # print(boxscore)
    newwindow.title(home + " vs " + away)