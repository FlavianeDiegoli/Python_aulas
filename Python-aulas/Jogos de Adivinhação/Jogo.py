# Este é o jogo adivinhe o número.
print('********************************')
print('Bem vindo ao jogo de adivinhação')
print('********************************')
import random

tentativas = 0
print("Olá! Qual é o seu nome?")
meuNome = input()
numero = random.randint(1, 100)
print("Bem, " + meuNome + ", eu estou pensando em um número entre 1 e 100.")

while tentativas < 6:
    print("Tente adivinhar!") # Há quatro espaços na frente do print.
    palpite = input()
    palpite = int(palpite)
    tentativas = tentativas + 1
    
    if palpite < numero:
        print(" é muito baixo!") # Há oito espaços na frente do print.
    if palpite > numero:
        print("é muito alto!")
    if palpite == numero:
        break
