import tkinter
from functools import reduce

class Aplication:
    def __init__ (self, master = None):
        tamButtom = 5

        self.widget1 = tkinter.Frame(master)
        self.widget1["pady"] = 10
        self.widget1.pack(fill = "both", expand = True)

        self.containner1 = tkinter.Frame(master)
        self.containner1["pady"] = 5
        self.containner1["padx"] = 10
        self.containner1.pack()

        self.containner2 = tkinter.Frame(master)
        self.containner2["pady"] = 5
        self.containner2["padx"] = 10
        self.containner2.pack()

        self.containner3 = tkinter.Frame(master)
        self.containner3["pady"] = 5
        self.containner3["padx"] = 10
        self.containner3.pack()
        
        self.containner4 = tkinter.Frame(master)
        self.containner4["pady"] = 5
        self.containner4["padx"] = 10
        self.containner4.pack()

        self.containner5_6 = tkinter.Frame(master)
        self.containner5_6["padx"] = 10
        self.containner5_6.pack(side = "left")

        self.containner5 = tkinter.Frame(self.containner5_6)
        self.containner5.pack(side = "left")

        self.containner5_1 = tkinter.Frame(self.containner5)
        self.containner5_1["pady"] = 5
        self.containner5_1.pack(side = "top")

        self.containner5_2 = tkinter.Frame(self.containner5)
        self.containner5_2["pady"] = 5
        self.containner5_2.pack(side = "bottom")
        
        self.containner6 = tkinter.Frame(self.containner5_6)
        self.containner6["pady"] = 5
        self.containner6.pack(side = "right")

        
        """
        #menu de opções
        opc = tkinter.StringVar()
        opc.set("File")
        self.caixa1 = tkinter.OptionMenu(self.containnerOpc, opc, "Opçao", "Help", "Credit")
        self.caixa1.pack(side = tkinter.LEFT)
        """

        #mensagem do topo
        self.msg = tkinter.Label(self.widget1, text="Calculadora Basica")
        self.msg.pack()
        self.msg["font"] = ("Verdana", "15", "italic", "bold")
        self.msg.pack(side = tkinter.BOTTOM, padx = 10, fill = 'x')
        
        #display
        self.display = tkinter.Entry(self.containner1, width = 20)
        self.display["font"] = ("Verdana", '15')
        self.display.pack(ipady = 10, ipadx = 10)

        #botton
        self.button7 = tkinter.Button(self.containner2)
        self.button7["text"] = "C"
        self.button7["font"] = ("Calibri", "18")
        self.button7.bind("<Button-1>", self.clear)
        self.button7.pack(padx = 5 , ipady = tamButtom, ipadx = tamButtom, side = 'left')

        self.button8 = tkinter.Button(self.containner2)
        self.button8["text"] = "/"
        self.button8["font"] = ("Calibri", "18")
        self.button8.bind("<Button-1>", self.insertdiv)
        self.button8.pack(padx = 5 , ipady = tamButtom, ipadx = tamButtom, side = 'left')
        
        self.button9 = tkinter.Button(self.containner2)
        self.button9["text"] = "*"
        self.button9["font"] = ("Calibri", "18")
        self.button9.bind("<Button-1>", self.insertmut)
        self.button9.pack(padx = 5 , ipady = tamButtom, ipadx = tamButtom, side = 'left')

        self.buttonp = tkinter.Button(self.containner2)
        self.buttonp["text"] = "-"
        self.buttonp["font"] = ("Calibri", "18")
        self.buttonp.bind("<Button-1>", self.inserts)
        self.buttonp.pack(padx = 5 , ipady = tamButtom, ipadx = tamButtom, side = 'left')

        self.button7 = tkinter.Button(self.containner3)
        self.button7["text"] = "7"
        self.button7["font"] = ("Calibri", "18")
        self.button7.bind("<Button-1>", self.insert7)
        self.button7.pack(padx = 5 , ipady = tamButtom, ipadx = tamButtom, side = 'left')

        self.button8 = tkinter.Button(self.containner3)
        self.button8["text"] = "8"
        self.button8["font"] = ("Calibri", "18")
        self.button8.bind("<Button-1>", self.insert8)
        self.button8.pack(padx = 5 , ipady = tamButtom, ipadx = tamButtom, side = 'left')
        
        self.button9 = tkinter.Button(self.containner3)
        self.button9["text"] = "9"
        self.button9["font"] = ("Calibri", "18")
        self.button9.bind("<Button-1>", self.insert9)
        self.button9.pack(padx = 5 , ipady = tamButtom, ipadx = tamButtom, side = 'left')

        self.buttonp = tkinter.Button(self.containner3)
        self.buttonp["text"] = "+"
        self.buttonp["font"] = ("Calibri", "18")
        self.buttonp.bind("<Button-1>", self.insertp)
        self.buttonp.pack(padx = 5 , ipady = tamButtom, ipadx = tamButtom, side = 'left')

        self.button4 = tkinter.Button(self.containner4)
        self.button4["text"] = "4"
        self.button4["font"] = ("Calibri", "18")
        self.button4.bind("<Button-1>", self.insert4)
        self.button4.pack(padx = 5 , ipady = tamButtom, ipadx = tamButtom, side = 'left')
        
        self.button5 = tkinter.Button(self.containner4)
        self.button5["text"] = "5"
        self.button5["font"] = ("Calibri", "18")
        self.button5.bind("<Button-1>", self.insert5)
        self.button5.pack(padx = 5 , ipady = tamButtom, ipadx = tamButtom, side = 'left')

        self.button6 = tkinter.Button(self.containner4)
        self.button6["text"] = "6"
        self.button6["font"] = ("Calibri", "18")
        self.button6.bind("<Button-1>", self.insert6)
        self.button6.pack(padx = 5 , ipady = tamButtom, ipadx = tamButtom, side = 'left')

        self.buttonm = tkinter.Button(self.containner4)
        self.buttonm["text"] = "."
        self.buttonm["font"] = ("Calibri", "18")
        self.buttonm.bind("<Button-1>", self.insertpt)
        self.buttonm.pack(padx = 5 , ipady = tamButtom, ipadx = tamButtom, side = 'left')

        self.button1 = tkinter.Button(self.containner5_1)
        self.button1["text"] = "1"
        self.button1["font"] = ("Calibri", "18")
        self.button1.bind("<Button-1>", self.insert1)
        self.button1.pack(padx = 5 , ipady = tamButtom, ipadx = tamButtom, side = 'left')
        
        self.button2 = tkinter.Button(self.containner5_1)
        self.button2["text"] = "2"
        self.button2["font"] = ("Calibri", "18")
        self.button2.bind("<Button-1>", self.insert2)
        self.button2.pack(padx = 5 , ipady = tamButtom, ipadx = tamButtom, side = 'left')
        
        self.button3 = tkinter.Button(self.containner5_1)
        self.button3["text"] = "3"
        self.button3["font"] = ("Calibri", "18")
        self.button3.bind("<Button-2>", self.insert3)
        self.button3.pack(padx = 5 , ipady = tamButtom, ipadx = tamButtom, side = 'left')
        
        self.buttoni = tkinter.Button(self.containner6)
        self.buttoni["text"] = "="
        self.buttoni.bind("<Button-1>", self.calcular)
        self.buttoni["font"] = ("Calibri", "18")
        self.buttoni.pack(padx = 5 , ipady = 34, ipadx = tamButtom, side = 'left')

        self.button0 = tkinter.Button(self.containner5_2, text = "0", font = ("Calibri", '18'))
        self.button0.bind("<Button-1>", self.insert0)
        self.button0.pack(padx = 5 , ipady = tamButtom, ipadx = 65, side = 'left')

    def insert0(self, parametro):
        self.display.insert(len(self.display.get()),"0")
    def insert1(self, parametro):
        self.display.insert(len(self.display.get()),"1")
    def insert2(self, parametro):
        self.display.insert(len(self.display.get()),"2")
    def insert3(self, parametro):
        self.display.insert(len(self.display.get()), "3")
    def insert4(self, parametro):
        self.display.insert(len(self.display.get()), "4")
    def insert5(self, parametro):
        self.display.insert(len(self.display.get()), "5")
    def insert6(self, parametro):
        self.display.insert(len(self.display.get()), "6")
    def insert7(self, parametro):
        self.display.insert(len(self.display.get()), "7")
    def insert8(self, parametro):
        self.display.insert(len(self.display.get()), "8")
    def insert9(self, parametro):
        self.display.insert(len(self.display.get()), "9")
    def inserts(self, parametro):
        self.display.insert(len(self.display.get()), "-")
    def insertp(self, parametro):
        self.display.insert(len(self.display.get()), "+")
    def insertmut(self, parametro):
        self.display.insert(len(self.display.get()), "*")
    def insertdiv(self, parametro):
        self.display.insert(len(self.display.get()), "/")
    def insertpt(self, parametro):
        self.display.insert(len(self.display.get()), ".")
    def clear(self, event):
        self.display.delete(0 , len(self.display.get()))
    def calcular(self, event):
        numero = self.display.get()
        operacoes = {
        "+" : lambda x, y: x + y,
        "-" : lambda x, y: x - y,
        "/" : lambda x, y: x / y,
        "*" : lambda x, y: x * y
        }
        numeros = []
        ind = []
        temp = ""

        try:
            for i in numero:
                if(i in operacoes):
                    numeros.append(float(temp))
                    ind.append(i)
                    temp = ""
                else:
                    temp += i
            numeros.append(float(temp))
        except:
            self.display.delete(0 , len(self.display.get()))
            self.display.insert(0, "Erro de sintaxe")
        
        result = 0
        for i in range(0, len(ind)):
            if i < len(ind) and ind[i] == "*":
                result = operacoes[ind[i]](numeros[i], numeros[i + 1])
                numeros.remove(numeros[i])
                numeros.insert(i, result)
                numeros.remove(numeros[i+1])
                ind.remove(ind[i])
        
        for i in range(0, len(ind)):
            if i < len(ind) and ind[i] == "/":
                try: 
                    result = operacoes[ind[i]](numeros[i], numeros[i + 1])
                    numeros.remove(numeros[i])
                    numeros.insert(i, result)
                    numeros.remove(numeros[i+1])
                    ind.remove(ind[i])
                except ZeroDivisionError as err:
                    self.display.delete(0 , len(self.display.get()))
                    self.display.insert(0, "Erro divisão por 0")
                    print(err)

        for i in range(0, len(ind)):
            if i < len(ind) and ind[i] == "+": 
                result = operacoes[ind[i]](numeros[i], numeros[i + 1])
                numeros.remove(numeros[i])
                numeros.insert(i, result)
                numeros.remove(numeros[i+1])
                ind.remove(ind[i])
        
        for i in range(0, len(ind)):
            if i < len(ind) and ind[i] == "-":
                result = operacoes[ind[i]](numeros[i], numeros[i + 1])
                numeros.remove(numeros[i])
                numeros.insert(i, result)
                numeros.remove(numeros[i+1])
                ind.remove(ind[i])
        
        print(ind)
        print(numeros)
        
        self.display.delete(0 , len(self.display.get()))
        self.display.insert(0, str(numeros[0]))

        
root = tkinter.Tk()
root.title("Calculadora em python")
app = Aplication(root)
root.mainloop()