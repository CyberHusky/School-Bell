# SchoolBell

School bell in Python (with GUI - Tkinter + .grid) that can play mp3 music at the time and have GUI with timer. Insulator for Linux_x64 version (tested on Ubuntu 16.04). If you make Windows installer (or EXE) it would be helpful for me!
Tested on Python version: 2.7.12
On Pythond 3 sould work too. 

## Features

What Schoolbell program can do:
- Show current time;
- Show time for nearest bell;
- Play music on the chosen time (you could change time only in .py file, not in executable file);
- Play music when you need;
- You could choose music for play (default: sound.mp3).

Setup in source file:
- You could choose time for bell in your school. Program automatically should to adapts to your setup;
- You could choose logo of your school;
- You could choose number of lessons.

![GitHub Logo](/program_gif.gif)

## Getting Started

Preinstall next stuff:
```
apt-get install python-gst-1.0 gstreamer1.0-plugins-good gstreamer1.0-plugins-ugly gstreamer1.0-tools
```

For develop use next libraries:
```
apt-get install python-tk python3-tk tk-dev
pip install --user pillow
pip3 install --user Image

For make an exe file use:
```
pip install pyinstaller
```
with command:
```
pyinstaller --onefile <your_script_name>.py
```

If you need to change num of lesson you should change "time_bell" value and "row" value in "FILE button + entry + play again" block in source file.

## RaspberryPi 

In RaspberryPi I was use pure python execution with script in "launcher.sh" file. For auto launch I was use "crontab -e" command in terminal with next code in the end of the file:
```
@reboot DISPLAY=:0 sh /home/pi/Desktop/School-Bell-master/launcher.sh >/home/pi/Desktop/School-Bell-master/logs/cronlog  2>&1
```

Note that you should uncomment block "for RaspberryPi" in source code and comment other part of code (read source code for details). Furthermore I added sleep timer before start the program, so if you want try program not in start of OS you should wait 40 sec or just comment this code for awhile.

## Authors
Gordieiev Artem. For questions you could write me on email: gordieiev.artem@gmail.com

It would be awesome if you help me to make this program better (make a different language, make a setup function in GUI).

