from flask import Flask, render_template, request, session, redirect, url_for
import mysql.connector

app = Flask(__name__)

app.secret_key = 'sub'

@app.route('/')
def raiz():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    login = request.form['login']
    senha = request.form['password']
    db = mysql.connector.connect(
        host="201.23.3.86",
        port="5000",
        user="usr_aluno",
        password="usr_aluno123",
        database="aula_fatec"
    )
    mycursor = db.cursor()
    query = "select login, senha from matheusfaria_tbusuarios where login = '" + login + "' and senha = '" + senha + "'"
    mycursor.execute(query)
    resultado = mycursor.fetchone()
    if resultado:
        session['logado'] = True
        return redirect('menu')
    else:
        return render_template('index.html', senhaErrada = 'Login ou senha invalido!')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/cadastrar', methods=['POST'])
def cadastrar_usuario():
    login = request.form['txt_login']
    senha = request.form['txt_senha']
    db = mysql.connector.connect(
        host="201.23.3.86",
        port="5000",
        user="usr_aluno",
        password="usr_aluno123",
        database="aula_fatec"
    )
    mycursor = db.cursor()
    query = "insert into matheusfaria_tbusuarios (login, senha) values(%s, %s)"
    values = (login, senha)
    mycursor.execute(query,values)
    db.commit()
    return redirect(url_for('lista_user'))

@app.route('/caduser')
def lista_user():
    db = mysql.connector.connect(
        host="201.23.3.86",
        port="5000",
        user="usr_aluno",
        password="usr_aluno123",
        database="aula_fatec"
    )
    mycursor = db.cursor()
    query = 'select login, senha, id from matheusfaria_tbusuarios'
    mycursor.execute(query)
    resultado = mycursor.fetchall()
    return render_template('caduser.html', opcao='listar', usuarios=resultado)

@app.route('/alterar_usuario/<user>')
def alterar_usuario(user):
    db = mysql.connector.connect(
        host="201.23.3.86",
        port="5000",
        user="usr_aluno",
        password="usr_aluno123",
        database="aula_fatec"
    )
    mycursor = db.cursor()
    query = "select login, id from matheusfaria_tbusuarios where id =" + user
    mycursor.execute(query)
    resultado = mycursor.fetchall()
    return render_template('caduser.html', opcao='alterar', usuarios=resultado)

@app.route('/update_usuario', methods=["POST"])
def update_usuario():
    id = request.form['txt_id']
    login = request.form['txt_login']
    senha = request.form['txt_senha']
    db = mysql.connector.connect(
        host="201.23.3.86",
        port="5000",
        user="usr_aluno",
        password="usr_aluno123",
        database="aula_fatec"
    )
    mycursor = db.cursor()
    query = "update matheusfaria_tbusuarios set login ='" + login + "', senha = '" + senha + "' where id = " + id
    mycursor.execute(query)
    db.commit()
    return redirect('/caduser')

@app.route('/excluir_usuario/<user>')
def excluir_usuario(user):
    db = mysql.connector.connect(
        host="201.23.3.86",
        port="5000",
        user="usr_aluno",
        password="usr_aluno123",
        database="aula_fatec"
    )
    mycursor = db.cursor()
    query = "DELETE FROM matheusfaria_tbusuarios WHERE id = %s"
    mycursor.execute(query, (user,))
    db.commit()
    return redirect('/caduser')

@app.route('/cadcarro')
def lista_carro():
    if session.get('logado') is None or False:
        return redirect('/')
    db = mysql.connector.connect(
        host="201.23.3.86",
        port="5000",
        user="usr_aluno",
        password="usr_aluno123",
        database="aula_fatec"
    )
    mycursor = db.cursor()
    query = 'SELECT marca, modelo, cor, placa, chassi, id FROM matheusfaria_tbcarros'
    mycursor.execute(query)
    resultado = mycursor.fetchall()
    return render_template('cadcarro.html', opcao='listar', carros=resultado)

@app.route('/cadastrar_carro', methods=['POST'])
def cadastrar_carro():
    marca = request.form['txt_marca']
    modelo = request.form['txt_modelo']
    cor = request.form['txt_cor']
    placa = request.form['txt_placa']
    chassi = request.form['txt_chassi']
    db = mysql.connector.connect(
        host="201.23.3.86",
        port="5000",
        user="usr_aluno",
        password="usr_aluno123",
        database="aula_fatec"
    )
    mycursor = db.cursor()
    query = "insert into matheusfaria_tbcarros (marca, modelo, cor, placa, chassi) values(%s, %s, %s, %s, %s)"
    values = (marca, modelo, cor, placa, chassi)
    mycursor.execute(query,values)
    db.commit()
    return redirect(url_for('lista_carro'))

@app.route('/alterar_carro/<user>')
def alterar_carro(user):
    db = mysql.connector.connect(
        host="201.23.3.86",
        port="5000",
        user="usr_aluno",
        password="usr_aluno123",
        database="aula_fatec"
    )
    mycursor = db.cursor()
    query = "select marca, modelo, cor, placa, chassi, id FROM matheusfaria_tbcarros where id =" + user
    mycursor.execute(query)
    resultado = mycursor.fetchall()
    return render_template('cadcarro.html', opcao='alterar', carros=resultado)

