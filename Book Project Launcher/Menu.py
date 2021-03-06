import tkinter
from tkinter import ttk
import runpy
import os
import sys
#  Games
pong = "games/pong.py"
mine = "games/minesweeper.py"
invade = "space_invaders.py"

window = tkinter.Tk()
window.title("Austin's Game Collection Menu!")


def play(game):
    window.destroy()
    if game == invade:
        os.chdir("games/space_invaders")
        sys.path.append(os.getcwd())
    runpy.run_path(game)


title = ttk.Label(window, font="TkDefaultFont 10 bold underline",
                  text="Choose a game:")
title.pack(padx=125)
button1 = ttk.Button(window, text="Pong", command=lambda: play(pong))
button1.pack(fill=tkinter.X)
button2 = ttk.Button(window, text="Minesweeper", command=lambda: play(mine))
button2.pack(fill=tkinter.X)
button3 = ttk.Button(window, text="Space Invaders", command=lambda: play(invade
                                                                         ))
button3.pack(fill=tkinter.X)
window.mainloop()
