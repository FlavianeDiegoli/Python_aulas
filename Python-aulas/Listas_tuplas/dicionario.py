meuDicionario = {
 'nome'      : 'Flaviane', 
 'sobrenome' : 'Diegoli ',
 'anos'      : 34                 
}
print(meuDicionario);


print(meuDicionario);
print();

frutasDicionario = { 
    "maça"      : 3, 
    "banana"    : 6,
    "uva"       : 8,
    'vitaminas' :{'a': 'boa para pele'}
    };

print("Significado encontrado no dicionario: " , frutasDicionario["maça"]);
print();
frutasDicionario["maça"] = 5;
frutasDicionario["laranja"] = 10;

print("Nova quantidade de maça: ", frutasDicionario["maça"]);
print();
print(frutasDicionario);


print(frutasDicionario);
print();

animaisDicionario = {};
animaisDicionario["Cachorro"] = "Beleba";
print(animaisDicionario);


aluno ={
    'nome'    : 'Flaviane',
    'idade'   : 34,
    'hobbias' : ['jogar','esporte']
    
}

print(aluno);

frutasDicionario = {
    'maça'       : 3,
    'banana'     : 6,
    'uva'        : 8,
    'laranja'    :10,
};

print();
print("Quantidade de maças: ",frutasDicionario.get("maça"));
print("Quantidade de banana: ", frutasDicionario.get("banana"));

print("quantidade de morango : ",frutasDicionario.get("morango","não foi encontrado a definição de morango"));

elementoRemovido = frutasDicionario.pop("laranja");
print(elementoRemovido);
print();
print("Dicionário atualizado:",frutasDicionario);


frutasDicionario = {
    'maça'       : 3,
    'banana'     : 6,
    'uva'        : 8,
    'laranja'    :10,
};

print();
print("Chaves encontradas no dicinário:", frutasDicionario.keys());
print("valores ebcibtrados no dicinário: ", frutasDicionario.valeus());
print(frutasDicionario.items());

 