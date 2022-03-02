# coding: utf-8

from flask import Blueprint, render_template, request
from util.banco import Banco
bp_sair = Blueprint('sair', __name__)

@bp_sair.route('/sair')
def site():
    return render_template('/sair.html'), 200