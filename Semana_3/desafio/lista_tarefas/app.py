from flask import Flask, render_template, request

app = Flask(__name__)

tarefas = []

@app.route("/", methods = ["POST", "GET"])
def index():
    if request.method == "POST" :
        tarefa = request.form["tarefa"]
        data_limite = request.form["data_limite"]
    
        if tarefa and data_limite:
            tarefas.append({'tarefa': tarefa, 'data_limite': data_limite})
            return render_template('sucesso.html', nome_tarefa=tarefa)
    
    return render_template("index.html", tarefas=tarefas)

@app.route("/sucesso")
def sucesso():
    nome_tarefa = request.args.get('nome_tarefa', '')
    return render_template("sucesso.html", nome_tarefa=nome_tarefa)

if __name__ == "__main__":
    app.run(debug=True)