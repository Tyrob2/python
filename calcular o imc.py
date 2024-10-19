#Função para calcular o IMC
def calcular_imc(peso, altura):
    return peso / (altura **2)
#Função para classificar o IMC baseado no sexo
def classificar_imc(imc, sexo):
    if sexo.lower() == 'm':
        #Classificação Masculina
        if imc < 20.7:
            return 'Abaixo do peso'
        elif 20.7 <= imc <= 26.4:
            return 'peso normal'
        elif 26.4 < imc <= 27.8:
            return 'Levemente acima do peso'
        elif 27.8 < imc <= 31.1:
            return 'Acima do peso ideal (sobrepeso)'
    elif sexo.lower() == 'f':
        #Classificação Feminina
        if imc < 19.1:
            return 'Abaixo do peso'
        elif 19.1 <= imc <= 25.8:
            return 'Peso normal'
        elif 25.8 < imc <= 27.3:
            return 'Levemente acima do peso'
        elif 27.3 < imc <= 32.3:
            return ' Acima do peso ideal (sobrepeso)'
        else:
            return 'Obesidade'
    else:
        return "Sexo inválido! Use 'M' para masculino ou 'F' para feminino"

#Função principal para coletar dados e calcular o IMC
def main():
    try:
        peso = float(input('Digite o peso em kg: '))
        altura = float(input('Digite a altura em metros: '))
        sexo =input('Digite o sexo (M para masculino, e F para feminino): ')

        #Calcular o IMC
        imc = calcular_imc(peso, altura)
        print(f'Seu IMC é: {imc:.2f}')

        #Classificar o IMC baseado sexo
        classificacao = classificar_imc(imc, sexo)
        print(f'Classificação: {classificacao}')

    except ValueError:
        print('Por favor, insira valores numéricos válidos para peso e altura.')
        return main()

#Executa o programa
main()
        
