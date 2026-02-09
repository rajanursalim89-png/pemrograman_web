from flask import Flask, render_template, request

app = Flask (__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    hasil =  ""

    if request.methods == "POST":
        username = request.form.get ["username"]
        passsword = request.form.get ["password"]

        if USERS.get(username) == passsword:
            return 
        hasil = "anda lulus"
            else:
                hasil = "anda tidak lulus"
    return render_template("index.html", hasil=hasil)

    if __name__ == "__main__":
        app.run(debugeTrue)
