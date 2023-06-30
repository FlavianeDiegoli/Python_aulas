"""
estrutras condicionais
"""
#Verificaçao de idade para entrada em club noturno

idade = int(input("Digite sua idade"));

if idade >= 18 :
  print("Bem-vinda , você pode entrar na festa ");

else: 
 print("Desculpa,você não tem idade suficiente para entrar na festa");  


#Verificar se um número está dentro de intervalo entre 10 e 20;
 
numero = 21;
 
if (numero >= 10)  and (numero <= 20):
     print("O número está dentro do intervalo");
      
else:
     print("O número esta fora do intervalo");  

#Comprar o tamanho de duas listas 

lista1 = [1,2,3,4,5];
lista2 = [5,4,3,2,'a'];      

if len(lista1) > len(lista2):
    print("A lista 1 é maior que a lista2");  
elif len(lista2) > len("lista1"):
    print("A lista 2 é maior que a 1");    
else:
    print("As lista tem o mesmo tamanho")    
    
#Verificação de acesso um sistema 

senha = input("Digite sua senha :");

senha_correta = "123456";

if senha == senha_correta:
    print("Usuario logado com sucesso");

else:
    print("A senha informada esta errada !");       
    