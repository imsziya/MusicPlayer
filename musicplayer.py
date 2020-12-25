
# importing necessary modules

import pygame
import tkinter as tk
from tkinter.filedialog import askdirectory
import os

# creating applications window
mp = tk.Tk()
# setting title name
title = mp.title("Music Player")
# setting the dimensions
mp.geometry('500x450')
# setting music directory
direc = askdirectory()
# setting music directory to current music directory
os.chdir(direc)
# creating songsList
songList = os.listdir()
# creating playList
playlist = tk.Listbox(mp, font='cambria 14 bold', bg='cyan2', selectmode=tk.SINGLE)

for item in songList:
    pos = 0
    playlist.insert(pos, item)
    pos = pos + 1

pygame.init()
pygame.mixer.init()


# defining play method
def play():
    pygame.mixer.music.load(playlist.get(tk.ACTIVE))
    var.set(playlist.get(tk.ACTIVE))
    pygame.mixer.music.play()


# defining stop method
def exit_music_player():
    pygame.mixer.music.stop()


# defining pause method
def pause():
    pygame.mixer.music.pause()


# defining resume method
def resume():
    pygame.mixer.music.unpause()


play_Button = tk.Button(mp, height=3, width=5, text='Play Music', font='cambria 14 bold', command=play, bg='lime green',
                        fg='black')

pause_Button = tk.Button(mp, height=3, width=5, text='Pause Music', font='cambria 14 bold', command=pause, bg='red',
                         fg='black')

resume_Button = tk.Button(mp, height=3, width=5, text='Resume Music', font='cambria 14 bold', command=resume,
                          bg='yellow', fg='black')

stop_Button = tk.Button(mp, height=3, width=5, text='Stop Music', font='cambria 14 bold', command=exit_music_player,
                        bg='red', fg='black')

play_Button.pack(fill='x')
pause_Button.pack(fill='x')
resume_Button.pack(fill='x')
stop_Button.pack(fill='x')

playlist.pack(fill='both', expand='yes')

var = tk.StringVar()

songTitle = tk.Label(mp, font='cambria 14 bold', textvariable=var)
songTitle.pack()
mp.mainloop()
