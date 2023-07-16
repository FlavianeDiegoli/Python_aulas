 
class Conta :
    def __init__(self, numero , titular, saldo = 0) :
     self.numero  = numero;
     self.titular = titular;
     self.saldo   = saldo;
     
    def depositar(self , valor ):
        self.saldo += valor;
        
    def secar(self, valor ):
        if valor <= self.saldo:
          self.saldo -= valor;
          
        else:
          print ("Saldo insufliciente");  
      
        
    def exibir_informacoes(self):
        print(f"Conta :{self.numero}");
        print(f"Titutar:{self.titular}");
        print(f"Saldo:{self.saldo}");
        #       
 
conta = Conta("Flaviane") ;

conta.depositar(1000);
conta.secar(500);
conta.exibir_informacoes();


       
          
    
    
        
         
         
        
    