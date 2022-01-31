from tkinter import *

def txt_to_lbl(event):
    t=Arv1.get()
    TX2.configure(text=t)

def discriminant(event):
    a=0
    b=0
    c=0
    a=float(Arv1.get())
    b=float(Arv2.get())
    c=float(Arv3.get())
    if a>0:
        D=b**2-4*a*c
        TX2.configure(text=f"D={D}")
        if D>0:
            X1=(-b+D**0.5)/(2*a)
            X2=(-b-D**0.5)/(2*a)
            TX2.configure(text=f"D={D}\n x1={X1}\n x2={X2}")
        elif D==0:
            X1=-b/(2*a)
            TX2.configure(text=f"1 корня={D}\n x1,2={X1}")
        elif D<0:
            TX2.configure(text=f"корня нет={D}")
    else:
         TX2.configure(text="ошибка")



akkan=Tk()# главное окно приложения
akkan.title("Kвадратного уравнения")
akkan.geometry("700x300")

TX=Label(akkan,text="Решение квадратного уравнения",height=1,font="Arial 20",bg="lightblue",fg="green")
TX2=Label(akkan,text="Решение\n",height=4,width=60,font="Arial 10",bg="yellow")
TX3=Label(akkan,text="x**2+",font="Arial 20",fg="green")
TX4=Label(akkan,text="x+",font="Arial 20",fg="green")
TX5=Label(akkan,text="=0",font="Arial 20",fg="green")


Arv1=Entry(akkan,width=5,font="Arial 20",bg="lightblue",justify=CENTER)
Arv2=Entry(akkan,width=5,font="Arial 20",bg="lightblue",justify=CENTER)
Arv3=Entry(akkan,width=5,font="Arial 20",bg="lightblue",justify=CENTER)

BT=Button(akkan,text="Решить",height=2,width=10,font="Arial 20",bg="green")
BT.bind("<Button-1>",discriminant)



TX5.place(x=390,y=130)
TX4.place(x=250,y=130)
TX3.place(x=80,y=130)
    #############
TX2.place(x=150,y=230)
TX.place(x=100,y=0)



BT.place(x=440,y=100)
Arv1.place(x=0,y=130)
Arv2.place(x=160,y=130)
Arv3.place(x=300,y=130)

akkan.mainloop()
