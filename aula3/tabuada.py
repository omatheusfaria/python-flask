from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def raiz():
    return render_template('index.html')

@app.route('/calcula_tabuada', methods=['POST'])
def calcula():
    numero = int(request.form['txt_numero'])
    result = {'tabuada_do' : numero, "valores" : []}

    for i in range(0,11):
        r = numero * i
        result['valores'].append(r)
    return render_template('index.html', resultado = result)

app.run()