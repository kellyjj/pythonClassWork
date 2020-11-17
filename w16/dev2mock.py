#kelly j 11-16-2020.  this is a mock up of the screen I will use for dev2.  I will be plugging 
#my dev 1 into a gui, and seeing what falls out.
# this will be very rough, and will little functionality.


from tkinter import *

def afunc():
    return

rootwindow = Tk()
rootwindow.title("File 2 Json ")

#maximize window on start up
w, h = rootwindow.winfo_screenwidth(), rootwindow.winfo_screenheight()
rootwindow.geometry("%dx%d+0+0" % (w, h))


#set up frames for each part
status_frame = LabelFrame(rootwindow,text = "Status ")

status_frame.grid(row=0,column =0,rowspan=1,sticky=W+E)
status_frame.grid_columnconfigure(0,weight=1)
status_frame.grid_rowconfigure(0, weight=1)

status_entry =  Text(status_frame,height = 5, width = 52).grid(row=0,column=0, sticky=W+E)

#set up frames for buttons, commands
command_frame = LabelFrame(rootwindow,text = "Commands ",height = 15)

command_frame.grid(row=1,column =0,rowspan=1,sticky=W+E)
command_frame.grid_columnconfigure(1,weight=1)
command_frame.grid_rowconfigure(1, weight=1)

FileCnt= Label(command_frame,text = "Files Processed").grid(row=0,column=0)
FilesBeingProcessed_entry =  Entry(command_frame).grid(row=0,column=1)

RecCnt= Label(command_frame,text = "Records Processed").grid(row=2,column=0)
NumberErrors =  Entry(command_frame).grid(row=2,column=1)

ErrorCnt = Label(command_frame,text = "Errors Encountered ").grid(row=1,column=0)
NumberRecsProcess =  Entry(command_frame).grid(row=1,column=1)


Convertbutton = Button(command_frame,text = "Convert",height = 5,width=10,command=afunc).grid(row=3, column=0)
SetConfigbutton = Button(command_frame,text = "Set Config",height = 5,width=10,command=afunc).grid(row=3, column=1)
OpenLogButton = Button(command_frame,text = "Open Log",height = 5,width=10,command=afunc).grid(row=3, column=2)


w, h = rootwindow.winfo_screenwidth(), rootwindow.winfo_screenheight()
rootwindow.geometry("%dx%d+0+0" % (w, h))

rootwindow.grid_columnconfigure(0,weight=1)
rootwindow.mainloop()
