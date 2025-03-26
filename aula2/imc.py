from flask import Flask, render_template, request

app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template('imc_calc.html')

@app.route('/calcular_imc_post', methods=['POST'])
def calcIMC():
    altura = float(request.form['txt_altura'])
    peso = float(request.form['txt_peso'])
    imc = peso / (altura * altura)
    return render_template('imc_calc.html', res_imc = imc)

@app.route('/calcular_imc_get', methods=['GET'])
def calcIMC_get():
    args = request.args
    altura = float(args.get('txt_altura'))
    peso = float(args.get('txt_peso'))
    imc = peso / (altura * altura)
    if (imc < 18.5):
        classificacao = 'Magreza'
    elif (imc >= 18.5 and imc <= 24.9):
        classificacao = 'Normal'
    elif (imc >= 25 and imc <= 29.9):
        classificacao = 'Sobrepeso'
    elif (imc >= 30 and imc <= 39.9):
        classificacao = 'Obesidade'
    else:
        classificacao = 'Obesidade grave'
    
    return render_template('imc_calc.html', res_imc = imc, classificado = classificacao)

app.run()