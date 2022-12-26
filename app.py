from flask import Flask, request
from flask_restful import Resource, Api
from models import Pessoas, Atividades

app = Flask(__name__)
api = Api(app)

# Verifica ou altera os dados da tabela pessoas (localizado pelo ID)
class Pessoa(Resource):
    # verifica as informações de um ID
    def get(self, id):
        try:
            pessoa = Pessoas.querry.filter_by(id=id).first()

            response = {
                'id': pessoa.id,
                'nome': pessoa.nome,
                'idade': pessoa.idade
            }
        # Casos de excessão:
        except AttributeError:
            mensagem = 'Pessoa de id {} nao encontrada'.format(id)
            response = {'Status': 'Erro', 'Mensagem': mensagem}
        except Exception:
            mensagem = 'Erro não identificado'
            response = {'Status': 'Erro', 'Mensagem': mensagem}
        return response
    # altera uma ou mais informações de um ID
    def put(self, id):
        try:
            pessoa = Pessoas.querry.filter_by(id=id).first()
            dados = request.json
            # altera o dado conforme o contido no input
            if 'nome' in dados:
                pessoa.nome = dados['nome']
            if 'idade' in dados:
                pessoa.idade = dados['idade']
            pessoa.save()

            response = {
                'id':pessoa.id,
                'nome':pessoa.nome,
                'idade':pessoa.idade
            }
        # Casos de excessão:
        except AttributeError:
            mensagem = 'Pessoa de id {} nao encontrada'.format(id)
            response = {'Status': 'Erro', 'Mensagem': mensagem}
        except Exception:
            mensagem = 'Erro nao identificado'
            response = {'Status': 'Erro', 'Mensagem': mensagem}

        return response

# Verifica/adiciona dados na tabela pessoas (sem localização pelo ID)
class ListaPessoa(Resource):
    # Verifica os dados da tabela
    def get(self):
        pessoas = Pessoas.querry.all()
        response = [{'id':i.id, 'nome':i.nome, 'idade':i.idade} for i in pessoas]
        return response
    # Adiciona um dado na tabela
    def post(self):
        dados = request.json
        pessoa = Pessoas(nome=dados['nome'], idade=dados['idade'])
        pessoa.save()

        response = {
            'id':pessoa.id,
            'nome':pessoa.nome,
            'idade':pessoa.idade
        }
        return response

# Verifica/adiciona dados na tabela atividades (sem localização pelo ID)
class ListaAtividade(Resource):
    # Verifica os dados da tabela
    def get(self):
        atividades = Atividades.querry.all()
        response = [{'id':i.id, 'nome':i.nome, 'pessoa':i.pessoa.nome} for i in atividades]
        return response

    # Adiciona um dado na tabela
    def post(self):
        dados = request.json
        pessoa = Pessoas.querry.filter_by(nome=dados['pessoa']).first()
        atividade = Atividades(nome=dados['nome'], pessoa=pessoa)
        atividade.save()
        response = {
            'id':atividade.id,
            'pessoa':atividade.pessoa.nome,
            'nome':atividade.nome
        }
        return response

# Adiciona as rotas na URI
api.add_resource(Pessoa, '/pessoa/<int:id>/')
api.add_resource(ListaPessoa, '/pessoa/')
api.add_resource(ListaAtividade, '/atividade/')

if __name__ == '__main__':
    app.run(debug=True)
