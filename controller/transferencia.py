# coding: utf-8

from flask import Blueprint, render_template
from util.banco import Banco
bp_transferencia = Blueprint('transferencia', __name__)
banco = Banco()

@bp_transferencia.route('/transferencia')
@bp_transferencia.route('/transferencia/<int:id>')
def transferencia(id = None):
    dados = {'id':'','nome':'','valor':''}
    jogadorest = banco.listjogadores()
    jogadoresr = banco.listjogadores()
    if id :
        dados = banco.getjogadores(id)

    return render_template('/transferencia.html', pedido=[], jogadorest=jogadorest, jogadoresr=jogadoresr), 200

