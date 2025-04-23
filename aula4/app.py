from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

@app.route('/')
def raiz():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    cpf = request.form['cpf']
    senha = request.form['password']
    db = mysql.connector.connect(host='201.232.3.86',
                                 port=5000,
                                 user='usr_aluno',
                                 password='usr_aluno123',
                                 database='aula_fatec')
    mycursor = db.cursor()
    query = "select, nome, cpf, senha from matheusfaria_tbusuarios where cpf = '" + cpf + "' and senha = '" + senha + "'"
    mycursor.execute(query)
    if mycursor.fetchall():
        return 'Logou'
    else:
        return render_template('index.html', senhaErrada = 'Usuário ou senha invalido!')
    
app.run()