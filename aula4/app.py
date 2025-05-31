from dotenv import load_dotenv
import os
from flask import Flask, render_template, request, session, redirect, url_for
import mysql.connector

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')
@app.route('/')
def raiz():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    cpf = request.form['cpf']
    senha = request.form['password']
    db = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        port=int(os.getenv('DB_PORT')),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )
    mycursor = db.cursor()
    query = "select nome, cpf, senha from matheusfaria_tbusuarios where cpf = '" + cpf + "' and senha = '" + senha + "'"
    mycursor.execute(query)
    resultado = mycursor.fetchone()
    if resultado:
        session['logado'] = True
        return redirect('menu')
    else:
        return render_template('index.html', senhaErrada = 'Usuário ou senha invalido!')
    
@app.route('/cadastrar', methods=['POST'])
def cadastrar_usuario():
    nome = request.form['txt_nome']
    cpf = request.form['txt_cpf']
    senha = request.form['txt_senha']
    db = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        port=int(os.getenv('DB_PORT')),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )
    mycursor = db.cursor()
    query = "insert into matheusfaria_tbusuarios (nome, cpf, senha) values(%s, %s, %s)"
    values = (nome, cpf, senha)
    mycursor.execute(query,values)
    db.commit()
    return redirect(url_for('menu', sucesso=1))

@app.route('/caduser')
def lista_user():
    if session.get('logado') is None:
        return redirect('/')
    db = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        port=int(os.getenv('DB_PORT')),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )
    mycursor = db.cursor()
    query = 'select nome, cpf, senha, id from matheusfaria_tbusuarios'
    mycursor.execute(query)
    resultado = mycursor.fetchall()
    return render_template('cadusuario.html', opcao='listar', usuarios=resultado)

@app.route('/alterar_usuario/<user>')
def alterar_usuario(user):
    db = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        port=int(os.getenv('DB_PORT')),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )
    mycursor = db.cursor()
    query = "select nome, cpf, id from matheusfaria_tbusuarios where id =" + user
    mycursor.execute(query)
    resultado = mycursor.fetchall()
    return render_template('cadusuario.html', opcao='alterar', usuarios=resultado)

@app.route('/update_usuario', methods=["POST"])
def update_usuario():
    id = request.form['txt_id']
    nome = request.form['txt_nome']
    cpf = request.form['txt_cpf']
    senha = request.form['txt_senha']
    db = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        port=int(os.getenv('DB_PORT')),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )
    mycursor = db.cursor()
    query = "update matheusfaria_tbusuarios set nome ='" + nome + "', cpf = '" + cpf + "', senha = '" + senha + "' where id = " + id
    print (query)
    mycursor.execute(query)
    db.commit()
    return redirect('/caduser')

@app.route('/excluir_usuario/<user>')
def excluir_usuario(user):
    db = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        port=int(os.getenv('DB_PORT')),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )
    mycursor = db.cursor()
    query = "DELETE FROM matheusfaria_tbusuarios WHERE id = %s"
    mycursor.execute(query, (user,))
    db.commit()
    return redirect('/caduser')

@app.route('/menu')
def menu():
    if session.get('logado') is None:
        return redirect('/')
    sucesso = request.args.get('sucesso')
    return render_template('menu.html', sucesso=sucesso)

@app.route('/cadcliente')
def cadcliente():
    if session.get('logado') is None:
        return redirect('/')
    db = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        port=int(os.getenv('DB_PORT')),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )
    mycursor = db.cursor()
    query = 'SELECT nome, cpf, rg, celular, rua, bairro, cidade, cep, uf, id FROM matheusfaria_tbclientes'
    mycursor.execute(query)
    resultado = mycursor.fetchall()
    return render_template('cadcliente.html', opcao='listar', clientes=resultado)

@app.route('/cadastrar_cliente', methods=['POST'])
def cadastrar_cliente():
    nome = request.form['txt_nome']
    cpf = request.form['txt_cpf']
    rg = request.form['txt_rg']
    cel = request.form['txt_cel']
    rua = request.form['txt_rua']
    bairro = request.form['txt_bairro']
    cidade = request.form['txt_cidade']
    cep = request.form['txt_cep']
    uf = request.form['txt_uf']
    db = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        port=int(os.getenv('DB_PORT')),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )
    mycursor = db.cursor()
    query = "insert into matheusfaria_tbclientes (nome, cpf, rg, celular, rua, bairro, cidade, cep, uf) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (nome, cpf, rg, cel, rua, bairro, cidade, cep, uf)
    mycursor.execute(query,values)
    db.commit()
    return redirect(url_for('menu', sucesso=2))

@app.route('/alterar_cliente/<user>')
def alterar_cliente(user):
    db = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        port=int(os.getenv('DB_PORT')),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )
    mycursor = db.cursor()
    query = "select nome, cpf, rg, celular, rua, bairro, cidade, cep, uf, id FROM matheusfaria_tbclientes where id =" + user
    mycursor.execute(query)
    resultado = mycursor.fetchall()
    return render_template('cadcliente.html', opcao='alterar', clientes=resultado)

@app.route('/update_cliente', methods=["POST"])
def update_cliente():
    id = request.form['txt_id']
    nome = request.form['txt_nome']
    cpf = request.form['txt_cpf']
    rg = request.form['txt_rg']
    cel = request.form['txt_cel']
    rua = request.form['txt_rua']
    bairro = request.form['txt_bairro']
    cidade = request.form['txt_cidade']
    cep = request.form['txt_cep']
    uf = request.form['txt_uf']
    db = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        port=int(os.getenv('DB_PORT')),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )
    mycursor = db.cursor()
    query = "update matheusfaria_tbclientes set nome ='" + nome + "', cpf = '" + cpf + "', rg = '" + rg + "', celular = '" + cel + "', rua = '" + rua + "', bairro = '" + bairro + "', cidade = '" + cidade + "', cep = '" + cep + "', uf = '" + uf + "' where id = " + id
    print (query)
    mycursor.execute(query)
    db.commit()
    return redirect('/cadcliente')

@app.route('/excluir_cliente/<user>')
def excluir_cliente(user):
    db = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        port=int(os.getenv('DB_PORT')),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )
    mycursor = db.cursor()
    query = "DELETE FROM matheusfaria_tbclientes WHERE id = %s"
    mycursor.execute(query, (user,))
    db.commit()
    return redirect('/cadcliente')
app.run()

