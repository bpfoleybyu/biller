# bpfoley... brandenfoley@gmail.com
# simple project to use for work
# look up -- tkFileDialog.askopenfilename()
#       this will do prompt for you... 
# 

import tkinter as tk
import tkinter.messagebox
from PIL import ImageTk, Image
from urllib.request import urlopen

# pull in image, either from url or local
#error check it, display it.
def doThing():
    link=tk.Entry.get(E1)
    tk.messagebox.showinfo("got link: ",link)
    try:
        if "http" in link:
            im = Image.open(urlopen(link))
        else:
            im=Image.open(link)
        im.show()
        panel = tk.Label(window, image = im)
    except IOError:
        tk.messagebox.showerror("ERROR", "bad image/image link")
    

window = tk.Tk()
window.title("BillReader")
window.geometry("300x300")
path="default.png"
img = ImageTk.PhotoImage(Image.open(path))
# cv = tk.Canvas()
# cv.create_image(10,10,image=img, anchor=CENTER)
# cv.grid(row=2, column=0)

L1 = tk.Label(window, text="Bill Reader",).grid(row=0, column=1)
L2 = tk.Label(window, text="Image url/link",).grid(row=1, column=0)
panel = tk.Label(window, image = img)
E1 = tk.Entry(window, bd=5)
E1.grid(row=1, column=1)
E2 = tk.Entry(window, bd=5)
B = tk.Button(window, text="Submit", command=doThing).grid(row=2, column=1,)

window.mainloop()
