from tkinter import tk

master = tk.Tk()
w = tk.Scale(master, from_=0, to=42)
w.pack()
w = tk.Scale(master, from_=0, to=200, orient=tk.HORIZONTAL)
w.pack()

mainloop()

