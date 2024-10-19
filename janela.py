#Importar Biblioteca
from tkinter import *
from tkinter import messagebox

#Janela 'ABA'
class MinhaGUI:
    def __init__(self):
        #Janela
        self.janela_principal = Tk()
        #Botao
        self.botao = Button(self.janela_principal, text='Clique aqui', command = self.hello_world)
        self.botao_sair = Button(self.janela_principal, text='Sair', command=self.quit)
        self.botao.pack()
        self.botao_sair.pack()
        self.janela_principal.mainloop()
    #Executa o botão Sair
    def quit(self):
        self.janela_principal.destroy()
    #Executa o botão Clique aqui
    def hello_world(self):
        messagebox.showinfo('aULA DE pYTHON!','Olá, mundo!')
#Executa a Class MinhaGUI
gui = MinhaGUI()
