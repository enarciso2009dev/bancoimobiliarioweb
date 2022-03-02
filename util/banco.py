# coding: utf-8

import dataset

class Banco():
    def saveGetjogadores(self, nome, valor):
        db = dataset.connect('sqlite:///jogo.db')  # criei o banco de dados
        print("entrou no saveGetjogadores")
        jogadorest = db['jogadorest'] # criei a tabela jogadores
        jogadoresr = db['jogadoresr']
        print("criou as tabelas")
        print(f"os resultados esta vindo {nome}, {valor}")
        jogadorest.insert(dict(nome=nome, valor=valor))
        jogadoresr.insert(dict(nome=nome, valor=valor))

    def listjogadores(self):
        with dataset.connect('sqlite:///jogo.db') as db:
            jogadorest = db['jogadorest'].all()
            if db['jogadorest'].count() > 0:
                return jogadorest
        db = dataset.connect('sqlite:///jogo.db')
        listat = db['jogadorest']
        listar = db['jogadoresr']

        html = u"Listando tudo!<br>"
        for linha in listat:
            html = html + str(linha['nome']) + u" -  Valor:" + (linha['valor']) + u" <br>"
            return html, 200
        for linha in listar:
            html = html + str(linha['nome']) + u" - Valor:" + (linha['valor']) + u" <br>"
            return html, 200


    def getjogadores(self, id):
        with dataset.connect('sqlite:///jogo.db') as db:
            jogadores = db['jogadorest'].find_one(id=id)

            if jogadores:
                return jogadores
            else:
                return False

    def updatejogadoresr(self, idr, valorr):
        print('esta no banco.updatejogadoresr')
        with dataset.connect('sqlite:///jogo.db') as db:
            return db['jogadoresr'].update(dict(id=idr, valor=valorr), ['id']) and db['jogadorest'].update(dict(id=idr, valor=valorr), ['id'])

    def updatejogadorest(self, idt, valort):
        print('esta no banco.updatejogadorest')
        with dataset.connect('sqlite:///jogo.db') as db:
            return db['jogadorest'].update(dict(id=idt, valor=valort), ['id']) and db['jogadoresr'].update(dict(id=idt, valor=valort), ['id'])