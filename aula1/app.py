from flask import Flask, render_template
 
app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template('home.html', titulo = 'Home')
 
@app.route('/clients')
def render_paginaClients():
    return render_template('clients.html')
 
@app.route('/about')
def render_paginaAbout():
    return render_template('about.html')

@app.route('/contact')
def render_paginaContact():
    return render_template('contact.html')
 
if __name__ == '__main__':
    app.run(debug=True)