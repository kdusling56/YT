import tkinter
import customtkinter
from pytube import YouTube

def convert():
    try:
         

# System Settings

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Our app frame
app = customtkinter.CTk()
app.geometry("900x640")

app.title("Youtube Downloader")

# Adding UI Elements
title = customtkinter.CTkLabel(app, text="Insert a YouTube link")
title.pack(padx=10, pady=10)

# Link Input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=500, height=50, textvariable=url_var)
link.pack()

# Download Button
convert = customtkinter.CTkButton(app, text="Convert", command=startConversion)

# Run app
app.mainloop()