from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    hasil =  ""

    if request. methods == "POST":
        username = request.form ["username"]
        passsword = request.form ["password"]

        if username == "admin" and passsword == "admin":
            hasil = "sukses login"
        else:
                hasil = "gagal login"
    return render_template("login.html", hasil=hasil)

    if __name__ == "__main__":
        app.run(debug=True)