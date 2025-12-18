from flask import Flask, render_template, request, redirect
import json



USER_FILE = r"C:\Übungen Python\git\Flask-uebung\user.json"



app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def test():
    if request.method == "POST":

        username = request.form.get("username", "")
        password = request.form.get("password", "")

        username = username.replace(" ","")
        password = password.replace(" ", "")
    
        with open(USER_FILE, "r", encoding="utf-8") as f:
            users = json.load(f)
        if username in users and users[username] == password:
            return render_template("mainmenu.html", name = username)
        else:
            return render_template("eingabefeld.html")

    return render_template("eingabefeld.html")


@app.route("/keinacc")
def show_anmeldung():
    return render_template("registrierung.html")

@app.route("/neueracc", methods = ["GET", "POST"])
def neuer_acc():
    if request.method == "GET":
         return render_template("/registrierung.html")
    
    new_user_name = request.form.get("username", "")
    new_user_pw = request.form.get("password", "")


    with open(r"C:\Übungen Python\git\Flask-uebung\user.json", "r") as f:
            content = f.read()
            if content:
                users = json.loads(content)
            else:
                users = {}

    if " " in new_user_name or " " in new_user_pw:
         return redirect("/neueracc")
    
    users[new_user_name] = new_user_pw


    with open(r"C:\Übungen Python\git\Flask-uebung\user.json", "w") as f:
        f.write(json.dumps(users, indent=4))
    return redirect("/")



