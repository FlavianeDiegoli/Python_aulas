print('********************************')
print('Bem Vinda Estrutura de repetição')
print('********************************')
# 1 - 
numero = 1
while numero <= 10:
  print(numero)
  numero += 1

# 2 - 
for numero in range(1, 11):
  print(numero)

# 3 - 
numero = 1
soma = 0
while numero <= 100:
    soma += numero
    numero += 1

print("A soma dos números de 1 a 100 é:", soma);

# 4 - 
soma = 0;

for numero in range(1, 100):
    soma += numero

print("A soma dos números de 1 a 100 é:", soma);

# 5 - 
numero = 1;

while numero <= 10:
    print(numero);
    numero += 1

# 6 -
for numero in range(2, 21, 2):
    print(numero)

# 7 - 
string = input("Digite uma string: ");
tamanho = len(string);
invertida = ""

while tamanho > 0:
    invertida += string[tamanho - 1]
    tamanho -= 1

print("A string invertida é:", invertida);

# 8 - 
palavra = input("Digite uma palavra: ")
invertida = ""

for letra in palavra:
    invertida = letra + invertida

if palavra == invertida:
    print("A palavra é um palíndromo.")
else:
    print("A palavra não é um palíndromo.")

# 9 - 
numero = 1

while numero ** 1 <= 1000:
    numero += 1

print("O menor número inteiro cujo quadrado é maior do que 1000 é:", numero);

                            # DESAFIO #

lista = [1, 2, 3, 4, 5];

for i in range(len(lista) - 1, -1, -1):
    print(lista[i]);