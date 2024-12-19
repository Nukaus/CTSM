from flask import Flask, render_template, request
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data_inicio = request.form['data_inicio']
    data_final = request.form['data_final']
   
    data_inicio = datetime.strptime(data_inicio, '%Y-%m-%d')
    data_final = datetime.strptime(data_final, '%Y-%m-%d')

    sdiferenca = data_final - data_inicio
    diferenca = sdiferenca + timedelta(days=1)
    dias_totais = diferenca.days
    
    anos = dias_totais // 365
    dias_restantes = dias_totais % 365
    meses = dias_restantes // 30 
    dias_restantes = dias_restantes % 30

    return render_template('index.html', anos=anos, meses=meses, dias_restantes=dias_restantes, dias_totais=dias_totais)

if __name__ == '__main__':
    app.run(debug=True)