# 1 

numero1 = int(input("digite o PRIMEIRO número: "));
numero2 = int(input("digite o SEGUNDO número: "));

soma            = numero1 + numero2;
subtracao       = numero1 - numero2;
multiplicacao   = numero1 * numero2;
divisao         = numero1 / numero2;

print("soma: ", soma);
print("subtração: ", subtracao);
print("multiplacação: ", multiplicacao);
print("divisão: ", divisao);

# 2 
temperatura = int(input("digite temperatura em graus celsius: "));

if temperatura > 100:
    print("a água está fervendo!");
    
print();

# 3 
numero = int(input("digite um número inteiro: "));

if numero % 2 == 0:
  print("esse número é par. ");
else:
    print("esse número é impar. ");
    
print();

# 4 -

senha = input("digite sua senha: ");

senha_correta = "123456";

if senha == senha_correta:
    print("usuário logado com sucesso!");
else:
    print("senha incorreta!");
    
print();

# 5 
idade = int(input("digite sua idade: "));

if (idade >= 18) and (idade <= 30):
    print("a idade está entre 18 e 30 anos");
else:
    print("a idade não está entre 18 e 30 anos");
    
print();

# 6 
numero1 = int(input("digite o primeiro número inteiro: "));
numero2 = int(input("digite o segundo número inteiro: "));
numero3 = int(input("digite o terceiro número inteiro: "));

if (numero1 > 0) or (numero2 > 0) or (numero3 > 0):
    print("um dos números é positivo.");
else:
    print("nenhum dos números é positivo.");
    
print();

# 7 
letra = input("digite uma letra: ");

if letra.lower() in ['a','e','i','o','u']:
    print("é uma vogal");
else:
    print("não é vogal");

print();

# 8 
numero = int(input("digite o primeiro número inteiro: "));

if numero > 0:
    print("número é positivo.");
elif numero < 0:
    print("número é negativo.");
else:
    print("número é zero.");

print();

# 9 
numero1 = float(input("digite 1º Número: "));
numero2 = float(input("digite 2º Número: "));
numero3 = float(input("digite 3º Número: "));

if (numero1 < numero2 < numero3):
    print("os números estão em ordem crescente.");
else:
    print("os números não estão em ordem crescente.");

print();

# 10 
numero = int(input("digite um número inteiro: "));

if (numero % 3 == 0) and (numero % 5 == 0):
    print("número é um múltiplo de 3 e 5 ao mesmo tempo.");
else:
    print("número não é um múltiplo de 3 e 5 ao mesmo tempo.");

print();
 