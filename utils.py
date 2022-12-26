from models import Pessoas
# Insere uma pessoa na tabela Pessoas
def insere_pessoa():
    pessoa = Pessoas(nome='Gih', idade  = 22)
    print(pessoa)
    pessoa.save()
# Consulta uma pessoa na tabela Pessoas
def consulta_pessoa():
      pessoa = Pessoas.querry.all()
      print(pessoa)

     # Outros possiveis prints:
     # for p in pessoa:
     #    print(p.id)

     # pessoa = Pessoas.querry.filter_by(id='1').first()
     # print(pessoa.nome)
     # print(pessoa.idade)

# Altera uma pessoa na tabela Pessoas
def altera_pessoa():
    pessoa = Pessoas.querry.filter_by(id='1').first() #Filtro por ID
    pessoa.idade = 19
    pessoa.save()

# Exclui uma pessoa na tabela Pessoas
def exclui_pessoa():
    pessoa = Pessoas.querry.filter_by(id='1').first()
    pessoa.delete()


# Função main:
if __name__ == '__main__':
    # insere_pessoa()
     consulta_pessoa()
    # altera_pessoa()
    # exclui_pessoa()