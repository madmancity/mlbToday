import math
from datetime import datetime
from PIL import ImageTk
import tkinter as tk
from tkinter import *
from pybaseball import *
from matchfunctions import get_teamabbr, teamabbr, abbrtoimg
import tkinter as tk
from datetime import datetime
from tkinter import *
from gamerecap import gamerecap
from PIL import ImageTk
from PIL import Image as IMG
from pybaseball import *
def format_name(plrname):
    last = plrname.split()[-1];
    if("Jr" in last):
        last = plrname.split()[-2]
    initials = "".join(filter(str.isupper, plrname))
    return initials[0] + ". " + last[:7];


divs = ["AL East", "AL Central", "AL West", "NL East", "NL Central", "NL West"]

y_cur = datetime.now().year
m_cur = datetime.now().month;
d_cur = datetime.now().day;
data = standings(2016)
batstat = batting_stats(2016)[['Name', 'Team', 'AVG', 'H', 'HR', 'RBI', 'OPS', 'SB']]

teamabbrlst = list(teamabbr.values())

# Load batting stats for each division
bsALE = batstat[batstat.Team.isin(teamabbrlst[0:5])].reset_index(drop=True)
bsALC = batstat[batstat.Team.isin(teamabbrlst[5:10] + teamabbrlst[30:30])].reset_index(drop=True)
bsALW = batstat[batstat.Team.isin(teamabbrlst[10:15])].reset_index(drop=True)
bsNLE = batstat[batstat.Team.isin(teamabbrlst[15:20])].reset_index(drop=True)
bsNLC = batstat[batstat.Team.isin(teamabbrlst[20:25])].reset_index(drop=True)
bsNLW = batstat[batstat.Team.isin(teamabbrlst[25:30])].reset_index(drop=True)
print(bsALC)



# leaderavg = batstat.iloc[batstat['AB'].max(), 0]
#print(leaderavg)
#pitstat = pitching_stats_brespecdiv(2024);

lstf = ""
for i in range(len(data)):
    if i == 0:
        lstf = [data[i].columns.values.tolist()] + [data[i].values.tolist()]
    else:
        lstf += [data[i].columns.values.tolist()] + [data[i].values.tolist()]

window = tk.Tk()
window.title("MLBToday")
#getting screen width and height of display
width= window.winfo_screenwidth()
height= window.winfo_screenheight()
#setting tkinter window size
window.geometry("%dx%d" % (width, height))
photo = tk.PhotoImage(file="mlbToday/images/BOS.png")
window.iconphoto(False, photo)
thumbsize = (25,25)
paths = ["mlbToday/images/BAL.png", "mlbToday/images/BOS.png"]

def get_game_recap(team):
    gamerecap(window, team);

def getimageobject(i):
    imgstring = "mlbToday/images/" + teamabbrlst[i] + ".png"

    return newimg
f = 0
for i in range(30):
    img = IMG.open(abbrtoimg[teamabbrlst[i]])
    img.thumbnail(thumbsize);
    newimg = ImageTk.PhotoImage(img)
    piclabel = tk.Label(window, image=newimg)
    piclabel.image = newimg
    if i % 2 == 0:
        piclabel.grid(row=21, column=math.floor(i / 2))
    else:
        piclabel.grid(row=22, column=math.floor(i / 2))
gamelabel = tk.Label(window, text="04/07 5pm")
gamelabel.grid(row = 20, column = 0)
btn = Button(window, text ="View More", command = lambda: get_game_recap("BOS"));
btn.grid(row = 20, column = 1)




'''
imgbos = IMG.open("mlbToday/images/BOS.png")

imgbos.thumbnail(thumbsize);
newbos = ImageTk.PhotoImage(imgbos)
boslabel = tk.Label(window, image=newbos)
# Title within window
newLabel = tk.Label(window, image=photo)
'''

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def specdiv(x):
    return {
        0: bsALE,
        1: bsALC,
        2: bsALW,
        3: bsNLE,
        4: bsNLC,
        5: bsNLW
    }
def getLeaderStat(div, stat):
    return(format_name(specdiv(div).get(div, 0).iloc[specdiv(div).get(div,0)[stat].idxmax(), 0])) + " " + str(specdiv(div).get(div,0)[stat].max())



