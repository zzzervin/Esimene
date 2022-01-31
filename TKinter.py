from tkinter import *
from math import *
import matplotlib.pyplot as plt#y=...
import numpy as np #x =[max , min ]
global D,t
D=-1
t=""
T=0

def txt_to_lbl(t:str):
    t=Arv1.get()
    TX2.configure(text=t)

def discriminant():
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
            graf=True
        elif D==0:
            X1=-b/(2*a)
            TX2.configure(text=f"1 корня={D}\n x1,2={X1}")
            graf=True
        else:
            txt_to_lbl(text=f"корня нет=  {D}")

    return D,t,graf

def graafik():
    D,t,graf=discriminant()
    if graf==True:
        a=float(Arv1.get())
        b=float(Arv2.get())
        c=float(Arv3.get())
        x0=(-b)/(2*a)
        y0=a*x0*x0+b*x0+c
        x1= np.arange(x0-10,x0+10, 0.5)#Диапозон
        y1=a*x1*x1+b*x1+c
        fig = plt.figure()
        plt.plot(x1,y1,"r-d")
        plt.title("квадратного уравнения")
        plt.ylabel("y")
        plt.xlabel("x")
        plt.grid(True)
        plt.show()
        text=f"Вершина порабулы({x0},{x0})"
    else:
        text=f"Графика нет "
    TX2.configure(text=f"D={D}\n {t}\n {text}")
    
def veel() :
    global T 
    if T==0:
        akkan.geometry(str(akkan.winfo_width())+"x"+str(akkan.winfo_width()+150))
        btn_veel.config(text="Уменьшить окно")
        T=1
    else:
        akkan.geometry(str(akkan.winfo_width())+"x"+str(akkan.winfo_width()-150))
        btn_veel.config(text="Увеличеть окно")
        T=0

def glass():

akkan=Tk()# главное окно приложения
akkan.title("Kвадратного уравнения")
akkan.geometry("900x375")
f1=Frame(akkan,width=900,height=300,bg="blue")
f1.place(x=0,y=0)
f2=Frame(akkan,width=900,height=300,bg="yellow")
f2.place(x=0,y=300)



TX=Label(f1,text="Решение квадратного уравнения",height=1,font="Arial 20",bg="lightblue",fg="green")
TX2=Label(f1,text="Решение",height=4,width=60,font="Arial 10",bg="orange")
TX3=Label(f1,text="x**2+",font="Arial 20",fg="green")
TX4=Label(f1,text="x+",font="Arial 20",fg="green")
TX5=Label(f1,text="=0",font="Arial 20",fg="green")


Arv1=Entry(f1,width=5,font="Arial 20",bg="lightblue",justify=CENTER)
Arv2=Entry(f1,width=5,font="Arial 20",bg="lightblue",justify=CENTER)
Arv3=Entry(f1,width=5,font="Arial 20",bg="lightblue",justify=CENTER)

BT=Button(f1,text="Решить",height=2,width=10,font="Arial 20",bg="green",command=discriminant)
#BT.bind("<Button-1>",discriminant)
BT2=Button(f1,text="График",height=2,width=10,font="Arial 20",bg="green",command=graafik)

var=IntVar()
btn_veel=Button(f2,text="Увеличеть окно", font="Calibri 26", bg="green",command=veel)

TX5.place(x=390,y=130)
TX4.place(x=250,y=130)
TX3.place(x=80,y=130)
    #############
TX2.place(x=150,y=230)
    #############
TX.place(x=100,y=0)


BT2.place(x=640,y=100)
BT.place(x=440,y=100)
btn_veel.place(x=260,y=0)


Arv1.place(x=0,y=130)
Arv2.place(x=160,y=130)
Arv3.place(x=300,y=130)

akkan.mainloop()
