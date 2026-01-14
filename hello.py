from flask import Flask, render_template, request, redirect, session, url_for
import json

USER_FILE = r"C:\Übungen Python\git\Flask-uebung\user.json"

app = Flask(__name__)
app.secret_key = "(R&b5r8(BR85rb/)TtnN&T)ntNT)&n7t&TN)T&9nt9n"


@app.route("/", methods=["GET", "POST"])
def test():
    name = session.get("username")

    if name == None:

        if request.method == "POST":

            username = request.form.get("username", "")
            password = request.form.get("password", "")

            username = username.replace(" ","")
            password = password.replace(" ", "")
        
            with open(USER_FILE, "r", encoding="utf-8") as f:
                users = json.load(f)

            if username in users and users[username] == password:
                session["username"] = username
                session["password"] = password
                return render_template("mainmenu.html")
            else:
                return render_template("wrong_pw.html")
        else:
            return render_template("eingabefeld.html")
    else:
        return render_template("mainmenu.html")


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

    if " " in new_user_name or " " in new_user_pw or "" == new_user_pw:
         return redirect("/neueracc")
    
    if new_user_name in users:
        return render_template("exis_pw.html")
    else:
        users[new_user_name] = new_user_pw

    with open(r"C:\Übungen Python\git\Flask-uebung\user.json", "w") as f:
        f.write(json.dumps(users, indent=4))
    return redirect("/")

@app.route("/logout")
def logout():

    session.pop('username', None)
    return redirect("/")

@app.route("/löschen")
def delete():
    name = session.get("username")

    with open(USER_FILE, "r", encoding="utf-8") as f:
        users = json.load(f)
        del users[name]

        with open(r"C:\Übungen Python\git\Flask-uebung\user.json", "w") as f:
            f.write(json.dumps(users, indent=4))

        session.clear()
        return render_template("/eingabefeld.html")

@app.route("/daten_aendern")
def ame_aendern():
    return render_template("/rename.html")

@app.route("/geaendert", methods = ["POST"])
def name_abgeaendert():

    old_name = session.get("username")
    old_password = session.get("password")
    password = request.form.get("password")

    if old_password == password:
        new_name = request.form.get("username", " ")
        with open(r"C:\Übungen Python\git\Flask-uebung\user.json", "r", encoding="utf-8") as f:
            users = json.load(f)

            if new_name in users:
                return render_template("exis_pw.html")
            
            else:
                users[new_name] = old_password

            del users[old_name]

            users[new_name] = old_password

        with open(USER_FILE, "w") as f:
            f.write(json.dumps(users, indent=4))
            session["username"] = new_name
            return redirect("/")
    else:
        return render_template("wrong_pw.html")
        
    


