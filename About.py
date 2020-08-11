from tkinter import *
from tkinter import font
from PIL import Image,ImageTk
import Register
import Original_Pad

def about():
    root = Tk()
    root.title("notePAD")
    root.geometry("600x600+350+100")
    root.configure(bg="#f26666")

    fontStyle3 =font.Font(family="Times New Roman", size=13)

    frame1 = Frame(root,width=250,height=250,highlightthickness=4,highlightbackground="#f26666")
    frame1.pack(side=LEFT,expand=True,fill=BOTH)
    frame1.place(relx=0.0)

    img = Image.open('My_pic.jpg')
    logo = ImageTk.PhotoImage(img)

    canvas = Canvas(frame1,width=245,height=250,bg='#262121',highlightthickness=4,highlightbackground="#706d6d")
    canvas.create_image(127,120,image=logo)
    canvas.pack(side=RIGHT,fill=BOTH,expand=True)

    a = Text(root,width=27,height=16,bg="#262121",fg="white",font=fontStyle3,highlightthickness=4,highlightbackground="#706d6d")
    a.pack(side=LEFT,expand=True,fill=BOTH)
    a.place(relx=0.01,rely=0.445)

    a.insert(END,"                ABOUT  notePAD\n\n")

    a.insert(END,"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\n\n")



    t = Text(root,width=35,height=30,bg="#262121",fg="white",font=fontStyle3,highlightthickness=4,highlightbackground="#706d6d")
    t.pack(side=RIGHT)
    t.place(relx=0.44,rely=0.008)

    t.insert(END,"                                Description\n\n\n")


    t.insert(END,"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\n\n")
    t.insert(END,"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")

    # activate_f = Frame(root,width=580,height=20,bg="#706d6d")
    # activate_f.pack(fill=BOTH,expand=True)
    # activate_f.place(x=6.3,y=580)

    activate= Button(root,text="Activate notePAD",width=50,command=Register.register)
    activate.place(x=120,y=580)



    root.mainloop()


if __name__ == "__main__":
     about()