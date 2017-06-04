
#from Tkinter import messagebox

from Tkinter import *
import Tkinter
from netifaces import interfaces, ifaddresses, AF_INET
import socket
import sys
import datetime
import subprocess
from datetime import datetime
global ips,lista,direcciones
ips=[]
lista=[]
direcciones=[]
#####Funcion que realiza el escaneo obteniendo la ip del equipo de manera automatica#####

def scan():
    global ips, ip, lista
###Obtiene la ip del equipo
    for ifaceName in interfaces():
        addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] )]
        #print '%s: %s' % (ifaceName, ', '.join(addresses))
        direcciones.append(str(addresses))
    dir=str(direcciones[2])
    direc=(dir.lstrip("[u'")).rstrip("']")
###Realiza la separacion de la ip por puntos
    ipa=direc.split(".")
    print ipa
    ipa[3]=''
    ip_auto=".".join(ipa)
    print ip_auto
######Realiza el escaneo de equipos de acuerdo a la ip del equipo
    if ip_auto:
        ListaEquiposActivos.delete(0, END)   #Borra los elementos de la lista
        t_in = datetime.now()
        ips=[]######################################
        lista=[]
        for ping in range(1, 255):
            ip= ip_auto + str(ping)
            #result=subprocess.call(["ping", "-c1", "-n", "-i 0.3", "-W1", ip])
            result=subprocess.call(['ping', '-n',' 1 ','-w',' 2','-l 10','-i 0.2', ip])
            if result == 0:
                ips.append(ip)
        for lista in ips:
            ListaEquiposActivos.insert(END,lista)
            print lista + " activo"
        t_fin=datetime.now()
        t_t=t_fin-t_in
        tiempo=str(t_t.total_seconds())
        etiquetaIP = Label(ventana,text=" Escaneo terminado en "+tiempo+" segundos",font=("Helvetica",12),bitmap="hourglass", compound="left").place(x=200,y=350)
        return ips
        print ips
    else:
        return 0
#### FUncion para proporcionar la ip privada del equipo########
def myip():
    ventana3=Toplevel(ventana)
    ventana3.iconbitmap('esime.ico')
    ventana3.title("Direccion IP")
    ventana3.geometry("235x30")
    ventana3.configure(background=colorFondo)
    for ifaceName in interfaces():
        addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] )]
        print '%s: %s' % (ifaceName, ', '.join(addresses))
        direcciones.append(str(addresses))
    dir=str(direcciones[5])
    direc=(dir.lstrip("[u'")).rstrip("']")
    print direc
    myip = Label(ventana3,text="Mi IP: "+direc,bg=colorFondo,fg=colorLetra,font=("Helvetica",16))
    myip.pack()
    ventana3.mainloop()
#######FUncion que realiza el escaneo de puertos#########
def ports():
    print ips
    ventana2=Toplevel(ventana)
    ventana2.iconbitmap('esime.ico')
    ventana2.title("Puertos activos")
    ventana2.geometry("340x380")
    ventana2.configure(background=colorFondo)
    opcion=ListaEquiposActivos.curselection()
    host=int(opcion[0])
    equipo = Label(ventana2,text="Equipo escaneado: "+str(ips[host]),bg=colorFondo,fg=colorLetra,font=("Helvetica",13))
    resultado = Listbox(ventana2,font=("Helvetica",16))
    espacio=Label(ventana2, text="",bg=colorFondo)
    espacio1=Label(ventana2, text="",bg=colorFondo)
    espacio2=Label(ventana2, text="",bg=colorFondo)
    espacio1.pack()
    equipo.pack()
    espacio.pack()
    resultado.pack()
    #print "Escaneando: ",ips[host]
    IP=ips[host]
    inicio = datetime.now()
    for i in range(1, 200):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((IP, i))
        if(result == 0) :
            print'Port open' ,i
            a="Puerto: "+str(i)
            resultado.insert(END,a)
    s.close()
    final = datetime.now()
    tiempo = final - inicio
    segundos = tiempo.total_seconds()
    espacio2.pack()
    tiempo = Label(ventana2,text="Tiempo de espera: "+str(segundos)+" segundos",fg=colorLetra,font=("Helvetica",12),bitmap="hourglass", compound="left")
    tiempo.pack()
    print 'Tiempo De Espera: ', segundos , 'segundos'
    ventana2.mainloop()
