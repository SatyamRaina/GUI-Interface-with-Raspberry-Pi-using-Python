from tkinter import *  #to access functions from tkinter
import RPi.GPIO as GPIO

red = 10
blue = 11
green = 12

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)


win = Tk()
win.title("LED Toggler")
win.geometry('300x300')
#myFont = tkinter.font.Font(family = "Verdana", size = 12, weight = "bold")

var = IntVar()         #for holding and accessing integer data
def ledToggle():
    global var
    Clear() 
    if(var.get()==1):
        print("RED")
        redFn()
    elif(var.get()==2):
        print("BLUE")
        blueFn()
    elif(var.get()==3):
        print("GREEN")
        greenFn()
    else:
        Clear()
        print("Resetting...")


def Clear():
    global red, blue, green
    GPIO.output(red, GPIO.LOW)
    GPIO.output(blue, GPIO.LOW)
    GPIO.output(green, GPIO.LOW)
    
def redFn():
    global red
    GPIO.output(red, GPIO.HIGH)

def blueFn():
    global blue
    GPIO.output(blue, GPIO.HIGH)

def greenFn():
    global green
    GPIO.output(green, GPIO.HIGH)
    

redButton = Radiobutton(win, text = "Red", variable = var, value = 1, command = ledToggle)
redButton.place(relx=0.5, rely=0.3, anchor = CENTER) #Place resizes itself within the frame

blueButton = Radiobutton(win, text = "Blue", variable = var, value = 2, command = ledToggle)
blueButton.place(relx=0.5, rely=0.4, anchor = CENTER)

greenButton = Radiobutton(win, text = "Green", variable = var, value = 3, command = ledToggle)
greenButton.place(relx=0.5, rely=0.5, anchor = CENTER)

resetButton = Radiobutton(win, text = "Reset", variable = var, value = 4, command = ledToggle)

resetButton.place(relx=0.5, rely=0.6, anchor = CENTER)

win.mainloop()
GPIO.cleanup