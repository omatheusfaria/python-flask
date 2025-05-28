# 📚 Programação Web com Flask

Este repositório contém os projetos desenvolvidos na disciplina de **Programação Web**, utilizando o framework **Flask** em Python.  
Cada pasta representa uma aula com conteúdos específicos!

---

## 📂 Organização do Repositório

```
/python-flask/
├── aula1/   # Introdução ao Flask
│   ├── app.py
│   ├── templates/
│   ├── static/
│   └── env/ (não enviado ao GitHub)
│
├── aula2/   # Calculadora de IMC
│   ├── imc.py
│   ├── templates/
│   ├── static/
│   └── env/ (não enviado ao GitHub)
│
├── aula3/   # Tabuada Interativa
│   ├── tabuada.py
│   ├── templates/
│   ├── static/
│   └── env/ (não enviado ao GitHub)
│
├── aula4/   # Sistema de Cadastro com Flask e MySQL
│   ├── app.py
│   ├── templates/
│   ├── static/
│   └── env/ (não enviado ao GitHub)
```

---

## ✅ Descrição das Aulas

| Aula   | Descrição                                                                                                                                     |
| ------ | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Aula 1 | 🚀 Introdução ao Flask, abordando conceitos de **rotas (routes)**, **static** e **templates**.                                                |
| Aula 2 | 🧮 Calculadora de **IMC (Índice de Massa Corporal)**, com interação via formulário.                                                           |
| Aula 3 | ⚡ Aplicação de **Tabuada Interativa** usando Flask, com processamento de formulários e templates.                                             |
| Aula 4 | 🗂️ Sistema completo de **cadastro e autenticação** usando Flask, integração com **MySQL**, e operações de **CRUD** para usuários e clientes. |

---

## ⚙️ Como usar o projeto

### 1. 📥 Clone o repositório

```bash
git clone https://github.com/omatheusfaria/python-flask.git
```

---

### 2. 📂 Escolha a aula que deseja rodar

```bash
cd python-flask/aula1  # Para a Aula 1
# ou
cd python-flask/aula2  # Para a Aula 2
# ou
cd python-flask/aula3  # Para a Aula 3
# ou
cd python-flask/aula4  # Para a Aula 4
```

---

### 3. 🐍 Crie o ambiente virtual (se ainda não existir)

```bash
python -m venv env
```

---

### 4. ✅ Ative o ambiente virtual

#### Windows:
```bash
env\Scripts\activate
```

#### Linux/Mac:
```bash
source env/bin/activate
```

> Você vai ver o nome do ambiente ativado no terminal, exemplo: `(env)`.

---

### 5. 📦 Instale as dependências

#### Para as Aulas 1, 2 e 3:
```bash
pip install flask
```
#### Para a Aula 4:
```bash
pip install flask mysql-connector-python python-dotenv
```
---

### 6. ▶️ Rode o projeto

#### Aula 1:
```bash
python app.py
```

#### Aula 2:
```bash
python imc.py
```

#### Aula 3:
```bash
python tabuada.py
```

#### Aula 4:
```bash
python app.py
```
---

### 7. 🌐 Acesse no navegador

```
http://127.0.0.1:5000/
```

---

### 8. 🔻 Desative o ambiente virtual quando terminar

```bash
deactivate
```

---

## 💻 Tecnologias Utilizadas

| Tecnologia | Descrição |
|------------|-----------|
| [![Python](https://img.shields.io/badge/Python-3.12.9-blue?logo=python)](https://www.python.org/) | Linguagem principal utilizada no desenvolvimento dos projetos. |
| [![Flask](https://img.shields.io/badge/Flask-Framework-black?logo=flask)](https://flask.palletsprojects.com/) | Microframework para aplicações web em Python. |
| [![MySQL](https://img.shields.io/badge/MySQL-005C84?logo=mysql&logoColor=white)](https://www.mysql.com/) | Sistema de gerenciamento de banco de dados usado na Aula 4. |
| [![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)](https://developer.mozilla.org/docs/Web/HTML) | Estruturação de páginas web. |
| [![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)](https://developer.mozilla.org/docs/Web/CSS) | Estilização dos templates das aplicações. |
| [![dotenv](https://img.shields.io/badge/python--dotenv-004d7a?logo=python&logoColor=white)](https://pypi.org/project/python-dotenv/) | Gerenciamento de variáveis de ambiente na Aula 4. |

---

## ✍️ Autor

Desenvolvido por **Matheus Faria**.  
> Projeto com fins educacionais.
