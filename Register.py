from tkinter import Tk,Canvas,Frame,Label,Entry,Button,Listbox,W,E,S,N,END,scrolledtext,WORD,font,PhotoImage,messagebox
from PIL import Image,ImageTk
import psycopg2
import Original_Pad

def register():
    window = Tk()

    window.title("Python and PostgreSQL")
    window.geometry("800x800+300+10")
    window.config(bg="#423c3c")

    # # img = Image.open('My_pic.jpg')
    # img = Image.open('C:\\Users\\shubham kumar\\Pictures\\Saved Pictures\\pic.jpg')
    # background_image=ImageTk.PhotoImage(img)

    # background_label = Label(window, image=background_image)
    # background_label.place(x=0, y=0, relwidth=1, relheight=1)

    fontStyle = font.Font(family="Times New Roman", size=18)
    fontStyle1 = font.Font(family="Times New Roman", size=13)

    def Save(name, age, email):
        conn = psycopg2.connect(dbname='postgres',
                                user="",
                                password="",
                                host="localhost",
                                port="5432"
                                )
        cursor = conn.cursor()
        try:
            query = """INSERT INTO Users(name,age,email) VALUES(%s,%s,%s)"""
            cursor.execute(query, (name, age, email))
            messagebox.showinfo(title="notePAD", message="            WELCOME               ")
            print("Data Saved")
        except:
            bx = Listbox(frame, width=50, fg="#edd5d5", height=5, bg="#423c3c")
            bx.grid(row=10, column=1, columnspan=4, pady=15)
            bx.insert(END, "Please  fillup the form first")
        finally:
            conn.commit()
            conn.close()
            Original_Pad.original()


    # def Display_All_Users():
    #     conn = psycopg2.connect(dbname='postgres',
    #                             user="postgres",
    #                             password="avq891@#",
    #                             host="localhost",
    #                             port="5432"
    #                             )
    #     cursor = conn.cursor()
    #     query = """SELECT * FROM Users"""
    #     cursor.execute(query)
    #     row = cursor.fetchall()
    #     # Here row contains all the packs of tuple,means number
    #     # of tuples and each tuple has four items that is column
    #     #          Means
    #     # You retrieved a list of rows, and each row is a tuple
    #     # of columns.As each row contains four column the rows are tuples with four value each.
    #
    #     listbox =Listbox(frame,width=35,height=5)
    #     listbox.grid(row=5,column=1,columnspan=4,sticky="w",pady=15)
    #
    #     for x in row:
    #         listbox.insert(END,x[1])
    #
    #     conn.commit()
    #     conn.close()

    def Display_Searched_name(row1):
        row1 = row1
        listbox1 = Listbox(frame, width=50, fg="#edd5d5", height=5, bg="#423c3c")
        listbox1.grid(row=10, column=1, columnspan=4, pady=15)
        Label(frame, text="Searched Details", fg="#edd5d5", bg="#423c3c", font=fontStyle1).grid(row=9, column=1,
                                                                                                columnspan=4)

        try:
            details = {'Id': row1[0], 'name': row1[1], 'age': row1[2], 'email': row1[3]}
            # //////////////using .forma()//////////////////////////////////////
            # listbox1.insert(END,"Id number : {} ".format(details['Id']),
            #                 "Name : {} ".format(details['name']),
            #                 "Age : {} ".format(details['age']),
            #                 "Email : {} ".format(details['email']))
            # //////////////// using f"{}"/////////////////////////////////////////
            listbox1.insert(END, f"Id number : {details['Id']}",
                            f"Name : {details['name']}",
                            f"Age : {details['age']}",
                            f"Email : {details['email']}")

        except:
            listbox1.insert(END, "Invalid Details")

    def Display_Searched_id(row2):
        row2 = row2
        # label2 = Label(frame, text=row2)
        # label2.grid(row=7,column=3)
        listbox2 = Listbox(frame, width=50, fg="#edd5d5", height=5, bg="#423c3c")
        listbox2.grid(row=10, column=1, columnspan=4, pady=15)
        Label(frame, text="Searched Details", bg="#423c3c", fg="#edd5d5", font=fontStyle1).grid(row=9, column=1,
                                                                                                columnspan=4)
        details = {'Id': row2[0], 'name': row2[1], 'age': row2[2], 'email': row2[3]}
        # /////////////using .forma()//////////////////////////////////////
        listbox2.insert(END, "Id number : {} ".format(details['Id']),
                        "Name : {} ".format(details['name']),
                        "Age : {} ".format(details['age']),
                        "Email : {} ".format(details['email']))
        # //////////////// using f"{}"/////////////////////////////////////////
        # listbox2.insert(END, f"Id number : {details['Id']}",
        #                 f"Name : {details['name']}",
        #                 f"Age : {details['age']}",
        #                 f"Email : {details['email']}")

    def Search1(name):
        conn = psycopg2.connect(dbname='postgres',
                                user="postgres",
                                password="avq891@#",
                                host="localhost",
                                port="5432"
                                )
        cursor = conn.cursor()

        query = """SELECT * FROM Users WHERE name=%s"""
        cursor.execute(query, (name,))
        row1 = cursor.fetchone()
        Display_Searched_name(row1)
        conn.commit()
        conn.close()

    def Search2(id):
        conn = psycopg2.connect(dbname='postgres',
                                user="postgres",
                                password="avq891@#",
                                host="localhost",
                                port="5432"
                                )
        cursor = conn.cursor()

        query = """SELECT * FROM Users WHERE id=%s"""
        try:
            # Note the error
            cursor.execute(query, (id,))
            row2 = cursor.fetchone()
            Display_Searched_id(row2)
            conn.commit()
            conn.close()
        except:
            Label(frame, text="Searched Details", fg="#edd5d5", bg="#423c3c", font=fontStyle1).grid(row=9, column=1,
                                                                                                    columnspan=4)
            box = Listbox(frame, width=50, bg="#423c3c", height=5, fg="#edd5d5")
            box.grid(row=10, column=1, columnspan=4, pady=15)
            box.insert(END, "Searched Id does't exists")

    l = Label(window,text="Please Register yourself to be the part of our notePAD family", fg="#edd5d5", bg="#423c3c",
              font=fontStyle1)
    l.pack(pady=20)

    frame = Frame(window, bg="#423c3c")
    frame.pack(expand=True)
    frame.place(relx=0.3, rely=0.1)

    label = Label(frame, text='Register Here', fg="#edd5d5", font=fontStyle, bg="#423c3c")
    label.grid(row=0, column=2, columnspan=4, sticky="w", pady=15)

    # ///////////Name///////////////////////
    label = Label(frame, text='Name', fg="#edd5d5", font=fontStyle1, bg="#423c3c")
    label.grid(row=1, column=1, sticky="w", pady=15)

    entry_name = Entry(frame, width=30)
    entry_name.grid(row=1, column=2, pady=15)

    # ///////////////Age////////////////////////
    label = Label(frame, text='Age', fg="#edd5d5", font=fontStyle1, bg="#423c3c")
    label.grid(row=2, column=1, sticky="w", pady=15)

    entry_age = Entry(frame, width=30)
    entry_age.grid(row=2, column=2, pady=15)

    # ///////////////Email Address////////////////////////
    label = Label(frame, text='Email', fg="#edd5d5", font=fontStyle1, bg="#423c3c")
    label.grid(row=3, column=1, sticky="w", pady=15)

    entry_email = Entry(frame, width=30)
    entry_email.grid(row=3, column=2, pady=15)

    button = Button(frame, text="Save", fg="#edd5d5", bg="#423c3c", font=fontStyle1,
                    command=lambda: Save(entry_name.get(),
                                         entry_age.get(),
                                         entry_email.get()
                                         ))
    button.grid(row=4, column=2, columnspan=4, sticky="w", pady=15)

    # Display_All_Users()

    l = Label(frame, text="Search Data", fg="#edd5d5", font=fontStyle, bg="#423c3c")
    l.grid(row=6, column=2, columnspan=4, sticky="w", pady=15)

    # /////////////Search by Name/////////////////////////
    search_entry_name = Entry(frame, font=fontStyle1, width=20)
    search_entry_name.grid(row=7, column=2, pady=15, padx=15)
    search_entry_name.insert(0, "Search here by name")

    search1 = Button(frame, text='Search Name', fg="#edd5d5", bg="#423c3c",
                     command=lambda: Search1(search_entry_name.get()), font=fontStyle1)
    search1.grid(row=7, column=1, sticky="w", pady=15)

    # ////////////////Search by Id/////////////////////////////
    search_entry_id = Entry(frame, font=fontStyle1, width=20)
    search_entry_id.grid(row=8, column=2, pady=15, padx=15)
    search_entry_id.insert(0, "Search here by Id")

    search2 = Button(frame, text='Search Id', bg="#423c3c", fg="#edd5d5",
                     command=lambda: Search2(search_entry_id.get()), font=fontStyle1)
    search2.grid(row=8, column=1, sticky="w", pady=15)

    jump_to_notepad = Button(frame,text="Jump to notepad",command=Original_Pad.original,font=fontStyle)
    jump_to_notepad.grid(row=11,columnspan=4)

    window.mainloop()

if __name__ == "__main__":
     register()
