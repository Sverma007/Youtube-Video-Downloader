from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox
import pytube
import time

master =  tk.Tk()
master.title("Youtube Downloader")
master.geometry('700x300')
master.maxsize(700,300)
master.minsize(700,250)
master.iconbitmap('tube.png')


def download_act():
    link = text.get("1.0","end-1c")
    if link=='':
        messagebox.showerror('Youtube Downloader',"Please Paste a link here!!")

    else:
        yt=pytube.YouTube(link)
        stream = yt.streams.first()
        time.sleep(2)
        text.delete(1.0,'end')
        text.insert('end','Waiting For Download.........')
        time.sleep(3)
        stream.download()
        messagebox.showinfo('Youtube Downloader','Video Has been sucessfully downloaded')
        text.delete(1.0,'end')
        text.insert('end','Your Video Has Been Downloaded Sucessfully')

def clear():
    text.delete(1.0,'end')

header = Label(master,bg="black",width="300",height="2")
header.place(x=0,y=0)
yt_logo= ImageTk.PhotoImage(Image.open('ytube.png'))
logo= Label(master,image = yt_logo,borderwidth=0)
logo.place(x=10,y=10)
caption = Label(master,text="Youtube Downloader",font=('verdana',10,'bold'))
caption.place(x=50,y=10)
yt1_logo= ImageTk.PhotoImage(Image.open('ytube_dark.png'))
logo1= Label(master,image = yt1_logo,borderwidth=0)
logo1.place(x=0,y=36)
text= Text(master,width=60,height=2,font=('verdana',10,'bold'))
text.place(x=90,y=180)
text.insert('end',"Paste Your Video Link Here...")
button = Button(master,text="Download",relief=RIDGE,font=('verdana',10,'bold'),bg="red",fg="white",command=download_act)
button.place(x=180,y=220)
button1 = Button(master,text="Clear Search Bar",relief=RIDGE,font=('verdana',10,'bold'),bg="red",fg="white",command=clear)
button1.place(x=280,y=220)
button1 = Button(master,text="Exit Downloader",relief=RIDGE,font=('verdana',10,'bold'),bg="red",fg="white",command=master.quit)
button1.place(x=430,y=220)
label1=Label(master,text="Software Designed By Suneet Verma",font=("roboto",8,"italic"),bg='black',fg='white')
label1.place(x=270,y=280)
master.mainloop()