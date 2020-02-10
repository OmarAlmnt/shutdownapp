#####YOUTUBE Omar Almonte################
import os
from tkinter import *
from tkinter import messagebox
vent = Tk()
vent.geometry("365x140")
vent.title("ShutdownApp")
vent.resizable(0,0)
def shutdown():
    global tiempor
    if tiempo.get():
        if hora.get():
            if  hora.get() == "hora":
                    tiempor = float()
                    tiempor = float(tiempo.get()) * 3600
                    os.system("shutdown /s /t %d" % tiempor)
            
            elif hora.get() == "minuto":
                    tiempor = float()
                    tiempor = float(tiempo.get()) * 60
                    os.system("shutdown /s /t %d" % tiempor)
            
            elif hora.get() == "segundo":
                    tiempor = float()
                    tiempor = float(tiempo.get()) 
                    os.system("shutdown /s /t %d" % tiempor)
                    
            elif hora.get() == "dia":
                    tiempor = float()
                    tiempor = float(tiempo.get()) * 86400 
                    os.system("shutdown /s /t %d" % tiempor)
        else:
         messagebox.showinfo("Error","Seleccione hora,segundo o minuto")
    else:
        messagebox.showinfo("Error","Especifique el tiempo")

def restart():
    global tiempor
    if tiempo.get():
        if hora.get():
            if  hora.get() == "hora":
                    tiempor = float()
                    tiempor = float(tiempo.get()) * 3600
                    os.system("shutdown /r /t %d" % tiempor)
            
            elif hora.get() == "minuto":
                    tiempor = float()
                    tiempor = float(tiempo.get()) * 60
                    os.system("shutdown /r /t %d" % tiempor)
            
            elif hora.get() == "segundo":
                    tiempor = float()
                    tiempor = float(tiempo.get()) 
                    os.system("shutdown /r /t %d" % tiempor)
                    
            elif hora.get() == "dia":
                    tiempor = float()
                    tiempor = float(tiempo.get()) * 86400 
                    os.system("shutdown /r /t %d" % tiempor)
        else:
             messagebox.showinfo("Error","Seleccione hora,segundo o minuto")
    else:
        messagebox.showinfo("Error","Especifique el tiempo")
        
def cancel():
    os.system("shutdown /a")

def sleep():
    try:
        os.system("shutdown /h")
        messagebox.showinfo("Cancel","Cancelado con exito")
    except Exception:
        messagebox.showinfo("Cancel","No se pudo cancelar")
def ext():
    exit()

hora=StringVar()
tiempo=StringVar()#####YOUTUBE Omar Almonte################


sht = Button(vent,text="Shutdown", width=8,command=shutdown).place(x = 10, y = 20)
reset = Button(vent,text="Restart",width=8,command=restart).place(x = 80, y = 20)
sleep = Button(vent,text="Sleep",width=8,command=sleep).place(x= 220, y = 20)
cancel = Button(vent,text="Cancel",width=8,command=cancel).place(x= 290, y = 20)
exitb = Button(vent,text="Exit",width=8,command=ext).place(x= 150, y = 20)
Tmp = Label(vent,text="Tiempo:").place(x=10,y=60)
cuadro = Entry(vent,font=('70'),textvariable=tiempo,width = 33).place(x = 57, y = 60)
D = Radiobutton(vent,text="Dias",variable=hora,value="dia").place(x = 10, y = 90)
B = Radiobutton(vent,text="Horas",variable=hora,value="hora").place(x = 80, y = 90)
A = Radiobutton(vent,text="Minutos",variable=hora,value="minuto").place(x = 150, y = 90)
C = Radiobutton(vent,text="Segundos",variable=hora,value="segundo").place(x = 220, y = 90)

#####YOUTUBE Omar Almonte################
by = Label(vent,text="Developed by Youtube: Omar Almonte").place(x = 70,y=120)
vent.mainloop()
