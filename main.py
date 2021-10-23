import tkinter as tk
from pytube import YouTube
import os

def downloadVideo():
    try:
        url = YouTube(str(link.get()))
        video = url.streams.filter(res = "720p").first()
        video.download()
        tk.Label(window, text = "Your YouTube video finished downloading and has been stored in " + os.getcwd(), font = ("PT Mono", 7, "bold"),fg = "White",bg = "#EC7063").place(x = 6 , y = 140)
    except:
        tk.Label(window, text = "The program ran into a fatal error :(", font = ("PT Mono", 7, "bold"),fg = "White",bg = "#EC7063").place(x = 6 , y = 140)  

def downloadAudio():
    try:
        url = YouTube(str(link.get()))
        audio = url.streams.filter(only_audio = True).first()
        audioDL = audio.download()
        base, ext = os.path.splitext(audioDL)
        audioRename = base + ".mp3"
        os.rename(audioDL, audioRename)
        tk.Label(window, text = "Your YouTube audio finished downloading and has been stored in " + os.getcwd(), font = ("PT Mono", 7, "bold"),fg = "White",bg = "#EC7063").place(x = 6 , y = 140)
    except:
        tk.Label(window, text = "The program ran into a fatal error :(", font = ("PT Mono", 7, "bold"),fg = "White",bg = "#EC7063").place(x = 6 , y = 140)

window = tk.Tk()
window.geometry("1200x250")
window.config(bg = "#181620")
window.resizable(width = False,height = False)
window.title("YouTube DL")
 
link = tk.StringVar()
tk.Label(window,text = "YouTube DL", font = ("PT Mono", 20, "bold"),fg = "#b09e99",bg = "#181620").pack()
tk.Label(window, text = "Paste Your YouTube Link Here:", font = ("PT Mono", 20, "bold"),fg = "#b09e99",bg = "#181620").place(x = 150 , y = 60)
link_enter = tk.Entry(window, width = 47 ,textvariable = link,font = ("PT Mono", 15, "bold"),bg = "#181620").place(x = 150, y = 100)
tk.Button(window,text = "DOWNLOAD VIDEO", font = ("PT Mono", 15, "bold") ,fg = "white",bg = "#b09e99", padx = 2,command = downloadVideo).place(x = 745 ,y = 140)
tk.Button(window,text = "DOWNLOAD AUDIO", font = ("PT Mono", 15, "bold") ,fg = "white",bg = "#b09e99", padx = 2,command = downloadAudio).place(x = 745 ,y = 200)
 
window.mainloop()