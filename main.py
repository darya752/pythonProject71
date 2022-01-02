from tkinter import Tk, Button, Canvas, Image, Frame, Label
from PIL import ImageTk, Image

root = Tk()
root.configure(bg='#74AF4A')
root.geometry('1200x1200')
image_screen = ImageTk.PhotoImage(file='screen0.jpg')

Button(root, image=image_screen, highlightthickness=0, bd=0).place(x=300, y=520)

frame = Frame(root, width=200, heigh=50, bg='#74AF4A')
frame.grid(row=0, column=5)

frame1 = Frame(root, width=500, heigh=400, bg='#A3CCC8')
frame1.grid(row=0, column=30)

image_sb = ImageTk.PhotoImage(file='sb.jpg')


label1 = Label(frame1, text='Нажмите "enter" для получения денег', bg='#c7ddda', font="Arial 14", padx=80, pady=160)
label1.grid()

def click():
    image_k = ImageTk.PhotoImage(file='5k.jpg')
    Button(root, image=image_k, highlightthickness=0, bd=0).place(x=550, y=420)
    return ImageTk.PhotoImage(image_k)

image1 = ImageTk.PhotoImage(file='101.jpg')
Button(root, image=image1, highlightthickness=0, bd=0).place(x=330, y=540)

image2 = ImageTk.PhotoImage(file='202.jpg')
Button(root, image=image2, highlightthickness=0, bd=0).place(x=387, y=541)

image3 = ImageTk.PhotoImage(file='303.jpg')
Button(root, image=image3, highlightthickness=0, bd=0).place(x=446, y=542)

image_cancel = ImageTk.PhotoImage(file='cancel.jpg')
Button(root, image=image_cancel, highlightthickness=0, bd=0).place(x=500, y=542)

image4 = ImageTk.PhotoImage(file='404.jpg')
Button(root, image=image4, highlightthickness=0, bd=0).place(x=333, y=584)

image5 = ImageTk.PhotoImage(file='505.jpg')
Button(root, image=image5, highlightthickness=0, bd=0).place(x=389, y=584)

image6 = ImageTk.PhotoImage(file='606.jpg')
Button(root, image=image6, highlightthickness=0, bd=0).place(x=445, y=584)

image7 = ImageTk.PhotoImage(file='707.jpg')
Button(root, image=image7, highlightthickness=0, bd=0).place(x=334, y=624)

image_cor = ImageTk.PhotoImage(file='correction.jpg')
Button(root, image=image_cor, highlightthickness=0, bd=0).place(x=501, y=584)

image8 = ImageTk.PhotoImage(file='808.jpg')
Button(root, image=image8, highlightthickness=0, bd=0).place(x=387, y=624)

image9 = ImageTk.PhotoImage(file='909.jpg')
Button(root, image=image9, highlightthickness=0, bd=0).place(x=445, y=626)

image_bl = ImageTk.PhotoImage(file='black.jpg')
Button(root, image=image_bl, highlightthickness=0, bd=0).place(x=501, y=626)

image0 = ImageTk.PhotoImage(file='000.jpg')
Button(root, image=image0, highlightthickness=0, bd=0).place(x=387, y=667)

image_no = ImageTk.PhotoImage(file='none.jpg')
Button(root, image=image_no, highlightthickness=0, bd=0).place(x=332, y=667)

image_non = ImageTk.PhotoImage(file='none.jpg')
Button(root, image=image_non, highlightthickness=0, bd=0).place(x=442, y=667)


image_enter = ImageTk.PhotoImage(file='enter.jpg')
Button(root, image=image_enter, highlightthickness=0, bd=0, command=click).place(x=498, y=669)

image_card = ImageTk.PhotoImage(file='card.jpg')
Button(root, image=image_card, highlightthickness=0, bd=0).place(x=850, y=20)

image_circle1 = ImageTk.PhotoImage(file='circle.jpg')
Button(root, image=image_circle1, highlightthickness=0, bd=0).place(x=720, y=50)
image_circle2 = ImageTk.PhotoImage(file='circle.jpg')
Button(root, image=image_circle1, highlightthickness=0, bd=0).place(x=720, y=150)
image_circle3 = ImageTk.PhotoImage(file='circle.jpg')
Button(root, image=image_circle1, highlightthickness=0, bd=0).place(x=720, y=250)

image_circle4 = ImageTk.PhotoImage(file='circle.jpg')
Button(root, image=image_circle1, highlightthickness=0, bd=0).place(x=90, y=50)
image_circle5 = ImageTk.PhotoImage(file='circle.jpg')
Button(root, image=image_circle1, highlightthickness=0, bd=0).place(x=90, y=150)
image_circle6 = ImageTk.PhotoImage(file='circle.jpg')
Button(root, image=image_circle1, highlightthickness=0, bd=0).place(x=90, y=250)

image_l = ImageTk.PhotoImage(file='l.jpg')
Button(root, image=image_l, highlightthickness=0, bd=0).place(x=50, y=420)

image_r = ImageTk.PhotoImage(file='r.jpg')
Button(root, image=image_r, highlightthickness=0, bd=0).place(x=550, y=420)


root.mainloop()