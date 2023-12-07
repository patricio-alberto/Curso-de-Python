a = 'AAAAA'
b = 'BBBBB'
c = 1.1

string = 'b={nome3} a={nome2} c={nome3}'
formato = string.format(
    nome1=b, nome2=a, nome3=c 
)

print(formato)