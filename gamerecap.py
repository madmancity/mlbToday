from matchfunctions import get_teamabbr, teamabbr
import tkinter as tk
from datetime import datetime
from tkinter import *

from PIL import ImageTk
from PIL import Image as IMG
from pybaseball import *


def gamerecap(window, team):
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(window)

    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")

    # sets the geometry of toplevel
    newWindow.geometry("200x200")

    # A Label widget to show in toplevel
    Label(newWindow,
          text="Boston vs Yo mama").pack()