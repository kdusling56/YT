import tkinter
import customtkinter
from pytube import YouTube

# System Settings

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Our app frame
app = customtkinter.CTk()
app.geometry("900x640")

app.title("Youtube Downloader")

# Run app
app.mainloop()