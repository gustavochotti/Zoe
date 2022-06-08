# Criação de um jogo de jokenpo

from random import choice
from time import sleep
import sys
import os


# Função para reiniciar o programa
def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)


# Apresentação
print('===== JOKENPÔ =====')

print(' ')

itens = ['pedra', 'papel', 'tesoura']
options = print('''Suas Opções:  
 - Pedra
 - Papel
 - Tesoura''')

print(' ')

# Sessão de jogadas
jogador = str(input('Ben: Qual a sua jogada? ')).lower().strip()
computador = choice(itens)

print('=' * 20)

# Caso ocorra jogada inválida
if jogador in itens:
    pass

else:
    print('Ben: JOGADA INVÁLIDA')
    print('=' * 20)

    reiniciar = str(input('''Ben: Deseja jogar novamente? Sim ou não?
--> ''')).strip().lower()

    if reiniciar == 'sim':
        os.system('cls')
        restart_program()

    else:
        sys.exit()

# Siga
print('JO')
sleep(0.8)
print('KEN')
sleep(0.85)
print('PO')
sleep(0.8)

print('=' * 20)

print(f'Ben jogou: {computador}')

if jogador == computador:
    print(f'Você jogou: {jogador}')
    print('=' * 20)
    print('EMPATE')


# Jogadas Papel
elif jogador == 'papel' and computador == 'tesoura':
    print(f'Você jogou: {jogador}')
    print('=' * 20)
    print('BEN VENCE')

elif jogador == 'papel' and computador == 'pedra':
    print(f'Você jogou: {jogador}')
    print('=' * 20)
    print('JOGADOR VENCE')

elif jogador == 'tesoura' and computador == 'papel':
    print(f'Você jogou: {jogador}')
    print('=' * 20)
    print('JOGADOR VENCE')

elif jogador == 'pedra' and computador == 'papel':
    print(f'Você jogou: {jogador}')
    print('=' * 20)
    print('BEN VENCE')


# Jogadas Pedra
elif jogador == 'pedra' and computador == 'tesoura':
    print(f'Você jogou: {jogador}')
    print('=' * 20)
    print('JOGADOR VENCE')

elif jogador == 'pedra' and computador == 'papel':
    print(f'Você jogou: {jogador}')
    print('=' * 20)
    print('BEN VENCE')

elif jogador == 'tesoura' and computador == 'pedra':
    print(f'Você jogou: {jogador}')
    print('=' * 20)
    print('BEN VENCE')

elif jogador == 'papel' and computador == 'pedra':
    print(f'Você jogou: {jogador}')
    print('=' * 20)
    print('JOGADOR VENCE')


# Jogadas Tesoura
elif jogador == 'tesoura' and computador == 'pedra':
    print(f'Você jogou: {jogador}')
    print('=' * 20)
    print('BEN VENCE')

elif jogador == 'tesoura' and computador == 'papel':
    print(f'Você jogou: {jogador}')
    print('=' * 20)
    print('JOGADOR VENCE')

elif jogador == 'pedra' and computador == 'tesoura':
    print(f'Você jogou: {jogador}')
    print('=' * 20)
    print('JOGADOR VENCE')

elif jogador == 'papel' and computador == 'tesoura':
    print(f'Você jogou: {jogador}')
    print('=' * 20)
    print('BEN VENCE')

print('=' * 20)

# Reiniciar o programa
reiniciar = str(input('''Ben: Deseja jogar novamente? Sim ou não?
--> ''')).strip().lower()

if reiniciar == 'sim':
    os.system('cls')
    restart_program()

else:
    sys.exit()
