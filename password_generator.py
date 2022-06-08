# Gerador Automático de senhas

# Importar as bibliotecas
from random import choice  # Fazer as escolhas aleatórias dos caractéres
import string  # Gerar os caractéres
import os  # Reiniciar o programa
import sys  # Reiniciar o programa

# Código das Strings
string.ascii_lowercase  # abcdefghijklmnopqrstuvwxyz
string.ascii_uppercase  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
string.ascii_letters  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
string.digits  # 0123456789
string.punctuation  # <=>?@[\]^_`{|}~.


# Função para reiniciar o programa
def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)


# Tipos das senhas
easy_password = string.ascii_lowercase + string.ascii_uppercase  # Senha fácil
medium_password = string.ascii_lowercase + string.ascii_uppercase + string.digits  # Senha média
strong_password = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation  # Senha forte

# Opção do estilo de senha que o usuário deseja
password_style = print('''Ben: Como deseja a força da sua senha?
( 1 ) Fácil (Letras maiúsculas e minúsculas)
( 2 ) Média (Letras e números)
( 3 ) Forte (Letras, números e símbolos)
''')

user_choice = int(input('Ben: Digite o número da sua opção: '))
password_size = int(input('Ben: Números de caractéres da senha: '))

# Condições para gerar a senha

# Senha fácil
if user_choice == 1:
    password_size = password_size
    user_choice = easy_password
    password = ''
    for i in range(password_size):
        password += choice(user_choice)

# Senha média
elif user_choice == 2:
    password_size = password_size
    user_choice = medium_password
    password = ''
    for i in range(password_size):
        password += choice(user_choice)

# Senha forte
else:
    password_size = password_size
    user_choice = strong_password
    password = ''
    for i in range(password_size):
        password += choice(user_choice)

print('')  # pular linha

print(f'Ben: SENHA GERADA: {password}')  # mostrar a senha gerada

print('')  # pular linha

# Reiniciar o programa

restart = str(input('''Ben: Deseja gerar uma nova senha? Sim ou não?
-->''')).strip().lower()

# Reiniciar
if restart == 'sim':
    os.system('cls')  # Limpar o código antigo do console
    restart_program()  # Efetuar o reinício

# Não reiniciar
else:
    sys.exit()  # Encerrar o programa