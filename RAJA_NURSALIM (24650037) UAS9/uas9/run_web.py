from flask import Flask, render_template, request

app = Flask(__name__)

data_siswa = [
    {"nama": "la ilham", "jk": "Laki-laki", "nilai": 100},
    {"nama": "wa qari", "jk": "Perempuan", "nilai": 100},
    {"nama": "wa cika", "jk": "Perempuan", "nilai": 90},
    {"nama": "la sabrian", "jk": "Laki-laki", "nilai": 80},
    {"nama": "la datri", "jk": "Laki-laki", "nilai": 70},
    {"nama": "wa nayla", "jk": "Perempuan", "nilai": 50},
    {"nama": "wa salsa", "jk": "Perempuan", "nilai": 48},
    {"nama": "la raja", "jk": "Laki-laki", "nilai": 40},
    {"nama": "la rahmat", "jk": "Laki-laki", "nilai": 30},
    {"nama": "la daus", "jk": "Laki-laki", "nilai": 23},
]

@app.route("/", methods=["GET", "POST"])
def index():
    batas = None
    lulus = []
    tidak_lulus = []

    if request.method == "POST":
        batas = int(request.form["batas"])

        for s in data_siswa:
            if s["nilai"] >= batas:
                lulus.append(s)
            else:
                tidak_lulus.append(s)

    return render_template(
        "index.html",
        batas=batas,
        lulus=lulus,
        tidak_lulus=tidak_lulus
    )

if __name__ == "__main__":
    app.run(debug=True)