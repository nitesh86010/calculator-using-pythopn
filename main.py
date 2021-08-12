from tkinter import *
from tkinter.messagebox import *
import math as m

#some usefull variabble
font = ('Verdana',20,'bold')
# working functions
def clear():
    ex=textfield.get()
    ex = ex[0:len(ex)-1]
    textfield.delete(0,END)
    textfield.insert(0,ex)


def all_clear():
    textfield.delete(0,END)

def click_btn_function(event):
    print("btn clicked")
    b = event.widget
    text = b['text']
    print(text)
    if text=='x':
        textfield.insert(END,"*")
        return

    if text=='=':
        try:
            ex = textfield.get()
            anser = eval(ex)
            textfield.delete(0,END)
            textfield.insert(0,anser)
        except Exception as e:
            print("Error..")
            showerror("Error",e)
        return
    textfield.insert(END,text)

window=Tk()
window.title("Calculator")
window.geometry("480x570")
#picture lable
pic = PhotoImage(file='calulator.png')
headinglable = Label(window,image=pic)
headinglable.pack(side=TOP,pady=15)

# heading level
heading  =Label(window,text='My Calculator',font=font)
heading.pack(side=TOP)

# text field
textfield = Entry(window,font = font,justify = CENTER)
textfield.pack(side = TOP,pady =10,fill=X,padx =10)

# button
buttonFrame=Frame(window)
buttonFrame.pack(side =TOP,pady = 5)
# adding button
temp=1
for i in range(0,3):
    for j in range(0,3):
        btn=Button(buttonFrame,text=str(temp),font = font,width = 5,relief = 'ridge',activebackground = 'orange',activeforeground = 'white')
        btn.grid(row=i,column=j,padx = 2, pady = 2)
        temp = temp+1
        btn.bind('<Button-1>',click_btn_function)


zeroBtn = Button(buttonFrame,text='0',font = font,width = 5,relief = 'ridge',activebackground = 'orange',activeforeground = 'white')
zeroBtn.grid(row=3,column=1,padx = 2, pady = 2)

dotBtn = Button(buttonFrame,text='.',font = font,width = 5,relief = 'ridge',activebackground = 'orange',activeforeground = 'white')
dotBtn.grid(row=3,column=0,padx = 2, pady = 2)

equalBtn = Button(buttonFrame,text='=',font = font,width = 5,relief = 'ridge',activebackground = 'orange',activeforeground = 'white')
equalBtn.grid(row=3,column=2,padx = 2, pady = 2)

plusbtn = Button(buttonFrame,text='+',font = font,width = 5,relief = 'ridge',activebackground = 'orange',activeforeground = 'white')
plusbtn.grid(row=0,column=3,padx = 2, pady = 2)

minusbtn = Button(buttonFrame,text='-',font = font,width = 5,relief = 'ridge',activebackground = 'orange',activeforeground = 'white')
minusbtn.grid(row=1,column=3,padx = 2, pady = 2)

multbtn = Button(buttonFrame,text='x',font = font,width = 5,relief = 'ridge',activebackground = 'orange',activeforeground = 'white')
multbtn.grid(row=2,column=3,padx = 2, pady = 2)

divbtn = Button(buttonFrame,text='/',font = font,width = 5,relief = 'ridge',activebackground = 'orange',activeforeground = 'white')
divbtn.grid(row=3,column=3,padx = 2, pady = 2)

clearbtn = Button(buttonFrame,text='CLEAR',font = font,width = 11,relief = 'ridge',activebackground = 'orange',activeforeground = 'white',command = clear)
clearbtn.grid(row=4,column=2,padx = 2, pady = 2,columnspan=2)

allbtn = Button(buttonFrame,text='AC',font = font,width = 11,relief = 'ridge',activebackground = 'orange',activeforeground = 'white',command = all_clear)
allbtn.grid(row=4,column=0,padx = 2, pady = 2,columnspan=2)

#binding all buttons

zeroBtn.bind('<Button-1>',click_btn_function)
equalBtn.bind('<Button-1>',click_btn_function)
divbtn.bind('<Button-1>',click_btn_function)
multbtn.bind('<Button-1>',click_btn_function)
dotBtn.bind('<Button-1>',click_btn_function)
plusbtn.bind('<Button-1>',click_btn_function)
minusbtn.bind('<Button-1>',click_btn_function)


