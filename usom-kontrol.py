from tkinter import *
import datetime
def kontrol_et():
    dosya=open("uso.txt","r")
    icerik=dosya.read()
    dosya.close()
    ip=entry1.get()
    bugun=datetime.datetime.now()
    if str(ip) in icerik:
        dosya=open("log.txt","a")
        yazi=str(ip)+"Zararlı\nTarih:"+str(bugun)+"\n"
        dosya.write(yazi)
        dosya.close()
        v.set("IP Zararlıdır")
    else:
        dosya=open("log.txt","a")
        yazi=str(ip)+"Zararlı Değil\nTarih:"+str(bugun)+"\n"
        dosya.write(yazi)
        dosya.close()
        v.set("IP Zararlı Değildir")
top=Tk()
top.title("usom ıp kontrol")
b=Button(top,text="Kontrol Et",command=kontrol_et)
b.place(x=50,y=50)
b.pack()
label1=Label(top,text="Kontrol Edilecek IP Adresini Giriniz:")
label1.place(x=50,y=80)
label1.pack()
entry1=Entry(top)
entry1.place(x=50,y=90)
entry1.pack()
v=StringVar ()
entry2=Entry(top,textvariable=v)
entry2.place(x=50,y=100)
entry2.pack()
top.mainloop()
