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


# window content

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
    global expnum, firstresult
    if not firstresult:
        expnum.append(str(num))
        displayexpnum.config(text="".join(expnum))
    if firstresult:
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
    currentnum = currentnum.replace("x", "*").replace("÷", "/")
    displaynum.config(text=(round(eval(currentnum), 5)))
    memorynum = displaynum.cget("text")
    firstresult = True


def clear():
    global expnum, displayexpnum, finalnum, firstresult
    expnum = []
    finalnum = 0
    displayexpnum.config(text="")
    displaynum.config(text=0)
    firstresult = False


def delete():
    global expnum, displayexpnum
    last_element = expnum[-1]
    expnum.remove(last_element)
    displayexpnum.config(text="".join(expnum))


# screen number

finalnum = 0

expnum = []


memorynum = 0

firstresult = False


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
    text=finalnum,
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

"""
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
"""

butt1 = Button(
    numbers,
    text="1",
    width=5,
    height=2,
    font=("Arial", 25),
    bg="#333333",
    fg="white",
    command=lambda: addscreen(1),
)
butt2 = Button(
    numbers,
    text="2",
    width=5,
    height=2,
    font=("Arial", 25),
    bg="#333333",
    fg="white",
    command=lambda: addscreen(2),
)
butt3 = Button(
    numbers,
    text="3",
    width=5,
    height=2,
    font=("Arial", 25),
    bg="#333333",
    fg="white",
    command=lambda: addscreen(3),
)
butt4 = Button(
    numbers,
    text="4",
    width=5,
    height=2,
    font=("Arial", 25),
    bg="#333333",
    fg="white",
    command=lambda: addscreen(4),
)
butt5 = Button(
    numbers,
    text="5",
    width=5,
    height=2,
    font=("Arial", 25),
    bg="#333333",
    fg="white",
    command=lambda: addscreen(5),
)
butt6 = Button(
    numbers,
    text="6",
    width=5,
    height=2,
    font=("Arial", 25),
    bg="#333333",
    fg="white",
    command=lambda: addscreen(6),
)
butt7 = Button(
    numbers,
    text="7",
    width=5,
    height=2,
    font=("Arial", 25),
    bg="#333333",
    fg="white",
    command=lambda: addscreen(7),
)
butt8 = Button(
    numbers,
    text="8",
    width=5,
    height=2,
    font=("Arial", 25),
    bg="#333333",
    fg="white",
    command=lambda: addscreen(8),
)
butt9 = Button(
    numbers,
    text="9",
    width=5,
    height=2,
    font=("Arial", 25),
    bg="#333333",
    fg="white",
    command=lambda: addscreen(9),
)


"""
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
"""
buttplus = Button(
    numbers,
    text="+",
    width=5,
    height=2,
    font=("Arial", 25),
    bg="#fe9504",
    fg="white",
    command=lambda: addscreen("+"),
)
buttminus = Button(
    numbers,
    text="-",
    width=5,
    height=2,
    font=("Arial", 25),
    bg="#fe9504",
    fg="white",
    command=lambda: addscreen("-"),
)
buttmulti = Button(
    numbers,
    text="x",
    width=5,
    height=2,
    font=("Arial", 25),
    bg="#fe9504",
    fg="white",
    command=lambda: addscreen("x"),
)
buttdiv = Button(
    numbers,
    text="÷",
    width=5,
    height=2,
    font=("Arial", 25),
    bg="#fe9504",
    fg="white",
    command=lambda: addscreen("÷"),
)

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
buttplus.grid(row=3, column=4)
buttminus.grid(row=3, column=5)
buttmulti.grid(row=2, column=4)
buttdiv.grid(row=2, column=5)
buttresult.grid(row=4, column=5)
buttclear.grid(row=4, column=4)
buttdeci.grid(row=4, column=2)
buttparent.grid(row=1, column=4)
buttparent2.grid(row=1, column=5)

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
win.mainloop()
