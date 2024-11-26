from tkinter import*
import math as m

window=Tk()
window.geometry("383x570+470+20")
window.config(bg="white")
window.title("python calculator")
window.resizable(True,False)
#window.overriderdirect(1)

# function

def close():
    window.destroy()
def clear():
    entry.delete(0,"end")

def back():
    last_number = len(entry.get())-1
    entry.delete(last_number)

def press(input):
    lenth = len(entry.get())
    entry.insert(lenth,input)
def add(a,b):
    return float(a)+float(b)

def subtract(a,b):
    return float(a)-float(b)

def divide(a,b):
    return float(a)/float(b)

def multiply(a,b):
    return float(a)*float(b)

def percnatge(a,b):
    return float(a)%float(b)

def expression_break(sign, expression):
    values = expression.split(sign,1)
    return values

def scientific(expression):
    data = expression_break("(",expression)
    if data[0] == "tan":
        result = m.tan(float(data[1]))

    elif data[0] == "cos":
        result = m.cos(float(data[1]))

    elif data[0] == "sin":
        result = m.sin(float(data[1]))

    elif data[0] == "sqrt":
        result = m.sqrt(float(data[1]))

    elif data[0] == "log":
        result =m.log10(float(data[1]))

    elif data[0] == "ln":
        result = m.log(float(data[1]))

    elif data[0] == "deg":
        result = m.degrees(float(data[1]))

    elif data[0] == "rad":
        result = m.radians(float(data[1]))

    elif data[0] == "fac":
        result = m.factorial(float(data[1]))
    return result


def equal():
    expression = entry.get()
    clear()
    try:
  
       

       if expression.find("(") > 0:
           result = scientific(expression)

       elif expression.find("pow") > 0:
                data = expression_break("pow",expression)
                result = m.pow(float(data[0]),float(data[1]))

       elif expression.find("rem") > 0:
         data = expression_break("rem", expression)
         result = m.remainder(float(data[0]),float(data[1]))

       elif expression.find("x") > 0:
                data = expression_break("x",expression)
                result = multiply(data[0],data[1])

       elif expression.find("*") > 0:
         data = expression_break("*", expression)
         result = multiply(data[0],data[1])

       elif expression.find("÷") > 0:
         data = expression_break("÷", expression)
         result = divide(data[0],data[1])

       elif expression.find("/") > 0:
         data = expression_break("/", expression)
         result = divide(data[0],data[1])


       elif expression.find("%") > 0:
         data = expression_break("%", expression) 
         result = percnatge(data[0],data[1])


       elif expression.find("+") > 0:
         first = expression.find("+")
         second = expression.find("+",(first+1),(first+5))
         if first > second:
            data = expression_break("+", expression)
            result = add(data[0],data[1])
         else:
            result = add(expression[0:second],expression[second+1:])
         
       elif   expression.rindex("-") > 0:
              sign = expression.rindex("-")
              result = subtract(expression[0:sign],expression[sign+1:])


       entry.insert(0, result)

    except:
        entry.insert(0,"Error")

entry_string = StringVar()

# define button
#entry = Entry(window, textvariable = entry_string, foreground="white",background="grey20",border=0,font=("bahnschrift semibold",26))
entry=Entry(window,font=('arial',19,'bold'),bg='white',fg='black',bd=10,relief=SUNKEN,width=25)
entry.grid(columnspan=4,ipady=10)


font_value = ("calibari",18)
btn_tan = Button(window, text="tan", background="skyblue",foreground="white", font=font_value,borderwidth=1,relief= SOLID, command= lambda:press("tan("))
btn_tan.grid(row=1,column=0, sticky=E+W, ipady=5)

btn_cos = Button(window, text="cos", background="skyblue",foreground="white", font=font_value,borderwidth=1,relief= SOLID, command= lambda:press("cos("))
btn_cos.grid(row=1,column=1, sticky=E+W, ipady=5)

btn_sin = Button(window, text="sin", background="skyblue",foreground="white", font=font_value,borderwidth=1,relief= SOLID,command= lambda:press("sin(")) 
btn_sin.grid(row=1,column=2, sticky=E+W, ipady=5)

btn_sqrt = Button(window, text="sqrt", background="skyblue",foreground="white", font=font_value,borderwidth=1,relief= SOLID,command= lambda:press("sqrt(")) 
btn_sqrt.grid(row=1,column=3, sticky=E+W, ipady=5)

btn_log = Button(window, text="log", background="skyblue",foreground="white", font=font_value,borderwidth=1,relief= SOLID,command= lambda:press("log("))
btn_log.grid(row=2,column=0, sticky=E+W, ipady=5)

btn_ln = Button(window, text="ln", background="skyblue",foreground="white", font=font_value,borderwidth=1,relief= SOLID,command= lambda:press("ln(")) 
btn_ln.grid(row=2,column=1, sticky=E+W, ipady=5)


btn_deg = Button(window, text="deg", background="skyblue",foreground="white", font=font_value,borderwidth=1,relief= SOLID,command= lambda:press("deg("))  # deg dgree 
btn_deg.grid(row=2,column=2, sticky=E+W, ipady=5)

btn_rad = Button(window, text="rad", background="skyblue",foreground="white", font=font_value,borderwidth=1,relief= SOLID, command= lambda:press("rad("))
btn_rad.grid(row=2,column=3, sticky=E+W, ipady=5)

btn_fac = Button(window, text="fac", background="skyblue",foreground="white", font=font_value,borderwidth=1,relief= SOLID, command= lambda:press("fac("))    # fac
btn_fac.grid(row=3,column=0, sticky=E+W, ipady=5)

