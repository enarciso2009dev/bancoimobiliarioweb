# coding: utf-8

from flask import Blueprint, render_template, request
from util.banco import Banco
bp_cadastro = Blueprint('cadastro', __name__)
banco = Banco()


@bp_cadastro.route('/cadastro')
def cadastro():
    return render_template('/cadastro.html'), 200










