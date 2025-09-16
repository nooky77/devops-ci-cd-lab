from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/groupe10")
def groupe10():
    return render_template("groupe10.html")


@app.route("/groupe20")
def groupe20():
    return render_template("groupe20.html")


@app.route("/groupe30")
def groupe30():
    return render_template("groupe30.html")


@app.route("/groupe40")
def groupe40():
    return render_template("groupe40.html")


@app.route("/groupe50")
def groupe50():
    return render_template("groupe50.html")


if __name__ == "__main__":
    app.run(debug=True)
