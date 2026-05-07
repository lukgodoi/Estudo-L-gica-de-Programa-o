print("Qual é o número!")
contagem_de_vezes = 0

while True:
    '''O try foi adicionado porque caso o usuário digite algum valor inválido retorna para ele a mensagem de erro'''
    try:
        resposta = int(input("Adivinhe em que numéro estou pensando de 0 a 20: "))
        contagem_de_vezes += 1
        if resposta == 19:
            print("Parabéns você acertou!")
            print(f"Levou só {contagem_de_vezes} para você acertar!")
            break
        '''Caso o usuário não termine o jogo, acaba em vinte tentativas '''
        if contagem_de_vezes == 20:
            print('Seu burro!!!!!! Não acertou!!!!!')
            break
    except ValueError:
        print("Digite um número, por favor!")