import tkinter as tk
import tkinter.font as font
from Gesture_Controller import gest_control
from eye import eye_move
from samvk import vk_keyboard
from PIL import Image, ImageTk
from Proton import proton_chat

window = tk.Tk()
window.title("Gesture Controlled Virtual Mouse and Keyboard")
window.iconphoto(False, tk.PhotoImage(file='mn.png'))
window.geometry('1080x700')


frame1 = tk.Frame(window)

label_title = tk.Label(frame1, text="Gesture Controlled Virtual Mouse and Keyboard")
label_font = font.Font(size=30, weight='bold',family='Helvetica')
label_title['font'] = label_font
label_title.grid(pady=(10,10), column=2)


icon = Image.open('icons/man.jpeg')
icon = icon.resize((450,350), Image.ANTIALIAS)
icon = ImageTk.PhotoImage(icon)
label_icon = tk.Label(frame1, image=icon)
label_icon.grid(row=1, pady=(15,20), column=2)


btn1_image = Image.open('icons/bot.png')
btn1_image = btn1_image.resize((80,80), Image.ANTIALIAS)
btn1_image = ImageTk.PhotoImage(btn1_image)

btn2_image = Image.open('icons/keyboard.png')
btn2_image = btn2_image.resize((80,80), Image.ANTIALIAS)
btn2_image = ImageTk.PhotoImage(btn2_image)


btn5_image = Image.open('icons/exit.png')
btn5_image = btn5_image.resize((50,50), Image.ANTIALIAS)
btn5_image = ImageTk.PhotoImage(btn5_image)

btn3_image = Image.open('icons/eye.jpeg')
btn3_image = btn3_image.resize((100,100), Image.ANTIALIAS)
btn3_image = ImageTk.PhotoImage(btn3_image)

btn4_image = Image.open('icons/hand.png')
btn4_image = btn4_image.resize((80,80), Image.ANTIALIAS)
btn4_image = ImageTk.PhotoImage(btn4_image)


# --------------- Buttons -------------------#

btn_font = font.Font(size=25)
btn1 = tk.Button(frame1, text='VoiceBot', height=200, width=280, fg='green',command = proton_chat, image=btn1_image, compound='left')
btn1['font'] = btn_font
btn1.grid(row=3, pady=(20,10))

btn_font = font.Font(size=25)
btn2 = tk.Button(frame1, text='Keyboard', height=200, width=280, fg='red', command=vk_keyboard, compound='left', image=btn2_image)
btn2['font'] = btn_font
btn2.grid(row=3, pady=(20,10), column=3, padx=(20,10))

btn_font = font.Font(size=25)
btn3 = tk.Button(frame1, text='Eye', height=200, width=280, fg='blue', command=eye_move, image=btn3_image, compound='left')
btn3['font'] = btn_font
btn3.grid(row=5, pady=(20,10))

btn_font = font.Font(size=25)
btn4 = tk.Button(frame1, text='Gesture', height=200, width=280, fg='orange', command=gest_control, image=btn4_image, compound='left')
btn4['font'] = btn_font
btn4.grid(row=5, pady=(20,10), column=3)

btn_font = font.Font(size=25)
btn5 = tk.Button(frame1, height=200, width=280, fg='red', command=window.quit, image=btn5_image)
btn5['font'] = btn_font
btn5.grid(row=5, pady=(20,10), column=2)

frame1.pack()
window.mainloop()