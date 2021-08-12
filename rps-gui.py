import tkinter as tk

# button
def hard_reset():
	print("Hard reset happens.");
# display
def get_voltage():
	print("Get voltage.");
# box
def set_voltage():
	print("Set voltage.");
# display
def get_current():
	print("Get current.");
# box
def set_current_limit():
	print("Set current limit.");
# drop menu
def set_channel():
	print("Set channel.");
# box
def set_baud_rate():
	print("Set baud rate.");
	
# create a main window
gui = tk.Tk(screenName=None,  baseName=None,  className=' Remote Power Supply GUI',  useTk=1)

frame = tk.Frame(gui)
frame.pack()

button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)

slogan = tk.Button(frame,
                   text="Hello",
                   command=hard_reset)
slogan.pack(side=tk.RIGHT)

# infinite loop used to run the application
gui.mainloop()

