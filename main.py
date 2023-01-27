import tkinter as tk
import tkinter.font as tkFont
import time
from SimConnect import *
import time
import os
import pygame

# VARS
flightStarted = False
pygame.mixer.init()

if os.sys.platform == ("win32" or "win64"):
    os.add_dll_directory(r"C:\Users\ropil\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\pygame")

# STATUS FORM (State, Speed, Altitude, VS, audio, delay.)
# Speed, where None is not used
# Altitude where None is not used
# VS where 9999 is not used.
# Audio where None is not used.
# Delay where None is not used.
buttons = {}

currentState = {
    "Departure-Parked": [True, None, None, None, "HoldMyHand.mp3", None], 
    "Pushback": [False, 5, None, None, "Saftey", 8], 
    "Taxi-Out": [False, 10, None, None, "Saftey", None], 
    "Takeoff": [False, 40, None, None, None, None], 
    "Climb": [False, 230, None, 9999, "Climb", 10], 
    "Cruise": [False, None, None, 0, "Cruise", 600], 
    "Decent": [False, None, None, None, "Descent", 600], 
    "Landing": [False, 180, 3000, None, None, None], 
    "Taxi-In": [False, 50, None, None, "Final Audio", None], 
    "Arrival-Parked": [False, 0, None, None, None, None]
    }

positions = {
    1: [10, 180],
    2: [10, 240],
    3: [10, 300],
    4: [10, 360],
    5: [10, 420],
    6: [155, 180],
    7: [155, 240],
    8: [155, 300],
    9: [155, 360],
    10:[155, 420],
    }

def checkState():
    trueState = None
    nextState = None
    for item in currentState:
        if currentState[item][0] == True: 
            trueState = item

            try:
                nextState = list(currentState)[list(currentState).index(item) + 1]
            except:
                nextState = None
            break

    return trueState, nextState

def getData(trueState, nextState):
    # FIND CURRENT DATA FROM SIM
    PLANE_ALTITUDE = aq.get("PLANE_ALTITUDE")
    AIRSPEED_TRUE = aq.get("AIRSPEED_TRUE")
    VERTICAL_SPEED = round(aq.get("VERTICAL_SPEED"), 4)
    currentData = [AIRSPEED_TRUE, PLANE_ALTITUDE, VERTICAL_SPEED]
    
    # FIND CURRENTSTATES DATA
    currentLows = currentState[trueState]
    nextLows = currentState[nextState]
    
    return currentData, currentLows, nextLows
    
#def startFlight():
    #while flightStarted == True:
        #time.sleep(2)
        #trueState, nextState = checkState()
        #currentData, currentLows, nextLows = getData(trueState, nextState)
        
        # CHECK TO SEE IF A NEW STATE IS DETECTED
    
def play_audio_command(key):
    print("Key: " + key)
    value = buttons[key].cget("text")
    for button in buttons:
        text = buttons[button].cget("text")
        
        print(text)
    pygame.mixer.music.load("Audio\{0}\{1}.mp3".format(select_airline_input.get(), value))
    pygame.mixer.music.play()
        
        
def airline_select_button_command():
    global namesInUse
    airlineSelected = select_airline_input.get()
    validAirlines = os.listdir("Audio")

    if airlineSelected in validAirlines:
        if len(buttons) == 0:
            pass
        else:
            while len(buttons) > 0:
                i = len(buttons)
                item = buttons.pop("button" + str(i))
                print(item)
                item.destroy()
                
        print("Airline is Found")
        audios = os.listdir("Audio\{0}".format(airlineSelected))
        i = 0
        for item in audios:
            i += 1
            text = item.strip(".mp3")
            newName = (text.lower()) + "Button"
            # CREATE BUTTON
            newButtonName = "button" + str(i)
            buttons[newButtonName] = tk.Button(root, borderwidth="1px", font=tkFont.Font(family='Arial',size=8), fg="#333333", justify="center", text=text, command=lambda key=newButtonName:play_audio_command(key))
            buttons[newButtonName].place(x=(positions[i])[0],y=(positions[i])[1],width=135,height=50)
            #buttons[newButtonName].config(command=lambda: play_audio_command(newButtonName))
        
        print(buttons)

                    
