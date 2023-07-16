idade = 20;
possuiCarteira = False;
  
if idade >= 18 and not possuiCarteira:
     print ("Voce está apto a dirigir");  
       
else:
    print("voce presica de ter a cateria de motorista!"); 
       
#Match CASE 

commando = 'Ola,Mundo!'

match commando:
    case "Olá mundo!":
        print("Olá para voce também");
    case "Adeus , mundo":
     print ("Adeus!");
    case _:
        print("sem resultados!");      
         