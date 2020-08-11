from tkinter import Tk,Canvas,Frame,Label,Entry,Menu,Button,StringVar,Listbox,W,E,S,N,END,scrolledtext,WORD,font,PhotoImage,BOTH,RIGHT,messagebox,filedialog
from PIL import Image,ImageTk
import psycopg2
import os

def original():
    master2 = Tk()
    master2.title("notePAD - A new way to note your thoughts")
    master2.geometry("800x800+300+10")
    master2.config(bg="#423c3c")

    fontStyle =font.Font(family="Times New Roman", size=20)

    menubar = Menu(master2)
    master2.config(menu=menubar)

    def Save_File():
        save_me = text_field.get("1.0",END)
        # text_field1 = scrolledtext.ScrolledText(master2, fg="black", font=fontStyle, bg="white", width=50, height=22,
        #                                        wrap=WORD, highlightthickness=4, highlightbackground="#f26666")
        # text_field1.pack(fill=BOTH)
        # text_field1.place(x=10, y=80)

        with open("default.txt","w",encoding="utf-8") as write_on_me:
            write_on_me.write(save_me)


    def file():
        try:
            file = filedialog.askopenfile()

            # here this file is encoded with "cp1252" so we have to
            # convert it into encode of "utf-8" so that we can read or write
            file_path = file.name
            with open(file_path,'r',encoding='utf-8') as r_file:
                 text_in_file = r_file.read()
                 open_writing_box(text_in_file)
            save_me = text_field.get("1.0", END)
        except:
            print("Cancled")




    def open_writing_box(text):
        text_field.insert(END,text)
        Save_File()




    # /////Create items///////////////
    filename1 = Menu(menubar)
    menubar.add_cascade(label="File",menu=filename1)
    filename1.add_cascade(label="New",command=lambda:text_field.delete(1.0,END))
    filename1.add_separator()
    filename1.add_cascade(label='file',command=lambda:file())
    filename1.add_separator()
    filename1.add_cascade(label='save',command=lambda :Save_File())
    filename1.add_separator()
    filename1.add_cascade(label='Exit',command=quit)

    filename2 = Menu(menubar)
    menubar.add_cascade(label='View',menu=filename2)
    filename2.add_cascade(label='Appearance')
    filename4 = Menu(menubar)
    filename4.add_separator()
    filename4.add_cascade(label="About")


    # Head = Frame(master2,width=785,height=70,bg="#423c3c",highlightthickness=2,highlightbackground="#f26666")
    # Head.pack()
    # Head.place(y=10,x=10)

    text_field = scrolledtext.ScrolledText(master2,font=fontStyle,fg="black",bg="white",width=66,height=30,wrap=WORD,highlightthickness=4,highlightbackground="#f26666")
    text_field.pack(fill=BOTH,expand=True)
    text_field.place(x=10,y=80)
    text_field.insert(END,"Write your content here.....................")
    master2.mainloop()



if __name__ == "__main__":
    original()