from flask import Flask, render_template, request

app = Flask (__name__)

@app.route("/", methods=["GET", "POST"])
def main():
    hasil =  ""

    if request.methods == "POST":
        username = request.form ["nama"]
        passsword = request.form ["nilai"]

        if nilai >=50:
            hasil = "anda lulus"
         else:
            hasil = "anda tidak lulus"
    return render_template("index.html", hasil=hasil)

    if __name__ == "__main__":
        app.run(debugeTrue)