def enterclick(event):
    print(':hiiiii')
    e = Event()
    e.widget = equalBtn
    click_btn_function(e)

textfield.bind('<Return>',enterclick)


#########################################################################################
# functions

sc_frame = Frame(window)
sqrtbtn = Button(sc_frame,text='sqrt',font = font,width = 5,relief = 'ridge',activebackground = 'orange',activeforeground = 'white')
sqrtbtn.grid(row=0,column=0,padx = 3, pady = 3)

powbtn = Button(sc_frame,text='^',font = font,width = 5,relief = 'ridge',activebackground = 'orange',activeforeground = 'white')
powbtn.grid(row=0,column=1,padx = 3, pady = 3)

factbtn = Button(sc_frame,text='!',font = font,width = 5,relief = 'ridge',activebackground = 'orange',activeforeground = 'white')
factbtn.grid(row=0,column=2,padx = 3, pady = 3)

radbtn = Button(sc_frame,text='Rad',font = font,width = 5,relief = 'ridge',activebackground = 'orange',activeforeground = 'white')
radbtn.grid(row=0,column=3,padx = 3, pady = 3)

sinbtn = Button(sc_frame,text='sin',font = font,width = 5,relief = 'ridge',activebackground = 'orange',activeforeground = 'white')
sinbtn.grid(row=1,column=0,padx = 3, pady = 3)

cosbtn = Button(sc_frame,text='cos',font = font,width = 5,relief = 'ridge',activebackground = 'orange',activeforeground = 'white')
cosbtn.grid(row=1,column=1,padx = 3, pady = 2)

tanbtn = Button(sc_frame,text='tan',font = font,width = 5,relief = 'ridge',activebackground = 'orange',activeforeground = 'white')
tanbtn.grid(row=1,column=2,padx = 3, pady = 3)


degbtn = Button(sc_frame,text='Deg',font = font,width = 5,relief = 'ridge',activebackground = 'orange',activeforeground = 'white')
degbtn.grid(row=1,column=3,padx = 3, pady = 3)


normal_calc=True

def cal_sc(event):
    print("btn...")
    btn=event.widget
    text = btn['text']
    print(text)
    ex = textfield.get()
    answer = ''
    if text == 'Rad':
        print("radian")
        answer=str(m.degrees(float(ex)))
        
    elif text == "Deg":
        print("degree")
        answer = str(m.radians(float(ex)))
    elif text=="sin":
        print("sin")
        answer = str(m.sin(m.radians(float(ex))))
    elif text=="cos":
        print("cos")
        answer= str(m.cos(m.radians(int(ex))))
    elif text=="tan":
        print("tan")
        answer = str(m.tan(m.radians(int(ex))))
    elif text =="!":
        print("factorial")
        answer = str(m.factorial(int(ex)))

    elif text  == "sqrt":
        print('squaroot')
        answer = str(m.sqrt(int(ex)))

    elif text=='^':
        print("power")
        base,pow = ex.split("^")
        print('base')
        print("power")
        answer=m.pow(int(base),int(pow))

    textfield.delete(0,END)
    textfield.insert(0,answer)

def sc_click():
    global normal_calc
    if (normal_calc):
        buttonFrame.pack_forget()
        sc_frame.pack(side=TOP,pady = 5)
        buttonFrame.pack(side=TOP)
        window.geometry("480x700")

        print("Show scientific")
        normal_calc = False
    else:
        print("Show normal")
        sc_frame.pack_forget()
        window.geometry("480x570")
        normal_calc = True

# binding sc button

powbtn.bind('<Button-1>',cal_sc)
sinbtn.bind('<Button-1>',cal_sc)
cosbtn.bind('<Button-1>',cal_sc)
tanbtn.bind('<Button-1>',cal_sc)
factbtn.bind('<Button-1>',cal_sc)
sqrtbtn.bind('<Button-1>',cal_sc)
degbtn.bind('<Button-1>',cal_sc)
radbtn.bind('<Button-1>',cal_sc)


fontMenu = ('',12,'bold')
menubar = Menu(window)

mode = Menu(menubar,font= fontMenu,tearoff=0)
mode.add_checkbutton(label="Scientific Mode",command=sc_click)


menubar.add_cascade(label="Mode",menu=mode)
window.config(menu=menubar)



window.mainloop()