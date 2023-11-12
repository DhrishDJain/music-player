from tkinter import *
import tkinter as tk
root=Tk()
root.config(background="#DEDEDE")
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
        option_frame=tk.Label(root,background="BLACK")
        option_frame.pack(side=LEFT,fill=Y)
        play_butt.place(x=115)
        play_butt.update()
        option_butt=Button(option_frame,width=12)
        option_butt.pack(side=BOTTOM)
        option_butt=Button(option_frame,width=12,text="kk")
        option_butt.pack(padx=9)
        option_butt=Button(option_frame,width=12)
        option_butt.pack()
        option_butt=Button(option_frame,width=12)
        option_butt.pack()
        print(option_frame.winfo_children())
        count+=1
    else:
        clear_frame()
        count=0
        play_butt.place(x=0)
        play_butt.update()

# butt_label=Label(background="#696969")
# butt_label.pack(anchor=NW)
opimg=PhotoImage(file="option image.png")
play_butt=Button(root,background="black",image=opimg,width=30,border=0,command=side_menu)
play_butt.pack(anchor=NW)


root.mainloop()

