from tkinter import *
from tkinter import ttk
import tkinter as tk
import threading
from time import sleep
import pygame
import os
back_control_colour="#BEB89A"
opbutt_color="#1D1D1D"
root=tk.Tk()
root.config(background=back_control_colour)
root.minsize(width=700,height=500)
pygame.mixer.init()
#function to delete frame
def clear_frame(frame):
   frame.destroy()

#side menu button frame
opbuttf=Frame(root,background=opbutt_color)
opbuttf.pack(side=LEFT,fill=Y)

#icons
plimg=PhotoImage(file="play.png")
playlimg=PhotoImage(file="playlist.png")
addimg=PhotoImage(file="add.png")
opimg=PhotoImage(file="option-image.png")
albimg=PhotoImage(file="music.png")
previmg=PhotoImage(file="previous.png")
pausimg=PhotoImage(file="pause.png")
neximg=PhotoImage(file="next-button.png")

#frames for progress bar and play/pause button
control=Frame(root,background=back_control_colour)
control.pack(side=BOTTOM,fill=X)

#intial width of progress bar
global wid
wid=0
#var that represent weather side menu is open or not
global count
count=0
#control button var
global play_button
global next_button
global previous_button

stop = False
stat=False

def pausesong():
  global stop
  global stat
  global play_button
  stat=True
  stop=True
  play_button.config(command=unpausesong,image=plimg)
  pygame.mixer.music.pause()
  

def unpausesong():
    global stop
    global play_button
    pygame.mixer.music.unpause()
    stop = False
    music_starter()
    try:
        play_button.config(command=pausesong,image=pausimg)
    except:
        pass
    

def playsong():
    global stop
    global play_button
    global wid
    global stat
    play_button.config(command=pausesong,image=pausimg)
    if stat==False:
        stop=False
        pygame.mixer.music.play(loops=0)


    try:
        while 100 and not stop:
            prog.set(wid)
            prog.update()
            wid+=1
            print(wid)
            sleep(1)
        print("breaked")
    except:
        pygame.mixer.music.unload()
        print("unloaded")
        pass


def music_starter():
  global t
  t = threading.Thread(target=playsong)
  t.start()

song_no=0
def nextsong():
    global song_no
    song_no+=1
    load(song_no)

def previoussong():
    global song_no
    song_no-=1
    load(song_no)

previous_button=Button(control,width=32,border=0,background=back_control_colour,activebackground=back_control_colour,foreground=back_control_colour,image=previmg,command=previoussong)
previous_button.pack(side=LEFT,padx=(270,0))
play_button=Button(control,width=32,border=0,background=back_control_colour,activebackground=back_control_colour,foreground=back_control_colour,image=plimg,command=music_starter)
play_button.pack(side=LEFT,padx=(30,26))
next_button=Button(control,width=32,border=0,background=back_control_colour,activebackground=back_control_colour,foreground=back_control_colour,image=neximg,command=nextsong)
next_button.pack(side=LEFT)

#MUSIC STATUS PROGRESS BAR
prog=Scale(root,orient=HORIZONTAL,highlightthickness=0,width=4,length=660,foreground="#dfdfdf",background=back_control_colour,troughcolor="red")
prog.pack(side=BOTTOM,padx=6,fill=X)
def load(index=0):
    global play_button
    global stop
    global wid
    global prog
    global stat
    global t
    stop=True
    stat=False
    wid=0
    prog.set(wid)
    music_list=os.listdir("geet")
    play_button.config(image=pausimg)
    path=f"geet\{music_list[index]}"
    pygame.mixer.music.load(path)
    root.after(1000,music_starter)
    print("loaded")
load()

     

#resizing and respacing window/button on minimizing or maxismizing window
def window_event(e=None):
    global play_button
    global next_button
    global previous_button
    global prog
    scr=root.winfo_width()
    hig=root.winfo_height()
    print(scr,hig)
    if scr==1366 and hig==705:
        prog.config(length=1366)
        previous_button.pack(side=LEFT,padx=(600,0))
        play_button.pack(side=LEFT,padx=(30,26))
        next_button.pack(side=LEFT)
    if (scr==700 and hig==500) or (scr==853 and hig==500) or (scr==1370 and hig==500) or (scr==782 and hig==500) :
        prog.config(length=660)
        previous_button.pack(side=LEFT,padx=(275,0))
        play_button.pack(side=LEFT,padx=(30,26))
        next_button.pack(side=LEFT)
    if count==1:
        root.minsize(width=800,height=500)


