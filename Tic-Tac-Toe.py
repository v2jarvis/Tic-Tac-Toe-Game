from tkinter import *
from tkinter import ttk
import tkinter.messagebox

root=Tk()
root.title("Tic-Tac-Toe")

button1=ttk.Button(root,text=' ')
button1.grid(row=0,column=0,sticky='snew',ipadx=40,ipady=40)
button1.config(command=lambda: ButtonClick(1))

button2=ttk.Button(root,text=' ')
button2.grid(row=0,column=1,sticky='snew',ipadx=40,ipady=40)
button2.config(command=lambda: ButtonClick(2))

button3=ttk.Button(root,text=' ')
button3.grid(row=0,column=2,sticky='snew',ipadx=40,ipady=40)
button3.config(command=lambda: ButtonClick(3))

button4=ttk.Button(root,text=' ')
button4.grid(row=1,column=0,sticky='snew',ipadx=40,ipady=40)
button4.config(command=lambda: ButtonClick(4))

button5=ttk.Button(root,text=' ')
button5.grid(row=1,column=1,sticky='snew',ipadx=40,ipady=40)
button5.config(command=lambda: ButtonClick(5))

button6=ttk.Button(root,text=' ')
button6.grid(row=1,column=2,sticky='snew',ipadx=40,ipady=40)
button6.config(command=lambda: ButtonClick(6))

button7=ttk.Button(root,text=' ')
button7.grid(row=2,column=0,sticky='snew',ipadx=40,ipady=40)
button7.config(command=lambda: ButtonClick(7))

button8=ttk.Button(root,text=' ')
button8.grid(row=2,column=1,sticky='snew',ipadx=40,ipady=40)
button8.config(command=lambda: ButtonClick(8))

button9=ttk.Button(root,text=' ')
button9.grid(row=2,column=2,sticky='snew',ipadx=40,ipady=40)
button9.config(command=lambda: ButtonClick(9))

playerturn=ttk.Label(root,text="   Player 1 turn!  ")
playerturn.grid(row=3,column=0,sticky='snew',ipadx=40,ipady=40)

playerdetails=ttk.Label(root,text="    Player 1 is X\n\n    Player 2 is O")
playerdetails.grid(row=3,column=2,sticky='snew',ipadx=40,ipady=40)

res=ttk.Button(root,text='Restart')
res.grid(row=3,column=1,sticky='snew',ipadx=40,ipady=40)
res.config(command=lambda: restartbutton())

a=1
b=0
c=0

def restartbutton():
    global a,b,c
    a=1
    b=0
    c=0
    playerturn['text']="   Player 1 turn!   "
    button1['text']=' '
    button2['text']=' '
    button3['text']=' '
    button4['text']=' '
    button5['text']=' '
    button6['text']=' '
    button7['text']=' '
    button8['text']=' '
    button9['text']=' '
    button1.state(['!disabled'])
    button2.state(['!disabled'])
    button3.state(['!disabled'])
    button4.state(['!disabled'])
    button5.state(['!disabled'])
    button6.state(['!disabled'])
    button7.state(['!disabled'])
    button8.state(['!disabled'])
    button9.state(['!disabled'])
    
def disableButton():
    button1.state(['disabled'])
    button2.state(['disabled'])
    button3.state(['disabled'])
    button4.state(['disabled'])
    button5.state(['disabled'])
    button6.state(['disabled'])
    button7.state(['disabled'])
    button8.state(['disabled'])
    button9.state(['disabled'])

def ButtonClick(id):
    global a,b,c
    print("ID:{}".format(id))

    if id==1 and button1['text']==' ' and a==1:
        button1['text']="X"
        a=0
        b+=1
    if id==2 and button2['text']==' ' and a==1:
        button2['text']="X"
        a=0
        b+=1
    if id==3 and button3['text']==' ' and a==1:
        button3['text']="X"
        a=0
        b+=1
    if id==4 and button4['text']==' ' and a==1:
        button4['text']="X"
        a=0
        b+=1
    if id==5 and button5['text']==' ' and a==1:
        button5['text']="X"
        a=0
        b+=1
    if id==6 and button6['text']==' ' and a==1:
        button6['text']="X"
        a=0
        b+=1
    if id==7 and button7['text']==' ' and a==1:
        button7['text']="X"
        a=0
        b+=1
    if id==8 and button8['text']==' ' and a==1:
        button8['text']="X"
        a=0
        b+=1
    if id==9 and button9['text']==' ' and a==1:
        button9['text']="X"
        a=0
        b+=1
    
    
    if id==1 and button1['text']==' ' and a==0:
        button1['text']="O"
        a=1
        b+=1
    if id==2 and button2['text']==' ' and a==0:
        button2['text']="O"
        a=1
        b+=1
    if id==3 and button3['text']==' ' and a==0:
        button3['text']="O"
        a=1
        b+=1
    if id==4 and button4['text']==' ' and a==0:
        button4['text']="O"
        a=1
        b+=1
    if id==5 and button5['text']==' ' and a==0:
        button5['text']="O"
        a=1
        b+=1
    if id==6 and button6['text']==' ' and a==0:
        button6['text']="O"
        a=1
        b+=1
    if id==7 and button7['text']==' ' and a==0:
        button7['text']="O"
        a=1
        b+=1
    if id==8 and button8['text']==' ' and a==0:
        button8['text']="O"
        a=1
        b+=1
    if id==9 and button9['text']==' ' and a==0:
        button9['text']="O"
        a=1
        b+=1
        
       
    if( button1['text']=='X' and button2['text']=='X' and button3['text']=='X' or
        button4['text']=='X' and button5['text']=='X' and button6['text']=='X' or
        button7['text']=='X' and button8['text']=='X' and button9['text']=='X' or
        button1['text']=='X' and button4['text']=='X' and button7['text']=='X' or
        button2['text']=='X' and button5['text']=='X' and button8['text']=='X' or
        button3['text']=='X' and button6['text']=='X' and button9['text']=='X' or
        button1['text']=='X' and button5['text']=='X' and button9['text']=='X' or
        button3['text']=='X' and button5['text']=='X' and button7['text']=='X'):
            disableButton()
            c=1
            tkinter.messagebox.showinfo("Tic-Tac-Toe","Winner is player 1")
    elif( button1['text']=='O' and button2['text']=='O' and button3['text']=='O' or
        button4['text']=='O' and button5['text']=='O' and button6['text']=='O' or
        button7['text']=='O' and button8['text']=='O' and button9['text']=='O' or
        button1['text']=='O' and button4['text']=='O' and button7['text']=='O' or
        button2['text']=='O' and button5['text']=='O' and button8['text']=='O' or
        button3['text']=='O' and button6['text']=='O' and button9['text']=='O' or
        button1['text']=='O' and button5['text']=='O' and button9['text']=='O' or
        button3['text']=='O' and button5['text']=='O' and button7['text']=='O'):
            disableButton()
            c=1
            tkinter.messagebox.showinfo("Tic-Tac-Toe","Winner is player 2")
    elif b==9:
            disableButton()
            c=1
            tkinter.messagebox.showinfo("Tic-Tac-Toe","Match is Draw.")

    if a==1 and c==0:
        playerturn['text']="   Player 1 turn!   "
    elif a==0 and c==0:
        playerturn['text']="   Player 2 turn!   "
            
root.mainloop()

