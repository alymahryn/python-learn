import tkinter as tk
from tkinter import ttk

miles = 0

def converter():
    global miles
    try:
        invalid.config(text="")
        km = int(km_entry.get())
        miles = km * 0.621371
        
        miles_result.config(text=f"Miles: {round(miles, 2)}")


    except ValueError:
        invalid.config(text="Please enter a valid number (㏎)")


window = tk.Tk()
window.title("Km to Miles Converter")
window.geometry("300x110")
window.resizable(False, False)


convert_frame = tk.Frame()

km_entry = ttk.Entry(master=convert_frame)
km_label = ttk.Label(master=convert_frame, text="Km:")

km_entry.pack(side="right")
km_label.pack(side="left")

convert_frame.pack(pady=5)

convert_button = ttk.Button(text="Convert", command=converter)
convert_button.pack()

miles_result = tk.Label(window, text=f"Miles: {round(miles, 2)}")
miles_result.pack()

invalid = tk.Label()
invalid.pack()




window.mainloop()
   
    
