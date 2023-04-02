import re
import os
from tkinter import *
import vlc
from pytube import YouTube
import random
from PIL import Image, ImageTk

fpath = os.path.abspath(__file__)[:-7]
os.chdir(fpath)
last = 0
if "cfg.txt" in os.listdir(fpath):
    f = open(fpath + "cfg.txt", "r" )
    chosendirectory = f.readline()
    print(chosendirectory[-1])
    chosendirectory = chosendirectory[:-1]
    os.chdir(chosendirectory)
    f.close()

root = Tk()
root.geometry("1400x650") ##will be dynamic according to image sizes
root.resizable(False, False)
root.title("thug prompter")
tupac = PhotoImage(file=fpath + "2pacbg2.png")
bgg = Label(root, image = tupac)
bgg.place(width=1400, height=650, x= 0, y= 0)
bgg.grid_propagate(False)
#root.wm_attributes('-transparentcolor', 'white')

title = Label(bgg, text = "tupac's quick fileprompter", bg="#111111", fg="#b0b0b0", width=444)
title.config()
title.pack(side=TOP, pady= 5)

def spindex():
    return imagearray[last % len(imagearray)]


def findtext(texti):
    return re.sub("(\.....)|(\....)", ".txt", texti)

def dchange(event):
    chosendirectory = event.widget.get("1.0", END)
    try:
        with  open(fpath + "cfg.txt", "r") as f:
             x = f.readlines()

    except: 
        with open(fpath + "cfg.txt", "x") as f:
            print("made new cfg")

    if not x:
        x = [""]
    x[0] = chosendirectory
    with open(fpath + "cfg.txt", "w") as f:
        f.writelines(x)


        
##directory
dectory = Text(bgg, height = 1, width = 40)
dectory.pack(side=TOP, pady= 5)
try : dectory.insert_text("1.0", chosendirectory)
except : print("nodirectorylul") 
dectory.bind("<<Modified>>", dchange)

##rename all images by number
rename = Button(bgg, text= "rename all files numerically")
rename.pack(side=TOP, pady= 5)

def switch(event):
    global last
    swatched = False

    if promptbox.focus_get() != promptbox:
        if event.keysym == "Right":
                ##save prompt
            with open(findtext(spindex()), "w") as f:
                print(promptbox.get("1.0", END))
                f.writelines(promptbox.get("1.0", END))
            last = last + 1
                #load prompt
            loadprompt(spindex())
            loadimage()
            root.update()
            swatched = True

        if event.keysym == "Left":
                ##save prompt
            with open(findtext(spindex()), "w") as f:
                print(promptbox.get("1.0", END))
                f.writelines(promptbox.get("1.0", END))
            last = last - 1
                #load prompt
            loadprompt(spindex())
            loadimage()
            root.update()
            swatched = True
            
        if swatched == True:
            with open(fpath + "cfg.txt", "r") as f:
                gg = f.readlines()
                gg[1] = str(last)
            with open(fpath + "cfg.txt", "w") as f:
                f.writelines(gg)
            print("it is written")
            swatched = False
        print(event.keysym)
        print(event)
        refresh()


imagearray = []
farray = os.listdir(chosendirectory)
print("balls")
for f in farray:
    if f.split(".")[-1] in ["jpg", "jpeg", "png", "jfif", "webp", "gif"]:  ##finds length of filename in case there is "."s so the last word is checked
        imagearray.append(f)
        showingimage = True
        print(f)

with open(fpath + "cfg.txt", "r") as f:
    lass = f.readlines()
    print(lass)
    if "-" in lass[1]:
        last = int(lass[1])
    else:
        last = int(lass[1])

##image viewer
def loadimage():
    global imageviewer, imgee
    try:
        imgee = ImageTk.PhotoImage(file=chosendirectory + "\\" + spindex())
        imageviewer = Label(bgg, image=imgee)
        imageviewer.place(x=442, y=120)
    except Exception as e:
        print(f"Error loading image: {e}")
print(last)
loadimage()

def exit(event):
    if event.widget.focus_get() == promptbox:
        event.widget.master.focus()
    else:
        event.widget.focus()
    return "break"

cantcontain2pac = Label(bgg, width=410, height= 226, image= PhotoImage("3pac.png"))
cantcontain2pac.place(x=969, y=359)
##prompt box
promptbox = Text(cantcontain2pac, height = 14, width = 51, background='grey', exportselection=FALSE, wrap="word")
promptbox.place(x=0, y=0)
promptbox.bind("<Return>", exit)


saveload = Frame(width= 410, height= 30, background="black")
saveload.place(x=973, y=607)

def refresh():
    


    bgg.place(width=1400, height=650, x= 0, y= 0)
    title.pack(side=TOP, pady= 5)
    dectory.pack(side=TOP, pady= 5)
    rename.pack(side=TOP, pady= 5)
    loadimage()
    cantcontain2pac.place(x=969, y=359)
    promptbox.place(x=0, y=0)
    saveload.place(x=973, y=607)
    bgg.update()
    title.update()
    dectory.update()
    rename.update()
    imageviewer.update()
    cantcontain2pac.update()
    promptbox.update()
    root.update()



def loadprompt(texto):
    global promptbox
    pfile = findtext(texto)
    try:
        with open(pfile, "r") as f:
            p = f.read().strip()
            print(str(p))
            promptbox.delete("1.0", END)
            promptbox.insert("1.0", str(p))
    except FileNotFoundError as e:
        print(f"no prompt file found for {texto}. make sure it is named the same as the image. tried: {pfile}")
        print(f"Error message: {str(e)}")
    promptbox.place(x=0, y=0)
    promptbox.update()

loadprompt(spindex())

playlist = ["https://www.youtube.com/watch?v=41qC3w3UUkU", "https://www.youtube.com/watch?v=eXvBjCO19QY", "https://www.youtube.com/watch?v=H1HdZFgR-aA", "https://www.youtube.com/watch?v=77nB_9uIcN4", "https://www.youtube.com/watch?v=5gLoEBbZNis", "https://www.youtube.com/watch?v=n8QurABRsqE", "https://www.youtube.com/watch?v=z0OCnssz2Gc"]

def on_song_end(event):
    global player
    song = YouTube(random.choice(playlist)).streams.get_audio_only().url
    vlc_instance = vlc.Instance()
    player = vlc_instance.media_player_new()
    media = vlc_instance.media_new(song)
    player.set_media(media)
    event_manager = media.event_manager()
    event_manager.event_attach(vlc.EventType.MediaPlayerEndReached, on_song_end)
    player.play()

song = YouTube(random.choice(playlist)).streams.get_audio_only().url
vlc_instance = vlc.Instance()
player = vlc_instance.media_player_new()
media = vlc_instance.media_new(song)
player.set_media(media)
event_manager = media.event_manager()
event_manager.event_attach(vlc.EventType.MediaPlayerEndReached, on_song_end)
player.play()





root.bind("<Key>", switch)
root.mainloop()

##delete button in image viewer
##ability to view and alter prompt underneath image
##left arrow goes to next iamge, other hotkeys
##abilty to set a root prompt and copy into each image.txt

#def mkaeprompts():

    
