from tkinter import *
import pyttsx3
import datetime
import time
import webbrowser
import os
from tkinter import ttk
from playsound import playsound
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
def vp():
    if c.get()=='Male':
        j.setProperty('voice',o[0].id)
    elif c.get()=='Female':
        j.setProperty('voice',o[1].id)
    j.setProperty('volumn',vs.get())

    if vs.get()>=50 and vs.get()<=100:
        vs.configure(troughcolor='yellow')
cn=IntVar()
vs=Scale(rt,length=320,troughcolor='red',variable=cn)
vs.place(x=580,y=356)

def july():
    
    if mc.get()=='google':
        j.say('here found boss')
        j.runAndWait()
        webbrowser.open('https://google.com')
    elif mc.get()=='my song':
        j.say('here found boss')
        j.runAndWait()
        webbrowser.open('https://www.youtube.com/watch?v=sAzlWScHTc4')
    elif mc.get()=='github':
        j.say('here found boss')
        j.runAndWait()
        webbrowser.open('https://www.github.com')
    elif mc.get()=='gmail':
        j.say('here found boss')
        j.runAndWait()
        webbrowser.open('https://mail.google.com/mail/u/0/#inbox')
    elif mc.get()=='youtube':
        j.say('here found boss')
        j.runAndWait()
        webbrowser.open('https://www.youtube.com')
    elif mc.get()=='twitter':
        j.say('here found boss')
        j.runAndWait()
        webbrowser.open('https://www.twitter.com')
    elif mc.get()=='':
        j.say('please enter something')
        j.runAndWait()
    elif mc.get()=='song':
        os.startfile('C:\\Users\\adity\\Desktop\\turtle\\j.mp3')
    elif mc.get()=='day':
        j.say('today is day '+ time.strftime('%A'))
        j.runAndWait()
btn=Button(rt,text='Speak',bg='red',fg='white',width=21,font='Arial 20 bold',command=july)
btn.place(x=111,y=200)
vb=Button(rt,text='Select',width=21,bg='yellow',fg='purple',command=vp)
vb.place(x=0,y=420)
rt.mainloop()
