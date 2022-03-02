# coding: utf-8

from flask import Blueprint, render_template, url_for, request
from util.banco import Banco
import dataset

bp_site = Blueprint('site', __name__)

banco = Banco()


@bp_site.route('/',  methods=['GET', 'POST'])
def site():
    listat = banco.listjogadores()
    print('entrou no site')
    return render_template('/index.html',listat=listat), 200

def atualiza():
    if request.method == "POST":
        nomet = request.form["nome"]
        nomer = request.form["nome"]
        valor = request.form["valor"]
        print(request.form['nomet'], request.form['valor'], request.form['nomer'])
        banco.updatejogadores(nomet, nomer, valor)
        print(nomet, nomer, valor)







