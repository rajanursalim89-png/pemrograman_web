from flask import Flask, render_template, request
from core.services import hitung_layang_layang

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def layang_layang():
    hasil = None

    if request.method == "POST":
        d1 = float(request.form["d1"])
        d2 = float(request.form["d2"])
        a = float(request.form["a"])
        b = float(request.form["b"])

        hasil = hitung_layang_layang(d1, d2, a, b)

    return render_template("layang_layang.html", hasil=hasil)

if __name__ == "__main__":
    app.run(debug=True)
