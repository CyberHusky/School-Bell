import Tkinter as tk
import time
# Tkinter import Separator, Style
#from Tkinter import *
from playsound import playsound
from PIL import Image


# ====================================

begin_ms = "Welcome to School bell app. This app will help you to automatizate your school bell. \n What you need?\n-PC with Ubuntu;\n-Installed Python 3.\nAuthor of app: Gordieiev Artem (gordieiev.artem@gmail.com). V1.0. \n\n"
print(begin_ms)

# ====================================

fields = ['Lesson 1:' , 'Lesson 2:', 'Lesson 3:', 'Lesson 4:' , 'Lesson 5:' , 'Lesson 6:']
len(fields)

global mute_logo_visible
#times_from  = [9:15]
#times_to	 = []

# playsound("/home/artem/PycharmProjects/SchoolBell/sound.mp3") # Play sound


def buttonMute():
	global mute_logo_visible

	if mute_logo_visible == True:
		mute_logo.grid_forget()
		mute_logo_visible = False
	else:
		mute_logo.grid(row=8, column=1, columnspan=1, rowspan=1, sticky="W")
		mute_logo_visible = True


if __name__ == '__main__':

	window = tk.Tk()
	window.title('SchoolBell. V1.0')

	# === Labels ===
	for i in range(1, len(fields)):
		tk.Label(window, text=fields[i-1], font=("Ubuntu", 8)).grid(row=i)
		tk.Entry(window, state='readonly').grid(row=i, column=1)
		tk.Entry(window, state='readonly').grid(row=i, column=2)

	tk.Label(window, text="From:", font=("Ubuntu", 8)).grid(row=0, column=1)
	tk.Label(window, text="To:", font=("Ubuntu", 8)).grid(row=0, column=2)

	button_mute = tk.Button(window,
								text = "Mute", font=("Ubuntu", 8),
								command = buttonMute).grid(row=8, column=0)

	#tk.Separator(window,orient="vertical").grid(column=3, rowspan=7)

	#column = 3
	localtime = time.asctime( time.localtime(time.time()) )
	#print "Local time is:", localtime.tm_year
	print "Local time is:", datetime.now().strftime('%Y-%m-%d %H:%M:%S')

	tk.Entry(window, state='readonly').grid(row=1, column=3)
	tk.Label(window, text="TIME NOW:", font=("Ubuntu", 14)).grid(row=2, column=3)
	tk.Entry(window, state='readonly').grid(row=3, column=3)
	tk.Label(window, text="TIME TO BELL:", font=("Ubuntu", 14)).grid(row=4, column=3)
	tk.Entry(window, state='readonly').grid(row=5, column=3)

	#logo1 = tk.PhotoImage(file="volume-off-indicator.png")	
	#tk.Label(window, 
	#				image = logo1).grid(row=8, column=1, columnspan=1, rowspan=1, sticky="W")
	
	#mute_img = Image.open("volume-off-indicator.png")
	mute_photo = tk.PhotoImage(file="volume-off-indicator.png")

	mute_logo = tk.Label(image = mute_photo)
	mute_logo.image = mute_photo
	mute_logo.grid(row=8, column=1, columnspan=1, rowspan=1, sticky="W")
	mute_logo_visible = True
	
	#

	#column = 4
	button_file = tk.Button(window, font=("Ubuntu", 8),
								text = "FILE...").grid(row=1, column=4)

	#column=5   BELL LOGO

	#bell_img = Image.open("bell-outline.png")
	bell_photo = tk.PhotoImage(file="bell-outline.png")

	bell_logo = tk.Label(image = bell_photo)
	bell_logo.image = bell_photo
	bell_logo.grid(row=1, column=5, columnspan=2, rowspan=3)

	window.mainloop()
'''
	logo2 = tk.PhotoImage(file="bell-outline.png")
	
	label_logo2 = tk.Label(window, 
					image = logo2).grid(row=1, column=5, columnspan=2, rowspan=3, sticky="W"+"E"+"N"+"S")

	
	label_logo2 = tk.Label(window, image = logo2)
	label_logo2 = grid(row=1, column=5, columnspan=2, rowspan=3, sticky="W"+"E"+"N"+"S")
	#logo2.grid(row=1, column=5, columnspan=2, rowspan=3, sticky="W"+"E"+"N"+"S")

	
	#label_logo2.set(state = disabled)
'''
	
'''
	

	

	tk.Label(window, 
					text = "Hello2!",
					fg 	 = "red").pack(side="left")
	
	button1 = tk.Button(window,
					text = "Button1").pack()

'''

	