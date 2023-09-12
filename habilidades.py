from flask_restful import Resource
from flask import request
import json

lista_habilidades = ['Python', 'Java', 'Flask', 'PHP', 'C#', 'GoLang', 'Pandas']

class Habilidades(Resource):
    def get(self):
        return lista_habilidades
    
    def post(self):
        data = request.get_json()
        habilidade = data['habilidade']
        lista_habilidades.append(habilidade)
        mensagem = f'Habilidade adicionada com sucesso! Nova Habilidade: {habilidade}'
        return {'status': mensagem}
    

class HabilidadeId(Resource):
    def put(self, id):
       data = request.json
       novo_nome = data['novo_nome']
       
       if id >= 0 and id < len(lista_habilidades):
           lista_habilidades[id] = novo_nome
           mensagem = f'Habilidade com o Id:{id}, foi alterada com sucesso! Novo nome: {novo_nome}'
           return {'status':mensagem}
       else:
           return {'status':'id inválido'}
    def delete(self, id):
        lista_habilidades.pop(id)
        return {'status':'sucesso', 'mensagem':'Registro Excluído'}
        