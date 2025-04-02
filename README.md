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
└── aula2/   # Calculadora de IMC
    ├── imc.py
    ├── templates/
    ├── static/
    └── env/ (não enviado ao GitHub)
```

---

## ✅ Descrição das Aulas

| Aula   | Descrição                                                                          |
|-------|-------------------------------------------------------------------------------------|
| Aula 1 | 🚀 Introdução ao Flask, abordando conceitos de **rotas (routes)**, **static** e **templates**. |
| Aula 2 | 🧮 Calculadora de **IMC (Índice de Massa Corporal)**, com interação via formulário.  |

---

## ⚙️ Como usar o projeto

### 1. 📥 Clone o repositório

```bash
git clone https://github.com/omatheusfaria/python-flask.git
```

---

### 2. 📂 Escolha a aula que deseja rodar

```bash
cd python-flask/aula1  # Para a aula 1
# ou
cd python-flask/aula2  # Para a aula 2
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

### 5. 📦 Instale o Flask (requisito para rodar o projeto)

```bash
pip install flask
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

- 🐍 **Python 3.12.9**
- 🔥 **Flask**
- 🎨 **HTML5 e CSS3** (para templates e estilos)

---

## ✍️ Autor

Desenvolvido por **Matheus Faria**.  
> Projeto com fins educacionais.
