usuario = input ("digite o seu usuario :");
senha   = input ("digite seu senha:")

usuarioCorreto = "admin";
senhaCorreto  =  "admin";
    
   
if usuario != usuarioCorreto:
  print("usuário esta incorreto!");
  
elif not (senha == senhaCorreto):
  print("A senha está incorreta!");  
  
elif usuario == usuarioCorreto and senha == senhaCorreto:
    print("login bem -sucedido");
    
else:
  print("O usuario ou  senha estão incorreto ");
  
 
 #verificação de multiplas condiçoes  com "and" oi "or"
 
numero = 10;

if(numero > 0 and numero < 5 ) or (numero > 10 and numero < 15):
  print("O número atende aos criterios ");
else:
  print("O número não atende aos criterios ");
          