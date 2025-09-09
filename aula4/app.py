from dotenv import load_dotenv
import os
from flask import Flask, render_template, request, session, redirect, url_for
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

# It's better to have a function to get the DB connection
def get_db_connection():
    db = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        port=int(os.getenv('DB_PORT')),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )
    return db

@app.route('/')
def raiz():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    cpf = request.form['cpf']
    senha = request.form['password']
    db = get_db_connection()
    mycursor = db.cursor(dictionary=True)

    query = "SELECT * FROM matheusfaria_tbusuarios WHERE cpf = %s"
    mycursor.execute(query, (cpf,))
    user = mycursor.fetchone()

    mycursor.close()
    db.close()

    if user and check_password_hash(user['senha'], senha):
        session['logado'] = True
        return redirect(url_for('menu'))
    else:
        return render_template('index.html', senhaErrada = 'Usuário ou senha inválido!')
    
@app.route('/cadastrar', methods=['POST'])
def cadastrar_usuario():
    nome = request.form['txt_nome']
    cpf = request.form['txt_cpf']
    senha = request.form['txt_senha']

    hashed_password = generate_password_hash(senha)

    db = get_db_connection()
    mycursor = db.cursor()
    query = "INSERT INTO matheusfaria_tbusuarios (nome, cpf, senha) VALUES (%s, %s, %s)"
    values = (nome, cpf, hashed_password)
    try:
        mycursor.execute(query, values)
        db.commit()
    except mysql.connector.Error as err:
        db.rollback()
        # A proper user-facing error should be implemented
        return f"Erro ao cadastrar: {err}", 500
    finally:
        mycursor.close()
        db.close()

    return redirect(url_for('menu', sucesso=1))

@app.route('/caduser')
def lista_user():
    if session.get('logado') is None:
        return redirect('/')
    db = get_db_connection()
    mycursor = db.cursor(dictionary=True)
    # Do not fetch password to template
    query = 'SELECT nome, cpf, id FROM matheusfaria_tbusuarios'
    mycursor.execute(query)
    resultado = mycursor.fetchall()
    mycursor.close()
    db.close()
    return render_template('cadusuario.html', opcao='listar', usuarios=resultado)

@app.route('/alterar_usuario/<int:user_id>')
def alterar_usuario(user_id):
    if session.get('logado') is None:
        return redirect('/')
    db = get_db_connection()
    mycursor = db.cursor(dictionary=True)
    query = "SELECT nome, cpf, id FROM matheusfaria_tbusuarios WHERE id = %s"
    mycursor.execute(query, (user_id,))
    resultado = mycursor.fetchone()
    mycursor.close()
    db.close()
    return render_template('cadusuario.html', opcao='alterar', usuario=resultado)

@app.route('/update_usuario', methods=["POST"])
def update_usuario():
    if session.get('logado') is None:
        return redirect('/')

    id = request.form['txt_id']
    nome = request.form['txt_nome']
    cpf = request.form['txt_cpf']
    senha = request.form.get('txt_senha')

    db = get_db_connection()
    mycursor = db.cursor()

    if senha:
        hashed_password = generate_password_hash(senha)
        query = "UPDATE matheusfaria_tbusuarios SET nome = %s, cpf = %s, senha = %s WHERE id = %s"
        values = (nome, cpf, hashed_password, id)
    else:
        query = "UPDATE matheusfaria_tbusuarios SET nome = %s, cpf = %s WHERE id = %s"
        values = (nome, cpf, id)

    try:
        mycursor.execute(query, values)
        db.commit()
    except mysql.connector.Error as err:
        db.rollback()
        return f"Erro ao atualizar: {err}", 500
    finally:
        mycursor.close()
        db.close()

    return redirect(url_for('caduser'))

@app.route('/excluir_usuario/<int:user_id>')
def excluir_usuario(user_id):
    if session.get('logado') is None:
        return redirect('/')
    db = get_db_connection()
    mycursor = db.cursor()
    query = "DELETE FROM matheusfaria_tbusuarios WHERE id = %s"
    mycursor.execute(query, (user_id,))
    db.commit()
    mycursor.close()
    db.close()
    return redirect(url_for('caduser'))

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
    db = get_db_connection()
    mycursor = db.cursor()
    query = 'SELECT nome, cpf, rg, celular, rua, bairro, cidade, cep, uf, id FROM matheusfaria_tbclientes'
    mycursor.execute(query)
    resultado = mycursor.fetchall()
    mycursor.close()
    db.close()
    return render_template('cadcliente.html', opcao='listar', clientes=resultado)

@app.route('/cadastrar_cliente', methods=['POST'])
def cadastrar_cliente():
    if session.get('logado') is None:
        return redirect('/')
    nome = request.form['txt_nome']
    cpf = request.form['txt_cpf']
    rg = request.form['txt_rg']
    cel = request.form['txt_cel']
    rua = request.form['txt_rua']
    bairro = request.form['txt_bairro']
    cidade = request.form['txt_cidade']
    cep = request.form['txt_cep']
    uf = request.form['txt_uf']
    db = get_db_connection()
    mycursor = db.cursor()
    query = "INSERT INTO matheusfaria_tbclientes (nome, cpf, rg, celular, rua, bairro, cidade, cep, uf) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (nome, cpf, rg, cel, rua, bairro, cidade, cep, uf)
    mycursor.execute(query, values)
    db.commit()
    mycursor.close()
    db.close()
    return redirect(url_for('menu', sucesso=2))

@app.route('/alterar_cliente/<int:user_id>')
def alterar_cliente(user_id):
    if session.get('logado') is None:
        return redirect('/')
    db = get_db_connection()
    mycursor = db.cursor()
    # Using parameterized query
    query = "SELECT nome, cpf, rg, celular, rua, bairro, cidade, cep, uf, id FROM matheusfaria_tbclientes WHERE id = %s"
    mycursor.execute(query, (user_id,))
    resultado = mycursor.fetchall()
    mycursor.close()
    db.close()
    return render_template('cadcliente.html', opcao='alterar', clientes=resultado)

@app.route('/update_cliente', methods=["POST"])
def update_cliente():
    if session.get('logado') is None:
        return redirect('/')
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
    db = get_db_connection()
    mycursor = db.cursor()
    # Using parameterized query
    query = """UPDATE matheusfaria_tbclientes
               SET nome = %s, cpf = %s, rg = %s, celular = %s, rua = %s, bairro = %s, cidade = %s, cep = %s, uf = %s
               WHERE id = %s"""
    values = (nome, cpf, rg, cel, rua, bairro, cidade, cep, uf, id)
    mycursor.execute(query, values)
    db.commit()
    mycursor.close()
    db.close()
    return redirect(url_for('cadcliente'))

@app.route('/excluir_cliente/<int:user_id>')
def excluir_cliente(user_id):
    if session.get('logado') is None:
        return redirect('/')
    db = get_db_connection()
    mycursor = db.cursor()
    query = "DELETE FROM matheusfaria_tbclientes WHERE id = %s"
    mycursor.execute(query, (user_id,))
    db.commit()
    mycursor.close()
    db.close()
    return redirect(url_for('cadcliente'))

if __name__ == '__main__':
    app.run(debug=True)

