# coding: utf-8

from flask import Flask, session
from controller.site import bp_site
from controller.cadastro import bp_cadastro
from controller.saldo import bp_saldo
from controller.transferencia import bp_transferencia
from controller.resultado import bp_resultado
from controller.atualiza_saldo import bp_atualiza_saldo
from controller.sair import bp_sair

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

app.register_blueprint(bp_site)
app.register_blueprint(bp_cadastro)
app.register_blueprint(bp_saldo)
app.register_blueprint(bp_transferencia)
app.register_blueprint(bp_resultado)
app.register_blueprint(bp_atualiza_saldo)
app.register_blueprint(bp_sair)

app.run()
