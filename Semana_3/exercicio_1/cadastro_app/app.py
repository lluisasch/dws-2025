from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/cadastro", methods = ["POST", "GET"])
def cadastro():
    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        senha = request.form.get("senha")
        return render_template("sucesso.html", nome=nome, email=email, senha=senha)    
    return render_template("cadastro.html")
   
@app.route("/sucesso")
def sucesso():
    return render_template("sucesso.html")
    
if __name__ == "__main__":
    app.run(debug=True)
    