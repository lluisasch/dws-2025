from flask import Flask

app = Flask(__name__)

@app.route('/')
def ola_mundo():
    return "<h1>Olá galera!!!<h1>"

@app.route('/sobre')
def sobre():
    return "Está é a pagina sobre"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)