def settings_cog_command():
    print("SETTINGS")


def autouse_simdata_check_command():
    print("AUTOUSE SIM DATA")


def start_flight_button_command():
    print("START FLIGHT")
    global flightStarted
    flightStarted = True
    startFlight()

root = tk.Tk()

def createUI():
    
    #setting title
    root.title("Airline Audio")
    #setting window size
    width=300
    height=500
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(alignstr)
    root.resizable(width=False, height=False)

    # TITLE TEXT
    title_text=tk.Label(root)
    title_text["bg"] = "#ff4b4b"
    title_text["borderwidth"] = "0px"
    ft = tkFont.Font(family='Arial',size=13)
    title_text["font"] = ft
    title_text["fg"] = "#ffffff"
    title_text["justify"] = "center"
    title_text["text"] = "IN-FLIGHT ANNOUNCEMENTS"
    title_text["relief"] = "raised"
    title_text.place(x=0,y=0,width=300,height=38)

    # SUBMIT SELECTED AIRLINE
    global airline_select_button
    airline_select_button=tk.Button(root)
    airline_select_button["bg"] = "#f0f0f0"
    airline_select_button["borderwidth"] = "1px"
    ft = tkFont.Font(family='Arial',size=8)
    airline_select_button["font"] = ft
    airline_select_button["fg"] = "#000000"
    airline_select_button["justify"] = "center"
    airline_select_button["text"] = "SELECT"
    airline_select_button.place(x=10,y=70,width=237,height=20)
    airline_select_button["command"] = airline_select_button_command
    # INPUT SELECTED AIRLINE
    global select_airline_input
    select_airline_input=tk.Entry(root)
    select_airline_input["borderwidth"] = "1px"
    ft = tkFont.Font(family='Arial',size=8)
    select_airline_input["font"] = ft
    select_airline_input["fg"] = "#333333"
    select_airline_input["justify"] = "center"
    select_airline_input["text"] = "SELECT AIRLINE"
    select_airline_input.place(x=10,y=50,width=237,height=20)
    # SETTINGS COG
    global settings_cog
    settings_cog=tk.Button(root)
    settings_cog["bg"] = "#f0f0f0"
    settings_cog["borderwidth"] = "0px"
    ft = tkFont.Font(family='Arial',size=18)
    settings_cog["font"] = ft
    settings_cog["fg"] = "#000000"
    settings_cog["justify"] = "center"
    settings_cog["text"] = "⚙"
    settings_cog.place(x=250,y=50,width=40,height=40)
    settings_cog["command"] = settings_cog_command
    # DIVIDER
    divider1=tk.Label(root)
    divider1["bg"] = "#000000"
    ft = tkFont.Font(family='Arial',size=10)
    divider1["font"] = ft
    divider1["fg"] = "#333333"
    divider1["justify"] = "center"
    divider1["text"] = ""
    divider1.place(x=0,y=100,width=300,height=1)
    # AUTO USE SIM DATA CHECK
    global autouse_simdata_check
    autouse_simdata_check=tk.Checkbutton(root)
    ft = tkFont.Font(family='Arial',size=10)
    autouse_simdata_check["font"] = ft
    autouse_simdata_check["fg"] = "#333333"
    autouse_simdata_check["justify"] = "center"
    autouse_simdata_check["text"] = "Automatically Use Sim Data"
    autouse_simdata_check.place(x=10,y=110,width=282,height=30)
    autouse_simdata_check["offvalue"] = "0"
    autouse_simdata_check["onvalue"] = "1"
    autouse_simdata_check["command"] = autouse_simdata_check_command
    # START FLIGHT BUTTON
    global start_flight_button
    start_flight_button=tk.Button(root)
    start_flight_button["activebackground"] = "#1aff00"
    start_flight_button["bg"] = "#f0f0f0"
    start_flight_button["borderwidth"] = "1px"
    ft = tkFont.Font(family='Arial',size=10)
    start_flight_button["font"] = ft
    start_flight_button["fg"] = "#000000"
    start_flight_button["justify"] = "center"
    start_flight_button["text"] = "Start Flight"
    start_flight_button.place(x=0,y=140,width=300,height=30)
    start_flight_button["command"] = start_flight_button_command

createUI()
root.mainloop()