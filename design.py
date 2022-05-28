from tkinter import *
import pyttsx3
import datetime
import time
import webbrowser
import os
from tkinter import ttk
rt=Tk()
j=pyttsx3.init()
o=j.getProperty('voices')
j.setProperty('voice',o[1].id)
h=int(time.strftime('%H'))
m=int(time.strftime('%M'))
if h>=5 and h<=12:
    j.say('good morning boss')
    j.runAndWait()
elif h>=12 and h<=17:
    j.say('good afternoon boss')
    j.runAndWait()
elif h>=17 and h<=20:
    j.say('good eveing boss')
    j.runAndWait()
elif h>=20 and h<=0:
    j.say('good night boss')
    j.runAndWait()    
rt.geometry('700x700')
rt.zoomed()
rt.configure(background='blue')
l=Label(rt,text='Jarvis',font='Arial 18 bold')
l.place(x=0,y=0)
mc=Entry(rt,width=167,font='Arial 18 bold')
mc.place(x=0,y=100)
v=StringVar()
v=['Male','Female']
c=ttk.Combobox(rt,textvariable=v,value=v)
c.place(x=0,y=350)
c.set('Female')
lv=Label(rt,text='Voices',font='Arial 16 bold',fg='white',bg='black')
lv.place(x=0,y=320)
if v=='Male':
    j.setProperty('voice',o[0].id)
elif v=='Female':
    j.setProperty('voice',o[1].id)
def july():
    if mc.get()=='google':
        webbrowser.open('https://google.com')
        
btn=Button(rt,text='Speak',bg='red',fg='white',width=21,font='Arial 20 bold',command=july)
btn.place(x=111,y=200)
rt.mainloop()
