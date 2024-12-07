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
   
    data_inicio = datetime.strptime(data_inicio, '%Y-%m-%d')
    data_final = datetime.strptime(data_final, '%Y-%m-%d')

    diferenca = data_final - data_inicio 
    dias_totais = diferenca.days
    
    anos = dias_totais // 365
    dias_restantes = dias_totais % 365
    meses = dias_restantes // 30 
    dias_restantes = dias_restantes % 30

    return render_template('index.html', anos=anos, meses=meses, dias_restantes=dias_restantes, dias_totais=dias_totais)

if __name__ == '__main__':
    app.run(debug=True)