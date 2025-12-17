from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def test():
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        if username == "bene" and password == "123":
            return render_template("/mainmenu.html")
        else: 
            return render_template("/eingabefeld.html")
    return render_template("/eingabefeld.html")



@app.route("/meinmenu")
def show_name():
    return render_template("/angecklickt.html")


