#kelly j 11-16-2020.  this is a mock up of the screen I will use for dev2.  I will be plugging 
#my dev 1 into a gui, and seeing what falls out.
# this will be very rough, and will little functionality.


from tkinter import *

def afunc():
    return

rootwindow = Tk()
rootwindow.title("File 2 Json ")

#maximize window on start up
rootwindow.geometry("500x600")




FileCnt= Label(rootwindow,text = "Files Processed").place(x=10,y=10,width=130,height=25)
FilesBeingProcessed_entry =  Entry(rootwindow).place(x=150,y=10,width=160,height=25)

RecCnt= Label(rootwindow,text = "Records Processed").place(x=10,y=30,width=130,height=25)
NumberErrors =  Entry(rootwindow).place(x=150,y=30,width=160,height=25)

ErrorCnt = Label(rootwindow,text = "Errors Encountered ").place(x=10,y=50,width=130,height=25)
NumberRecsProcess =  Entry(rootwindow).place(x=150,y=50,width=160,height=25)


Convertbutton = Button(rootwindow,text = "Convert",height = 5,width=10,pady=15,command=afunc).place(x=10,y=100,width=100,height=100)
SetConfigbutton = Button(rootwindow,text = "Set Config",height = 5,width=10,pady=15,command=afunc).place(x=10,y=225,width=100,height=100)
OpenLogButton = Button(rootwindow,text = "Open Log",height = 5,width=10,pady=15,command=afunc).place(x=10,y=350,width=100,height=100)
PauseButton = Button(rootwindow,text = "Pause Processing",height = 5,width=10,pady=15,command=afunc).place(x=150,y=100,width=130,height=100)
PauseButton = Button(rootwindow,text = "Stop Processing",height = 5,width=10,pady=15,command=afunc).place(x=150,y=225,width=130,height=100)


rootwindow.mainloop()
