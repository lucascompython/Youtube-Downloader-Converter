from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import youtube_dl

Folder_Name = ""

#file location
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        locationError.config(text=Folder_Name,fg="green")
    else:
        locationError.config(text="Please Choose Folder!!",fg="red")

#donwload video
def DownloadVideo():
    
    url = ytdEntry.get()
    
    
    ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl':Folder_Name + '/%(title)s.%(ext)s',
        }

    

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    # os.system(f"youtube-dl -o '{Folder_Name}'  -f 18 {url}")




root = Tk()
root.title("YTD Downloader")
root.geometry("350x400") #set window
root.columnconfigure(0,weight=1)#set all content in center.

ytdLabel = Label(root,text="Enter the URL of the Video or Playlist",font=("jost",15))
ytdLabel.grid()

ytdEntryVar = StringVar()
ytdEntry = Entry(root,width=50,textvariable=ytdEntryVar)
ytdEntry.grid()


saveLabel = Label(root,text="Choose the Folder",font=("jost",15,"bold"))
saveLabel.grid()

saveEntry = Button(root,width=10,bg="red",fg="white",text="Choose Path",command=openLocation)
saveEntry.grid()

locationError = Label(root,text="Error Msg of Path",fg="red",font=("jost",10))
locationError.grid()


downloadbtn = Button(root,text="Donwload",width=10,bg="red",fg="white",command=DownloadVideo)
downloadbtn.grid()

developerlabel = Label(root,text="YT downloader by Lucas",font=("jost",15))
developerlabel.grid()
root.mainloop()
