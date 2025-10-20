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

screen = Frame(win)
screen.pack(side="top")

#####################################################################################

# def areas

def bigwich(x, y):
    if x < y:
        return x
    elif y < x:
        return y
    else:
        return x


def addscreen(num):
    global decinum, decicount
    currentnum = displaynum.cget("text")
    if not decinum:
        displaynum.config(text=currentnum * 10 + (num))
    elif decinum:
        displaynum.config(
            text=round(currentnum + (num * 10**decicount), abs(decicount))
        )
        decicount -= 1


def adddeci():
    global decinum, decicount
    if decinum:
        pass
    else:
        currentnum = displaynum.cget("text")
        displaynum.config(text=float(currentnum))
        decinum = True


def metplus():
    global memorynum, metchoice, decinum, decicount, decimem
    memorynum += displaynum.cget("text")
    metchoice = "+"
    decinum = False
    decimem = decicount
    decicount = -1
    displaynum.config(text=0)


def metminus():
    global memorynum, metchoice, decinum, decicount, decimem
    memorynum = displaynum.cget("text") - memorynum
    metchoice = "-"
    decinum = False
    decimem = decicount
    decicount = -1
    displaynum.config(text=0)


def metmulti():
    global memorynum, metchoice, decinum, decicount, decimem
    if memorynum == 0:
        memorynum = (memorynum + 1) * displaynum.cget("text")
    else:
        memorynum = (memorynum) * displaynum.cget("text")
    metchoice = "*"
    decinum = False
    decimem = decicount
    decicount = -1
    displaynum.config(text=0)


def metdiv():
    global memorynum, metchoice, decinum, decicount, decimem
    if memorynum == 0:
        memorynum = displaynum.cget("text") / (memorynum + 1)
    else:
        memorynum = displaynum.cget("text") / memorynum
    metchoice = "/"
    decinum = False
    decimem = decicount
    decicount = -1
    displaynum.config(text=0)


def result():
    global memorynum, metchoice, decinum, decicount, decimem
    currentnum = displaynum.cget("text")
    if metchoice == "+":
        displaynum.config(
            text=round(
                float(currentnum) + float(memorynum), abs(bigwich(decicount, decimem))
            )
        )
    elif metchoice == "-":
        displaynum.config(
            text=round(
                float(memorynum) - float(currentnum), abs(bigwich(decicount, decimem))
            )
        )
    elif metchoice == "*":
        displaynum.config(
            text=round(
                float(memorynum) * float(currentnum), abs(bigwich(decicount, decimem))
            )
        )
    elif metchoice == "/":
        if currentnum == 0:
            displaynum.config(text="Erro..")
        else:
            displaynum.config(
                text=round(
                    float(memorynum) / float(currentnum),
                    abs(bigwich(decicount, decimem)),
                )
            )
    memorynum = 0
    metchoice = ""
    decinum = False
    decimem = 0
    decicount = -1


def clear():
    global memorynum, metchoice, decinum, decicount
    memorynum = 0
    metchoice = ""
    decinum = False
    decicount = -1
    displaynum.config(text=0)


# screen number
num = StringVar()
num = 0

decinum = False
decicount = -1
decimem = 0

metchoice = ""
memorynum = 0


# fram SCREEN_NUM

displaynum = Label(
    win,
    text=num,
    bg="black",
    fg="white",
    font=("Arial", 50),
)
displaynum.pack(side="right")


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
buttplus = Button(
    numbers,
    text="+",
    width=5,
    height=2,
    font=("Arial", 25),
    bg="#fe9504",
    fg="white",
    command=lambda: metplus(),
)
buttminus = Button(
    numbers,
    text="-",
    width=5,
    height=2,
    font=("Arial", 25),
    bg="#fe9504",
    fg="white",
    command=lambda: metminus(),
)
buttmulti = Button(
    numbers,
    text="x",
    width=5,
    height=2,
    font=("Arial", 25),
    bg="#fe9504",
    fg="white",
    command=lambda: metmulti(),
)
buttdiv = Button(
    numbers,
    text="÷",
    width=5,
    height=2,
    font=("Arial", 25),
    bg="#fe9504",
    fg="white",
    command=lambda: metdiv(),
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
    width=10,
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
    command=lambda: adddeci(),
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
buttresult.grid(row=4, column=4, columnspan=2, sticky="We")
buttclear.grid(row=1, column=4, columnspan=2, sticky="We")
buttdeci.grid(row=4, column=2)


# start window
win.mainloop()
