from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_imc(peso, altura):
    if altura == 0:
        return None, "Altura não pode ser zero."

    imc = peso / (altura * altura)

    if imc < 18.5:
        classificacao = 'Magreza'
    elif 18.5 <= imc <= 24.9:
        classificacao = 'Normal'
    elif 25 <= imc <= 29.9:
        classificacao = 'Sobrepeso'
    elif 30 <= imc <= 39.9:
        classificacao = 'Obesidade'
    else:
        classificacao = 'Obesidade grave'

    return round(imc, 2), classificacao

@app.route('/')
def index():
    return render_template('imc_calc.html')

@app.route('/calcular_imc', methods=['GET', 'POST'])
def calcular_imc():
    if request.method == 'POST':
        altura_str = request.form.get('txt_altura')
        peso_str = request.form.get('txt_peso')
    else: # GET
        altura_str = request.args.get('txt_altura')
        peso_str = request.args.get('txt_peso')

    if not altura_str or not peso_str:
        # Don't render an error on first load
        if request.method == 'GET' and not request.args:
            return render_template('imc_calc.html')
        return render_template('imc_calc.html', error="Altura e peso são obrigatórios.")

    try:
        # Replace comma with dot for decimal conversion
        altura = float(altura_str.replace(',', '.'))
        peso = float(peso_str.replace(',', '.'))
    except (ValueError, TypeError):
        return render_template('imc_calc.html', error="Valores de altura e peso devem ser numéricos.")

    imc, classificacao = calculate_imc(peso, altura)
    
    if imc is None:
        return render_template('imc_calc.html', error=classificacao)

    return render_template('imc_calc.html', res_imc=imc, classificado=classificacao)


if __name__ == '__main__':
    app.run(debug=True)