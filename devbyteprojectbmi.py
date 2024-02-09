from tkinter import *
from tkinter import messagebox

def cal_bmi(a,b,c):
    #calculating bmi
    bmi = int(c)/((int(b)/100)**2)
    if bmi < 18.5:
        d = str(a)+", you are underweight."
        messagebox.showinfo('Body Mass index',d)
    elif bmi < 25:
        d = "VERY GOOD " +str(a)+", you were in normal range."
        messagebox.showinfo('Body Mass index',d)
    elif bmi < 30:
        d = str(a)+", you are Overweight."
        messagebox.showinfo('Body Mass index',d)
    else:
        d = str(a)+", you are Obese."
        messagebox.showinfo('Body Mass index',d)
        


def bmi_entry_gui():
    #GUI code for bmi entry
    win = Tk()
    win.title("BMI's Entry")
    win.config(bg="light green")
    win.geometry("500x200")

    
    lbl1 = Label (win, text = "Your name :" , font = ('Verdana',20),bg="light green")
    lbl1.place(x=10,y=10)
    txt1 = Entry(win, width = 16 , font = ('Verdana',20))
    txt1.place (x=200,y=10)
    
    lbl2 = Label(win,text="Your Height:" ,font=('Verdana' , 20),bg="light green")
    lbl2.place(x=10,y=50)
    txt2 = Entry(win , width=10,font=('Verdana' , 20))
    txt2.place(x=200 , y =50)
    lbel2 = Label(win,text="CM" ,font=('Verdana' , 20),bg="light green")
    lbel2.place(x=400,y=50)
    
    lbl3 = Label(win,text="Your Weight:" ,font=('Verdana' , 20),bg="light green")
    lbl3.place(x=10,y=90)
    txt3 = Entry(win , width=10,font=('Verdana' , 20))
    txt3.place(x=200 , y =90)
    lbel2 = Label(win,text="KG" ,font=('Verdana' , 20),bg="light green")
    lbel2.place(x=400,y=90)
    

    butn1 = Button(win, text = "ENTER" , activebackground = "yellow" , bg = "green" , command = lambda:cal_bmi(txt1.get() , txt2.get(), txt3.get()))
    butn1.place(x=430,y=150)


#calling the function
bmi_entry_gui()
