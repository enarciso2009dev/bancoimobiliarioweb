# coding: utf-8

from flask import Blueprint, render_template, request
from util.banco import Banco
bp_resultado = Blueprint('resultado', __name__)

banco = Banco()

@bp_resultado.route('/resultado', methods=['GET', 'POST'])
def resultado():
    if request.method == "GET":
        print(request.method)
        return "Get",200
    elif request.method == "POST":
        nome=request.form["nome"]
        valor=request.form["valor"]
        print(request.form['nome'], request.form['valor'])
        banco.saveGetjogadores(nome, valor)
        return render_template('/resultado.html'), 200

    else:
        return "Não Definido",200



