# coding: utf-8

from flask import Blueprint, render_template

bp_saldo = Blueprint('saldo', __name__)


@bp_saldo.route('/saldo')
def site():
    return render_template('/saldo.html'), 200