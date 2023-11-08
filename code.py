from tkinter import *
import tkinter as tk
root=Tk()
root.config(background="#d1d1d1")
root.minsize(width=700,height=500)

def clear_frame(event=None):
   global option_frame
#    for widgets in option_frame.winfo_children():
#       widgets.destroy()
   option_frame.destroy()
global option_frame
count=0
def side_menu():
    global count
    global option_frame
    if count==0:
        option_frame=tk.Label(root,background="#696969")
        option_frame.pack(side=LEFT,fill=Y)
        option_butt=Button(option_frame,width=12)
        option_butt.pack(side=BOTTOM)
        option_butt=Button(option_frame,width=12,text="kk")
        option_butt.pack()
        option_butt=Button(option_frame,width=12)
        option_butt.pack()
        option_butt=Button(option_frame,width=12)
        option_butt.pack()
        count+=1
    else:
        clear_frame()
        count=0


play_butt=Button(root,background="black",width=3,border=0,command=side_menu)
play_butt.pack(anchor=NW)


root.mainloop()

