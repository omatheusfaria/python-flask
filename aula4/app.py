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

@app.route('/cadastro')
def cadastro():
    return render_template('cadusuario.html')

@app.route('/cadastrar', methods=['POST'])
def cadastrar_usuario():
    nome = request.form['nome']
    cpf = request.form['cpf']
    senha = request.form['senha']
    db = mysql.connector.connect(host='201.232.3.86',
                                 port=5000,
                                 user='usr_aluno',
                                 password='usr_aluno123',
                                 database='aula_fatec')
    mycursor = db.cursor()
    query = "insert into matheusfaria_tbusuario (nome, cpf, senha) values(%s, %s, %s)"
    values = (nome, cpf, senha)
    mycursor.execute(query,values)
    db.commit()
    return render_template('caduser')

@app.route('/caduser')
def lista_user():
    if session.get('logado') is None:
        return redirect('/')
    db = mysql.connector.connect(host='201.232.3.86',
                                 port=5000,
                                 user='usr_aluno',
                                 password='usr_aluno123',
                                 database='aula_fatec')
    mycursor = db.cursor()
    query = 'select user, cpf, senha, id from matheusfaria_tbusuario'
    mycursor.execute(query)
    resultado = mycursor.fetchall()
    return render_template('cadusuario.html', opcao='listar', usuarios=resultado)

@app.route('/alterar_usuario/<user>')
def alterar_usuario(user):
    db = mysql.connector.connect(host='201.232.3.86',
                                 port=5000,
                                 user='usr_aluno',
                                 password='usr_aluno123',
                                 database='aula_fatec')
    mycursor = db.cursor()
    query = "select user, cpf, id from matheusfaria_tbusuario where id =" + user
    mycursor.execute(query)
    resultado = mycursor.fetchall()
    return render_template('cadusuario.html', opcao='alterar', usuarios=resultado)

@app.route('/update_usuario', methods=["POST"])
def update_usuario(user):
    db = mysql.connector.connect(host='201.232.3.86',
                                 port=5000,
                                 user='usr_aluno',
                                 password='usr_aluno123',
                                 database='aula_fatec')
    mycursor = db.cursor()
    query = "select user, email, id from matheusfaria_tbusuario where id = " + user
    mycursor.execute(query)
    resultado = mycursor.fetchall()
    return render_template('cadusuario.html', opcao='alterar', usuario=resultado)

app.run()

