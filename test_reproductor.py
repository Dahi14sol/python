from tkinter import * 
from tkinter.ttk import * 
from Reproductor  import *

musica = Reproductor('wefere.mp3')
display = "iniciando"

def play_musica():
    musica.volume(0.8)
    display = musica.play()
    label.config(text=display)

def pause_musica():
    display = musica.pause()
    label.config(text=display)

def volume_menos():
    display = musica.volume(-0.1)
    label.config(text=display)
   
def volume_mas():
    display = musica.volume(0.1)
    label.config(text=display)

master = Tk()
master.geometry("200x200")
master.config(bg="orange")

label = Label(master, text = display)
label.pack(pady = 10)

btn_play = Button(master, text = "PLAY", command = play_musica )
btn_play.pack(pady = 10 )
btn_pause = Button(master, text = "PAUSE", command = pause_musica)
btn_pause.pack(pady = 10 )
btn_menos_volumen = Button(master, text = "-", command = volume_menos )
btn_menos_volumen.pack(pady = 10 )
btn_mas_volumen = Button(master, text = "+", command = volume_mas)
btn_mas_volumen.pack(pady = 10 )

master.mainloop()
