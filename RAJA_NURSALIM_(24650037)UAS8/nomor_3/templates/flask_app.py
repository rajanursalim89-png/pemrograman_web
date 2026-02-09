from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/")
def produk():
    return render_template("produk.html")

@app.route("laporan")
def produk():
    return render_template("laporan.html")
if __name__ == "__main__":
    app.run(debug=True)