from util.banco import Banco
import dataset
banco = Banco()

class Calculo():
    def calculot(self, idt, valor):
        with dataset.connect('sqlite:///jogo.db') as db:
            self.idt=idt
            self.valor = db['jogadorest'].find_one(id=idt)
            valort = self.valor['valor']
            print(f'entrou no print calculot idt{idt}, valor {valor} e valort {valort}' )
            #return db['pizzas'].update(dict(id=id, nome=nome, descricao=descricao, status=status), ['id'])

            if self.idt != None:
                print('entrou no print do idt')
                self.valort -= valor
                print(f'valor que sera retornado do idt {idt} e valor {self.valort}')
            return self. idt, self.valort

    def calculor(self, idr, valor):
        with dataset.connect('sqlite:///jogo.db') as db:
            self.idr=idr
            self.valor = db['jogadoresr'].find_one(id=idr)
            valorr = self.valor['valor']
            print(f'entrou no print calculor idr: {idr}, valor: {valor} e valorr {valorr}')
            if self.idr != None:
                print('entrou no if do idr')
                self.valorr += valor
                print(f'valor que sera retornado do idr {idr} e valor {self.valorr}')

            return self, idr, self.valorr
