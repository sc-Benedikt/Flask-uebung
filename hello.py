from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def test():
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        if username == "bene" and password == "123":
            return render_template("/mainmenu.html")
        else: 
            new_title = "bitte feld ausfüllen"
            return render_template("/eingabefeld.html", new_title= grund )
    return render_template("/eingabefeld.html")


@app.route("/keinacc")
def show_anmeldung():
    return render_template("/registrierung.html")


