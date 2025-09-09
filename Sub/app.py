from flask import Flask, render_template, request, session, redirect, url_for
import mysql.connector
from dotenv import load_dotenv
import os
from werkzeug.security import generate_password_hash, check_password_hash

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'a_default_secret_key_if_not_set')

def get_db_connection():
    # Using environment variables for DB connection
    # Note: The original file had different credentials.
    # This assumes the .env file will be configured correctly.
    db = mysql.connector.connect(
        host=os.getenv('DB_HOST_SUB', '201.23.3.86'),
        port=int(os.getenv('DB_PORT_SUB', 5000)),
        user=os.getenv('DB_USER_SUB', 'usr_aluno'),
        password=os.getenv('DB_PASSWORD_SUB', 'usr_aluno123'),
        database=os.getenv('DB_NAME_SUB', 'aula_fatec')
    )
    return db

@app.route('/')
def raiz():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    login_user = request.form['login']
    senha = request.form['password']
    db = get_db_connection()
    mycursor = db.cursor(dictionary=True)

    query = "SELECT * FROM matheusfaria_tbusuarios WHERE login = %s"
    mycursor.execute(query, (login_user,))
    user = mycursor.fetchone()

    mycursor.close()
    db.close()

    if user and check_password_hash(user['senha'], senha):
        session['logado'] = True
        return redirect(url_for('menu'))
    else:
        return render_template('index.html', senhaErrada = 'Login ou senha inválido!')

@app.route('/menu')
def menu():
    if not session.get('logado'):
        return redirect(url_for('raiz'))
    return render_template('menu.html')

@app.route('/cadastrar', methods=['POST'])
def cadastrar_usuario():
    login = request.form['txt_login']
    senha = request.form['txt_senha']

    hashed_password = generate_password_hash(senha)

    db = get_db_connection()
    mycursor = db.cursor()
    query = "INSERT INTO matheusfaria_tbusuarios (login, senha) VALUES (%s, %s)"
    values = (login, hashed_password)
    try:
        mycursor.execute(query, values)
        db.commit()
    except mysql.connector.Error as err:
        db.rollback()
        return f"Erro ao cadastrar: {err}", 500
    finally:
        mycursor.close()
        db.close()

    return redirect(url_for('lista_user'))

@app.route('/caduser')
def lista_user():
    if not session.get('logado'):
        return redirect(url_for('raiz'))
    db = get_db_connection()
    mycursor = db.cursor(dictionary=True)
    query = 'SELECT login, id FROM matheusfaria_tbusuarios' # Do not fetch password
    mycursor.execute(query)
    resultado = mycursor.fetchall()
    mycursor.close()
    db.close()
    return render_template('caduser.html', opcao='listar', usuarios=resultado)

@app.route('/alterar_usuario/<int:user_id>')
def alterar_usuario(user_id):
    if not session.get('logado'):
        return redirect(url_for('raiz'))
    db = get_db_connection()
    mycursor = db.cursor(dictionary=True)
    query = "SELECT login, id FROM matheusfaria_tbusuarios WHERE id = %s"
    mycursor.execute(query, (user_id,))
    resultado = mycursor.fetchone()
    mycursor.close()
    db.close()
    return render_template('caduser.html', opcao='alterar', usuario=resultado)

@app.route('/update_usuario', methods=["POST"])
def update_usuario():
    if not session.get('logado'):
        return redirect(url_for('raiz'))
    id = request.form['txt_id']
    login = request.form['txt_login']
    senha = request.form.get('txt_senha')

    db = get_db_connection()
    mycursor = db.cursor()

    if senha:
        hashed_password = generate_password_hash(senha)
        query = "UPDATE matheusfaria_tbusuarios SET login = %s, senha = %s WHERE id = %s"
        values = (login, hashed_password, id)
    else:
        query = "UPDATE matheusfaria_tbusuarios SET login = %s WHERE id = %s"
        values = (login, id)

    try:
        mycursor.execute(query, values)
        db.commit()
    except mysql.connector.Error as err:
        db.rollback()
        return f"Erro ao atualizar: {err}", 500
    finally:
        mycursor.close()
        db.close()

    return redirect(url_for('lista_user'))

@app.route('/excluir_usuario/<int:user_id>')
def excluir_usuario(user_id):
    if not session.get('logado'):
        return redirect(url_for('raiz'))
    db = get_db_connection()
    mycursor = db.cursor()
    query = "DELETE FROM matheusfaria_tbusuarios WHERE id = %s"
    mycursor.execute(query, (user_id,))
    db.commit()
    mycursor.close()
    db.close()
    return redirect(url_for('lista_user'))

@app.route('/cadcarro')
def lista_carro():
    if not session.get('logado'):
        return redirect(url_for('raiz'))
    db = get_db_connection()
    mycursor = db.cursor()
    query = 'SELECT marca, modelo, cor, placa, chassi, id FROM matheusfaria_tbcarros'
    mycursor.execute(query)
    resultado = mycursor.fetchall()
    mycursor.close()
    db.close()
    return render_template('cadcarro.html', opcao='listar', carros=resultado)

@app.route('/cadastrar_carro', methods=['POST'])
def cadastrar_carro():
    if not session.get('logado'):
        return redirect(url_for('raiz'))
    marca = request.form['txt_marca']
    modelo = request.form['txt_modelo']
    cor = request.form['txt_cor']
    placa = request.form['txt_placa']
    chassi = request.form['txt_chassi']
    db = get_db_connection()
    mycursor = db.cursor()
    query = "INSERT INTO matheusfaria_tbcarros (marca, modelo, cor, placa, chassi) VALUES (%s, %s, %s, %s, %s)"
    values = (marca, modelo, cor, placa, chassi)
    mycursor.execute(query, values)
    db.commit()
    mycursor.close()
    db.close()
    return redirect(url_for('lista_carro'))

