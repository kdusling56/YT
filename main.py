import tkinter
import customtkinter
from pytube import YouTube

def startConversion():
    try:
        ytLink = link.get()
        ytObject = Youtube(ytLink)
        mp3 = ytObject.streams.get_audio_only()
        mp3.download()
    except:
        print("YouTube link is invalid!")
    print("Download Complete!")

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
convert.pack(padx =20, pady=20)

# Run app
app.mainloop()