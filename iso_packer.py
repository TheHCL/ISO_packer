import tkinter as tk
import os
from tkinter import filedialog
import threading


iso_name=""


def file_loc():
	global f
	f=filedialog.askdirectory()
	f=f.replace("/","\\")
def output_loc():
	global o
	o=filedialog.askdirectory()
	o=o.replace("/","\\")

def run_all():
#OSCDIMG.exe -lWIN10_OS -m -u2 -bD:\windows_install\boot\etfsboot.com D:\windows_install D:\WIN10.iso
	a = (var.get()).upper()
	lock.acquire()
	os.system("oscdimg.exe -l"+a+" -m -u2 -betfsboot.com "+f+" "+o+"\\"+a+".iso")
	lock.release()

def thread_run():
	threading.Thread(target=run_all).start()

#def get_iso_name():
lock=threading.Lock()
window = tk.Tk()
window.geometry('300x150')
window.title("ISO Packer")
var=tk.StringVar()
content = tk.Entry(window,textvariable=var).pack()


tk.Button(window,text="Files Location",command=file_loc).pack()
tk.Button(window,text="output Location",command=output_loc).pack()
tk.Button(window,text="run",command=thread_run).pack()
window.mainloop()

