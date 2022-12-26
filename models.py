from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
# Cria a database
engine = create_engine('sqlite:///dbatividades')
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.querry = db_session.query_property()

# Cria a tabela "Pessoas" na db
class Pessoas(Base):
    __tablename__ = 'pessoas'

    # informações sobre as colunas da tabela
    id = Column(Integer, primary_key=True)
    nome = Column(String(70),nullable=False)
    idade = Column(Integer, nullable=False)

    # Representação caso tenha um print(Pessoas)
    def __repr__(self):
        return '<Pessoa {}>'.format(self.nome)

    # Função para salvar as alterações na tabela
    def save(self):
        db_session.add(self)
        db_session.commit()
    # Função para deletar uma informação da tabela
    def delete(self):
        db_session.delete(self)
        db_session.commit()

# Cria a tabela "Atividades" na db
class Atividades(Base):
    __tablename__ = 'atividades'

    # informações sobre as colunas da tabela
    id = Column(Integer, primary_key=True)
    nome = Column(String(80))
    pessoa_id = Column(Integer, ForeignKey('pessoas.id'))
    pessoa = relationship("Pessoas")

    # Representação caso tenha um print(Atividades)
    def __repr__(self):
        return '<Atividade {}>'.format(self.id)

    # Função para salvar as alterações na tabela
    def save(self):
        db_session.add(self)
        db_session.commit()

    # Função para deletar uma informação da tabela
    def delete(self):
        db_session.delete(self)
        db_session.commit()
# Inicia o db
def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()