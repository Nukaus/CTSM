from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data_inicio = request.form['data_inicio']
    data_final = request.form['data_final']
   
    separado_inicial = data_inicio.split("")
    ano_inicial = int(separado_inicial [0])
    mes_inicial = int(separado_inicial [1])
    dia_inicial = int(separado_inicial [2])


    separado_final = data_final.split("")
    ano_final = int(separado_final [0])
    mes_final = int(separado_final [1])
    dia_final = int(separado_final [2])

    data_inicio = datetime(dia_inicial, mes_inicial, ano_inicial)
    data_final = datetime(dia_final, mes_final, ano_final)

    diferenca = data_final - data_inicio 
    dias_totais = diferenca.days
    
    anos = dias_totais // 365
    dias_restantes = dias_totais % 365
    meses = dias_restantes // 30 
    dias_restantes = dias_restantes % 30

    return render_template('index.html', anos=anos, meses=meses, dias_restantes=dias_restantes, dias_totais=dias_totais)

if __name__ == '__main__':
    app.run(debug=True)