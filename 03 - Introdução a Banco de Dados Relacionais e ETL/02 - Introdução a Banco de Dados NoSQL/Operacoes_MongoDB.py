'''
################### Operações no MongoDB

- Instalação do Compass
❏ https://www.mongodb.com/docs/compass/master/install/


- Criando um DataBase
use {{nome_do_banco}}
use {{viagens}}
Enquanto o database não tiver uma collection ele não será
apresentado na lista

db.usuarios.insertOne({})
{
  acknowledged: true,
  insertedId: ObjectId('694e815531f7779d637d9151')
}

/** 
* Paste one or more documents here
*/
{
  "_id": {"$oid": "694e85b54bf5bb12c2ab9faf"},     
  "_id": "",  
  "nome": "nome",
  "data_nascimento": "1990-10-05",
  "email": "pamela.apolinario.borges@gmail.com",
  "endereco": "Av Manoel Marques de Jesus, 380 - Vila Xavier, Araraquara/SP" 
}

Links Úteis

● Referências:
○ https://www.mongodb.com/docs/manual/reference/method/db.collection.find/
○ https://www.mongodb.com/docs/manual/reference/method/db.collection.findAndModify/
○ https://www.mongodb.com/docs/manual/reference/method/db.collection.findOne/
○ https://www.mongodb.com/docs/v6.0/tutorial/insert-documents/






'''








