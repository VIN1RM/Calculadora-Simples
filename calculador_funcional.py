import tkinter as tk

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("350x500")
        self.root.configure(bg="#2E2E2E")
        self.root.bind("<Key>", self.teclado)  
        self.root.bind("<F11>", self.toggle_fullscreen) 

        self.expressao = ""
        self.fullscreen = False

        self.entrada_texto = tk.StringVar()
        self.entrada = tk.Entry(root, textvariable=self.entrada_texto, font=("Arial", 24), justify="right",
                                bd=10, relief="ridge", bg="#D3D3D3")
        self.entrada.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15, padx=10, pady=20, sticky="nsew")

        botoes = [
            ('7', '8', '9', '/'), ('4', '5', '6', '*'),
            ('1', '2', '3', '-'), ('0', '.', '+', '='),
            ('C', '(', ')', '⌫')
        ]
        cores = {"/": "#4F4F4F", "*": "#4F4F4F", "-": "#4F4F4F", "+": "#4F4F4F",
                 "=": "#FF9500", "C": "#FF3B30", "⌫": "#FFCC00"}

        for i, linha in enumerate(botoes):
            for j, texto in enumerate(linha):
                tk.Button(root, text=texto, font=("Arial", 18), fg="#FFFFFF",
                          bg=cores.get(texto, "#6E6E6E"), width=5, height=2, relief="ridge",
                          command=lambda t=texto: self.clicar(t)).grid(row=i+1, column=j,
                                                                       padx=5, pady=5, sticky="nsew")

        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)

    def clicar(self, texto):
        if texto == "=":
            try:
                self.expressao = str(eval(self.expressao))
            except:
                self.expressao = "Erro"
        elif texto == "C":
            self.expressao = ""
        elif texto == "⌫":
            self.expressao = self.expressao[:-1]
        else:
            self.expressao += texto
        self.entrada_texto.set(self.expressao)

    def teclado(self, event):
        if event.keysym in ["Return", "BackSpace"]:
            self.clicar("=" if event.keysym == "Return" else "⌫")
        elif event.char in "0123456789+-*/().":
            self.clicar(event.char)

    def toggle_fullscreen(self, event=None):
        self.fullscreen = not self.fullscreen
        self.root.attributes("-fullscreen", self.fullscreen)

if __name__ == "__main__":
    root = tk.Tk()
    Calculadora(root)
    root.mainloop()