from ast import Lambda
from cProfile import label
import math
from tkinter import *
from matplotlib.pyplot import text 
from PIL import ImageTk, Image

from numpy import column_stack, number
from pyrsistent import v

root=Tk()
root.title('simple calculator')
root.iconbitmap('C:/Users/pm291/Desktop/cal.ico') 


e= Entry(root, width=35, borderwidth=5) #properties of the entry
e.grid(row= 0, column=0, columnspan=3, padx=10, pady=10)

def button_add(number):
    current=e.get()
    e.delete(0, END)
    e.insert(0,str(current) + str (number))

def buttonclear():
    e.delete(0, END)

def buttonadd():
    #get the first input and remember it when another input is entered
    first_number= e.get() 
    global f_num
    global math
    math= "addition"
    f_num=int(first_number)
    e.delete(0, END)


def buttonmult():
    #get the first input and remember it when another input is entered
    first_number= e.get() 
    global f_num
    global math
    math= "multiplication"
    f_num=int(first_number)
    e.delete(0, END)
      
   

def buttonsub():
    first_number=e.get()
    global f_num
    global math
    math="subtraction"
    f_num= int(first_number)
    e.delete(0, END)



def buttondivide():
    first_number=e.get()
    global f_num
    global math
    math="division"
    f_num= int(first_number)
    e.delete(0, END)

    
def buttonperce():
    first_number=e.get()
    global f_num
    global math
    math="percentage"
    f_num= int(first_number)
    e.delete(0, END)

    


   

def buttonequal( ):
    second_number=e.get()
    e.delete(0, END)

    if math== "addition":
        e.insert(0,f_num + int(second_number))          

    if math== "subtraction":
        e.insert(0,f_num - int(second_number)) 

    if math== "division":
        e.insert(0,f_num / int(second_number))               
    if math== "multiplication":
        e.insert(0,f_num * int(second_number))     
    
     
    

 #define buttons
button1=Button(root,text='1', padx=40, pady=20,command= lambda:button_add(1))
button2=Button(root, text='2', padx=40, pady=20, command=lambda:button_add(2))
button3=Button(root, text='3', padx=40, pady=20, command=lambda:button_add(3))
button4=Button(root, text='4', padx=40, pady=20, command=lambda:button_add(4))
button5=Button(root, text='5', padx=40, pady=20, command=lambda:button_add(5))
button6=Button(root, text='6', padx=40, pady=20, command=lambda:button_add(6))
button7=Button(root, text='7', padx=40, pady=20, command=lambda:button_add(7))
button8=Button(root, text='8', padx=40, pady=20, command=lambda:button_add(8))
button9=Button(root, text='9', padx=40, pady=20, command=lambda:button_add(9))
button0=Button(root, text='0', padx=40, pady=20, command=lambda:button_add(0))


#operations
buttonadd=Button(root, text='+', padx=40, pady=20, command=buttonadd)
buttonsub=Button(root, text='-', padx=40, pady=20, command=buttonsub)
buttonequal=Button(root, text='=', padx=40, pady=20, command=buttonequal)
buttondivide=Button(root, text='/', padx=40, pady=20, command=buttondivide)
buttonclear=Button(root, text='C', padx=40, pady=20, command=buttonclear)
buttonmult=Button(root, text='*', padx=40, pady=20, command=buttonmult)
buttonperce=Button(root, text='%', padx=40, pady=20, command=buttonperce)

#put the button on the screen
button1.grid(row=3, column=1)
button2.grid(row=3, column=2)
button3.grid(row=3, column=3)
button4.grid(row=2, column=1)
button5.grid(row=2, column=2)
button6.grid(row=2, column=3)
button7.grid(row=1, column=1)
button8.grid(row=1, column=2)
button9.grid(row=1, column=3)
button0.grid(row=4, column=1)
buttonadd.grid(row=4, column=2)
buttonsub.grid(row=4, column=3)
buttonequal.grid(row=5, column=1)
buttondivide.grid(row=5, column=2)
buttonclear.grid(row=5, column=3)
buttonmult.grid(row=6, column=1)
buttonperce.grid(row=6, column=2)

#mybutton=Button(root, text="Enter your stock Quote", command=myClick)


root.mainloop()

