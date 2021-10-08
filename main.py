from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import font
from pytube import YouTube

Folder_Name = ""

#Function for file location
def Openlocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    # print(Folder_Name)
    
    if(len(Folder_Name) > 1):
        locationError.config(text=Folder_Name , fg="#004b23")
    else:
        locationError.config(text="Please Choose folder",fg="#eae2b7")

#Function for downloading the video
def downloadvideo():
    if(len(Folder_Name) < 1):
        Openlocation()

    choice = ytchoice.get()
    url = ytEntryVar.get()

    # print(url)
    
    if(len(url) > 1):
        ytError.config(text="")
        try:
            yt = YouTube(url)
        except:
            ytError.config(text="Invalid!! URL",fg="red")
            ytError.place(x = 165 , y = 380)

        try:

            if(choice == choices[0]):
                select = yt.streams.filter(progressive=True,file_extension='mp4').last()
                
            elif(choice == choices[1]):
                select = yt.streams.filter(progressive=True).first()
                
            elif(choice == choices[2]):
                select = yt.streams.filter(only_audio=True).first()
                
            else:
                ytError.config(text="Paste Link again!!",fg="red")
                ytError.place(x = 165 , y = 380)

        except:
            ytError.config(text="Invalid!! URL",fg="red")
            ytError.place(x = 165 , y = 380)

    else:
        ytError.config(text="Invalid!! LINK",fg="red")

    try:
        select.download(Folder_Name)
        ytcomplete.config(text="Download Completed!!",fg="#004b23")

    except:
        ytError.config(text="Invalid!! URL")

if __name__ == "__main__":

    root = Tk()
    root.title("Youtube Downloader")
    root.geometry("400x450") #Sets Window
    root.minsize(450,450)
    root.maxsize(450,450)
    root.columnconfigure(0 , weight=1) #Set all content center
    root.configure(bg='#eae2b7')

    # GUI
    URLlabel = Label(root , text = "Enter The URL of The Video" , font = ("calibri",25,"bold") , bg='#eae2b7')
    URLlabel.place(x = 36 , y = 20)

    # Entry Box
    ytEntryVar = StringVar()
    ytEntry = Entry(root , font = ("calibri",15) , fg= '#3d405b', bg= '#e9edc9' ,textvariable=ytEntryVar)
    ytEntry.place(x = 72 , y = 80 , width=300 , height=30)

    #Asking Save file Label
    savelabel = Label(root , text="Save the Video file",font=('calibri',18,"bold") , bg='#eae2b7')
    savelabel.place(x = 132 , y = 150)

    #btn of save file
    saveEntry = Button(root, width=10,bg="#d62828",fg="white" , font=('calibri',10,"bold") ,text="Choose Path" , command=Openlocation)
    saveEntry.place(x = 182 , y = 195)

    #Error Message for not choosing location
    locationError = Label(root , text="",fg="red",font=('calibri',10) , bg='#eae2b7')
    locationError.place(x = 160 , y = 225)

    #Download Quality
    ytQuality = Label(root ,text="Select Quality",font=("calibri",18,"bold") , bg='#eae2b7')
    ytQuality.place(x = 152 , y = 265)

    #choice box for quality

    #Styling combo box
    style= ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox", fieldbackground= "#e9edc9", background= "#3d405b")

    choices = ["High","Low","Only Audio"]
    ytchoice = ttk.Combobox(root , font = ("calibri",10) , values=choices)
    ytchoice.place(width= 100 , x = 172 , y = 305)


    #Download Button
    ytdownload = Button(root, width=10,bg="#d62828",fg="white" , font=('calibri',10,"bold") ,text="Download" , command=downloadvideo)
    ytdownload.place(x = 180 , y = 337)

    #Error Msg
    ytError = Label(root,text="",fg="red",font=("calibri" , 15) , bg='#eae2b7')
    ytError.place(x = 165 , y = 380)

    #Download Complete
    ytcomplete = Label(root,text="",fg="#004b23",font=("calibri" , 15 , "bold") , bg='#eae2b7')
    ytcomplete.place(x = 120 , y = 380)


    root.mainloop()
