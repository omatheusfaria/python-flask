from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def raiz():
    return render_template('index.html')

@app.route('/calcula_tabuada', methods=['POST'])
def calcula():
    numero_str = request.form.get('txt_numero')

    if not numero_str:
        return render_template('index.html', error="Por favor, digite um número.")

    try:
        numero = int(numero_str)
    except ValueError:
        return render_template('index.html', error="Por favor, digite um número válido.")

    # A list comprehension is a more concise way to generate the list of results.
    valores = [numero * i for i in range(11)]

    result = {
        'tabuada_do': numero,
        "valores": valores
    }

    return render_template('index.html', resultado=result)

if __name__ == '__main__':
    app.run(debug=True)