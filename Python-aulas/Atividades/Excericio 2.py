frutas =["maça","banana","laranja","abacaxi","melancia"];
print(frutas);
print();

#Adicione a fruta
frutas.append("uva");
print(frutas);

#emova a fruta
frutaRemovida = frutas.remove("banana");

frutaRemovida = frutas.pop(2);
print(frutas);
print(frutaRemovida);

#uma variável chamada
fruta_selecionada = frutas[1] 
{
  
  'maçã'      : 3,
  'banana'    : 6,
  'laranja'   : 8,
  'abacaxi'   : 9,
  'melancia'  : 10
};

print();
print("Valores", fruta_selecionada.values());
print(fruta_selecionada.items());

#tupla chamada
tuplaCores = ["vermelho", "azul", "verde", "amarelo" , "roxo"];
print(tuplaCores);
print();

#uma variável chamada
cor_selecionada = {
    'vermelho'   : 1,
    ' azul '     : 2,
    'verde'      : 3,
    'amarelo'    : 4,
    'roxo'       : 5,
};
print();
print("Valores", cor_selecionada.values());
print(cor_selecionada.items());

# esta dificil a erro ?
frutas[1] = "laranja";
print("Tamanho 1: ", len(frutas));
frutas.append("abacaxi");
print(frutas);

aluno = {
     'nome'      : 'Flaviane',
     'anos'      : 34  ,
     'cidade'    :'Brusque SC'
}
print(aluno);
print();

print("Idade do aluno : ", aluno["anos"]);
print();

generoAluno = ["feminino"];
print("Gênero: ", generoAluno);
print();

print("aluno e chave genero  " ,aluno ["anos"]);
print();


elementoRemovido = aluno.pop("cidade");
print(elementoRemovido);
print();
print("Dicionário atualizado:",aluno);