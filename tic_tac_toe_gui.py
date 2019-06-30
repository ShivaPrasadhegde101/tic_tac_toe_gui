from tkinter import *
from tkinter import messagebox

window=Tk()
    
window.configure(background="light blue")
window.title("TIC-TAC-TOE-GAME")
l1=Label(window,text="Player1:-X",font=('Times New Roman','12'))
l1.grid(row=0,column=0)
l2=Label(window,text="Player2:-0",font=('Times New Roman','12'))
l2.grid(row=0,column=2)
l3=Label(window,text='Player1 turn ',font=('Times New Roman','12'))
l3.grid(row=1,column=0)

win=1
running=0
game=running
chance=0

def click1():
    
    global chance
    global game
    if(game==running):
        if(b1['text']!=' '):
            messagebox.showinfo('Error','Already choosen')
        else:
            
            if(chance%2==0):
                b1['text']='X'
                l3['text']='Player2 turn'
            else:
                b1['text']='O'
                l3['text']='Player1 turn'
            Winner()
            result(chance)
            chance=chance+1

def click2():
    global chance
    global game
    if(game==running):
        if(b2['text']!=' '):
            messagebox.showinfo('Error','Already choosen')
        else:
            
            if(chance%2==0):
                b2['text']='X'
                l3['text']='Player2 turn'
            else:
                b2['text']='O'
                l3['text']='Player1 turn'
            Winner()
            result(chance)
            chance=chance+1

def click3():
    global chance
    global game
    if(game==running):
        if(b3['text']!=' '):
            messagebox.showinfo('Error','Already choosen')
        else:
            
            if(chance%2==0):
                b3['text']='X'
                l3['text']='Player2 turn'
            else:
                b3['text']='O'
                l3['text']='Player1 turn'
            Winner()
            result(chance)
            chance=chance+1

def click4():
    global chance
    global game
    if(game==running):
        if(b4['text']!=' '):
            messagebox.showinfo('Error','Already choosen')
        else:
            
            if(chance%2==0):
                b4['text']='X'
                l3['text']='Player2 turn'
            else:
                b4['text']='O'
                l3['text']='Player1 turn'
            Winner()
            result(chance)
            chance=chance+1

def click5():
    global chance
    global game
    if(game==running):
        if(b5['text']!=' '):
            messagebox.showinfo('Error','Already choosen')
        else:
            
            if(chance%2==0):
                b5['text']='X'
                l3['text']='Player2 turn'
            else:
                b5['text']='O'
                l3['text']='Player1 turn'
            Winner()
            result(chance)
            chance=chance+1

def click6():
    global chance
    global game
    if(game==running):
        if(b6['text']!=' '):
            messagebox.showinfo('Error','Already choosen')
        else:
            
            if(chance%2==0):
                b6['text']='X'
                l3['text']='Player2 turn'
            else:
                b6['text']='O'
                l3['text']='Player1 turn'
            Winner()
            result(chance)
            chance=chance+1

def click7():
    global chance
    global game
    if(game==running):
        if(b7['text']!=' '):
            messagebox.showinfo('Error','Already choosen')
        else:
            
            if(chance%2==0):
                b7['text']='X'
                l3['text']='Player2 turn'
            else:
                b7['text']='O'
                l3['text']='Player1 turn'
            Winner()
            result(chance)
            chance=chance+1

def click8():
    global chance
    global game
    if(game==running):
        if(b8['text']!=' '):
            messagebox.showinfo('Error','Already choosen')
        else:
            
            if(chance%2==0):
                b8['text']='X'
                l3['text']='Player2 turn'
            else:
                b8['text']='O'
                l3['text']='Player1 turn'
            Winner()
            result(chance)
            chance=chance+1

def click9():
    global chance
    global game
    if(game==running):
        if(b9['text']!=' '):
            messagebox.showinfo('Error','Already choosen')
        else:
            if(chance%2==0):
                b9['text']='X'
                l3['text']='Player2 turn'
            else:
                b9['text']='O'
                l3['text']='Player1 turn'
            Winner()
            result(chance)
            chance=chance+1

    

    


b1 = Button(window, text=' ', font='Arial', bg='light green', fg='black', height=6, width=10, command=click1)
b1.grid(row=3, column=0)

b2 = Button(window, text=' ', font='Arial', bg='light green', fg='black', height=6, width=10, command=click2)
b2.grid(row=3, column=1)

b3 = Button(window, text=' ',font='Arial', bg='light green', fg='black', height=6, width=10, command=click3)
b3.grid(row=3, column=2)

b4 = Button(window, text=' ', font='Arial', bg='light green', fg='black', height=6, width=10, command= click4)
b4.grid(row=4, column=0)

b5 = Button(window, text=' ', font='Arial', bg='light green', fg='black', height=6, width=10, command=click5)
b5.grid(row=4, column=1)

b6 = Button(window, text=' ', font='Arial', bg='light green', fg='black', height=6, width=10, command=click6)
b6.grid(row=4, column=2)

b7 = Button(window, text=' ', font='Arial', bg='light green', fg='black', height=6, width=10, command=click7)
b7.grid(row=5, column=0)

b8 = Button(window, text=' ', font='Arial', bg='light green', fg='black', height=6, width=10, command=click8)
b8.grid(row=5, column=1)

b9 = Button(window, text=' ', font='Arial', bg='light green', fg='black', height=6, width=10, command=click9)
b9.grid(row=5, column=2)
def Winner():
    global game
    if(b1['text']==b2['text'] and b2['text'] ==b3['text'] and b2['text']!=' '):
        game=win
    elif(b4['text']==b5['text'] and b5['text'] ==b6['text'] and b5['text']!=' '):
        game=win
    elif(b7['text']==b8['text'] and b8['text'] ==b9['text'] and b8['text']!=' '):
        game=win
    elif(b1['text']==b4['text'] and b4['text'] ==b7['text'] and b1['text']!=' '):
        game=win
    elif(b2['text']==b5['text'] and b5['text'] ==b8['text'] and b2['text']!=' '):
        game=win
    elif(b3['text']==b6['text'] and b6['text'] ==b9['text'] and b3['text']!=' '):
        game=win
    elif(b1['text']==b5['text'] and b5['text'] ==b9['text'] and b5['text']!=' '):
        game=win
    elif(b3['text']==b5['text'] and b5['text'] ==b7['text'] and b5['text']!=' '):
        game=win
    elif(b1['text']!=' ' and b2['text']!=' ' and b3['text']!=' ' and b4['text']!=' ' and b5['text']!=' ' and b6['text']!=' ' and b7['text']!=' ' and b8['text']!=' ' and b9['text']!=' '):
        game=-1
    else:
        game=running

def result(chance):
    global game
    if(game==1):
        if(chance%2==0):
            messagebox.showinfo('Result','Player 1 won!!!')
        else:
            messagebox.showinfo('Result','Player 2 won!!!')
    elif(game==-1):
        messagebox.showinfo('Result','Its a tie!!!')



window.mainloop()
        