root.bind("<Map>", window_event)


option_butt=Button(opbuttf,border=0,bg=opbutt_color,image=addimg,compound=tk.LEFT,width=70,text="      Add",foreground="white")
option_butt.pack(pady=(45,11),padx=(0,12))
option_butt=Button(opbuttf,border=0,bg=opbutt_color,image=albimg,compound=tk.LEFT,width=70,foreground="white",text="   Album")
option_butt.pack(pady=15,padx=(0,12))
option_butt=Button(opbuttf,border=0,bg=opbutt_color,height=30,image=playlimg,compound=tk.LEFT,width=70,text="   Playlist",foreground="white")
option_butt.pack(pady=15,padx=(0,12))
option_butt=Button(opbuttf,border=0,bg=opbutt_color,width=12,text="Podcast",foreground="white")
option_butt.pack(pady=15,padx=(0,12))

# #function of side menu
# def side_menu():
#     global count#to check weather side bar is open or not
#     global option_frame#to pass side menu frame to clear frame function
#     global playing#to edit frame attributes out function once they are deleted for first time
#     global control#to edit frame attributes out function once they are deleted for first time
#     global prog#to keep progress bar in sync with when the menu is off/on 
#     global play_button#to edit button attributes out function once they are deleted for first time
#     global next_button#to edit button attributes out function once they are deleted for first time
#     global previous_button#to edit button attributes out function once they are deleted for first time
#     global stop
#     global stat
#     global wid
#     if count==0:
#         clear_frame(control)#to use fill=y of side menu
#         clear_frame(playing)#to use fill=y of side menu
#         option_frame=tk.Label(root,background="black")
#         option_frame.pack(side=LEFT,fill=Y)
#         #to increas size of window on opening side menu
#         if root.winfo_width()==700 and root.winfo_height()==500:
#             root.minsize(width=800,height=500)

#         #recreating/
#         control=Frame(root,background="#dedede") 
#         control.pack(side=BOTTOM,fill=X)
#         playing=Frame(root,background="#dedede") 
#         playing.pack(side=BOTTOM,fill=X)
        
#         prog=Scale(playing,orient=HORIZONTAL,highlightthickness=0,width=4,length=660,foreground="#dfdfdf",background="red",troughcolor="red")
#         prog.set(wid)
#         prog.pack(side=LEFT,padx=6)
#         previous_button=Button(control,width=24,border=0,background="#dfdfdf",activebackground="#dfdfdf",image=previmg,command=previoussong)
#         previous_button.pack(side=LEFT,padx=(270,0))
#         # if stat==False:
#         #     play_button=Button(control,width=24,border=0,background="#dfdfdf",activebackground="#dfdfdf",image=plimg,command=music_starter)
#         #     play_button.pack(side=LEFT,padx=(30,26))
#         if stop==True:
#             play_button=Button(control,width=24,border=0,background="#dfdfdf",activebackground="#dfdfdf",image=plimg,command=unpausesong)
#             play_button.pack(side=LEFT,padx=(30,26))
#         elif stop==False:
#             play_button=Button(control,width=24,border=0,background="#dfdfdf",activebackground="#dfdfdf",image=pausimg,command=pausesong)
#             play_button.pack(side=LEFT,padx=(30,26))

#         next_button=Button(control,width=24,border=0,background="#dfdfdf",activebackground="#dfdfdf",image=neximg,command=nextsong)
#         next_button.pack(side=LEFT)
#         #\recreating

#         option_butt=Button(option_frame,border=0,bg="black",width=12,text="Add song",foreground="white")
#         option_butt.pack(pady=5,padx=9)
#         option_butt=Button(option_frame,border=0,bg="black",foreground="white",width=12,text="kk")
#         option_butt.pack(pady=5)
#         option_butt=Button(option_frame,border=0,bg="black",width=12,text="kk",foreground="white")
#         option_butt.pack(pady=5)
#         option_butt=Button(option_frame,border=0,bg="black",width=12,text="kk",foreground="white")
#         option_butt.pack(pady=5)
#         count+=1
#     else:
#         clear_frame(option_frame)
#         root.minsize(width=700,height=500)
#         count=0
 #SIDE MENU BUTTON  #0AF7C2      
# side_butt=Button(opbuttf,background="#0AF7C2",activebackground="#DEDEDE",image=opimg,width=29,border=0,command=side_menu)
# side_butt.pack(anchor=NW)



root.mainloop()

