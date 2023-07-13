class Cachorro:
  def __init__(self, nome , idade):
    self.nome  = nome;
    self.idade = idade;
  
  def latir(self):  
   print(f"{self.nome} está latindo!");
   
  def anos(self):
      print(f"{self.nome} está latindo e tem {self.idade} anos") 
 
  def fome(self):
      print(f"{self.nome}está com fome")
      
      
# Criação de objeito da classe "cachorro" 
 
Cachorro1 = Cachorro("Bebela", 8 );  
Cachorro2 = Cachorro("Nina",12);

#Chamada de métodos dos objetos
Cachorro1.latir();
Cachorro2.latir();
print("");
Cachorro1.anos();
Cachorro2.anos();

Cachorro2.fome();