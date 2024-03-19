from tkinter import *


window = Tk()
window.title("Calculator")
window.geometry("500x500")
window.resizable(False,False)
window.configure(bg="#17161b")

equation = ""

def show(value):
    global equation
    equation+=value
    label_result.config(text=equation)
    
    
def clear():
    global equation
    equation = ""
    label_result.config(text=equation)
    
    
def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)
        except:
            result = "error"
            equation = ""
    label_result.config(text=result)

label_result = Label(window,width=45,height=3,text="",font=100)
label_result.pack()

Button(window,text="C",width=5, height=1, font=("arial",20,"bold"),fg="#fff", bg="#3697f5",command=lambda:clear()).place(x=20,y=100)
Button(window,text="/",width=5, height=1, font=("arial",20,"bold"),fg="#fff", bg="#2a2d36",command=lambda:show("/")).place(x=140,y=100)
Button(window,text="%",width=5, height=1, font=("arial",20,"bold"),fg="#fff", bg="#2a2d36",command=lambda:show("%")).place(x=260,y=100)
Button(window,text="x",width=5, height=1, font=("arial",20,"bold"),fg="#fff", bg="#2a2d36",command=lambda:show("x")).place(x=380,y=100)


Button(window,text="7",width=5, height=1, font=("arial",20,"bold"),fg="#fff", bg="#2a2d36",command=lambda:show("7")).place(x=20,y=180)
Button(window,text="8",width=5, height=1, font=("arial",20,"bold"),fg="#fff", bg="#2a2d36",command=lambda:show("8")).place(x=140,y=180)
Button(window,text="9",width=5, height=1, font=("arial",20,"bold"),fg="#fff", bg="#2a2d36",command=lambda:show("9")).place(x=260,y=180)
Button(window,text="-",width=5, height=1, font=("arial",20,"bold"),fg="#fff", bg="#2a2d36",command=lambda:show("-")).place(x=380,y=180)


Button(window,text="4",width=5, height=1, font=("arial",20,"bold"),fg="#fff", bg="#2a2d36",command=lambda:show("4")).place(x=20,y=260)
Button(window,text="5",width=5, height=1, font=("arial",20,"bold"),fg="#fff", bg="#2a2d36",command=lambda:show("5")).place(x=140,y=260)
Button(window,text="6",width=5, height=1, font=("arial",20,"bold"),fg="#fff", bg="#2a2d36",command=lambda:show("6")).place(x=260,y=260)
Button(window,text="+",width=5, height=1, font=("arial",20,"bold"),fg="#fff", bg="#2a2d36",command=lambda:show("+")).place(x=380,y=260)


Button(window,text="1",width=5, height=1, font=("arial",20,"bold"),fg="#fff", bg="#2a2d36",command=lambda:show("1")).place(x=20,y=340)
Button(window,text="2",width=5, height=1, font=("arial",20,"bold"),fg="#fff", bg="#2a2d36",command=lambda:show("2")).place(x=140,y=340)
Button(window,text="3",width=5, height=1, font=("arial",20,"bold"),fg="#fff", bg="#2a2d36",command=lambda:show("3")).place(x=260,y=340)


Button(window,text="=",width=5, height=3, font=("arial",20,"bold"),fg="#fff", bg="#FF5900",command=lambda:calculate()).place(x=380,y=350)

Button(window,text="0",width=12, height=1, font=("arial",20,"bold"),fg="#fff", bg="#2a2d36",command=lambda:show("0")).place(x=20,y=420)

Button(window,text=".",width=5, height=1, font=("arial",20,"bold"),fg="#fff", bg="#2a2d36",command=lambda:show(".")).place(x=260,y=420)


window.mainloop()