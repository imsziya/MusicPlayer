import tkinter as tkk
from tkinter.filedialog import askdirectory
import pygame
import os

tk = tkk.Tk()  # In order to create an empty window

# Title of the window
tk.title("MusicPlayer")
# Window Geometry
tk.geometry("1000x200+200+200")
# Initiating Pygame
pygame.init()
# Initiating Pygame Mixer
pygame.mixer.init()
# Declaring track Variable
var = tkk.StringVar()
# Declaring Status Variable
status = tkk.StringVar()


def playsong():
    pygame.mixer.music.load(playlist.get(tkk.ACTIVE))
    status.set("-Playing")
    var.set(playlist.get(tkk.ACTIVE))
    pygame.mixer.music.play()


def stopsong():
    # Displaying Status
    status.set("-Stopped")
    # Stopped Song
    pygame.mixer.music.stop()


def pausesong():
    # Displaying Status
    status.set("-Paused")
    # Paused Song
    pygame.mixer.music.pause()


def unpausesong():
    # It will Display the  Status
    status.set("-Playing")
    # Playing back Song
    pygame.mixer.music.unpause()


# Creating the Track Frames for Song label & status label
trackframe = tkk.LabelFrame(tk, text="Song Track", font=("times new roman", 15, "bold"), bg="Navyblue",
                            fg="white", bd=5, relief=tkk.GROOVE)
trackframe.place(x=0, y=0, width=600, height=100)
# Inserting Song Track Label
songtrack = tkk.Label(trackframe, textvariable=var, width=20, font=("times new roman", 24, "bold"), bg="Orange",
                      fg="gold").grid(row=0, column=0, padx=10, pady=5)
# Inserting Status Label
trackstatus = tkk.Label(trackframe, textvariable=status, font=("times new roman", 24, "bold"), bg="orange", fg="gold").grid(
    row=0, column=1, padx=10, pady=5)

# Creating Button Frame
buttonframe = tkk.LabelFrame(tk, text="Control Panel", font=("times new roman", 15, "bold"), bg="grey",
                             fg="white", bd=5, relief=tkk.GROOVE)
buttonframe.place(x=0, y=100, width=600, height=100)
# Inserting Play Button
playbtn = tkk.Button(buttonframe, text="PLAYSONG", command=playsong, width=10, height=1,
                 font=("times new roman", 16, "bold"), fg="navyblue", bg="pink").grid(row=0, column=0, padx=10,
                                                                                      pady=5)
# Inserting Pause Button
playbtn = tkk.Button(buttonframe, text="PAUSE", command=pausesong, width=8, height=1, font=("times new roman", 16, "bold"),
                     fg="navyblue", bg="pink").grid(row=0, column=1, padx=10,
                                                pady=5)
# Inserting Unpause Button
playbtn = tkk.Button(buttonframe, text="UNPAUSE", command=unpausesong, width=10, height=1,
                     font=("times new roman", 16, "bold"), fg="navyblue", bg="pink").grid(row=0, column=2, padx=10,
                                                                                      pady=5)
# Inserting Stop Button
playbtn = tkk.Button(buttonframe, text="STOPSONG", command=stopsong, width=10, height=1,
                     font=("times new roman", 16, "bold"), fg="navyblue", bg="pink").grid(row=0, column=3, padx=10,
                                                                                      pady=5)

# Creating Playlist Frame
songsframe = tkk.LabelFrame(tk, text="Song Playlist", font=("times new roman", 15, "bold"), bg="grey",
                            fg="white", bd=5, relief=tkk.GROOVE)
songsframe.place(x=600, y=0, width=400, height=200)
# Inserting scrollbar
scrol_y = tkk.Scrollbar(songsframe, orient=tkk.VERTICAL)
# Inserting Playlist listbox
playlist = tkk.Listbox(songsframe, yscrollcommand=scrol_y.set, selectbackground="gold", selectmode=tkk.SINGLE,
                       font=("times new roman", 12, "bold"), bg="silver", fg="navyblue", bd=5, relief=tkk.GROOVE)
# Applying Scrollbar to listbox
scrol_y.pack(side=tkk.RIGHT, fill=tkk.Y)
scrol_y.config(command=playlist.yview)
playlist.pack(fill=tkk.BOTH)
# Changing Directory for fetching Songs
direc = askdirectory()
os.chdir(direc)
# Fetching Songs
songtracks = os.listdir()
# Inserting Songs into Playlist
for track in songtracks:
    playlist.insert(tkk.END, track)

tk.mainloop()
