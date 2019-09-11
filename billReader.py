# bpfoley... brandenfoley@gmail.com
# simple project to use for work
# look up -- tkFileDialog.askopenfilename()
#       this will do prompt for you... 
# 

import tkinter as tk
import tkinter.messagebox
import pyscreenshot as ImageGrab
import datetime
import PIL.ImageGrab
from PIL import ImageTk, Image
from urllib.request import urlopen

# pull in image, either from url or local
#error check it, display it.
# def doThing():
#     link=tk.Entry.get(E1)
#     tk.messagebox.showinfo("got link: ",link)
#     try:
#         if "http" in link:
#             im = Image.open(urlopen(link))
#         else:
#             im=Image.open(link)
#         im.show()
#         panel = tk.Label(window, image = im)
#     except IOError:
#         tk.messagebox.showerror("ERROR", "bad image/image link")
#     return

def catchScreen():
    #use pil.imagegrab instead
    im = PIL.ImageGrab.grab()
    im.save('test.png')
    
    return
    

window = tk.Tk()
window.title("BillReader")
window.geometry("300x300")
# img = ImageTk.PhotoImage(Image.open(path))
# cv = tk.Canvas()
# cv.create_image(10,10,image=img, anchor=CENTER)
# cv.grid(row=2, column=0)

L1 = tk.Label(window, text="Bill Reader",).grid(row=0, column=1)
B = tk.Button(window, text="Grab Screen", command=catchScreen).grid(row=2, column=1)

window.mainloop()
