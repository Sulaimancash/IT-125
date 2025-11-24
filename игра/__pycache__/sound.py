import tkinter as tk
from tkinter import PhotoImage
import pygame
import os

pygame.mixer.init()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def abs_path(file):
    return os.path.join(BASE_DIR, file)

def play_sound(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

def create_app():
    root = tk.Tk()
    root.title("Мемы")
    root.geometry("500x700")


    meme1_img = PhotoImage(file=abs_path("картинка/20 снимков эмоциональных сов, которые кого угодно сразят своим обаянием.jfif"))
    meme2_img = PhotoImage(file=abs_path("картинка/Grand Theft Auto V.jfif"))
    meme3_img = PhotoImage(file=abs_path("картинка/Без названия.jfif"))
    meme4_img = PhotoImage(file=abs_path("картинка/Причина братан это фиаско мем тряски.jfif"))
    meme5_img = PhotoImage(file=abs_path("картинка/суету навести охота.jfif"))

    tk.Button(
        root,
        image=meme1_img,
        borderwidth=0,
        command=lambda: play_sound(abs_path("sounds/camera-i-thought-it-was-an-owl.mp3"))
    ).pack(pady=10)

    tk.Button(
        root,
        image=meme2_img,
        borderwidth=0,
        command=lambda: play_sound(abs_path("sounds/music-with-completed-mission-from-gta-san-andreas.mp3"))
    ).pack(pady=10)

    tk.Button(
        root,
        image=meme3_img,
        borderwidth=0,
        command=lambda: play_sound(abs_path("sounds/motivatsiiu-nado-podniat.mp3"))
    ).pack(pady=10)

    tk.Button(
        root,
        image=meme4_img,
        borderwidth=0,
        command=lambda: play_sound(abs_path("sounds/it39s-a-fiasco-bro.mp3"))
    ).pack(pady=10)


    tk.Button(
        root,
        image=meme5_img,
        borderwidth=0,
        command=lambda: play_sound(abs_path("sounds/want-to-make-a-fuss.mp3"))
    ).pack(pady=10)

    root.meme1 = meme1_img
    root.meme2 = meme2_img
    root.meme3 = meme3_img
    root.meme4 = meme4_img
    root.meme5 = meme5_img

    root.mainloop()


create_app()
