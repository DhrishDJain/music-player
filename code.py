from tkinter import *
from tkinter import ttk
import threading
import tkinter as tk
from tkinter.font import Font
from time import sleep
root=tk.Tk()
root.config(background="#dfdfdf")
root.minsize(width=700,height=500)
#function to delete frame
def clear_frame(frame):
   frame.destroy()

#side menu button frame
opbuttf=Frame(root,background="#0AF7C2")
opbuttf.pack(side=LEFT,fill=Y)

#icons
plimg=PhotoImage(file="play.png")
opimg=PhotoImage(file="option-image.png")
previmg=PhotoImage(file="previous.png")
pausimg=PhotoImage(file="pause.png")
neximg=PhotoImage(file="next-button.png")

#frames for progress bar and play/pause button
control=Frame(root,background="#dfdfdf")
control.pack(side=BOTTOM,fill=X)
playing=Frame(root,background="#dfdfdf")
playing.pack(side=BOTTOM,fill=X)


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

ds=Font(size=0)

stop = False

def pausesong():
  # If the STOP button is pressed then terminate the loop
  global stop
  global play_button
  play_button.config(command=music_starter,image=plimg)
  
  stop = True

def playsong():
    global stop
    global play_button
    global wid
    stop = False
    play_button.config(command=pausesong,image=pausimg)
    try:
        while 100 and not stop:
            prog.set(wid)
            prog.update()
            wid+=1
            print(wid)
            sleep(1)
    except:
        pass

def music_starter():
  t = threading.Thread(target=playsong)
  t.start()


def nextsong():
    global wid
    global prog
    wid=0
    prog.set(wid)
    pausesong()

def previoussong():
    global wid
    global prog
    wid=0
    prog.set(wid)
    pausesong()
     
previous_button=Button(control,width=24,border=0,background="#dfdfdf",activebackground="#dfdfdf",image=previmg,command=previoussong)
previous_button.pack(side=LEFT,padx=(270,0))
play_button=Button(control,width=24,border=0,background="#dfdfdf",activebackground="#dfdfdf",image=plimg,command=music_starter)
play_button.pack(side=LEFT,padx=(30,26))
next_button=Button(control,width=24,border=0,background="#dfdfdf",activebackground="#dfdfdf",image=neximg,command=nextsong)
next_button.pack(side=LEFT)


#MUSIC STATUS PROGRESS BAR
prog=Scale(playing,orient=HORIZONTAL,highlightthickness=0,width=4,length=660,foreground="#dfdfdf",background="#dfdfdf",troughcolor="red")
prog.pack(side=LEFT,padx=6,fill=X)

#resizing and respacing window/button on minimizing or maxismizing window
def window_event(e=None):
    global play_button
    global next_button
    global previous_button
    global prog
    scr=root.winfo_width()
    hig=root.winfo_height()
    if scr==1366 and hig==705:
        prog.config(length=1366)
        previous_button.pack(side=LEFT,padx=(600,0))
        play_button.pack(side=LEFT,padx=(30,26))
        next_button.pack(side=LEFT)
    if (scr==700 and hig==500) or (scr==800 and hig==500) or (scr==1370 and hig==500) or (scr==705 and hig==500) :
        prog.config(length=660)
        previous_button.pack(side=LEFT,padx=(275,0))
        play_button.pack(side=LEFT,padx=(30,26))
        next_button.pack(side=LEFT)
    if count==1:
        root.minsize(width=800,height=500)


root.bind("<Map>", window_event)


#function of side menu
def side_menu():
    global count#to check weather side bar is open or not
    global option_frame#to pass side menu frame to clear frame function
    global playing#to edit frame attributes out function once they are deleted for first time
    global control#to edit frame attributes out function once they are deleted for first time
    global prog#to keep progress bar in sync with when the menu is off/on 
    global play_button#to edit button attributes out function once they are deleted for first time
    global next_button#to edit button attributes out function once they are deleted for first time
    global previous_button#to edit button attributes out function once they are deleted for first time
    if count==0:
        clear_frame(control)#to use fill=y of side menu
        clear_frame(playing)#to use fill=y of side menu
        option_frame=tk.Label(root,background="black")
        option_frame.pack(side=LEFT,fill=Y)
        #to increas size of window on opening side menu
        if root.winfo_width()==700 and root.winfo_height()==500:
            root.minsize(width=800,height=500)

        #recreating/
        control=Frame(root,background="#dedede") 
        control.pack(side=BOTTOM,fill=X)
        playing=Frame(root,background="#dedede") 
        playing.pack(side=BOTTOM,fill=X)
        
        prog=Scale(playing,orient=HORIZONTAL,highlightthickness=0,width=4,length=660,foreground="#dfdfdf",background="#dfdfdf",troughcolor="red")
        prog.pack(side=LEFT,padx=6)

        previous_button=Button(control,width=24,border=0,background="#dfdfdf",activebackground="#dfdfdf",image=previmg,command=previoussong)
        previous_button.pack(side=LEFT,padx=(270,0))
        play_button=Button(control,width=24,border=0,background="#dfdfdf",activebackground="#dfdfdf",image=plimg,command=music_starter)
        play_button.pack(side=LEFT,padx=(30,26))
        next_button=Button(control,width=24,border=0,background="#dfdfdf",activebackground="#dfdfdf",image=neximg,command=nextsong)
        next_button.pack(side=LEFT)
        #\recreating

        option_butt=Button(option_frame,border=0,bg="black",width=12,text="Add song",foreground="white")
        option_butt.pack(pady=5,padx=9)
        option_butt=Button(option_frame,border=0,bg="black",foreground="white",width=12,text="kk")
        option_butt.pack(pady=5)
        option_butt=Button(option_frame,border=0,bg="black",width=12,text="kk",foreground="white")
        option_butt.pack(pady=5)
        option_butt=Button(option_frame,border=0,bg="black",width=12,text="kk",foreground="white")
        option_butt.pack(pady=5)
        count+=1
    else:
        clear_frame(option_frame)
        root.minsize(width=700,height=500)
        count=0
 #SIDE MENU BUTTON  #0AF7C2      
side_butt=Button(opbuttf,background="#0AF7C2",activebackground="#DEDEDE",image=opimg,width=29,border=0,command=side_menu)
side_butt.pack(anchor=NW)



root.mainloop()

