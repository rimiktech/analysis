#write a program to created a digital clock with use Tkinter Module ?
from tkinter import *
from tkinter.ttk import *


from time import strftime


root = Tk()
root.title('DIGITAL CLOCK')


def time():
	string = strftime('%H:%M:%S %p')
	lbl.config(text = string)
	lbl.after(300, time)


lbl = Label(root, font = ('ds-digital', 25, 'bold'),
			background = 'green',
			foreground = 'black')


lbl.pack(anchor = 'center')
time()

mainloop()