###Funcion para escanear un equipo o subred introduciendo la ip manualmente
def hosts():

    ListaEquiposActivos.delete(0, END)
    global ip_auto, ips, lista
    if checke.get()==1 and checks.get()==0 and ingresatuIP.get():
        ips=[]
        lista=[]  ######################################
        ip_auto= ingresatuIP.get()
        ips.append(ip_auto)
        lista.append(ip_auto)
        t_in = datetime.now()
        result=subprocess.call(['ping', '-n',' 1 ','-w',' 3','-l 10','-i 0.2',ip_auto])
        if result == 0:
            ListaEquiposActivos.insert(END,ip_auto)
            print ip_auto
        t_fin=datetime.now()
        t_t=t_fin-t_in
        tiempo=str(t_t.total_seconds())
        etiquetaIP = Label(ventana,text=" Escaneo terminado en "+tiempo+" segundos",font=("Helvetica",12),bitmap="hourglass", compound="left").place(x=200,y=350)

    elif checke.get()==0 and checks.get()==1 and ingresatuIP.get():
        ips=[]      ###Vacia la los datos de la lista
        lista=[]
        ipa=str(ingresatuIP.get()).split(".")
        ipa[3]=''
        ip_auto='.'.join(ipa)
        print ip_auto
        eq()
    else:
        return 0
def eq():
    t_in = datetime.now()
    for ping in range(1, 255):
        ip= ip_auto + str(ping)
        #result=subprocess.call(["ping", "-c1", "-n", "-i 0.3", "-W1", ip])
        result=subprocess.call(['ping', '-n',' 1 ','-w',' 5','-l 10','-i 0.2', ip])
        if result == 0:
            ips.append(ip)
    for lista in ips:
        ListaEquiposActivos.insert(END,lista)
        print lista + " activo"
    t_fin=datetime.now()
    t_t=t_fin-t_in
    tiempo=str(t_t.total_seconds())
    etiquetaIP = Label(ventana,text=" Escaneo terminado en "+tiempo+" segundos",font=("Helvetica",12),bitmap="hourglass", compound="left").place(x=200,y=350)

ventana = Tk()
imagen = PhotoImage(file="es.gif")
ventana.iconbitmap('guinda.ico')
ingresatuIP = StringVar()
global ListaEquiposActivos
checke=IntVar()
checks=IntVar()
colorFondo = "#BFBFFF"
colorLetra = "#004040"
ventana.title("Escaner de Equipos y Puertos activos")
ventana.geometry("660x390")
ventana.configure(background=colorFondo)

#escudo = Label (ventana,image=imagen,width=100,height=100).place(x=10,y=110)
etiquetaTitulo = Label(ventana,text="Escaner de Equipos y Puertos Activos",bg=colorFondo,fg=colorLetra,font=("Helvetica",18))
etiquetaIP = Label(ventana,text="Ingresa la IP: ",bg=colorFondo,fg=colorLetra,font=("Helvetica",14)).place(x=196,y=76)
cajaIP = Entry(ventana,textvariable=ingresatuIP).place(x=330,y=80)
botonMIIP = Button(ventana, text=" Mi IP",command=myip, bitmap="questhead", compound="left").place(x=30,y=30)
botonEquiposActivos = Button(ventana, text="Escanear", command=hosts,compound="left").place(x=30,y=210)
botonprueba = Button(ventana, text="Escaneo Automatico", command=scan,compound="left").place(x=520,y=160)
ListaEquiposActivos = Listbox(ventana, height=10,width=30)
espacio=Label(ventana, text="\n\n\n\n\n",bg=colorFondo)
unespacio=Label(ventana, text="",bg=colorFondo)
checkequipo=Checkbutton(text="Escanear equipo",bg=colorFondo, variable=checke).place(x=30,y=140)
checksubred=Checkbutton(text="Escanear subred",bg=colorFondo, variable=checks).place(x=30,y=170)
#Posicion de los elementos
unespacio.pack()
etiquetaTitulo.pack()
espacio.pack()
ListaEquiposActivos.pack()
botonEscanearPuertos = Button(ventana, text="Escanear Puertos",command=ports).place(x=520,y=303)
ventana.mainloop()