class Table:
        def __init__(self, root, iter):
                self.d = Entry(root, width=10, fg='white', font=('Arial', 16, 'bold'), state="normal")
                #Move NL Stuff to the right
                if iter > 2:
                    rofs=3
                    cofs=10
                    self.d.config(readonlybackground='blue')
                    #Make the headers
                    for i in range(4):
                        self.nlb = Entry(root, width=10, readonlybackground='blue', font=('Arial', 16, 'bold'), state="readonly")
                        self.nlb.grid(row=7*(iter-3), column=11+i)
                else:
                    rofs=0
                    cofs=0
                    self.d.config(readonlybackground='red')
                    for i in range(4):
                        self.alb = Entry(root, width=10, readonlybackground='red', font=('Arial', 16, 'bold'), state="readonly")
                        self.alb.grid(row=7*iter, column=1+i)
                self.d.grid(row=7 * (iter-rofs), column=cofs);
                self.d.insert(END, divs[iter]);
                self.d.config(state="readonly")
                lst = data[iter].values.tolist()
                for j in range(5):
                    lst[j][0] = get_teamabbr(lst[j][0])
                    for k in range(5):
                        self.e = Entry(root, width=10, fg='black', font=('Arial', 16, 'bold'), state="normal")
                        if iter > 2:
                            self.e.grid(row=j + (7 * (iter - 3)) + 1, column=k + 10)
                        else:
                            self.e.grid(row=j + (7 * iter) + 1, column=k)
                        self.e.insert(END, lst[j][k])
                        self.e.config(state="readonly")
class Leaders:
    def __init__(self, root, iter):
        if iter > 2:
            rofs = 3;
            cofs = 10;
        else:
            rofs = 0;
            cofs = 0;
        self.a = Entry(root, width=5, fg='black', font=('Arial', 12, 'bold'), state="normal", borderwidth=0)
        self.a.grid(row=0 + (7*(iter-rofs)), column=6 + cofs)
        self.a.insert(END, "AVG")
        self.al = Entry(root, width=15, fg='black', font=('Arial', 11, 'bold'), state="normal", borderwidth=0)
        self.al.grid(row=0 + (7*(iter-rofs)), column=7 + cofs)
        self.al.insert(END, getLeaderStat(iter, 'AVG'))
        self.h = Entry(root, width=5, fg='black', font=('Arial', 12, 'bold'), state="normal", borderwidth=0)
        self.h.grid(row=1 + (7*(iter-rofs)), column=6 + cofs)
        self.h.insert(END, "H")
        self.hl = Entry(root, width=15, fg='black', font=('Arial', 11, 'bold'), state="normal", borderwidth=0)
        self.hl.grid(row=1 + (7*(iter-rofs)), column=7 + cofs)
        self.hl.insert(END, getLeaderStat(iter, 'H'))
        self.hr = Entry(root, width=5, fg='black', font=('Arial', 12, 'bold'), state="normal", borderwidth=0)
        self.hr.grid(row=2 + (7*(iter-rofs)), column=6 + cofs)
        self.hr.insert(END, "HR")
        self.hrl = Entry(root, width=15, fg='black', font=('Arial', 11, 'bold'), state="normal", borderwidth=0)
        self.hrl.grid(row=2 + (7*(iter-rofs)), column=7 + cofs)
        self.hrl.insert(END, getLeaderStat(iter, 'HR'))
        self.rb = Entry(root, width=5, fg='black', font=('Arial', 12, 'bold'), state="normal", borderwidth=0)
        self.rb.grid(row=3 + (7*(iter-rofs)), column=6 + cofs)
        self.rb.insert(END, "RBI")
        self.rbl = Entry(root, width=15, fg='black', font=('Arial', 11, 'bold'), state="normal", borderwidth=0)
        self.rbl.grid(row=3 + (7*(iter-rofs)), column=7 + cofs)
        self.rbl.insert(END, getLeaderStat(iter, 'RBI'))
        self.er = Entry(root, width=5, fg='black', font=('Arial', 12, 'bold'), state="normal", borderwidth=0)
        self.er.grid(row=4 + (7*(iter-rofs)), column=6 + cofs)
        self.er.insert(END, "OPS")
        self.erl = Entry(root, width=15, fg='black', font=('Arial', 11, 'bold'), state="normal", borderwidth=0)
        self.erl.grid(row=4 + (7*(iter-rofs)), column=7 + cofs)
        self.erl.insert(END, getLeaderStat(iter, 'OPS'))
        self.w = Entry(root, width=5, fg='black', font=('Arial', 12, 'bold'), state="normal", borderwidth=0)
        self.w.grid(row=5 + (7*(iter-rofs)), column=6 + cofs)
        self.w.insert(END, "SB")
        self.wl = Entry(root, width=15, fg='black', font=('Arial', 11, 'bold'), state="normal", borderwidth=0)
        self.wl.grid(row=5 + (7*(iter-rofs)), column=7 + cofs)
        self.wl.insert(END, getLeaderStat(iter, 'HR'))
        ''' self.na = Entry(root, width=5, fg='black', font=('Arial', 12, 'bold'), state="normal", borderwidth=0)
        self.na.grid(row=0, column=8)
        self.na.insert(END, "AVG.")
        self.nal = Entry(root, width=15, fg='black', font=('Arial', 11, 'bold'), state="normal", borderwidth=0)
        self.nal.grid(row=0, column=9)
        self.nal.insert(END, "M.OZUNA .302")'''


for i in range(6):
    t = Table(window, i)
    l = Leaders(window, i)
window.mainloop();