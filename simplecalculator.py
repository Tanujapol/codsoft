from tkinter import*
strng=""
def click(n):
    global strng
    strng=strng+str(n)
    eq.set(strng)

def equalto():
    try:
        global strng
        result=str(eval(strng))
        eq.set(result)
        strng=""
    except:
        eq.set(" invalid ")
        strng=""
def clear():
    global strng
    strng=""
    eq.set("")

def into():
    global strng
    if strng:
       strng2=strng[:-1]
       exp_f.delete(0,END)
       exp_f.insert(0,strng2)
       strng=strng2

if __name__=="__main__":
    gui=Tk()
    gui.configure(bg="black")
    gui.title("simple calculator")
    gui.geometry("280x450")
    eq=StringVar()

    exp_f=Entry(gui,textvariable=eq)
    exp_f.grid(columnspan=50,ipadx=80)
    button1=Button(gui,text="1",fg="black",bg="white",command=lambda:click(1),height=5,width=10)
    button1.grid(row=2,column=0)
    button2=Button(gui,text=" 2 ",fg="black",bg="white",command=lambda:click(2),height=5,width=10)
    button2.grid(row=2,column=1)
    button3=Button(gui,text=" 3 ",fg="black",bg="white",command=lambda:click(3),height=5,width=10)
    button3.grid(row=2,column=2)
    button4=Button(gui,text=" 4 ",fg="black",bg="white",command=lambda:click(4),height=5,width=10)
    button4.grid(row=3,column=0)
    button5=Button(gui,text=" 5 ",fg="black",bg="white",command=lambda:click(5),height=5,width=10)
    button5.grid(row=3,column=1)
    button6=Button(gui,text=" 6 ",fg="black",bg="white",command=lambda:click(6),height=5,width=10)
    button6.grid(row=3,column=2)
    button7=Button(gui,text=" 7 ",fg="black",bg="white",command=lambda:click(7),height=5,width=10)
    button7.grid(row=4,column=0)
    button8=Button(gui,text=" 8 ",fg="black",bg="white",command=lambda:click(8),height=5,width=10)
    button8.grid(row=4,column=1)
    button9=Button(gui,text=" 9 ",fg="black",bg="white",command=lambda:click(9),height=5,width=10)
    button9.grid(row=4,column=2)
    button0=Button(gui,text=" 0 ",fg="black",bg="white",command=lambda:click(0),height=5,width=10)
    button0.grid(row=5,column=1)
    plus=Button(gui,text=" + ",fg="black",bg="white",command=lambda:click("+"),height=5,width=5)
    plus.grid(row=2,column=3)
    minus=Button(gui,text=" - ",fg="black",bg="white",command=lambda:click("-"),height=5,width=5)
    minus.grid(row=3,column=3)
    multiply=Button(gui,text=" * ",fg="black",bg="white",command=lambda:click("*"),height=5,width=5)
    multiply.grid(row=4,column=3)
    divide=Button(gui,text=" / ",fg="black",bg="white",command=lambda:click("/"),height=5,width=5)
    divide.grid(row=5,column=3)
    equalto=Button(gui,text=" = ",fg="black",bg="orange",command=equalto,height=5,width=5)
    equalto.grid(row=6,column=3)
    clear=Button(gui,text="Clear",fg="black",bg="white",command=clear,height=5,width=10)
    clear.grid(row=6,column=0,columnspan=3,sticky="ew")
    for i in range(4):
        clear.columnconfigure(i,weight=1)
    decimal=Button(gui,text=" . ",fg="black",bg="white",command=lambda:click("."),height=5,width=10)
    decimal.grid(row=5,column=2)
    into=Button(gui,text=" X ",fg="black",bg="white",command=into,height=5,width=10)
    into.grid(row=5,column=0)
    gui.mainloop()