@app.route('/alterar_carro/<int:car_id>')
def alterar_carro(car_id):
    if not session.get('logado'):
        return redirect(url_for('raiz'))
    db = get_db_connection()
    mycursor = db.cursor()
    query = "SELECT marca, modelo, cor, placa, chassi, id FROM matheusfaria_tbcarros WHERE id = %s"
    mycursor.execute(query, (car_id,))
    resultado = mycursor.fetchall()
    mycursor.close()
    db.close()
    return render_template('cadcarro.html', opcao='alterar', carros=resultado)

@app.route('/update_carro', methods=["POST"])
def update_carro():
    if not session.get('logado'):
        return redirect(url_for('raiz'))
    id = request.form['txt_id']
    marca = request.form['txt_marca']
    modelo = request.form['txt_modelo']
    cor = request.form['txt_cor']
    placa = request.form['txt_placa']
    chassi = request.form['txt_chassi']
    db = get_db_connection()
    mycursor = db.cursor()
    query = "UPDATE matheusfaria_tbcarros SET marca = %s, modelo = %s, cor = %s, placa = %s, chassi = %s WHERE id = %s"
    values = (marca, modelo, cor, placa, chassi, id)
    mycursor.execute(query, values)
    db.commit()
    mycursor.close()
    db.close()
    return redirect(url_for('lista_carro'))

@app.route('/excluir_carro/<int:car_id>')
def excluir_carro(car_id):
    if not session.get('logado'):
        return redirect(url_for('raiz'))
    db = get_db_connection()
    mycursor = db.cursor()
    query = "DELETE FROM matheusfaria_tbcarros WHERE id = %s"
    mycursor.execute(query, (car_id,))
    db.commit()
    mycursor.close()
    db.close()
    return redirect(url_for('lista_carro'))

@app.route('/cadconcessionaria')
def lista_concessionaria():
    if not session.get('logado'):
        return redirect(url_for('raiz'))
    db = get_db_connection()
    mycursor = db.cursor()
    query = 'SELECT nome, cnpj, inscricao, rua, bairro, cep, id FROM matheusfaria_tbconcessionarias'
    mycursor.execute(query)
    resultado = mycursor.fetchall()
    mycursor.close()
    db.close()
    return render_template('cadconcessionaria.html', opcao='listar', concessionarias=resultado)

@app.route('/cadastrar_concessionaria', methods=['POST'])
def cadastrar_concessionaria():
    if not session.get('logado'):
        return redirect(url_for('raiz'))
    nome = request.form['txt_nome']
    cnpj = request.form['txt_cnpj']
    inscricao = request.form['txt_inscricao']
    rua = request.form['txt_rua']
    bairro = request.form['txt_bairro']
    cep = request.form['txt_cep']
    db = get_db_connection()
    mycursor = db.cursor()
    query = "INSERT INTO matheusfaria_tbconcessionarias (nome, cnpj, inscricao, rua, bairro, cep) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (nome, cnpj, inscricao, rua, bairro, cep)
    mycursor.execute(query, values)
    db.commit()
    mycursor.close()
    db.close()
    return redirect(url_for('lista_concessionaria'))

@app.route('/alterar_concessionaria/<int:conc_id>')
def alterar_concessionaria(conc_id):
    if not session.get('logado'):
        return redirect(url_for('raiz'))
    db = get_db_connection()
    mycursor = db.cursor()
    query = "SELECT nome, cnpj, inscricao, rua, bairro, cep, id FROM matheusfaria_tbconcessionarias WHERE id = %s"
    mycursor.execute(query, (conc_id,))
    resultado = mycursor.fetchall()
    mycursor.close()
    db.close()
    return render_template('cadconcessionaria.html', opcao='alterar', concessionarias=resultado)

@app.route('/update_concessionaria', methods=["POST"])
def update_concessionaria():
    if not session.get('logado'):
        return redirect(url_for('raiz'))
    id = request.form['txt_id']
    nome = request.form['txt_nome']
    cnpj = request.form['txt_cnpj']
    inscricao = request.form['txt_inscricao']
    rua = request.form['txt_rua']
    bairro = request.form['txt_bairro']
    cep = request.form['txt_cep']
    db = get_db_connection()
    mycursor = db.cursor()
    query = "UPDATE matheusfaria_tbconcessionarias SET nome = %s, cnpj = %s, inscricao = %s, rua = %s, bairro = %s, cep = %s WHERE id = %s"
    values = (nome, cnpj, inscricao, rua, bairro, cep, id)
    mycursor.execute(query, values)
    db.commit()
    mycursor.close()
    db.close()
    return redirect(url_for('lista_concessionaria'))

@app.route('/excluir_concessionaria/<int:conc_id>')
def excluir_concessionaria(conc_id):
    if not session.get('logado'):
        return redirect(url_for('raiz'))
    db = get_db_connection()
    mycursor = db.cursor()
    query = "DELETE FROM matheusfaria_tbconcessionarias WHERE id = %s"
    mycursor.execute(query, (conc_id,))
    db.commit()
    mycursor.close()
    db.close()
    return redirect(url_for('lista_concessionaria'))

if __name__ == '__main__':
    app.run(debug=True)