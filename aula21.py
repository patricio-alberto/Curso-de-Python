"""
    OPERADORES LÓGICOS
    - AND (e) OR (OU) NOT (não)
"""

entrada = input('(E)ntrar ou (S)air? ')
senha_permitida = '123456'

if entrada == 'E' and senha_permitida == senha_permitida:
    print('Entrar')
else:
    print('Sair')


print(True and False and True)
print(True and 0 and True)
