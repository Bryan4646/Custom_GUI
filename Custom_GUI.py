#Custom Made GUI - to turn lights on depending on selected button
from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

win = Tk()
win.title("Traffic Lights")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

#Hardware

led1 = LED(10, False)
led2 = LED(9, False)
led3 = LED(11, False)


#Event Functions
def Red():
    if led1.is_lit:
        led1.off()
        ledButton1["text"] = "Turn Red LED on"
    else:
        led1.on()
        ledButton1["text"] = "Turn Red LED off"

def Yellow():
    if led2.is_lit:
        led2.off()
        ledButton2["text"] = "Turn Yellow LED on"
    else:
        led2.on()
        ledButton2["text"] = "Turn Yellow LED off"   

def Green():
    if led3.is_lit:
        led3.off()
        ledButton3["text"] = "Turn Green LED on"
    else:
        led3.on()
        ledButton3["text"] = "Turn Green LED off"

def close():
    GPIO.cleanup()
    win.destroy()

#Widgets
ledButton1 = Button(win, text = 'Turn Red LED on', font = myFont, command = Red, bg = 'red' , height =  1, width = 24)
ledButton1.grid (row=0, column=1)

ledButton2 = Button(win, text = 'Turn Yellow LED on', font = myFont, command = Yellow, bg = 'yellow' , height =  1, width = 24)
ledButton2.grid (row=2, column=1)

ledButton3 = Button(win, text= 'Turn Green LED on', font = myFont, command = Green, bg = 'green' , height =  1, width = 24)
ledButton3.grid (row=3, column=1)

ledButton4 = Button(win, text = 'Exit', font = myFont, command = close, bg = 'pink' , height =  1, width = 6)
ledButton4.grid (row=4, column=1)

win.protocol("WM_DELETE_WINDOW", close)
win.mainloop()
