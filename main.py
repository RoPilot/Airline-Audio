import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
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
        airline_select_button=tk.Button(root)
        airline_select_button["bg"] = "#f0f0f0"
        airline_select_button["borderwidth"] = "1px"
        ft = tkFont.Font(family='Arial',size=8)
        airline_select_button["font"] = ft
        airline_select_button["fg"] = "#000000"
        airline_select_button["justify"] = "center"
        airline_select_button["text"] = "SELECT"
        airline_select_button.place(x=10,y=70,width=237,height=20)
        airline_select_button["command"] = self.airline_select_button_command

        # INPUT SELECTED AIRLINE
        select_airline_input=tk.Entry(root)
        select_airline_input["borderwidth"] = "1px"
        ft = tkFont.Font(family='Arial',size=8)
        select_airline_input["font"] = ft
        select_airline_input["fg"] = "#333333"
        select_airline_input["justify"] = "center"
        select_airline_input["text"] = "SELECT AIRLINE"
        select_airline_input.place(x=10,y=50,width=237,height=20)

        # SETTINGS COG
        settings_cog=tk.Button(root)
        settings_cog["bg"] = "#f0f0f0"
        settings_cog["borderwidth"] = "0px"
        ft = tkFont.Font(family='Arial',size=18)
        settings_cog["font"] = ft
        settings_cog["fg"] = "#000000"
        settings_cog["justify"] = "center"
        settings_cog["text"] = "⚙"
        settings_cog.place(x=250,y=50,width=40,height=40)
        settings_cog["command"] = self.settings_cog_command

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
        autouse_simdata_check=tk.Checkbutton(root)
        ft = tkFont.Font(family='Arial',size=10)
        autouse_simdata_check["font"] = ft
        autouse_simdata_check["fg"] = "#333333"
        autouse_simdata_check["justify"] = "center"
        autouse_simdata_check["text"] = "Automatically Use Sim Data"
        autouse_simdata_check.place(x=10,y=110,width=282,height=30)
        autouse_simdata_check["offvalue"] = "0"
        autouse_simdata_check["onvalue"] = "1"
        autouse_simdata_check["command"] = self.autouse_simdata_check_command

        # START FLIGHT BUTTON
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
        start_flight_button["command"] = self.start_flight_button_command

    def airline_select_button_command(self):
        print("SELECTED AIRLINE")


    def settings_cog_command(self):
        print("SETTINGS")


    def autouse_simdata_check_command(self):
        print("AUTOUSE SIM DATA")


    def start_flight_button_command(self):
        print("START FLIGHT")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
