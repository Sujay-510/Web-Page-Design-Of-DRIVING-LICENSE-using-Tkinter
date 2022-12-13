from tkinter import *
#import mysql.connectora
#from tkinter import ttk
#from PIL import Image, ImageTk
import re
from tkinter import messagebox

class DL:
    def __init__(self,window):
        self.window = window
        self.window.title('Know Your Driving License Status')
        self.window.geometry("1300x770+0+0")
        self.window.minsize(1300, 770)
        self.window.maxsize(1300, 770)

        canvas = Canvas(relief=RIDGE, background='blue', height=50, width=1300)
        canvas.place(x=0, y=0)
        btn1 = Button(window, text='Home', width=5,
                      height=1, bg='blue', fg='white', command=window.destroy, activebackground='black',
                      font=('Helvetica', 12))
        btn1.place(x=670, y=13)

        btn2 = Button(window, text='Skip to main content ', width=15,
                      height=1, bg='blue', fg='white', activebackground='black', font=('Helvetica', 12))
        btn2.place(x=730, y=13)

        btn3 = Button(window, text='Skip to navigation', width=15,
                      height=1, bg='blue', fg='white', activebackground='black', font=('Helvetica', 12))
        btn3.place(x=880, y=13)

        btn4 = Button(window, text='A+', width=5,
                      height=1, bg='blue', fg='white', activebackground='black', font=('Helvetica', 12))
        btn4.place(x=1150, y=13)

        btn5 = Button(window, text='A', width=5,
                      height=1, bg='blue', fg='white', activebackground='black', font=('Helvetica', 12))
        btn5.place(x=1100, y=13)

        btn6 = Button(window, text='A-', width=5,
                      height=1, bg='blue', fg='white', activebackground='black', font=('Helvetica', 12))
        btn6.place(x=1050, y=13)

        canvas1 = Canvas(relief=RIDGE, background='white', height=100, width=1300)
        canvas1.place(x=0, y=50)

        photo1 = PhotoImage(file=r"C:\Users\DELL\PycharmProjects\DRIVING LICENSE\images\logo.jpg")
        logo = Label(self.window, text='yes', image=photo1)

        line = canvas1.create_line(320, 0, 320, 200)
        te = canvas1.create_text(700, 50,
                                 text="                   Goverment of India \n MINISTRY OF ROAD TRANSPORT & HIGHWAYS",
                                 fill="black", font=('Helvetica 15 bold'))

        # photo123 = PhotoImage(file = r"C:\Users\DELL\PycharmProjects\pythonProject\as.jpg")
        # flag = Label(window, image = photo123)
        # flag.configure(height = 225 , width = 225)

        canvas = Canvas(relief=RIDGE, bd=2, background='dark blue', height=30, width=1300)
        canvas.place(x=0, y=150)

        canvas3 = Canvas(window, bg='light gray', bd=6, height=520, width=1100)
        canvas3.place(x=100, y=210)

        canvas4 = Canvas(relief=RIDGE, background='light blue', height=40, width=1090)
        canvas4.place(x=110, y=220)
        text = canvas4.create_text(170, 20, text='Know Your Driving License Status', font=('boldface', 14, 'italic'))

        a = Label(canvas3, text='Driving Licence No.*', bg='light gray', fg='black',
                  font=('Helvetica bold', 13, 'italic')).place(x=300, y=70)
        b = Label(canvas3, text="Date Of Birth*", bg='light gray', fg='black',
                  font=('Helvetica bold', 13, 'italic')).place(x=300, y=130)
        c = Label(canvas3, text="Enter Verification Code*", bg='light gray', fg='black',
                  font=('Helvetica bold', 13, 'italic')).place(x=300, y=190)
        dlentry = Entry(canvas3, width=25,)
        dobentry = Entry(canvas3)
        captchaentry = Entry(canvas3)

        var1 = IntVar()
        c12 = Checkbutton(canvas3, text='Click to Agree T & C ', variable=var1, onvalue=1, offvalue=0, bg="light gray")

        # Driving license Number should be -- FIRST TWO CAPITAL LETTER -- THEN SPACE OR hyphen -- two numbers
        # -- YEAR 19 OR 20 AND A NUMBER FROM 0-9 ALSO A NUMBER FROM 0-9 -- 0-9 7 NUMBERS  ex- HR-0619850034761
        def isValidLicenseNo(str):
            regex = ("^(([A-Z]{2}[0-9]{2})" +
                     "( )|([A-Z]{2}-[0-9]" +
                     "{2}))((19|20)[0-9]" +
                     "[0-9])[0-9]{7}$")
            p = re.compile(regex)
            if (len(str) == 0):
                return messagebox.showwarning("showwarning", "Enter DL number")
            elif (re.search(p, str)):
                return True
            else:
                return messagebox.showwarning("showwarning", "INVALID DL NUMBER")

        def isvaliddob(str1):
            regex = ("^(([0-9]{2})" +
                     "-([0-9]" +
                     "{2}))-((19|20)[0-9]" +
                     "[0-9])$")
            p = re.compile(regex)
            if (len(str1) == 0):
                return messagebox.showwarning("showwarning", "Enter Date of Birth")
            elif (re.search(p, str1)):
                return True
            else:
                return messagebox.showwarning("showwarning", "INVALID Date of Birth")

        def isvalidcaptcha(str2):
            print(2)

        def isclicked(str3):
            if (str3 == 1):
                return 1
            else:
                return messagebox.showwarning("Showwarning", "Click Checkbox")

        def check():
            text = dlentry.get()
            print(text)
            isValidLicenseNo(text)
            textdob = dobentry.get()
            print(textdob)
            isvaliddob(textdob)
            textcaptcha = captchaentry.get()
            print(textcaptcha)
            isvalidcaptcha(textcaptcha)
            click = var1.get()
            print(click)
            isclicked(click)

        def reset():
            photo2 = PhotoImage(file=r"C:\Users\DELL\PycharmProjects\DRIVING LICENSE\images\5.jpg")
            imggs = Label(self.window, image=photo2)
            imggs.configure(height=50, width=130)

        btn7 = Button(canvas3, text='Check Status', width=10,
                      height=1, bg='blue', fg='white', activebackground='black', command=check, font=('bold', 12))
        btn7.place(x=500, y=250)

        btn8 = Button(canvas3, text='Reset', width=8,
                      height=1, bg='blue', fg='white', activebackground='black', command=reset, font=('bold', 12))
        btn8.place(x=620, y=250)

        photo2 = PhotoImage(file=r"C:\Users\DELL\PycharmProjects\DRIVING LICENSE\images\4.jpg")
        imgg = Label(self.window, image=photo2)
        imgg.configure(height=50, width=130)

        dlentry.place(x=500, y=70)
        dobentry.place(x=500, y=130)
        captchaentry.place(x=650, y=190)

        imgg.place(x=600, y=370)
        logo.place(x=100, y=60)
        # flag.place(x = 900, y = 30)
        c12.place(x=500, y=220)

        canvas5 = Canvas(relief=RIDGE, background='white', height=220, width=1090)
        note = Label(canvas5, text="Note :- ", bg='white', fg='black', font=('Helvetica 13 bold')).place(x=5, y=20)
        longtext = Label(canvas5,
                         text="Driving Licence number can be entered in any of the following formats: DL-1420110012345 or DL14 20110012345",
                         fg="red", bg='white', font=('italic', 10))
        longtext1 = Label(canvas5,
                          text="Total number of input characters should be exactly 16 (including space or '-').",
                          fg="red", bg='white', font=('italic', 10))
        longtext2 = Label(canvas5,
                          text="If you hold an old driving license with a different format, please convert the format as per below rule before entering",
                          fg="red", bg='white', font=('italic', 10))
        longtext3 = Label(canvas5, text="SS-RRYYYYNNNNNNN OR SSRR YYYYNNNNNNN", fg="red", bg='white',
                          font=('italic', 10))
        longtext4 = Label(canvas5,
                          text="Where SS - Two character State Code (like RJ for Rajasthan, TN for Tamil Nadu etc)",
                          fg="red", bg='white', font=('italic', 10))
        longtext5 = Label(canvas5, text="RR - Two digit RTO Code", fg="red", bg='white', font=('italic', 10))
        longtext6 = Label(canvas5,
                          text="YYYY - 4-digit Year of Issue (For Example: If year is mentioned in 2 digits, say 99, then it should be converted to 1999. Similarly use 2012 for 12)",
                          fg="red", bg='white', font=('italic', 10))
        longtext7 = Label(canvas5,
                          text="Rest of the numbers are to be given in 7 digits. If there are less number of digits, then additional 0's(zeros) may be added to make the total 7.",
                          fg="red", bg='white', font=('italic', 10))
        longtext8 = Label(canvas5,
                          text="For example: If the Driving Licence Number is RJ-13/DLC/12/ 123456 then please enter RJ-1320120123456 OR RJ13 20120123456",
                          fg="red", bg='white', font=('italic', 10))

        canvas5.place(x=110, y=500)
        longtext.place(x=70, y=22)
        longtext1.place(x=70, y=44)
        longtext2.place(x=70, y=66)
        longtext3.place(x=70, y=88)
        longtext4.place(x=70, y=110)
        longtext5.place(x=70, y=132)
        longtext6.place(x=70, y=154)
        longtext7.place(x=70, y=176)
        longtext8.place(x=70, y=198)


window = Tk()
obj = DL(window)
window.mainloop()