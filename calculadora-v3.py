# objetivo: fazer uma calculadora estilo a que eu tenho
# part1: fazer toods os botões da calculadora incluindo operações e botao de clear
# part2: criar tela para exibição de números

from tkinter import *

# create window
win = Tk()
win.title("Calculadora Teste.")
# window specs
largura = "525"
altura = "600"
win.geometry("%sx%s" % (largura, altura))
win.configure(bg="black")

# center window
largurawin = win.winfo_screenwidth()
alturawin = win.winfo_screenheight()

posX = largurawin // 2 - int(largura) // 2
posY = alturawin // 2 - int(altura) // 2
win.geometry(f"+{posX}+{posY}")


# frame areas and location

numbers = Frame(win)
numbers.pack(side="bottom")

expscreen = Frame(win)
expscreen.pack(side="top", anchor="w")

numscreen = Frame(win)
numscreen.pack(side="top", anchor="e")

screen = Frame(win)
screen.pack(side="top")

#####################################################################################

# def areas


def addscreen(num):
    global expnum, firstresult, firstnum
    if not firstresult:
        if ("".join(expnum)) == "" and num in ["+", "-", "x", "÷"]:
            pass
        else:
            if firstnum:
                expnum.append(str(num))
                displayexpnum.config(text="".join(expnum))
                firstnum = False
            elif not firstnum:
                if expnum == []:
                    if num in ["+", "-", "x", "÷"]:
                        pass
                    else:
                        expnum.append(str(num))
                        displayexpnum.config(text="".join(expnum))
                else:
                    last_element = expnum[-1]
                    if last_element in ["+", "-", "x", "÷"] and num in ["+", "-", "x", "÷"]:
                        pass
                    else:
                        expnum.append(str(num))
                        displayexpnum.config(text="".join(expnum))
    elif firstresult:
        if num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, "(", ")"]:
            pass
        else:
            expnum = [str(memorynum)]
            expnum.extend(str(num))
            displayexpnum.config(text="".join(expnum))
            firstresult = False


def result():
    global expnum, displaynum, finalnum, memorynum, firstresult
    currentnum = str(("".join(expnum)))
    if currentnum == "":
        pass
    else:
        currentnum = currentnum.replace("x", "*").replace("÷", "/")
        try:
            result = round(eval(currentnum), 5)
        except ZeroDivisionError:
            displaynum.config(text=("Math Error..."))
            firstresult = True
        else:
            displaynum.config(text=(result))
            memorynum = displaynum.cget("text")
            firstresult = True


def clear():
    global expnum, displayexpnum, firstresult, firstnum
    expnum = []
    displayexpnum.config(text="")
    displaynum.config(text=0)
    firstresult = False
    firstnum = True


def delete():
    global expnum, displayexpnum
    if firstresult:
        pass
    elif ("".join(expnum)) == "":
        pass
    else:
        last_element = expnum.pop()
        displayexpnum.config(text="".join(expnum))


# screen number

expnum = []

memorynum = 0

firstresult = False
firstnum = True


# frame SCREEN_NUM

displayexpnum = Label(
    expscreen,
    text=expnum,
    bg="black",
    fg="white",
    font=("Arial", 40),
)
displayexpnum.pack()

displaynum = Label(
    numscreen,
    text=0,
    bg="black",
    fg="white",
    font=("Arial", 50),
)
displaynum.pack()


# frame NUMBERS

butt0 = Button(
    numbers,
    text="0",
    width=10,
    height=2,
    font=("Arial", 25),
    bg="#333333",
    fg="white",
    command=lambda: addscreen(0),
)


# buttons 1 to 9
def ButtonCreator(x, y):
    for i in range(x, y):
        name = "butt" + str(i)
        globals()[name] = Button(
            numbers,
            text="%s" % (i),
            width=5,
            height=2,
            font=("Arial", 25),
            bg="#333333",
            fg="White",
            command=lambda digit=i: addscreen(digit),
        )


ButtonCreator(1, 10)


# buttons (+ - * /)
def ButtonCreatorlist(nums, names):
    for i, j in zip(nums, names):
        name = "butt" + str(j)
        globals()[name] = Button(
            numbers,
            text="%s" % (i),
            width=5,
            height=2,
            font=("Arial", 25),
            bg="#fe9504",
            fg="White",
            command=lambda digit=i: addscreen(digit),
        )


simbs = ["+", "-", "x", "÷"]
names = ["plus", "minus", "multi", "div"]
ButtonCreatorlist(simbs, names)


buttclear = Button(
    numbers,
    text="AC",
    width=5,
    height=2,
    font=("Arial", 25),
    bg="#a5a5a5",
    fg="white",
    command=lambda: clear(),
)

buttresult = Button(
    numbers,
    text="=",
    width=5,
    height=2,
    font=("Arial", 25),
    bg="#333333",
    fg="white",
    command=lambda: result(),
)
buttdeci = Button(
    numbers,
    text=".",
    width=5,
    height=2,
    font=("Arial", 25),
    bg="#333333",
    fg="white",
    command=lambda: addscreen("."),
)
buttparent = Button(
    numbers,
    text="(",
    width=5,
    height=2,
    font=("Arial", 25),
    bg="#333333",
    fg="white",
    command=lambda: addscreen("("),
)
buttparent2 = Button(
    numbers,
    text=")",
    width=5,
    height=2,
    font=("Arial", 25),
    bg="#333333",
    fg="white",
    command=lambda: addscreen(")"),
)

# coordlist =

butt0.grid(row=4, column=0, columnspan=2, sticky="We")
butt1.grid(row=3, column=0)
butt2.grid(row=3, column=1)
butt3.grid(row=3, column=2)
butt4.grid(row=2, column=0)
butt5.grid(row=2, column=1)
butt6.grid(row=2, column=2)
butt7.grid(row=1, column=0)
butt8.grid(row=1, column=1)
butt9.grid(row=1, column=2)
buttplus.grid(row=3, column=3)
buttminus.grid(row=3, column=4)
buttmulti.grid(row=2, column=3)
buttdiv.grid(row=2, column=4)
buttresult.grid(row=4, column=4)
buttclear.grid(row=4, column=3)
buttdeci.grid(row=4, column=2)
buttparent.grid(row=1, column=3)
buttparent2.grid(row=1, column=4)


# bind system
for i in range(10):
    win.bind("%s" % (i), lambda Event, digit=i: addscreen(digit))


win.bind("+", lambda Event: addscreen("+"))
win.bind("-", lambda Event: addscreen("-"))
win.bind("*", lambda Event: addscreen("x"))
win.bind("/", lambda Event: addscreen("÷"))
win.bind(".", lambda Event: addscreen("."))
win.bind("<Return>", lambda Event: result())
win.bind("<BackSpace>", lambda Event: delete())


# start window
if __name__ == '__main__':
    win.mainloop()
