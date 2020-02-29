import datetime
import os
import threading
import time
import tkinter as tk
from PySide2 import QtWidgets, QtGui
import sys

from System_Tray import *
from playsound import playsound

from __init__ import debugging, image_path
from Character_Manager import CharacterManager

isPlaying = False
CharacterManager.generate_character_list()
app_is_aslive = True

def create_character_list(listbox):
    for character in CharacterManager.character_list:
        if debugging:
            print(character.name)
        listbox.insert(character.index, character.name)

def update_current_time():
    time_label.config(text=datetime.datetime.now().strftime("%H:%M:%S"))
    root.after(1000,update_current_time)

def get_selected_character():
    current_character_label['text']=lb.get('active')
    CharacterManager.set_current_character(lb.get('active'))
    image_label.config(image=image[CharacterManager.current_character.index])
    if debugging:
        print(CharacterManager.current_character.name)
    if not isPlaying:
        is_playing = True
        playsound(CharacterManager.file_list[24],False)
        is_playing = False

def play_audio(index):
    if not isPlaying:
        is_playing = True
        playsound(CharacterManager.file_list[index],False)
        is_playing = False

timestamp = ["00:00:00","01:00:00","02:00:00","03:00:00","04:00:00","05:00:00","06:00:00","07:00:00","08:00:00","09:00:00","10:00:00","11:00:00","12:00:00","13:00:00","14:00:00","15:00:00","16:00:00","17:00:00","18:00:00","19:00:00","20:00:00","21:00:00","22:00:00","23:00:00"]
def check_for_time():
    while(app_is_aslive):
        for index in range(len(timestamp)):
            if(datetime.datetime.now().strftime("%H:%M:%S")==timestamp[index]):
                play_audio(index)
                time.sleep(3300)

def generaete_image():
    image_list = []
    for character in CharacterManager.character_list:
        image_list.append(tk.PhotoImage(file=image_path+character.name+".gif"))
    return image_list

def play_character_introduction():
    if not isPlaying:
        is_playing = True
        playsound(CharacterManager.file_list[25],False)
        is_playing = False


time_thread = threading.Thread(target=update_current_time)
check_thread = threading.Thread(target=check_for_time)

root = tk.Tk()
root.title("Kancolle Voice Clock by Conrad")
root.resizable(False,False)
root.config(bg="white")
root.protocol("WM_DELETE_WINDOW", root.withdraw)
icon_img=tk.PhotoImage("icon.ico")
root.iconbitmap(icon_img)

## set system tray
app = QtWidgets.QApplication(sys.argv)
app.font("Times New Roman")
w = QtWidgets.QWidget()
tray_icon = SystemTrayIcon(QtGui.QIcon("icon.png"), root,w)
tray_icon.show()
##

image=generaete_image()

canvas = tk.Canvas(root, width=500, height=500, bg="white")
canvas.pack()

message_frame=tk.Frame(root,bg="white")
message_frame.place(relwidth=0.3, relheight=0.3, relx=0.65, rely=0.05)
message_text = "Currently, the play audio option is mutithreaded, meaning it can play multiple audio at the same. I'm working to solve this problem."
message = tk.Message(message_frame, text=message_text,bg="white")
message.pack(side=tk.TOP)


exit_button_frame=tk.Frame(root, bg="white")
exit_button_frame.place(relwidth=0.4, relheight=0.1, relx=0.00, rely=0.925)
exit_button=tk.Button(exit_button_frame,text="Exit", command=root.destroy)
long_intro=tk.Button(exit_button_frame,text="Character Introduction", command=play_character_introduction)
exit_button.pack(side=tk.LEFT)
long_intro.pack(side=tk.RIGHT)


ver_frame = tk.Frame(root, bg="white")
ver_frame.place(relwidth=0.4, relheight=0.1, relx=0.00, rely=0.01)
ver_label = tk.Label(ver_frame,text="Ver. 0.2.1 Alpha Branch",bg="white")
ver_label.pack(side=tk.TOP)

character_image_frame = tk.Frame(root,bg="white")
character_image_frame.place(relwidth=0.6, relheight=0.9, relx=0.01, rely=0.05)
image_label = tk.Label(character_image_frame,image=image[0])
image_label.pack(side=tk.TOP)

time_frame = tk.Frame(root, bg="white")
time_frame.place(relwidth=0.3, relheight=0.1, relx=0.65, rely=0.35)
time_label = tk.Label(time_frame,text="TIME",bg="white")
time_label.pack(side=tk.TOP)
time_thread.start()
check_thread.start()
current_character_label = tk.Label(time_frame,text="Fubuki",bg="white")
current_character_label.pack(side=tk.BOTTOM)

character_list_frame = tk.Frame(root,bg="white")
character_list_frame.place(relwidth=0.3, relheight=0.4, relx=0.65, rely=0.5)
scrollbar = tk.Scrollbar(character_list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
label1 = tk.Label(character_list_frame,text="Characters",bg="white")
label1.pack(side=tk.TOP)
lb = tk.Listbox(character_list_frame, bg="white")
create_character_list(lb)
lb.pack(fill=tk.BOTH)
character_selection_button = tk.Button(character_list_frame,text="Select", command=get_selected_character)
character_selection_button.pack(side=tk.BOTTOM)
scrollbar.config(command=lb.yview)

root.mainloop()
app_is_aslive = False
check_thread.join()
time_thread.join()
