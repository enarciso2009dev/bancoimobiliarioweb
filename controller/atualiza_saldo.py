# coding: utf-8

from flask import Blueprint, render_template, url_for, request
from util.banco import Banco
from util.calculo import Calculo
from collections import OrderedDict
import dataset

bp_atualiza_saldo = Blueprint('atualiza_saldo', __name__)

banco = Banco()

calculo = Calculo()



@bp_atualiza_saldo.route('/atualiza_saldo', methods = ['GET', 'POST'])
def atualiza_saldo():
    with dataset.connect('sqlite:///jogo.db') as db:
        if request.method == "GET":
            print(f'imprime Get{request.method}')
            return "Get", 200
        elif request.method == "POST":
            idt = request.form["jogadorest"]
            idr = request.form['jogadoresr']
            valortrans = request.form["valor"]
            print(f"imprime POST idr: {request.form['jogadorest']}, idr: {request.form['jogadoresr']}, valor: {request.form['valor']}")
            valorbancoidr = db['jogadoresr'].find_one(id=idr)

            print('conversao de dados como dicionario')
            print(valortrans)
            valortrans = int(valortrans)
            print(type(valortrans))
            print('conversao de dados do dicio')
            dicio = {}
            print(type(valorbancoidr))

            d2 = dict(valorbancoidr)

            print(type(d2))
            print(d2)
            valoridr = int((d2['valor']))

            print(valoridr)
            print(type(valoridr))


            print('-------------------------------------------')
            print(f'linha 31 entrou no print calculor idr: {idr} e valorr {valoridr}')
            print('------------inicio do IDR-------------')
            if idr != None:
                print(f'entrou no if do idr: {idr}, valorr: {valoridr}, valoridr: {valoridr}, valorbr: {valortrans}')
                valorr = valoridr + valortrans
                print(f'valor que sera retornado do idr {idr} e valor {valorr}')
            print(f"print da atualiza_saldo idt  {idr}, valor {valorr}")
            print()
            print('-----------final do IDR---------------')
            print()
            print('-------------inicio IDT---------------')
            print()
            print(f"imprime POST idt: {request.form['jogadorest']}, idt: {request.form['jogadoresr']}, valor: {request.form['valor']}")
            valorbancoidt = db['jogadoresr'].find_one(id=idt)

            print('conversao de dados do dicio')
            dicio = {}
            print(type(valorbancoidt))

            d2 = dict(valorbancoidt)

            print(type(d2))
            print(d2)
            valoridt = int((d2['valor']))

            print(valoridt)
            print(type(valoridt))

            print('-------------------------------------------')
            print(f'entrou no print calculor idr: {idt} e valorr {valoridt}')
            print('------------inicio do IDT-------------')
            if idt != None:
                print(f'entrou no if do idt: {idr}, valort: {valoridt}, valoridt: {valoridt}, valorbr: {valortrans}')
                valort = valoridt - valortrans
                print(f'valor que sera retornado do idr {idt} e valor {valort}')
            print(f"print da atualiza_saldo idt  {idt}, valor {valort}")

            print('-----------final do IDR---------------')


            banco.updatejogadoresr(idr, valorr)
            banco.updatejogadorest(idt, valort)
            return render_template('/saldo.html'), 200

        else:
            return "Não Definido", 200