@app.route('/update_carro', methods=["POST"])
def update_carro():
    id = request.form['txt_id']
    marca = request.form['txt_marca']
    modelo = request.form['txt_modelo']
    cor = request.form['txt_cor']
    placa = request.form['txt_placa']
    chassi = request.form['txt_chassi']
    db = mysql.connector.connect(
        host="201.23.3.86",
        port="5000",
        user="usr_aluno",
        password="usr_aluno123",
        database="aula_fatec"
    )
    mycursor = db.cursor()
    query = "update matheusfaria_tbcarros set marca ='" + marca + "', modelo = '" + modelo + "', cor = '" + cor + "', placa = '" + placa + "', chassi = '" + chassi + "' where id = " + id
    print (query)
    mycursor.execute(query)
    db.commit()
    return redirect(url_for('lista_carro'))

@app.route('/excluir_carro/<user>')
def excluir_carro(user):
    db = mysql.connector.connect(
        host="201.23.3.86",
        port="5000",
        user="usr_aluno",
        password="usr_aluno123",
        database="aula_fatec"
    )
    mycursor = db.cursor()
    query = "DELETE FROM matheusfaria_tbcarros WHERE id = %s"
    mycursor.execute(query, (user,))
    db.commit()
    return redirect(url_for('lista_carro'))

@app.route('/cadconcessionaria')
def lista_concessionaria():
    if session.get('logado') is None or False:
        return redirect('/')
    db = mysql.connector.connect(
        host="201.23.3.86",
        port="5000",
        user="usr_aluno",
        password="usr_aluno123",
        database="aula_fatec"
    )
    mycursor = db.cursor()
    query = 'SELECT nome, cnpj, inscricao, rua, bairro, cep, id FROM matheusfaria_tbconcessionarias'
    mycursor.execute(query)
    resultado = mycursor.fetchall()
    return render_template('cadconcessionaria.html', opcao='listar', concessionarias=resultado)

@app.route('/cadastrar_concessionaria', methods=['POST'])
def cadastrar_concessionaria():
    nome = request.form['txt_nome']
    cnpj = request.form['txt_cnpj']
    inscricao = request.form['txt_inscricao']
    rua = request.form['txt_rua']
    bairro = request.form['txt_bairro']
    cep = request.form['txt_cep']
    db = mysql.connector.connect(
        host="201.23.3.86",
        port="5000",
        user="usr_aluno",
        password="usr_aluno123",
        database="aula_fatec"
    )
    mycursor = db.cursor()
    query = "insert into matheusfaria_tbconcessionarias (nome, cnpj, inscricao, rua, bairro, cep) values(%s, %s, %s, %s, %s, %s)"
    values = (nome, cnpj, inscricao, rua, bairro, cep)
    mycursor.execute(query,values)
    db.commit()
    return redirect(url_for('lista_concessionaria'))

@app.route('/alterar_concessionaria/<user>')
def alterar_concessionaria(user):
    db = mysql.connector.connect(
        host="201.23.3.86",
        port="5000",
        user="usr_aluno",
        password="usr_aluno123",
        database="aula_fatec"
    )
    mycursor = db.cursor()
    query = "select nome, cnpj, inscricao, rua, bairro, cep, id FROM matheusfaria_tbconcessionarias where id =" + user
    mycursor.execute(query)
    resultado = mycursor.fetchall()
    return render_template('cadconcessionaria.html', opcao='alterar', concessionarias=resultado)

@app.route('/update_concessionaria', methods=["POST"])
def update_concessionaria():
    id = request.form['txt_id']
    nome = request.form['txt_nome']
    cnpj = request.form['txt_cnpj']
    inscricao = request.form['txt_inscricao']
    rua = request.form['txt_rua']
    bairro = request.form['txt_bairro']
    cep = request.form['txt_cep']
    db = mysql.connector.connect(
        host="201.23.3.86",
        port="5000",
        user="usr_aluno",
        password="usr_aluno123",
        database="aula_fatec"
    )
    mycursor = db.cursor()
    query = "update matheusfaria_tbconcessionarias set nome ='" + nome + "', cnpj = '" + cnpj + "', inscricao = '" + inscricao + "', rua = '" + rua + "', bairro = '" + bairro + "', cep = '" + cep + "' where id = " + id
    print (query)
    mycursor.execute(query)
    db.commit()
    return redirect(url_for('lista_concessionaria'))

@app.route('/excluir_concessionaria/<user>')
def excluir_concessionaria(user):
    db = mysql.connector.connect(
        host="201.23.3.86",
        port="5000",
        user="usr_aluno",
        password="usr_aluno123",
        database="aula_fatec"
    )
    mycursor = db.cursor()
    query = "DELETE FROM matheusfaria_tbconcessionarias WHERE id = %s"
    mycursor.execute(query, (user,))
    db.commit()
    return redirect(url_for('lista_concessionaria'))

app.run()