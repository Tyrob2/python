#Importar a biblioteca
import tkinter as tk
from tkinter import messagebox

#Função para calcular o IMC
def calcular_imc():
    #Executa o codigo e ser houver erro roda o comando "except"
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        imc = peso / (altura **2)
        if imc < 18.5:
            situacao = 'Abaixo do peso'
        elif 18.5 <= imc < 24.9:
            situacao = 'Peso Normal'
        elif 25 <= imc < 29.9:
            situacao = 'Sobrepeso'
        else:
            situacao = 'Obesidade'
            
        messagebox.showinfo('Resultado', f'Seu IMC é: {imc:.2f}\nSituação: {situacao}')
    except ValueError:
        messsagebox.showerror('Erro', 'Por favor, insira valores válidos.')
#Variavel janela recebe a funçao da biblioteca tkinter chamada "Tk()"
janela = tk.Tk()
janela.title('Calucladora de IMC')

#Peso
label_peso = tk.Label(janela, text='Peso (kg):')
label_peso.grid(row=0, column=0, padx=10, pady=10)
entry_peso = tk.Entry(janela)
entry_peso.grid(row=0, column=1, padx=10, pady=10)

#Altura            
label_altura = tk.Label(janela, text='Altura (m):')
label_altura.grid(row=1, column=0, padx=10, pady=10)
entry_altura = tk.Entry(janela)
entry_altura.grid(row=1, column=1, padx=10, pady=10)

botao_calcular = tk.Button(janela, text='Calcular IMC', command=calcular_imc)
botao_calcular.grid(row=2, column=0, columnspan=2, pady=20)

#Mantém a janela aberta até um comando de botão
janela.mainloop()
            