btn_pow = Button(window, text="pow", background="skyblue",foreground="white", font=font_value,borderwidth=1,relief= SOLID, command= lambda:press("pow"))  # poe power
btn_pow.grid(row=3,column=1, sticky=E+W, ipady=5)

btn_rem = Button(window, text="rem", background="skyblue",foreground="white", font=font_value,borderwidth=1,relief= SOLID, command= lambda:press("rem"))  # red remainder
btn_rem.grid(row=3,column=2, sticky=E+W, ipady=5)

btn_pi = Button(window, text="π", background="skyblue",foreground="white", font=font_value,borderwidth=1,relief= SOLID,  command= lambda:press(3.141592))  
btn_pi.grid(row=3,column=3, sticky=E+W, ipady=5)


btn_clear = Button(window, text="C", background="black",foreground="white", font=font_value,borderwidth=1,relief= SOLID,command = clear)  # red remainder
btn_clear.grid(row=4, columnspan=2,column=0, sticky=E+W, ipady=5)

btn_backspace = Button(window, text="B", background="black",foreground="white", font=font_value,borderwidth=1,relief= SOLID,command = back)   
btn_backspace.grid(row=4, columnspan=2,column=2, sticky=E+W, ipady=5)


btn7 = Button(window, text="7", background="skyblue",foreground="white", font=font_value,borderwidth=1,relief= SOLID, command=lambda:press(7))
btn7.grid(row=5,column=0, sticky=E+W, ipady=5)

btn8 = Button(window, text="8", background="skyblue",foreground="white", font=font_value,borderwidth=1,relief= SOLID, command=lambda:press(8))
btn8.grid(row=5,column=1, sticky=E+W, ipady=5)

btn9 = Button(window, text="9", background="skyblue",foreground="white", font=font_value,borderwidth=1,relief= SOLID, command=lambda:press(9))
btn9.grid(row=5,column=2, sticky=E+W, ipady=5)

btn_div = Button(window, text="÷", background="white",foreground="red", font=font_value,borderwidth=1,relief= SOLID, command=lambda:press("÷"))
btn_div.grid(row=5,column=3, sticky=E+W, ipady=5)

btn4 = Button(window, text="4", background="skyblue",foreground="white", font=font_value,borderwidth=1,relief= SOLID, command=lambda:press(4) )
btn4.grid(row=6,column=0, sticky=E+W, ipady=5)

btn5 = Button(window, text="5", background="skyblue",foreground="white", font=font_value,borderwidth=1,relief= SOLID, command=lambda:press(5))
btn5.grid(row=6,column=1, sticky=E+W, ipady=5)


btn6 = Button(window, text="6", background="skyblue",foreground="white", font=font_value,borderwidth=1,relief= SOLID, command=lambda:press(6)) # deg dgree 
btn6.grid(row=6,column=2, sticky=E+W, ipady=5)

btn_multi = Button(window, text="x", background="white",foreground="red", font=font_value,borderwidth=1,relief= SOLID, command=lambda:press("*"))
btn_multi.grid(row=6,column=3, sticky=E+W, ipady=5)

btn1 = Button(window, text="1", background="skyblue",foreground="white", font=font_value,borderwidth=1,relief= SOLID, command=lambda:press(1))   # fac
btn1.grid(row=7,column=0, sticky=E+W, ipady=5)

btn2 = Button(window, text="2", background="skyblue",foreground="white", font=font_value,borderwidth=1,relief= SOLID,command=lambda:press(2) )   # poe power
btn2.grid(row=7,column=1, sticky=E+W, ipady=5)

btn3 = Button(window, text="3", background="skyblue",foreground="white", font=font_value,borderwidth=1,relief= SOLID,command=lambda:press(3) )  # red remainder
btn3.grid(row=7,column=2, sticky=E+W, ipady=5)


btn_sub = Button(window, text="-", background="white",foreground="red", font=font_value,borderwidth=1,relief= SOLID, command=lambda:press("-"))
btn_sub.grid(row=7,column=3, sticky=E+W, ipady=5)

btn_dot = Button(window, text=".", background="skyblue",foreground="white", font=font_value,borderwidth=1,relief= SOLID, command=lambda:press("."))
btn_dot.grid(row=8,column=0, sticky=E+W, ipady=5)

btn0 = Button(window, text="0", background="skyblue",foreground="white", font=font_value,borderwidth=1,relief= SOLID, command=lambda:press(0))
btn0.grid(row=8,column=1, sticky=E+W, ipady=5)


btn_e = Button(window, text="e", background="skyblue",foreground="white", font=font_value,borderwidth=1,relief= SOLID, command=lambda:press(2.71828)) # deg dgree 
btn_e.grid(row=8,column=2, sticky=E+W, ipady=5)

btn_add = Button(window, text="+", background="white",foreground="red", font=font_value,borderwidth=1,relief= SOLID, command=lambda:press("+"))
btn_add.grid(row=8,column=3, sticky=E+W, ipady=5)

btn_per = Button(window, text="%", background="skyblue",foreground="white", font=font_value,borderwidth=1,relief= SOLID, command=lambda:press("%"))  # red remainder
btn_per.grid(row=9,column=0, sticky=E+W, ipady=5)


btn_equal = Button(window, text="=", background="skyblue",foreground="white", font=font_value,borderwidth=1,relief= SOLID, command= equal)   # fac
btn_equal.grid(row=9,column=1, sticky=E+W, ipady=5)

btn_close = Button(window, text="close", background="skyblue",foreground="white", font=font_value,borderwidth=1,relief= SOLID, command = close)   # poe power
btn_close.grid(row=9, columnspan=2,column=2, sticky=E+W, ipady=5)

mainloop()