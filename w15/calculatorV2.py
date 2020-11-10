#kelly j 11-9-2020.  week 15 learn together, simple calculator v2
# learn together

#for this version of the calc, I am going to change this so that I can input everything in
# and then it equal. sorta like a standard calc.  somethign like 1+1+2x5
#I will use eval() to do this.  eval can be dangerous since it will do what ever I pass to it, 
#which could be very bad if I didn't control the input. But I am controling the input, and this is
#the simplest and fast way to get what I want.
#I also went ahead and bound some keys to my buttons/methods, like we would find in the calc app.

#the enter key will be Equal.  I also had to bind the num pad enter to maintain usability.
#esc will be the clear everything key.

#I didn't add any other math functions in (ie sq root, exponents).  I might do that in a V3 release.

#I used this stack over flow to get a example of the bind method of tkinter
#https://stackoverflow.com/questions/47475783/how-to-bind-enter-key-to-a-tkinter-button
#
#I used this url to find the name of the num pad enter event.
# https://www.linuxquestions.org/questions/programming-9/python-how-to-bind-tkinter-widget-to-numeric-enter-key-4175640691/

from tkinter import *
import re

def myClick():
    alable = Label(rootwindow,text = e.get())
    alable.pack()

def button_click(thenum):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(thenum))
    return

def button_clear(event=None):
    theListofNums.clear()
 
    e.delete(0,END)
    return

def doThesummary(event=None):
    theEQStr = e.get()
    theanswer = 0
    try:
        #lets double check to make sure someone isn't getting up to trouble
        onlymathreg = re.compile(r"[a-zA-Z]")
        trouble = onlymathreg.search(theEQStr)
        if (trouble == None):
            theanswer = eval(theEQStr)
        else:
            theanswer = "Invalid Math"
    except  Exception as ex:
        theanswer = "Critical Error. "
    finally:
        e.delete(0,END)
        e.insert(0,theanswer)
 

    k =1

theListofNums = []

rootwindow = Tk()
rootwindow.title("Simple Calculator")


rootwindow.bind('<Return>', lambda event=None: doThesummary())
rootwindow.bind('<KP_Enter>', lambda event=None: doThesummary())
rootwindow.bind('<Escape>', lambda event=None: button_clear())

e = Entry(rootwindow,width = 35,borderwidth = 5)

e.grid(row=0 ,column=0, columnspan = 3, padx =10,pady=10)
e.focus_set()

button1 = Button(rootwindow,text = "1",padx = 40,pady=20,command=lambda: button_click(1))
button2 = Button(rootwindow,text = "2",padx = 40,pady=20,command=lambda: button_click(2))
button3 = Button(rootwindow,text = "3",padx = 40,pady=20,command=lambda: button_click(3))
button4 = Button(rootwindow,text = "4",padx = 40,pady=20,command=lambda: button_click(4))
button5 = Button(rootwindow,text = "5",padx = 40,pady=20,command=lambda: button_click(5))
button6 = Button(rootwindow,text = "6",padx = 40,pady=20,command=lambda: button_click(6))
button7 = Button(rootwindow,text = "7",padx = 40,pady=20,command=lambda: button_click(7))
button8 = Button(rootwindow,text = "8",padx = 40,pady=20,command=lambda: button_click(8))
button9 = Button(rootwindow,text = "9",padx = 40,pady=20,command=lambda: button_click(9))
button0 = Button(rootwindow,text = "0",padx = 40,pady=20,command=lambda: button_click(0))

button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)
button0.grid(row=4,column=0) 

buttonClear = Button(rootwindow,text = "CE",padx = 40,pady=20,command=button_clear)
buttonClear.grid(row=0,column=3) 

buttonAdd = Button(rootwindow,text = "+",padx = 40,pady=20,command=lambda: button_click("+"))
buttonAdd.grid(row=1,column=3) 

buttonMinus = Button(rootwindow,text = "-",padx = 40,pady=20,command=lambda: button_click("-"))
buttonMinus.grid(row=2,column=3) 

buttonDiv = Button(rootwindow,text = "/",padx = 40,pady=20,command=lambda: button_click("/"))
buttonDiv.grid(row=3,column=3) 

buttonTimes = Button(rootwindow,text = "*",padx = 40,pady=20,command=lambda: button_click("*"))
buttonTimes.grid(row=4,column=3) 



buttonEq = Button(rootwindow,text = "=",padx = 40,pady=20,command=doThesummary)
buttonEq.grid(row=5,column=3) 




rootwindow.mainloop()